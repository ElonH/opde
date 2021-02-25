---
title: "compile.50"
date: 2021-02-25 14:20:49.078804
hidden: false
draft: false
weight: -50
---

build number: `50`

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
-- Include Plugin augeas
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
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target generate_version_script
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  0%] Creating version script
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  0%] Built target generate_version_script
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-core
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  0%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/errors.c.o
[  0%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/global.c.o
[  0%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/internal.c.o
[  0%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/kdbenum.c.o
[  1%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/key.c.o
[  1%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keyhelpers.c.o
[  1%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keymeta.c.o
[  1%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keyname.c.o
[  1%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keyset.c.o
[  1%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keytest.c.o
[  2%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/keyvalue.c.o
[  2%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/nolog.c.o
[  2%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/owner.c.o
[  2%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/proposal.c.o
[  2%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/rand.c.o
[  2%] Building C object src/libs/elektra/CMakeFiles/elektra-core.dir/__/loader/dl.c.o
[  3%] Linking C shared library ../../../lib/libelektra-core.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  3%] Built target elektra-core
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-ease-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  3%] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/array.c.o
[  4%] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/conversion.c.o
[  4%] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/functional.c.o
[  4%] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/keyname.c.o
[  4%] Building C object src/libs/ease/CMakeFiles/elektra-ease-objects.dir/reference.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-ease-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-ease
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Linking C shared library ../../../lib/libelektra-ease.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-ease
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-proposal-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Building C object src/libs/proposal/CMakeFiles/elektra-proposal-objects.dir/proposal.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-proposal-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-proposal
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Linking C shared library ../../../lib/libelektra-proposal.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-proposal
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-meta-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Building C object src/libs/meta/CMakeFiles/elektra-meta-objects.dir/meta.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-meta-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-meta
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Linking C shared library ../../../lib/libelektra-meta.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-meta
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-plugin-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Building C object src/libs/plugin/CMakeFiles/elektra-plugin-objects.dir/plugin.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-plugin-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-plugin
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Linking C shared library ../../../lib/libelektra-plugin.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-plugin
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-augeas
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Building C object src/plugins/augeas/CMakeFiles/elektra-augeas.dir/augeas.c.o
[  5%] Linking C shared module ../../../lib/libelektra-augeas.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  5%] Built target elektra-augeas
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-augeas-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  5%] Building C object src/plugins/augeas/CMakeFiles/elektra-augeas-objects.dir/augeas.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  5%] Built target elektra-augeas-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-base64
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  5%] Building C object src/plugins/base64/CMakeFiles/elektra-base64.dir/base64_functions.c.o
[  5%] Building C object src/plugins/base64/CMakeFiles/elektra-base64.dir/base64.c.o
[  5%] Linking C shared module ../../../lib/libelektra-base64.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  5%] Built target elektra-base64
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-base64-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  5%] Building C object src/plugins/base64/CMakeFiles/elektra-base64-objects.dir/base64_functions.c.o
[  6%] Building C object src/plugins/base64/CMakeFiles/elektra-base64-objects.dir/base64.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  6%] Built target elektra-base64-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-invoke-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  6%] Building C object src/libs/invoke/CMakeFiles/elektra-invoke-objects.dir/invoke.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  6%] Built target elektra-invoke-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-kdb
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  6%] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/backend.c.o
[  6%] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/kdb.c.o
[  6%] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/mount.c.o
[  6%] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/plugin.c.o
[  6%] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/split.c.o
[  6%] Building C object src/libs/elektra/CMakeFiles/elektra-kdb.dir/trie.c.o
[  7%] Linking C shared library ../../../lib/libelektra-kdb.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  7%] Built target elektra-kdb
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-invoke
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  7%] Linking C shared library ../../../lib/libelektra-invoke.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  7%] Built target elektra-invoke
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-blockresolver
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  7%] Building C object src/plugins/blockresolver/CMakeFiles/elektra-blockresolver.dir/blockresolver.c.o
[  7%] Linking C shared module ../../../lib/libelektra-blockresolver.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  7%] Built target elektra-blockresolver
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-blockresolver-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  7%] Building C object src/plugins/blockresolver/CMakeFiles/elektra-blockresolver-objects.dir/blockresolver.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  7%] Built target elektra-blockresolver-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-c
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  7%] Building C object src/plugins/c/CMakeFiles/elektra-c.dir/c.c.o
[  7%] Linking C shared module ../../../lib/libelektra-c.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  7%] Built target elektra-c
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-c-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  8%] Building C object src/plugins/c/CMakeFiles/elektra-c-objects.dir/c.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  8%] Built target elektra-c-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-cache
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  8%] Building C object src/plugins/cache/CMakeFiles/elektra-cache.dir/cache.c.o
[  8%] Linking C shared module ../../../lib/libelektra-cache.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  8%] Built target elektra-cache
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-cache-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  8%] Building C object src/plugins/cache/CMakeFiles/elektra-cache-objects.dir/cache.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  8%] Built target elektra-cache-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-ccode
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  8%] Building CXX object src/plugins/ccode/CMakeFiles/elektra-ccode.dir/ccode.cpp.o
[  8%] Building CXX object src/plugins/ccode/CMakeFiles/elektra-ccode.dir/coder.cpp.o
[  9%] Linking CXX shared module ../../../lib/libelektra-ccode.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  9%] Built target elektra-ccode
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-ccode-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  9%] Building CXX object src/plugins/ccode/CMakeFiles/elektra-ccode-objects.dir/ccode.cpp.o
[  9%] Building CXX object src/plugins/ccode/CMakeFiles/elektra-ccode-objects.dir/coder.cpp.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  9%] Built target elektra-ccode-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-conditionals
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  9%] Building C object src/plugins/conditionals/CMakeFiles/elektra-conditionals.dir/conditionals.c.o
[  9%] Linking C shared module ../../../lib/libelektra-conditionals.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  9%] Built target elektra-conditionals
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-conditionals-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  9%] Building C object src/plugins/conditionals/CMakeFiles/elektra-conditionals-objects.dir/conditionals.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  9%] Built target elektra-conditionals-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-constants
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 10%] Building C object src/plugins/constants/CMakeFiles/elektra-constants.dir/constants.c.o
[ 10%] Linking C shared module ../../../lib/libelektra-constants.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 10%] Built target elektra-constants
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-constants-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 10%] Building C object src/plugins/constants/CMakeFiles/elektra-constants-objects.dir/constants.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 10%] Built target elektra-constants-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-counter
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 10%] Building C object src/plugins/counter/CMakeFiles/elektra-counter.dir/counter.c.o
[ 10%] Linking C shared module ../../../lib/libelektra-counter.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 10%] Built target elektra-counter
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-counter-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 10%] Building C object src/plugins/counter/CMakeFiles/elektra-counter-objects.dir/counter.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 10%] Built target elektra-counter-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-cpptemplate
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 10%] Building CXX object src/plugins/cpptemplate/CMakeFiles/elektra-cpptemplate.dir/cpptemplate.cpp.o
[ 10%] Building CXX object src/plugins/cpptemplate/CMakeFiles/elektra-cpptemplate.dir/cpptemplate_delegate.cpp.o
[ 11%] Linking CXX shared module ../../../lib/libelektra-cpptemplate.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 11%] Built target elektra-cpptemplate
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-cpptemplate-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 11%] Building CXX object src/plugins/cpptemplate/CMakeFiles/elektra-cpptemplate-objects.dir/cpptemplate.cpp.o
[ 11%] Building CXX object src/plugins/cpptemplate/CMakeFiles/elektra-cpptemplate-objects.dir/cpptemplate_delegate.cpp.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 11%] Built target elektra-cpptemplate-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-crypto
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 11%] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto.dir/gcrypt_operations.c.o
[ 11%] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto.dir/helper.c.o
[ 11%] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto.dir/gpg.c.o
[ 12%] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto.dir/crypto.c.o
[ 12%] Linking C shared module ../../../lib/libelektra-crypto.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 12%] Built target elektra-crypto
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-crypto-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 12%] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto-objects.dir/gcrypt_operations.c.o
[ 12%] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto-objects.dir/helper.c.o
[ 12%] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto-objects.dir/gpg.c.o
[ 12%] Building C object src/plugins/crypto/CMakeFiles/elektra-crypto-objects.dir/crypto.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 12%] Built target elektra-crypto-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-csvstorage
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 12%] Building C object src/plugins/csvstorage/CMakeFiles/elektra-csvstorage.dir/csvstorage.c.o
[ 13%] Linking C shared module ../../../lib/libelektra-csvstorage.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 13%] Built target elektra-csvstorage
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-csvstorage-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 13%] Building C object src/plugins/csvstorage/CMakeFiles/elektra-csvstorage-objects.dir/csvstorage.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 13%] Built target elektra-csvstorage-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-curlget
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 13%] Building C object src/plugins/curlget/CMakeFiles/elektra-curlget.dir/curlget.c.o
[ 13%] Linking C shared module ../../../lib/libelektra-curlget.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 13%] Built target elektra-curlget
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-curlget-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 13%] Building C object src/plugins/curlget/CMakeFiles/elektra-curlget-objects.dir/curlget.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 13%] Built target elektra-curlget-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-date
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 13%] Building C object src/plugins/date/CMakeFiles/elektra-date.dir/date.c.o
[ 14%] Linking C shared module ../../../lib/libelektra-date.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 14%] Built target elektra-date
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-date-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 14%] Building C object src/plugins/date/CMakeFiles/elektra-date-objects.dir/date.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 14%] Built target elektra-date-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-dbus
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 14%] Building C object src/plugins/dbus/CMakeFiles/elektra-dbus.dir/dbus.c.o
[ 14%] Building C object src/plugins/dbus/CMakeFiles/elektra-dbus.dir/sendmessage.c.o
[ 14%] Linking C shared module ../../../lib/libelektra-dbus.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 14%] Built target elektra-dbus
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-dbus-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 14%] Building C object src/plugins/dbus/CMakeFiles/elektra-dbus-objects.dir/dbus.c.o
[ 15%] Building C object src/plugins/dbus/CMakeFiles/elektra-dbus-objects.dir/sendmessage.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Built target elektra-dbus-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-io-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Building C object src/libs/io/CMakeFiles/elektra-io-objects.dir/io.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Built target elektra-io-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-io
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Linking C shared library ../../../lib/libelektra-io.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Built target elektra-io
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target io-adapter-dbus
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Building C object src/libs/io/adapter/dbus/CMakeFiles/io-adapter-dbus.dir/dbus.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Built target io-adapter-dbus
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-dbusrecv
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Building C object src/plugins/dbusrecv/CMakeFiles/elektra-dbusrecv.dir/dbusrecv.c.o
[ 15%] Building C object src/plugins/dbusrecv/CMakeFiles/elektra-dbusrecv.dir/receivemessage.c.o
[ 15%] Linking C shared module ../../../lib/libelektra-dbusrecv.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Built target elektra-dbusrecv
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-dbusrecv-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Building C object src/plugins/dbusrecv/CMakeFiles/elektra-dbusrecv-objects.dir/dbusrecv.c.o
[ 15%] Building C object src/plugins/dbusrecv/CMakeFiles/elektra-dbusrecv-objects.dir/receivemessage.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Built target elektra-dbusrecv-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-desktop
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 16%] Building C object src/plugins/desktop/CMakeFiles/elektra-desktop.dir/desktop.c.o
[ 16%] Linking C shared module ../../../lib/libelektra-desktop.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 16%] Built target elektra-desktop
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-desktop-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 16%] Building C object src/plugins/desktop/CMakeFiles/elektra-desktop-objects.dir/desktop.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 16%] Built target elektra-desktop-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-directoryvalue
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 16%] Building CXX object src/plugins/directoryvalue/CMakeFiles/elektra-directoryvalue.dir/directoryvalue.cpp.o
[ 16%] Building CXX object src/plugins/directoryvalue/CMakeFiles/elektra-directoryvalue.dir/directoryvalue_delegate.cpp.o
[ 16%] Linking CXX shared module ../../../lib/libelektra-directoryvalue.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 16%] Built target elektra-directoryvalue
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-directoryvalue-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 17%] Building CXX object src/plugins/directoryvalue/CMakeFiles/elektra-directoryvalue-objects.dir/directoryvalue.cpp.o
[ 17%] Building CXX object src/plugins/directoryvalue/CMakeFiles/elektra-directoryvalue-objects.dir/directoryvalue_delegate.cpp.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 17%] Built target elektra-directoryvalue-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-doc
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 17%] Building C object src/plugins/doc/CMakeFiles/elektra-doc.dir/doc.c.o
[ 17%] Linking C shared module ../../../lib/libelektra-doc.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 17%] Built target elektra-doc
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-doc-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 17%] Building C object src/plugins/doc/CMakeFiles/elektra-doc-objects.dir/doc.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 17%] Built target elektra-doc-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-dpkg
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 17%] Building C object src/plugins/dpkg/CMakeFiles/elektra-dpkg.dir/dpkg.c.o
[ 17%] Linking C shared module ../../../lib/libelektra-dpkg.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 17%] Built target elektra-dpkg
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-dpkg-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 18%] Building C object src/plugins/dpkg/CMakeFiles/elektra-dpkg-objects.dir/dpkg.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 18%] Built target elektra-dpkg-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-dump
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 18%] Building CXX object src/plugins/dump/CMakeFiles/elektra-dump.dir/dump.cpp.o
[ 18%] Linking CXX shared module ../../../lib/libelektra-dump.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 18%] Built target elektra-dump
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-dump-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 18%] Building CXX object src/plugins/dump/CMakeFiles/elektra-dump-objects.dir/dump.cpp.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 18%] Built target elektra-dump-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-error
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 18%] Building C object src/plugins/error/CMakeFiles/elektra-error.dir/error.c.o
[ 18%] Linking C shared module ../../../lib/libelektra-error.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 18%] Built target elektra-error
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-error-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 19%] Building C object src/plugins/error/CMakeFiles/elektra-error-objects.dir/error.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 19%] Built target elektra-error-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-fcrypt
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 19%] Building C object src/plugins/fcrypt/CMakeFiles/elektra-fcrypt.dir/__/crypto/gpg.c.o
[ 19%] Building C object src/plugins/fcrypt/CMakeFiles/elektra-fcrypt.dir/fcrypt.c.o
[ 19%] Linking C shared module ../../../lib/libelektra-fcrypt.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 19%] Built target elektra-fcrypt
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-fcrypt-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 19%] Building C object src/plugins/fcrypt/CMakeFiles/elektra-fcrypt-objects.dir/__/crypto/gpg.c.o
[ 19%] Building C object src/plugins/fcrypt/CMakeFiles/elektra-fcrypt-objects.dir/fcrypt.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 19%] Built target elektra-fcrypt-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-file
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 20%] Building C object src/plugins/file/CMakeFiles/elektra-file.dir/file.c.o
[ 20%] Linking C shared module ../../../lib/libelektra-file.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 20%] Built target elektra-file
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-file-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 20%] Building C object src/plugins/file/CMakeFiles/elektra-file-objects.dir/file.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 20%] Built target elektra-file-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-filecheck
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 20%] Building C object src/plugins/filecheck/CMakeFiles/elektra-filecheck.dir/filecheck.c.o
../../../../src/plugins/filecheck/filecheck.c: In function 'checkFile':
../../../../src/plugins/filecheck/filecheck.c:212:17: warning: initialization of 'iconv_t' {aka 'long int'} from 'void *' makes integer from pointer without a cast [-Wint-conversion]
  iconv_t conv = NULL;
                 ^~~~
[ 20%] Linking C shared module ../../../lib/libelektra-filecheck.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 20%] Built target elektra-filecheck
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-filecheck-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 20%] Building C object src/plugins/filecheck/CMakeFiles/elektra-filecheck-objects.dir/filecheck.c.o
../../../../src/plugins/filecheck/filecheck.c: In function 'checkFile':
../../../../src/plugins/filecheck/filecheck.c:212:17: warning: initialization of 'iconv_t' {aka 'long int'} from 'void *' makes integer from pointer without a cast [-Wint-conversion]
  iconv_t conv = NULL;
                 ^~~~
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 20%] Built target elektra-filecheck-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-fstab
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Building C object src/plugins/fstab/CMakeFiles/elektra-fstab.dir/fstab.c.o
[ 21%] Linking C shared module ../../../lib/libelektra-fstab.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-fstab
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-fstab-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Building C object src/plugins/fstab/CMakeFiles/elektra-fstab-objects.dir/fstab.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-fstab-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-glob
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Building C object src/plugins/glob/CMakeFiles/elektra-glob.dir/glob.c.o
[ 21%] Linking C shared module ../../../lib/libelektra-glob.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-glob
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-glob-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Building C object src/plugins/glob/CMakeFiles/elektra-glob-objects.dir/glob.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-glob-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-opts-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Building C object src/libs/opts/CMakeFiles/elektra-opts-objects.dir/opts.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-opts-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-opts
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Linking C shared library ../../../lib/libelektra-opts.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-opts
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-gopts
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Building C object src/plugins/gopts/CMakeFiles/elektra-gopts.dir/gopts.c.o
[ 21%] Linking C shared module ../../../lib/libelektra-gopts.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-gopts
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-gopts-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Building C object src/plugins/gopts/CMakeFiles/elektra-gopts-objects.dir/gopts.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-gopts-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-hexcode
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Building C object src/plugins/hexcode/CMakeFiles/elektra-hexcode.dir/hexcode.c.o
[ 21%] Linking C shared module ../../../lib/libelektra-hexcode.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-hexcode
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-hexcode-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 22%] Building C object src/plugins/hexcode/CMakeFiles/elektra-hexcode-objects.dir/hexcode.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 22%] Built target elektra-hexcode-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-hexnumber
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 22%] Building C object src/plugins/hexnumber/CMakeFiles/elektra-hexnumber.dir/hexnumber.c.o
[ 22%] Linking C shared module ../../../lib/libelektra-hexnumber.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 22%] Built target elektra-hexnumber
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-hexnumber-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 22%] Building C object src/plugins/hexnumber/CMakeFiles/elektra-hexnumber-objects.dir/hexnumber.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 22%] Built target elektra-hexnumber-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-hidden
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 22%] Building C object src/plugins/hidden/CMakeFiles/elektra-hidden.dir/hidden.c.o
[ 22%] Linking C shared module ../../../lib/libelektra-hidden.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 22%] Built target elektra-hidden
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-hidden-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 23%] Building C object src/plugins/hidden/CMakeFiles/elektra-hidden-objects.dir/hidden.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 23%] Built target elektra-hidden-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-hosts
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 24%] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts.dir/hosts-get.c.o
[ 24%] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts.dir/hosts-set.c.o
[ 24%] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts.dir/keymetaformatting.c.o
[ 24%] Linking C shared module ../../../lib/libelektra-hosts.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 24%] Built target elektra-hosts
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-hosts-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 24%] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts-objects.dir/hosts-get.c.o
[ 24%] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts-objects.dir/hosts-set.c.o
[ 25%] Building C object src/plugins/hosts/CMakeFiles/elektra-hosts-objects.dir/keymetaformatting.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 25%] Built target elektra-hosts-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-iconv
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 25%] Building C object src/plugins/iconv/CMakeFiles/elektra-iconv.dir/iconv.c.o
[ 25%] Linking C shared module ../../../lib/libelektra-iconv.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 25%] Built target elektra-iconv
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-iconv-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 25%] Building C object src/plugins/iconv/CMakeFiles/elektra-iconv-objects.dir/iconv.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 25%] Built target elektra-iconv-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-ini
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 25%] Building C object src/plugins/ini/CMakeFiles/elektra-ini.dir/ini.c.o
[ 25%] Building C object src/plugins/ini/CMakeFiles/elektra-ini.dir/inih-r29/inih.c.o
[ 25%] Linking C shared module ../../../lib/libelektra-ini.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 25%] Built target elektra-ini
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-ini-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 26%] Building C object src/plugins/ini/CMakeFiles/elektra-ini-objects.dir/ini.c.o
[ 26%] Building C object src/plugins/ini/CMakeFiles/elektra-ini-objects.dir/inih-r29/inih.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 26%] Built target elektra-ini-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-ipaddr
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 27%] Building C object src/plugins/ipaddr/CMakeFiles/elektra-ipaddr.dir/ipaddr.c.o
[ 27%] Linking C shared module ../../../lib/libelektra-ipaddr.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 27%] Built target elektra-ipaddr
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-ipaddr-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 27%] Building C object src/plugins/ipaddr/CMakeFiles/elektra-ipaddr-objects.dir/ipaddr.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 27%] Built target elektra-ipaddr-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-iterate
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 27%] Building C object src/plugins/iterate/CMakeFiles/elektra-iterate.dir/iterate.c.o
[ 27%] Linking C shared module ../../../lib/libelektra-iterate.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 27%] Built target elektra-iterate
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-iterate-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 27%] Building C object src/plugins/iterate/CMakeFiles/elektra-iterate-objects.dir/iterate.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 27%] Built target elektra-iterate-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-kconfig
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 28%] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig.cpp.o
[ 28%] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig_delegate.cpp.o
[ 28%] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig_parser.cpp.o
[ 28%] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig_parser_exception.cpp.o
[ 28%] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/kconfig_serializer.cpp.o
[ 28%] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig.dir/file_utility.cpp.o
[ 29%] Linking CXX shared module ../../../lib/libelektra-kconfig.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 29%] Built target elektra-kconfig
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-kconfig-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 29%] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig.cpp.o
[ 29%] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig_delegate.cpp.o
[ 29%] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig_parser.cpp.o
[ 29%] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig_parser_exception.cpp.o
[ 29%] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/kconfig_serializer.cpp.o
[ 30%] Building CXX object src/plugins/kconfig/CMakeFiles/elektra-kconfig-objects.dir/file_utility.cpp.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 30%] Built target elektra-kconfig-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-keytometa
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 30%] Building C object src/plugins/keytometa/CMakeFiles/elektra-keytometa.dir/keytometa.c.o
[ 30%] Linking C shared module ../../../lib/libelektra-keytometa.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 30%] Built target elektra-keytometa
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-keytometa-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 30%] Building C object src/plugins/keytometa/CMakeFiles/elektra-keytometa-objects.dir/keytometa.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 30%] Built target elektra-keytometa-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-line
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 30%] Building C object src/plugins/line/CMakeFiles/elektra-line.dir/line.c.o
[ 30%] Linking C shared module ../../../lib/libelektra-line.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 30%] Built target elektra-line
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-line-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 31%] Building C object src/plugins/line/CMakeFiles/elektra-line-objects.dir/line.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 31%] Built target elektra-line-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-lineendings
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 31%] Building C object src/plugins/lineendings/CMakeFiles/elektra-lineendings.dir/lineendings.c.o
[ 31%] Linking C shared module ../../../lib/libelektra-lineendings.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 31%] Built target elektra-lineendings
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-lineendings-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 31%] Building C object src/plugins/lineendings/CMakeFiles/elektra-lineendings-objects.dir/lineendings.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 31%] Built target elektra-lineendings-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-list
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 31%] Building C object src/plugins/list/CMakeFiles/elektra-list.dir/list.c.o
[ 31%] Linking C shared module ../../../lib/libelektra-list.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 31%] Built target elektra-list
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-list-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 32%] Building C object src/plugins/list/CMakeFiles/elektra-list-objects.dir/list.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 32%] Built target elektra-list-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-logchange
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 32%] Building C object src/plugins/logchange/CMakeFiles/elektra-logchange.dir/logchange.c.o
[ 32%] Linking C shared module ../../../lib/libelektra-logchange.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 32%] Built target elektra-logchange
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-logchange-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 32%] Building C object src/plugins/logchange/CMakeFiles/elektra-logchange-objects.dir/logchange.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 32%] Built target elektra-logchange-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-macaddr
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 32%] Building C object src/plugins/macaddr/CMakeFiles/elektra-macaddr.dir/macaddr.c.o
[ 32%] Linking C shared module ../../../lib/libelektra-macaddr.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 32%] Built target elektra-macaddr
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-macaddr-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Building C object src/plugins/macaddr/CMakeFiles/elektra-macaddr-objects.dir/macaddr.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Built target elektra-macaddr-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-mathcheck
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Building C object src/plugins/mathcheck/CMakeFiles/elektra-mathcheck.dir/mathcheck.c.o
[ 33%] Building C object src/plugins/mathcheck/CMakeFiles/elektra-mathcheck.dir/floathelper.c.o
[ 33%] Linking C shared module ../../../lib/libelektra-mathcheck.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Built target elektra-mathcheck
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-mathcheck-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Building C object src/plugins/mathcheck/CMakeFiles/elektra-mathcheck-objects.dir/mathcheck.c.o
[ 33%] Building C object src/plugins/mathcheck/CMakeFiles/elektra-mathcheck-objects.dir/floathelper.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Built target elektra-mathcheck-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-utility-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Building C object src/libs/utility/CMakeFiles/elektra-utility-objects.dir/text.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Built target elektra-utility-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-utility
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Linking C shared library ../../../lib/libelektra-utility.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Built target elektra-utility
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-mini
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Building C object src/plugins/mini/CMakeFiles/elektra-mini.dir/mini.c.o
[ 33%] Linking C shared module ../../../lib/libelektra-mini.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Built target elektra-mini
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-mini-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Building C object src/plugins/mini/CMakeFiles/elektra-mini-objects.dir/mini.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Built target elektra-mini-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-mmapstorage
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 34%] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage.dir/dynarray.c.o
[ 34%] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage.dir/mmapstorage.c.o
[ 34%] Linking C shared module ../../../lib/libelektra-mmapstorage.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 34%] Built target elektra-mmapstorage
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-mmapstorage-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 34%] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage-objects.dir/dynarray.c.o
[ 34%] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage-objects.dir/mmapstorage.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 34%] Built target elektra-mmapstorage-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-mmapstorage_crc
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 34%] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage_crc.dir/dynarray.c.o
[ 35%] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage_crc.dir/mmapstorage.c.o
[ 35%] Linking C shared module ../../../lib/libelektra-mmapstorage_crc.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 35%] Built target elektra-mmapstorage_crc
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-mmapstorage_crc-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 35%] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage_crc-objects.dir/dynarray.c.o
[ 35%] Building C object src/plugins/mmapstorage/CMakeFiles/elektra-mmapstorage_crc-objects.dir/mmapstorage.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 35%] Built target elektra-mmapstorage_crc-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-mozprefs
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 35%] Building C object src/plugins/mozprefs/CMakeFiles/elektra-mozprefs.dir/mozprefs.c.o
[ 35%] Linking C shared module ../../../lib/libelektra-mozprefs.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 35%] Built target elektra-mozprefs
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-mozprefs-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 36%] Building C object src/plugins/mozprefs/CMakeFiles/elektra-mozprefs-objects.dir/mozprefs.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 36%] Built target elektra-mozprefs-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-network
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 36%] Building C object src/plugins/network/CMakeFiles/elektra-network.dir/network.c.o
[ 36%] Linking C shared module ../../../lib/libelektra-network.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 36%] Built target elektra-network
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-network-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 36%] Building C object src/plugins/network/CMakeFiles/elektra-network-objects.dir/network.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 36%] Built target elektra-network-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-ni
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 36%] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/ni.c.o
[ 36%] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/nickel-1.1.0/src/buf.c.o
[ 37%] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/nickel-1.1.0/src/hash.c.o
[ 37%] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/nickel-1.1.0/src/io.c.o
[ 37%] Building C object src/plugins/ni/CMakeFiles/elektra-ni.dir/nickel-1.1.0/src/nickel.c.o
[ 37%] Linking C shared module ../../../lib/libelektra-ni.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 37%] Built target elektra-ni
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-ni-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 37%] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/ni.c.o
[ 37%] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/nickel-1.1.0/src/buf.c.o
[ 38%] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/nickel-1.1.0/src/hash.c.o
[ 38%] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/nickel-1.1.0/src/io.c.o
[ 38%] Building C object src/plugins/ni/CMakeFiles/elektra-ni-objects.dir/nickel-1.1.0/src/nickel.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 38%] Built target elektra-ni-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-noresolver
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 38%] Building C object src/plugins/noresolver/CMakeFiles/elektra-noresolver.dir/noresolver.c.o
[ 38%] Linking C shared module ../../../lib/libelektra-noresolver.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 38%] Built target elektra-noresolver
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-noresolver-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 38%] Building C object src/plugins/noresolver/CMakeFiles/elektra-noresolver-objects.dir/noresolver.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 38%] Built target elektra-noresolver-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-null
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 38%] Building C object src/plugins/null/CMakeFiles/elektra-null.dir/null.c.o
[ 39%] Linking C shared module ../../../lib/libelektra-null.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 39%] Built target elektra-null
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-null-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 39%] Building C object src/plugins/null/CMakeFiles/elektra-null-objects.dir/null.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 39%] Built target elektra-null-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-passwd
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 39%] Building C object src/plugins/passwd/CMakeFiles/elektra-passwd.dir/passwd.c.o
[ 39%] Linking C shared module ../../../lib/libelektra-passwd.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 39%] Built target elektra-passwd
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-passwd-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 40%] Building C object src/plugins/passwd/CMakeFiles/elektra-passwd-objects.dir/passwd.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 40%] Built target elektra-passwd-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-path
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 40%] Building C object src/plugins/path/CMakeFiles/elektra-path.dir/path.c.o
[ 40%] Linking C shared module ../../../lib/libelektra-path.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 40%] Built target elektra-path
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-path-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 40%] Building C object src/plugins/path/CMakeFiles/elektra-path-objects.dir/path.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 40%] Built target elektra-path-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-pluginprocess-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 40%] Building C object src/libs/pluginprocess/CMakeFiles/elektra-pluginprocess-objects.dir/pluginprocess.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 40%] Built target elektra-pluginprocess-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-pluginprocess
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 41%] Linking C shared library ../../../lib/libelektra-pluginprocess.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 41%] Built target elektra-pluginprocess
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-process
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 41%] Building C object src/plugins/process/CMakeFiles/elektra-process.dir/process.c.o
[ 41%] Linking C shared module ../../../lib/libelektra-process.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 41%] Built target elektra-process
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-process-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 41%] Building C object src/plugins/process/CMakeFiles/elektra-process-objects.dir/process.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 41%] Built target elektra-process-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-profile
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 41%] Building C object src/plugins/profile/CMakeFiles/elektra-profile.dir/profile.c.o
[ 42%] Linking C shared module ../../../lib/libelektra-profile.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 42%] Built target elektra-profile
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-profile-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 42%] Building C object src/plugins/profile/CMakeFiles/elektra-profile-objects.dir/profile.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 42%] Built target elektra-profile-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-quickdump
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 42%] Building C object src/plugins/quickdump/CMakeFiles/elektra-quickdump.dir/quickdump.c.o
[ 42%] Linking C shared module ../../../lib/libelektra-quickdump.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 42%] Built target elektra-quickdump
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-quickdump-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 43%] Building C object src/plugins/quickdump/CMakeFiles/elektra-quickdump-objects.dir/quickdump.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 43%] Built target elektra-quickdump-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-range
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 43%] Building C object src/plugins/range/CMakeFiles/elektra-range.dir/range.c.o
[ 43%] Linking C shared module ../../../lib/libelektra-range.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 43%] Built target elektra-range
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-range-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 43%] Building C object src/plugins/range/CMakeFiles/elektra-range-objects.dir/range.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 43%] Built target elektra-range-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-globbing-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 44%] Building C object src/libs/globbing/CMakeFiles/elektra-globbing-objects.dir/globbing.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 44%] Built target elektra-globbing-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-globbing
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 44%] Linking C shared library ../../../lib/libelektra-globbing.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 44%] Built target elektra-globbing
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-reference
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 44%] Building C object src/plugins/reference/CMakeFiles/elektra-reference.dir/reference.c.o
[ 44%] Building C object src/plugins/reference/CMakeFiles/elektra-reference.dir/referencegraph.c.o
[ 44%] Linking C shared module ../../../lib/libelektra-reference.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 44%] Built target elektra-reference
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-reference-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 45%] Building C object src/plugins/reference/CMakeFiles/elektra-reference-objects.dir/reference.c.o
[ 45%] Building C object src/plugins/reference/CMakeFiles/elektra-reference-objects.dir/referencegraph.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 45%] Built target elektra-reference-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-rename
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 45%] Building C object src/plugins/rename/CMakeFiles/elektra-rename.dir/rename.c.o
[ 45%] Linking C shared module ../../../lib/libelektra-rename.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 45%] Built target elektra-rename
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-rename-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 45%] Building C object src/plugins/rename/CMakeFiles/elektra-rename-objects.dir/rename.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 45%] Built target elektra-rename-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_hpu_b-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 45%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hpu_b-objects.dir/resolver.c.o
[ 46%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hpu_b-objects.dir/filename.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 46%] Built target elektra-resolver_fm_hpu_b-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_uhb_xb
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 46%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_uhb_xb.dir/resolver.c.o
[ 46%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_uhb_xb.dir/filename.c.o
[ 47%] Linking C shared module ../../../lib/libelektra-resolver_fm_uhb_xb.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 47%] Built target elektra-resolver_fm_uhb_xb
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_xhp_x-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 47%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xhp_x-objects.dir/resolver.c.o
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xhp_x-objects.dir/filename.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_xhp_x-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_xhp_x
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xhp_x.dir/resolver.c.o
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xhp_x.dir/filename.c.o
[ 48%] Linking C shared module ../../../lib/libelektra-resolver_fm_xhp_x.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_xhp_x
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_pb_b-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_pb_b-objects.dir/resolver.c.o
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_pb_b-objects.dir/filename.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_pb_b-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_xp_x
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xp_x.dir/resolver.c.o
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xp_x.dir/filename.c.o
[ 48%] Linking C shared module ../../../lib/libelektra-resolver_fm_xp_x.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_xp_x
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_pb_b
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_pb_b.dir/resolver.c.o
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_pb_b.dir/filename.c.o
[ 48%] Linking C shared module ../../../lib/libelektra-resolver_fm_pb_b.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_pb_b
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_uhb_xb-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_uhb_xb-objects.dir/resolver.c.o
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_uhb_xb-objects.dir/filename.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_uhb_xb-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_b_b-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_b_b-objects.dir/resolver.c.o
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_b_b-objects.dir/filename.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_b_b-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_hp_b
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hp_b.dir/resolver.c.o
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hp_b.dir/filename.c.o
[ 48%] Linking C shared module ../../../lib/libelektra-resolver_fm_hp_b.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_hp_b
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_b_b
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_b_b.dir/resolver.c.o
[ 49%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_b_b.dir/filename.c.o
[ 49%] Linking C shared module ../../../lib/libelektra-resolver_fm_b_b.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 49%] Built target elektra-resolver_fm_b_b
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_hpu_b
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 49%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hpu_b.dir/resolver.c.o
[ 49%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hpu_b.dir/filename.c.o
[ 49%] Linking C shared module ../../../lib/libelektra-resolver_fm_hpu_b.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 49%] Built target elektra-resolver_fm_hpu_b
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_hb_b
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 49%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hb_b.dir/resolver.c.o
[ 49%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hb_b.dir/filename.c.o
[ 50%] Linking C shared module ../../../lib/libelektra-resolver_fm_hb_b.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 50%] Built target elektra-resolver_fm_hb_b
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_hb_b-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 50%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hb_b-objects.dir/resolver.c.o
[ 50%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hb_b-objects.dir/filename.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 50%] Built target elektra-resolver_fm_hb_b-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_xb_x-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 51%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xb_x-objects.dir/resolver.c.o
[ 51%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xb_x-objects.dir/filename.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 51%] Built target elektra-resolver_fm_xb_x-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_xb_x
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 51%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xb_x.dir/resolver.c.o
[ 51%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xb_x.dir/filename.c.o
[ 51%] Linking C shared module ../../../lib/libelektra-resolver_fm_xb_x.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 51%] Built target elektra-resolver_fm_xb_x
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_hp_b-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 52%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hp_b-objects.dir/resolver.c.o
[ 52%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_hp_b-objects.dir/filename.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 52%] Built target elektra-resolver_fm_hp_b-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_ub_x-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 52%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_ub_x-objects.dir/resolver.c.o
[ 52%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_ub_x-objects.dir/filename.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 52%] Built target elektra-resolver_fm_ub_x-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_ub_x
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 52%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_ub_x.dir/resolver.c.o
[ 53%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_ub_x.dir/filename.c.o
[ 53%] Linking C shared module ../../../lib/libelektra-resolver_fm_ub_x.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 53%] Built target elektra-resolver_fm_ub_x
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-resolver_fm_xp_x-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 53%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xp_x-objects.dir/resolver.c.o
[ 53%] Building C object src/plugins/resolver/CMakeFiles/elektra-resolver_fm_xp_x-objects.dir/filename.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 53%] Built target elektra-resolver_fm_xp_x-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-rgbcolor
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 54%] Building C object src/plugins/rgbcolor/CMakeFiles/elektra-rgbcolor.dir/rgbcolor.c.o
[ 54%] Linking C shared module ../../../lib/libelektra-rgbcolor.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 54%] Built target elektra-rgbcolor
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-rgbcolor-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 54%] Building C object src/plugins/rgbcolor/CMakeFiles/elektra-rgbcolor-objects.dir/rgbcolor.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 54%] Built target elektra-rgbcolor-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-shell
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 54%] Building C object src/plugins/shell/CMakeFiles/elektra-shell.dir/shell.c.o
[ 54%] Linking C shared module ../../../lib/libelektra-shell.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 54%] Built target elektra-shell
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-shell-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 54%] Building C object src/plugins/shell/CMakeFiles/elektra-shell-objects.dir/shell.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 54%] Built target elektra-shell-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-spec
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 54%] Building C object src/plugins/spec/CMakeFiles/elektra-spec.dir/spec.c.o
[ 55%] Linking C shared module ../../../lib/libelektra-spec.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 55%] Built target elektra-spec
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-spec-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 55%] Building C object src/plugins/spec/CMakeFiles/elektra-spec-objects.dir/spec.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 55%] Built target elektra-spec-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-specload
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 55%] Building C object src/plugins/specload/CMakeFiles/elektra-specload.dir/specload.c.o
[ 55%] Linking C shared module ../../../lib/libelektra-specload.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 55%] Built target elektra-specload
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-specload-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 55%] Building C object src/plugins/specload/CMakeFiles/elektra-specload-objects.dir/specload.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 55%] Built target elektra-specload-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-sync
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 55%] Building C object src/plugins/sync/CMakeFiles/elektra-sync.dir/sync.c.o
[ 56%] Linking C shared module ../../../lib/libelektra-sync.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 56%] Built target elektra-sync
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-sync-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 56%] Building C object src/plugins/sync/CMakeFiles/elektra-sync-objects.dir/sync.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 56%] Built target elektra-sync-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-syslog
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 56%] Building C object src/plugins/syslog/CMakeFiles/elektra-syslog.dir/syslog.c.o
[ 56%] Linking C shared module ../../../lib/libelektra-syslog.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 56%] Built target elektra-syslog
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-syslog-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 56%] Building C object src/plugins/syslog/CMakeFiles/elektra-syslog-objects.dir/syslog.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 56%] Built target elektra-syslog-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-tcl
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 56%] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl.dir/tcl.cpp.o
[ 57%] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl.dir/action.cpp.o
In file included from ../../../../src/plugins/tcl/action.cpp:18:
/openwrt/staging_dir/target-x86_64_musl/usr/include/boost/bind.hpp:41:1: note: #pragma message: The practice of declaring the Bind placeholders (_1, _2, ...) in the global namespace is deprecated. Please use <boost/bind/bind.hpp> + using namespace boost::placeholders, or define BOOST_BIND_GLOBAL_PLACEHOLDERS to retain the current behavior.
 )
 ^
[ 57%] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl.dir/printer.cpp.o
[ 57%] Linking CXX shared module ../../../lib/libelektra-tcl.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 57%] Built target elektra-tcl
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-tcl-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 57%] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl-objects.dir/tcl.cpp.o
[ 57%] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl-objects.dir/action.cpp.o
In file included from ../../../../src/plugins/tcl/action.cpp:18:
/openwrt/staging_dir/target-x86_64_musl/usr/include/boost/bind.hpp:41:1: note: #pragma message: The practice of declaring the Bind placeholders (_1, _2, ...) in the global namespace is deprecated. Please use <boost/bind/bind.hpp> + using namespace boost::placeholders, or define BOOST_BIND_GLOBAL_PLACEHOLDERS to retain the current behavior.
 )
 ^
[ 57%] Building CXX object src/plugins/tcl/CMakeFiles/elektra-tcl-objects.dir/printer.cpp.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 57%] Built target elektra-tcl-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-template
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 58%] Building C object src/plugins/template/CMakeFiles/elektra-template.dir/template.c.o
[ 58%] Linking C shared module ../../../lib/libelektra-template.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 58%] Built target elektra-template
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-template-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 58%] Building C object src/plugins/template/CMakeFiles/elektra-template-objects.dir/template.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 58%] Built target elektra-template-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-timeofday
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 58%] Building C object src/plugins/timeofday/CMakeFiles/elektra-timeofday.dir/timeofday.c.o
[ 58%] Linking C shared module ../../../lib/libelektra-timeofday.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 58%] Built target elektra-timeofday
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-timeofday-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 58%] Building C object src/plugins/timeofday/CMakeFiles/elektra-timeofday-objects.dir/timeofday.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 58%] Built target elektra-timeofday-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-tracer
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 59%] Building C object src/plugins/tracer/CMakeFiles/elektra-tracer.dir/tracer.c.o
[ 59%] Linking C shared module ../../../lib/libelektra-tracer.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 59%] Built target elektra-tracer
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-tracer-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 59%] Building C object src/plugins/tracer/CMakeFiles/elektra-tracer-objects.dir/tracer.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 59%] Built target elektra-tracer-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-type
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 59%] Building C object src/plugins/type/CMakeFiles/elektra-type.dir/type.c.o
[ 59%] Building C object src/plugins/type/CMakeFiles/elektra-type.dir/types.c.o
[ 59%] Linking C shared module ../../../lib/libelektra-type.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 59%] Built target elektra-type
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-type-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 59%] Building C object src/plugins/type/CMakeFiles/elektra-type-objects.dir/type.c.o
[ 60%] Building C object src/plugins/type/CMakeFiles/elektra-type-objects.dir/types.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 60%] Built target elektra-type-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-uname
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 60%] Building C object src/plugins/uname/CMakeFiles/elektra-uname.dir/uname.c.o
[ 60%] Linking C shared module ../../../lib/libelektra-uname.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 60%] Built target elektra-uname
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-uname-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 60%] Building C object src/plugins/uname/CMakeFiles/elektra-uname-objects.dir/uname.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 60%] Built target elektra-uname-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-unit
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 60%] Building C object src/plugins/unit/CMakeFiles/elektra-unit.dir/unit.c.o
[ 60%] Linking C shared module ../../../lib/libelektra-unit.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 60%] Built target elektra-unit
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-unit-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 61%] Building C object src/plugins/unit/CMakeFiles/elektra-unit-objects.dir/unit.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 61%] Built target elektra-unit-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-validation
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 61%] Building C object src/plugins/validation/CMakeFiles/elektra-validation.dir/validation.c.o
[ 61%] Building C object src/plugins/validation/CMakeFiles/elektra-validation.dir/lookupre.c.o
[ 61%] Linking C shared module ../../../lib/libelektra-validation.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 61%] Built target elektra-validation
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-validation-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 62%] Building C object src/plugins/validation/CMakeFiles/elektra-validation-objects.dir/validation.c.o
[ 62%] Building C object src/plugins/validation/CMakeFiles/elektra-validation-objects.dir/lookupre.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 62%] Built target elektra-validation-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-wresolver
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 62%] Building C object src/plugins/wresolver/CMakeFiles/elektra-wresolver.dir/wresolver.c.o
[ 62%] Linking C shared module ../../../lib/libelektra-wresolver.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 62%] Built target elektra-wresolver
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-wresolver-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 62%] Building C object src/plugins/wresolver/CMakeFiles/elektra-wresolver-objects.dir/wresolver.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 62%] Built target elektra-wresolver-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-xerces
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 62%] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces.dir/xerces.cpp.o
[ 63%] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces.dir/deserializer.cpp.o
[ 63%] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces.dir/serializer.cpp.o
[ 63%] Linking CXX shared module ../../../lib/libelektra-xerces.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 63%] Built target elektra-xerces
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-xerces-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 63%] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces-objects.dir/xerces.cpp.o
[ 63%] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces-objects.dir/deserializer.cpp.o
[ 63%] Building CXX object src/plugins/xerces/CMakeFiles/elektra-xerces-objects.dir/serializer.cpp.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 63%] Built target elektra-xerces-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-xmltool
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 64%] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool.dir/xmltool.c.o
[ 64%] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool.dir/stream.c.o
[ 64%] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool.dir/kdbtools.c.o
[ 64%] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool.dir/kscompare.c.o
[ 64%] Linking C shared module ../../../lib/libelektra-xmltool.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 64%] Built target elektra-xmltool
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-xmltool-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 64%] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool-objects.dir/xmltool.c.o
[ 64%] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool-objects.dir/stream.c.o
[ 65%] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool-objects.dir/kdbtools.c.o
[ 65%] Building C object src/plugins/xmltool/CMakeFiles/elektra-xmltool-objects.dir/kscompare.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 65%] Built target elektra-xmltool-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-yajl
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 65%] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl.c.o
[ 65%] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/iterator.c.o
[ 65%] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl_gen.c.o
[ 65%] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl_gen_open.c.o
[ 66%] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl_gen_close.c.o
[ 66%] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/yajl_parse.c.o
[ 66%] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl.dir/name.c.o
[ 66%] Linking C shared module ../../../lib/libelektra-yajl.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 66%] Built target elektra-yajl
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-yajl-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 66%] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl.c.o
[ 66%] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/iterator.c.o
[ 67%] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl_gen.c.o
[ 67%] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl_gen_open.c.o
[ 67%] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl_gen_close.c.o
[ 67%] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/yajl_parse.c.o
[ 67%] Building C object src/plugins/yajl/CMakeFiles/elektra-yajl-objects.dir/name.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 67%] Built target elektra-yajl-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-yamlcpp
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 67%] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp.dir/yamlcpp.cpp.o
[ 68%] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp.dir/read.cpp.o
[ 68%] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp.dir/write.cpp.o
[ 68%] Linking CXX shared module ../../../lib/libelektra-yamlcpp.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 68%] Built target elektra-yamlcpp
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-yamlcpp-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 68%] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp-objects.dir/yamlcpp.cpp.o
[ 68%] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp-objects.dir/read.cpp.o
[ 68%] Building CXX object src/plugins/yamlcpp/CMakeFiles/elektra-yamlcpp-objects.dir/write.cpp.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 68%] Built target elektra-yamlcpp-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-yamlsmith
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 69%] Building CXX object src/plugins/yamlsmith/CMakeFiles/elektra-yamlsmith.dir/yamlsmith.cpp.o
[ 69%] Linking CXX shared module ../../../lib/libelektra-yamlsmith.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 69%] Built target elektra-yamlsmith
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-yamlsmith-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 69%] Building CXX object src/plugins/yamlsmith/CMakeFiles/elektra-yamlsmith-objects.dir/yamlsmith.cpp.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 69%] Built target elektra-yamlsmith-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target io-adapter-zeromq
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 70%] Building C object src/libs/io/adapter/zeromq/CMakeFiles/io-adapter-zeromq.dir/zeromq.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 70%] Built target io-adapter-zeromq
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-zeromqrecv
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 70%] Building C object src/plugins/zeromqrecv/CMakeFiles/elektra-zeromqrecv.dir/zeromqrecv.c.o
[ 70%] Building C object src/plugins/zeromqrecv/CMakeFiles/elektra-zeromqrecv.dir/subscribe.c.o
[ 70%] Linking C shared module ../../../lib/libelektra-zeromqrecv.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 70%] Built target elektra-zeromqrecv
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-zeromqrecv-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 70%] Building C object src/plugins/zeromqrecv/CMakeFiles/elektra-zeromqrecv-objects.dir/zeromqrecv.c.o
[ 71%] Building C object src/plugins/zeromqrecv/CMakeFiles/elektra-zeromqrecv-objects.dir/subscribe.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 71%] Built target elektra-zeromqrecv-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-zeromqsend
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 71%] Building C object src/plugins/zeromqsend/CMakeFiles/elektra-zeromqsend.dir/zeromqsend.c.o
[ 71%] Building C object src/plugins/zeromqsend/CMakeFiles/elektra-zeromqsend.dir/publish.c.o
[ 71%] Linking C shared module ../../../lib/libelektra-zeromqsend.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 71%] Built target elektra-zeromqsend
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-zeromqsend-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 71%] Building C object src/plugins/zeromqsend/CMakeFiles/elektra-zeromqsend-objects.dir/zeromqsend.c.o
[ 71%] Building C object src/plugins/zeromqsend/CMakeFiles/elektra-zeromqsend-objects.dir/publish.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 71%] Built target elektra-zeromqsend-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektratools
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 72%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/backend.cpp.o
[ 72%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/backendbuilder.cpp.o
[ 72%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/backendparser.cpp.o
[ 72%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/backends.cpp.o
[ 72%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/helper/comparison.cpp.o
[ 72%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/helper/keyhelper.cpp.o
[ 73%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/automergeconfiguration.cpp.o
[ 73%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/automergestrategy.cpp.o
[ 73%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/importmergeconfiguration.cpp.o
[ 73%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/interactivemergestrategy.cpp.o
[ 73%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/mergeconflictstrategy.cpp.o
[ 73%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/mergeresult.cpp.o
[ 74%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/mergingkdb.cpp.o
[ 74%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/metamergestrategy.cpp.o
[ 74%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/newkeystrategy.cpp.o
[ 74%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/onesidemergeconfiguration.cpp.o
[ 74%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/onesidestrategy.cpp.o
[ 74%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/onesidevaluestrategy.cpp.o
[ 75%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/overwritemergeconfiguration.cpp.o
[ 75%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/merging/threewaymerge.cpp.o
[ 75%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/modules.cpp.o
[ 75%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/plugin.cpp.o
[ 75%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/plugindatabase.cpp.o
[ 75%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/plugins.cpp.o
[ 75%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/pluginspec.cpp.o
[ 76%] Building CXX object src/libs/tools/src/CMakeFiles/elektratools.dir/specreader.cpp.o
[ 76%] Linking CXX shared library ../../../../lib/libelektratools.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Built target elektratools
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target merging
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Building CXX object src/libs/tools/examples/CMakeFiles/merging.dir/merging.cpp.o
[ 76%] Linking CXX executable ../../../../bin/merging
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Built target merging
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target backend
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Building CXX object src/libs/tools/examples/CMakeFiles/backend.dir/backend.cpp.o
[ 76%] Linking CXX executable ../../../../bin/backend
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Built target backend
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target benchmark_plugins
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Building CXX object src/libs/tools/benchmarks/CMakeFiles/benchmark_plugins.dir/benchmark_plugins.cpp.o
[ 76%] Linking CXX executable ../../../../bin/benchmark_plugins
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Built target benchmark_plugins
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-highlevel-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Building C object src/libs/highlevel/CMakeFiles/elektra-highlevel-objects.dir/elektra.c.o
[ 76%] Building C object src/libs/highlevel/CMakeFiles/elektra-highlevel-objects.dir/elektra_array_value.c.o
[ 76%] Building C object src/libs/highlevel/CMakeFiles/elektra-highlevel-objects.dir/elektra_error.c.o
[ 76%] Building C object src/libs/highlevel/CMakeFiles/elektra-highlevel-objects.dir/elektra_value.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Built target elektra-highlevel-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-highlevel
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Linking C shared library ../../../lib/libelektra-highlevel.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Built target elektra-highlevel
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-merge-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Building C object src/libs/merge/CMakeFiles/elektra-merge-objects.dir/kdbmerge.c.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Built target elektra-merge-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra-merge
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 77%] Linking C shared library ../../../lib/libelektra-merge.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 77%] Built target elektra-merge
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target cpp_cascading
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 77%] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_cascading.dir/cpp_cascading.cpp.o
[ 77%] Linking CXX executable ../../../../bin/cpp_cascading
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 77%] Built target cpp_cascading
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target cpp_example_dup
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 78%] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_dup.dir/cpp_example_dup.cpp.o
[ 78%] Linking CXX executable ../../../../bin/cpp_example_dup
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 78%] Built target cpp_example_dup
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target cpp_example_get
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 78%] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_get.dir/cpp_example_get.cpp.o
[ 78%] Linking CXX executable ../../../../bin/cpp_example_get
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 78%] Built target cpp_example_get
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target cpp_example_set
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 79%] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_set.dir/cpp_example_set.cpp.o
[ 79%] Linking CXX executable ../../../../bin/cpp_example_set
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 79%] Built target cpp_example_set
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target cpp_example_userio
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 79%] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_userio.dir/cpp_example_userio.cpp.o
[ 79%] Linking CXX executable ../../../../bin/cpp_example_userio
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 79%] Built target cpp_example_userio
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target cpp_example_hello
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 79%] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_hello.dir/cpp_example_hello.cpp.o
[ 79%] Linking CXX executable ../../../../bin/cpp_example_hello
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 79%] Built target cpp_example_hello
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target cpp_example_hierarchy
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 80%] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_hierarchy.dir/cpp_example_hierarchy.cpp.o
[ 80%] Linking CXX executable ../../../../bin/cpp_example_hierarchy
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 80%] Built target cpp_example_hierarchy
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target cpp_example_iter
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 80%] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_iter.dir/cpp_example_iter.cpp.o
[ 80%] Linking CXX executable ../../../../bin/cpp_example_iter
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 80%] Built target cpp_example_iter
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target cpp_example_io
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 80%] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_io.dir/cpp_example_io.cpp.o
[ 80%] Linking CXX executable ../../../../bin/cpp_example_io
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 80%] Built target cpp_example_io
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target cpp_example_iter_name
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 81%] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_iter_name.dir/cpp_example_iter_name.cpp.o
[ 81%] Linking CXX executable ../../../../bin/cpp_example_iter_name
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 81%] Built target cpp_example_iter_name
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target cpp_example_ks
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 81%] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_ks.dir/cpp_example_ks.cpp.o
[ 81%] Linking CXX executable ../../../../bin/cpp_example_ks
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 81%] Built target cpp_example_ks
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target cpp_example_ordering
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 81%] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_ordering.dir/cpp_example_ordering.cpp.o
[ 81%] Linking CXX executable ../../../../bin/cpp_example_ordering
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 81%] Built target cpp_example_ordering
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target cpp_example_userexception
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 81%] Building CXX object src/bindings/cpp/examples/CMakeFiles/cpp_example_userexception.dir/cpp_example_userexception.cpp.o
[ 81%] Linking CXX executable ../../../../bin/cpp_example_userexception
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 81%] Built target cpp_example_userexception
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target benchmark_thread
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 82%] Building CXX object src/bindings/cpp/benchmarks/CMakeFiles/benchmark_thread.dir/benchmark_thread.cpp.o
[ 82%] Linking CXX executable ../../../../bin/benchmark_thread
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 82%] Built target benchmark_thread
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target benchmark_sync
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 82%] Building CXX object src/bindings/cpp/benchmarks/CMakeFiles/benchmark_sync.dir/benchmark_sync.cpp.o
[ 82%] Linking CXX executable ../../../../bin/benchmark_sync
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 82%] Built target benchmark_sync
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target kdb_gen_templates_generated
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 82%] Generating ../../../../include/gen/templates.hpp
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 82%] Built target kdb_gen_templates_generated
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target kdb-objects
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 82%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/ansicolors.cpp.o
[ 82%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/cache.cpp.o
[ 83%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/cmdline.cpp.o
[ 83%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/cmerge.cpp.o
[ 83%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/command.cpp.o
[ 83%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/complete.cpp.o
[ 83%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/convert.cpp.o
[ 83%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/cp.cpp.o
[ 84%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/editor.cpp.o
[ 84%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/export.cpp.o
[ 84%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/external.cpp.o
[ 84%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/file.cpp.o
[ 84%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/find.cpp.o
[ 84%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen.cpp.o
[ 84%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/highlevel/common.cpp.o
[ 85%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/highlevel/enums.cpp.o
[ 85%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/highlevel/highlevel.cpp.o
[ 85%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/highlevel/structs.cpp.o
[ 85%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/gen/template.cpp.o
[ 85%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/get.cpp.o
[ 85%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/globalmount.cpp.o
[ 86%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/globalumount.cpp.o
[ 86%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/import.cpp.o
[ 86%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/listcommands.cpp.o
[ 86%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/ls.cpp.o
[ 86%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/main.cpp.o
[ 86%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/merge.cpp.o
[ 87%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/mergehelper.cpp.o
[ 87%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/metaget.cpp.o
[ 87%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/metals.cpp.o
[ 87%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/metaremove.cpp.o
[ 87%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/metaset.cpp.o
[ 87%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/mount.cpp.o
[ 88%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/mountbase.cpp.o
[ 88%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/mv.cpp.o
[ 88%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/plugincheck.cpp.o
[ 88%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/plugininfo.cpp.o
[ 88%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/pluginlist.cpp.o
[ 88%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/remount.cpp.o
[ 89%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/rm.cpp.o
[ 89%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/set.cpp.o
[ 89%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/sget.cpp.o
[ 89%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/shell.cpp.o
[ 89%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/showmeta.cpp.o
[ 89%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/specmount.cpp.o
[ 89%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/test.cpp.o
[ 90%] Building CXX object src/tools/kdb/CMakeFiles/kdb-objects.dir/umount.cpp.o
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 90%] Built target kdb-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target kdb
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 90%] Linking CXX executable ../../../bin/kdb
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 90%] Built target kdb
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target elektra_config_headers
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 90%] Built target elektra_config_headers
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target set_key
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 90%] Building C object examples/CMakeFiles/set_key.dir/set_key.c.o
[ 90%] Linking C executable ../bin/set_key
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 90%] Built target set_key
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target keyBasename
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 91%] Building C object examples/CMakeFiles/keyBasename.dir/keyBasename.c.o
[ 91%] Linking C executable ../bin/keyBasename
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 91%] Built target keyBasename
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target kdbopen
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 91%] Building C object examples/CMakeFiles/kdbopen.dir/kdbopen.c.o
[ 91%] Linking C executable ../bin/kdbopen
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 91%] Built target kdbopen
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target optsSnippets
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 91%] Building C object examples/CMakeFiles/optsSnippets.dir/optsSnippets.c.o
[ 92%] Linking C executable ../bin/optsSnippets
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Built target optsSnippets
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target kdbget_error
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Building C object examples/CMakeFiles/kdbget_error.dir/kdbget_error.c.o
[ 92%] Linking C executable ../bin/kdbget_error
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Built target kdbget_error
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target reference
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Building C object examples/CMakeFiles/reference.dir/reference.c.o
[ 92%] Linking C executable ../bin/reference
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Built target reference
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target kdbget
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Building C object examples/CMakeFiles/kdbget.dir/kdbget.c.o
[ 92%] Linking C executable ../bin/kdbget
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Built target kdbget
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target hello
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Building C object examples/CMakeFiles/hello.dir/hello.c.o
[ 92%] Linking C executable ../bin/hello
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Built target hello
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target keyNew
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Building C object examples/CMakeFiles/keyNew.dir/keyNew.c.o
[ 92%] Linking C executable ../bin/keyNew
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Built target keyNew
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target keyCopy
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Building C object examples/CMakeFiles/keyCopy.dir/keyCopy.c.o
[ 92%] Linking C executable ../bin/keyCopy
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Built target keyCopy
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target ksIterate
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Building C object examples/CMakeFiles/ksIterate.dir/ksIterate.c.o
[ 93%] Linking C executable ../bin/ksIterate
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 93%] Built target ksIterate
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target functional
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 93%] Building C object examples/CMakeFiles/functional.dir/functional.c.o
[ 93%] Linking C executable ../bin/functional
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 93%] Built target functional
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target keyNewExample
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 94%] Building C object examples/CMakeFiles/keyNewExample.dir/keyNewExample.c.o
[ 94%] Linking C executable ../bin/keyNewExample
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 94%] Built target keyNewExample
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target keyMetaKeySet
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 95%] Building C object examples/CMakeFiles/keyMetaKeySet.dir/keyMetaKeySet.c.o
[ 95%] Linking C executable ../bin/keyMetaKeySet
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 95%] Built target keyMetaKeySet
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target cascading
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 95%] Building C object examples/CMakeFiles/cascading.dir/cascading.c.o
[ 95%] Linking C executable ../bin/cascading
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 95%] Built target cascading
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target gopts
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 95%] Building C object examples/CMakeFiles/gopts.dir/gopts.c.o
[ 96%] Linking C executable ../bin/gopts
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 96%] Built target gopts
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target keyName
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 96%] Building C object examples/CMakeFiles/keyName.dir/keyName.c.o
[ 96%] Linking C executable ../bin/keyName
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 96%] Built target keyName
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target kdbintro
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Building C object examples/CMakeFiles/kdbintro.dir/kdbintro.c.o
[ 97%] Linking C executable ../bin/kdbintro
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target kdbintro
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target opts
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Building C object examples/CMakeFiles/opts.dir/opts.c.o
[ 97%] Linking C executable ../bin/opts
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target opts
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target iterate
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Building C object examples/CMakeFiles/iterate.dir/iterate.c.o
[ 97%] Linking C executable ../bin/iterate
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target iterate
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target kdbset
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Building C object examples/CMakeFiles/kdbset.dir/kdbset.c.o
[ 97%] Linking C executable ../bin/kdbset
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target kdbset
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target helloElektra
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Building C object examples/CMakeFiles/helloElektra.dir/helloElektra.c.o
[ 97%] Linking C executable ../bin/helloElektra
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target helloElektra
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target keyset
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Building C object examples/CMakeFiles/keyset.dir/keyset.c.o
[ 97%] Linking C executable ../bin/keyset
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target keyset
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target meta
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Building C object examples/CMakeFiles/meta.dir/meta.c.o
[ 97%] Linking C executable ../bin/meta
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target meta
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target ksCut
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Building C object examples/CMakeFiles/ksCut.dir/ksCut.c.o
[ 97%] Linking C executable ../bin/ksCut
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target ksCut
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target ksNewExample
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Building C object examples/CMakeFiles/ksNewExample.dir/ksNewExample.c.o
[ 98%] Linking C executable ../bin/ksNewExample
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Built target ksNewExample
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target optsCommands
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Building C object examples/CMakeFiles/optsCommands.dir/optsCommands.c.o
[ 98%] Linking C executable ../bin/optsCommands
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Built target optsCommands
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target ksLookupPop
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Building C object examples/CMakeFiles/ksLookupPop.dir/ksLookupPop.c.o
[ 98%] Linking C executable ../bin/ksLookupPop
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Built target ksLookupPop
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target keyMeta
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Building C object examples/CMakeFiles/keyMeta.dir/keyMeta.c.o
[ 98%] Linking C executable ../bin/keyMeta
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Built target keyMeta
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target ksNew
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Building C object examples/CMakeFiles/ksNew.dir/ksNew.c.o
[ 98%] Linking C executable ../bin/ksNew
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Built target ksNew
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Scanning dependencies of target namespace
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Building C object examples/CMakeFiles/namespace.dir/namespace.c.o
[100%] Linking C executable ../bin/namespace
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[100%] Built target namespace
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  0%] Built target generate_version_script
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  3%] Built target elektra-core
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-ease-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-ease
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-proposal-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-proposal
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-meta-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-meta
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-plugin-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  4%] Built target elektra-plugin
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  5%] Built target elektra-augeas
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  5%] Built target elektra-augeas-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  5%] Built target elektra-base64
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  6%] Built target elektra-base64-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  6%] Built target elektra-invoke-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  7%] Built target elektra-kdb
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  7%] Built target elektra-invoke
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  7%] Built target elektra-blockresolver
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  7%] Built target elektra-blockresolver-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  7%] Built target elektra-c
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  8%] Built target elektra-c-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  8%] Built target elektra-cache
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  8%] Built target elektra-cache-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  9%] Built target elektra-ccode
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  9%] Built target elektra-ccode-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  9%] Built target elektra-conditionals
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[  9%] Built target elektra-conditionals-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 10%] Built target elektra-constants
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 10%] Built target elektra-constants-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 10%] Built target elektra-counter
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 10%] Built target elektra-counter-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 11%] Built target elektra-cpptemplate
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 11%] Built target elektra-cpptemplate-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 12%] Built target elektra-crypto
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 12%] Built target elektra-crypto-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 13%] Built target elektra-csvstorage
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 13%] Built target elektra-csvstorage-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 13%] Built target elektra-curlget
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 13%] Built target elektra-curlget-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 14%] Built target elektra-date
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 14%] Built target elektra-date-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 14%] Built target elektra-dbus
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Built target elektra-dbus-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Built target elektra-io-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Built target elektra-io
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Built target io-adapter-dbus
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Built target elektra-dbusrecv
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 15%] Built target elektra-dbusrecv-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 16%] Built target elektra-desktop
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 16%] Built target elektra-desktop-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 16%] Built target elektra-directoryvalue
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 17%] Built target elektra-directoryvalue-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 17%] Built target elektra-doc
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 17%] Built target elektra-doc-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 17%] Built target elektra-dpkg
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 18%] Built target elektra-dpkg-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 18%] Built target elektra-dump
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 18%] Built target elektra-dump-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 18%] Built target elektra-error
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 19%] Built target elektra-error-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 19%] Built target elektra-fcrypt
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 19%] Built target elektra-fcrypt-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 20%] Built target elektra-file
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 20%] Built target elektra-file-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 20%] Built target elektra-filecheck
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 20%] Built target elektra-filecheck-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-fstab
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-fstab-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-glob
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-glob-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-opts-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-opts
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-gopts
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-gopts-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 21%] Built target elektra-hexcode
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 22%] Built target elektra-hexcode-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 22%] Built target elektra-hexnumber
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 22%] Built target elektra-hexnumber-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 22%] Built target elektra-hidden
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 23%] Built target elektra-hidden-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 24%] Built target elektra-hosts
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 25%] Built target elektra-hosts-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 25%] Built target elektra-iconv
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 25%] Built target elektra-iconv-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 25%] Built target elektra-ini
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 26%] Built target elektra-ini-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 27%] Built target elektra-ipaddr
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 27%] Built target elektra-ipaddr-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 27%] Built target elektra-iterate
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 27%] Built target elektra-iterate-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 29%] Built target elektra-kconfig
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 30%] Built target elektra-kconfig-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 30%] Built target elektra-keytometa
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 30%] Built target elektra-keytometa-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 30%] Built target elektra-line
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 31%] Built target elektra-line-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 31%] Built target elektra-lineendings
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 31%] Built target elektra-lineendings-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 31%] Built target elektra-list
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 32%] Built target elektra-list-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 32%] Built target elektra-logchange
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 32%] Built target elektra-logchange-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 32%] Built target elektra-macaddr
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Built target elektra-macaddr-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Built target elektra-mathcheck
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Built target elektra-mathcheck-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Built target elektra-utility-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Built target elektra-utility
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Built target elektra-mini
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 33%] Built target elektra-mini-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 34%] Built target elektra-mmapstorage
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 34%] Built target elektra-mmapstorage-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 35%] Built target elektra-mmapstorage_crc
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 35%] Built target elektra-mmapstorage_crc-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 35%] Built target elektra-mozprefs
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 36%] Built target elektra-mozprefs-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 36%] Built target elektra-network
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 36%] Built target elektra-network-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 37%] Built target elektra-ni
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 38%] Built target elektra-ni-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 38%] Built target elektra-noresolver
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 38%] Built target elektra-noresolver-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 39%] Built target elektra-null
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 39%] Built target elektra-null-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 39%] Built target elektra-passwd
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 40%] Built target elektra-passwd-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 40%] Built target elektra-path
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 40%] Built target elektra-path-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 40%] Built target elektra-pluginprocess-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 41%] Built target elektra-pluginprocess
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 41%] Built target elektra-process
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 41%] Built target elektra-process-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 42%] Built target elektra-profile
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 42%] Built target elektra-profile-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 42%] Built target elektra-quickdump
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 43%] Built target elektra-quickdump-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 43%] Built target elektra-range
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 43%] Built target elektra-range-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 44%] Built target elektra-globbing-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 44%] Built target elektra-globbing
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 44%] Built target elektra-reference
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 45%] Built target elektra-reference-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 45%] Built target elektra-rename
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 45%] Built target elektra-rename-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 46%] Built target elektra-resolver_fm_hpu_b-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 47%] Built target elektra-resolver_fm_uhb_xb
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_xhp_x-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_xhp_x
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_pb_b-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_xp_x
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_pb_b
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_uhb_xb-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_b_b-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 48%] Built target elektra-resolver_fm_hp_b
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 49%] Built target elektra-resolver_fm_b_b
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 49%] Built target elektra-resolver_fm_hpu_b
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 50%] Built target elektra-resolver_fm_hb_b
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 50%] Built target elektra-resolver_fm_hb_b-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 51%] Built target elektra-resolver_fm_xb_x-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 51%] Built target elektra-resolver_fm_xb_x
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 52%] Built target elektra-resolver_fm_hp_b-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 52%] Built target elektra-resolver_fm_ub_x-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 53%] Built target elektra-resolver_fm_ub_x
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 53%] Built target elektra-resolver_fm_xp_x-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 54%] Built target elektra-rgbcolor
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 54%] Built target elektra-rgbcolor-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 54%] Built target elektra-shell
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 54%] Built target elektra-shell-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 55%] Built target elektra-spec
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 55%] Built target elektra-spec-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 55%] Built target elektra-specload
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 55%] Built target elektra-specload-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 56%] Built target elektra-sync
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 56%] Built target elektra-sync-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 56%] Built target elektra-syslog
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 56%] Built target elektra-syslog-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 57%] Built target elektra-tcl
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 57%] Built target elektra-tcl-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 58%] Built target elektra-template
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 58%] Built target elektra-template-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 58%] Built target elektra-timeofday
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 58%] Built target elektra-timeofday-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 59%] Built target elektra-tracer
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 59%] Built target elektra-tracer-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 59%] Built target elektra-type
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 60%] Built target elektra-type-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 60%] Built target elektra-uname
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 60%] Built target elektra-uname-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 60%] Built target elektra-unit
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 61%] Built target elektra-unit-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 61%] Built target elektra-validation
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 62%] Built target elektra-validation-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 62%] Built target elektra-wresolver
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 62%] Built target elektra-wresolver-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 63%] Built target elektra-xerces
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 63%] Built target elektra-xerces-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 64%] Built target elektra-xmltool
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 65%] Built target elektra-xmltool-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 66%] Built target elektra-yajl
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 67%] Built target elektra-yajl-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 68%] Built target elektra-yamlcpp
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 68%] Built target elektra-yamlcpp-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 69%] Built target elektra-yamlsmith
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 69%] Built target elektra-yamlsmith-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 70%] Built target io-adapter-zeromq
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 70%] Built target elektra-zeromqrecv
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 71%] Built target elektra-zeromqrecv-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 71%] Built target elektra-zeromqsend
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 71%] Built target elektra-zeromqsend-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Built target elektratools
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Built target merging
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Built target backend
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Built target benchmark_plugins
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Built target elektra-highlevel-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Built target elektra-highlevel
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 76%] Built target elektra-merge-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 77%] Built target elektra-merge
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 77%] Built target cpp_cascading
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 78%] Built target cpp_example_dup
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 78%] Built target cpp_example_get
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 79%] Built target cpp_example_set
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 79%] Built target cpp_example_userio
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 79%] Built target cpp_example_hello
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 80%] Built target cpp_example_hierarchy
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 80%] Built target cpp_example_iter
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 80%] Built target cpp_example_io
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 81%] Built target cpp_example_iter_name
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 81%] Built target cpp_example_ks
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 81%] Built target cpp_example_ordering
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 81%] Built target cpp_example_userexception
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 82%] Built target benchmark_thread
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 82%] Built target benchmark_sync
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 82%] Built target kdb_gen_templates_generated
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 90%] Built target kdb-objects
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 90%] Built target kdb
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 90%] Built target elektra_config_headers
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 90%] Built target set_key
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 91%] Built target keyBasename
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 91%] Built target kdbopen
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Built target optsSnippets
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Built target kdbget_error
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Built target reference
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Built target kdbget
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Built target hello
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Built target keyNew
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 92%] Built target keyCopy
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 93%] Built target ksIterate
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 93%] Built target functional
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 94%] Built target keyNewExample
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 95%] Built target keyMetaKeySet
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 95%] Built target cascading
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 96%] Built target gopts
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 96%] Built target keyName
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target kdbintro
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target opts
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target iterate
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target kdbset
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target helloElektra
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target keyset
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target meta
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 97%] Built target ksCut
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Built target ksNewExample
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Built target optsCommands
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Built target ksLookupPop
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Built target keyMeta
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[ 98%] Built target ksNew
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
[100%] Built target namespace
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
Install the project...
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
-- Installing: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-install/usr/lib/libelektra-augeas.so
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
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/build'
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-sync.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-plugin.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-resolver_fm_pb_b.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-proposal.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-utility.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-ease.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-meta.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-io.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-opts.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-highlevel.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-merge.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-mmapstorage.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-ni.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-globbing.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-cache.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-invoke.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-core.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-ini.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-pluginprocess.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core/usr/lib/libelektra-kdb.so.0.9.2: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-core into /openwrt/bin/packages/x86_64/packages/libelektra-core_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/elektra-kdb/usr/lib/libelektratools.so.0.9.2: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/elektra-kdb/usr/bin/kdb: executable
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/elektra-kdb into /openwrt/bin/packages/x86_64/packages/elektra-kdb_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_xb_x.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-wresolver.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_b_b.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_uhb_xb.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-noresolver.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_xp_x.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_xhp_x.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_hb_b.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_hp_b.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_ub_x.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers/usr/lib/libelektra-resolver_fm_hpu_b.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-resolvers into /openwrt/bin/packages/x86_64/packages/libelektra-resolvers_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-hosts.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-filecheck.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-network.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-lineendings.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-keytometa.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-hexnumber.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-quickdump.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-syslog.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-base64.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-path.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-range.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-uname.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-hexcode.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-ipaddr.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-unit.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-file.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-null.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-line.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-macaddr.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-type.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-hidden.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-date.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-csvstorage.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-profile.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-conditionals.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-rgbcolor.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-mathcheck.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-iconv.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-validation.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-shell.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-list.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-reference.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-glob.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins/usr/lib/libelektra-mini.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-plugins into /openwrt/bin/packages/x86_64/packages/libelektra-plugins_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-boost/usr/lib/libelektra-tcl.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-boost into /openwrt/bin/packages/x86_64/packages/libelektra-boost_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-cpp/usr/lib/libelektra-directoryvalue.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-cpp/usr/lib/libelektra-ccode.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-cpp/usr/lib/libelektra-dump.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-cpp into /openwrt/bin/packages/x86_64/packages/libelektra-cpp_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-curlget/usr/lib/libelektra-curlget.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-curlget into /openwrt/bin/packages/x86_64/packages/libelektra-curlget_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-crypto/usr/lib/libelektra-crypto.so: shared object
Packaged contents of /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-crypto into /openwrt/bin/packages/x86_64/packages/libelektra-crypto_0.9.2-2_x86_64.ipk
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-dbus/usr/lib/libelektra-dbus.so: shared object
rstrip.sh: /openwrt/build_dir/target-x86_64_musl/elektra-0.9.2/ipkg-x86_64/libelektra-dbus/usr/lib/libelektra-dbusrecv.so: shared object
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
