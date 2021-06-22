---
title: "compile.40"
date: 2021-06-22 10:46:12.832636
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
make package/feeds/packages/sysrepo/compile -j$(nproc) || make package/feeds/packages/sysrepo/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-add-generated-protobufc-files.patch using plaintext: 
patching file src/common/sysrepo.pb-c.c
patching file src/common/sysrepo.pb-c.h

Applying ./patches/006-update-generated-protobufc-files.patch using plaintext: 
patching file src/common/sysrepo.pb-c.c
patching file src/common/sysrepo.pb-c.h
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
-- ietf-yang-library revision: 2019-01-04
-- Sysrepo repository: /etc/sysrepo
-- Startup data path:  /etc/sysrepo/data
-- Notification path:  /etc/sysrepo/data/notif
-- YANG module path:   /etc/sysrepo/yang
-- SRPD plugins path:  /usr/lib/sysrepo/plugins
-- Looking for vdprintf
-- Looking for vdprintf - found
-- Looking for asprintf
-- Looking for asprintf - found
-- Looking for vasprintf
-- Looking for vasprintf - found
-- Looking for get_current_dir_name
-- Looking for get_current_dir_name - found
-- Looking for strndup
-- Looking for strndup - found
-- Looking for getline
-- Looking for getline - found
-- Could NOT find Uncrustify (missing: UNCRUSTIFY) (Required is at least version "0.71")
-- Looking for __atomic_fetch_add_4 in atomic
-- Looking for __atomic_fetch_add_4 in atomic - found
-- Found LibYANG: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libyang.so (found suitable version "1.10.17", minimum required is "1.9.11") 
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Looking for pthread_mutex_timedlock
-- Looking for pthread_mutex_timedlock - found
-- Looking for eaccess
-- Looking for eaccess - found
-- Looking for stdatomic.h
-- Looking for stdatomic.h - found
-- Looking for mkstemps
-- Looking for mkstemps - found
-- Found SWIG: /openwrt/staging_dir/hostpkg/bin/swig (found suitable version "4.0.2", minimum required is "3.0.12")  
-- Found PythonInterp: /openwrt/staging_dir/hostpkg/bin/python3 (found suitable version "3.9.5", minimum required is "3") 
-- Could NOT find PythonLibs (missing: PYTHON_LIBRARIES PYTHON_INCLUDE_DIRS) (Required is at least version "3")
CMake Error at bindings/CMakeLists.txt:27 (message):
  Python 3 libraries not found!


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/sysrepo-1.4.122/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:135: /openwrt/build_dir/target-mips_24kc_musl/sysrepo-1.4.122/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
