---
title: "compile.40"
date: 2021-06-22 10:45:15.545751
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
make package/feeds/packages/netwhere/compile -j$(nproc) || make package/feeds/packages/netwhere/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-libmicrohttpd.patch using plaintext: 
patching file webservice.hpp
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
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE) 
Doxygen need to be installed to generate documentation
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
    CMAKE_FIND_ROOT_PATH_MODE_LIBRARY
    CMAKE_MODULE_LINKER_FLAGS
    CMAKE_SHARED_LINKER_FLAGS
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-mips_24kc_musl/netwhere-0.9
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/netwhere-0.9'
[1/4] Building CXX object CMakeFiles/netwhere.dir/main.cpp.o
FAILED: CMakeFiles/netwhere.dir/main.cpp.o 
/openwrt/staging_dir/host/bin/ccache /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-g++   -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/netwhere-0.9=netwhere-0.9 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DNDEBUG -MD -MT CMakeFiles/netwhere.dir/main.cpp.o -MF CMakeFiles/netwhere.dir/main.cpp.o.d -o CMakeFiles/netwhere.dir/main.cpp.o -c main.cpp
In file included from main.cpp:10:
netwhere.hpp:11:10: fatal error: boost/format.hpp: No such file or directory
 #include <boost/format.hpp>
          ^~~~~~~~~~~~~~~~~~
compilation terminated.
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:43: /openwrt/build_dir/target-mips_24kc_musl/netwhere-0.9/.built] Error 1
```
