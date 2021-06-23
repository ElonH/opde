---
title: "compile.41"
date: 2021-06-23 23:25:01.766178
hidden: false
draft: false
weight: -41
---

build number: `41`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/spdlog/compile -j$(nproc) || make package/feeds/packages/spdlog/compile V=s
```

#### Compile.txt

``` bash
+ curl -f --connect-timeout 20 --retry 5 --location --insecure https://codeload.github.com/gabime/spdlog/tar.gz/v1.8.5?/spdlog-1.8.5.tar.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  313k    0  313k    0     0  2323k      0 --:--:-- --:--:-- --:--:-- 2323k
-- The CXX compiler identification is GNU 8.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Build spdlog: 1.8.5
-- Looking for C++ include pthread.h
-- Looking for C++ include pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Build type: Release
-- Generating install
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    CMAKE_ASM_COMPILER
    CMAKE_ASM_COMPILER_LAUNCHER
    CMAKE_C_COMPILER
    CMAKE_C_FLAGS_RELEASE
    CMAKE_EXPORT_NO_PACKAGE_REGISTRY
    CMAKE_EXPORT_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY
    CMAKE_FIND_ROOT_PATH_MODE_LIBRARY
    CMAKE_MODULE_LINKER_FLAGS
    CMAKE_SHARED_LINKER_FLAGS
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/spdlog-1.8.5
ninja: Entering directory `/openwrt/build_dir/target-x86_64_musl/spdlog-1.8.5'
[1/7] Building CXX object CMakeFiles/spdlog.dir/src/spdlog.cpp.o
FAILED: CMakeFiles/spdlog.dir/src/spdlog.cpp.o 
/openwrt/staging_dir/host/bin/ccache /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-g++ -DFMT_LOCALE -DFMT_SHARED -DSPDLOG_COMPILED_LIB -DSPDLOG_FMT_EXTERNAL -Iinclude -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/spdlog-1.8.5=spdlog-1.8.5 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto -DNDEBUG -std=c++11 -MD -MT CMakeFiles/spdlog.dir/src/spdlog.cpp.o -MF CMakeFiles/spdlog.dir/src/spdlog.cpp.o.d -o CMakeFiles/spdlog.dir/src/spdlog.cpp.o -c src/spdlog.cpp
In file included from src/spdlog.cpp:9:
include/spdlog/common-inl.h: In constructor 'spdlog::spdlog_ex::spdlog_ex(const string&, int)':
include/spdlog/common-inl.h:63:50: error: cannot convert 'const string' {aka 'const std::basic_string<char>'} to 'const char*'
     fmt::format_system_error(outbuf, last_errno, msg);
                                                  ^~~
In file included from include/spdlog/fmt/fmt.h:26,
                 from include/spdlog/common.h:36,
                 from include/spdlog/spdlog.h:12,
                 from include/spdlog/spdlog-inl.h:7,
                 from src/spdlog.cpp:8:
/openwrt/staging_dir/target-x86_64_musl/usr/include/fmt/format.h:2262:46: note:   initializing argument 3 of 'void fmt::v7::format_system_error(fmt::v7::detail::buffer<char>&, int, const char*)'
                                  const char* message) FMT_NOEXCEPT;
                                  ~~~~~~~~~~~~^~~~~~~
In file included from include/spdlog/pattern_formatter-inl.h:10,
                 from src/spdlog.cpp:13:
include/spdlog/details/fmt_helper.h: In function 'void spdlog::details::fmt_helper::pad2(int, spdlog::memory_buf_t&)':
include/spdlog/details/fmt_helper.h:57:40: warning: 'fmt::v7::appender fmt::v7::format_to(fmt::v7::basic_memory_buffer<char, SIZE, Allocator>&, fmt::v7::format_string<T ...>, T&& ...) [with T = {int&}; long unsigned int SIZE = 250; Allocator = std::allocator<char>; fmt::v7::format_string<T ...> = fmt::v7::basic_format_string<char, int&>]' is deprecated [-Wdeprecated-declarations]
         fmt::format_to(dest, "{:02}", n);
                                        ^
In file included from include/spdlog/fmt/fmt.h:26,
                 from include/spdlog/common.h:36,
                 from include/spdlog/spdlog.h:12,
                 from include/spdlog/spdlog-inl.h:7,
                 from src/spdlog.cpp:8:
/openwrt/staging_dir/target-x86_64_musl/usr/include/fmt/format.h:2787:21: note: declared here
 FMT_DEPRECATED auto format_to(basic_memory_buffer<char, SIZE, Allocator>& buf,
                     ^~~~~~~~~
In file included from include/spdlog/pattern_formatter-inl.h:10,
                 from src/spdlog.cpp:13:
include/spdlog/details/fmt_helper.h:57:40: warning: 'fmt::v7::appender fmt::v7::format_to(fmt::v7::basic_memory_buffer<char, SIZE, Allocator>&, fmt::v7::format_string<T ...>, T&& ...) [with T = {int&}; long unsigned int SIZE = 250; Allocator = std::allocator<char>; fmt::v7::format_string<T ...> = fmt::v7::basic_format_string<char, int&>]' is deprecated [-Wdeprecated-declarations]
         fmt::format_to(dest, "{:02}", n);
                                        ^
In file included from include/spdlog/fmt/fmt.h:26,
                 from include/spdlog/common.h:36,
                 from include/spdlog/spdlog.h:12,
                 from include/spdlog/spdlog-inl.h:7,
                 from src/spdlog.cpp:8:
/openwrt/staging_dir/target-x86_64_musl/usr/include/fmt/format.h:2787:21: note: declared here
 FMT_DEPRECATED auto format_to(basic_memory_buffer<char, SIZE, Allocator>& buf,
                     ^~~~~~~~~
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:66: /openwrt/build_dir/target-x86_64_musl/spdlog-1.8.5/.built] Error 1
```
