---
title: "compile.40"
date: 2021-06-22 10:50:44.058183
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
make package/feeds/packages/quickjspp/compile -j$(nproc) || make package/feeds/packages/quickjspp/compile V=s
```

#### Compile.txt

``` bash
Makefile:46: WARNING: skipping quickjspp -- package has no install section
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
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
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


-- Build files have been written to: /openwrt/build_dir/target-mips_24kc_musl/quickjspp-2021-03-23-1aa63ac1
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/quickjspp-2021-03-23-1aa63ac1'
[1/40] Building CXX object CMakeFiles/qjs.dir/qjs.cpp.o
[2/40] Building C object quickjs/CMakeFiles/quickjs-dumpleaks.dir/quickjs.c.o
FAILED: quickjs/CMakeFiles/quickjs-dumpleaks.dir/quickjs.c.o 
/openwrt/staging_dir/host/bin/ccache /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc -DCONFIG_BIGNUM -DCONFIG_VERSION=\"2020-11-08\" -DDUMP_LEAKS=1 -D_GNU_SOURCE  -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/quickjspp-2021-03-23-1aa63ac1=quickjspp-2021-03-23-1aa63ac1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -DNDEBUG -Wall -Wno-unused-parameter -MD -MT quickjs/CMakeFiles/quickjs-dumpleaks.dir/quickjs.c.o -MF quickjs/CMakeFiles/quickjs-dumpleaks.dir/quickjs.c.o.d -o quickjs/CMakeFiles/quickjs-dumpleaks.dir/quickjs.c.o -c quickjs/quickjs.c
quickjs/quickjs.c: In function 'JS_SetClassProto':
quickjs/quickjs.c:2192:16: warning: unused variable 'rt' [-Wunused-variable]
     JSRuntime *rt = ctx->rt;
                ^~
quickjs/quickjs.c: In function 'JS_GetClassProto':
quickjs/quickjs.c:2199:16: warning: unused variable 'rt' [-Wunused-variable]
     JSRuntime *rt = ctx->rt;
                ^~
quickjs/quickjs.c: In function 'num_keys_cmp':
quickjs/quickjs.c:7401:28: warning: variable 'atom2_is_integer' set but not used [-Wunused-but-set-variable]
     BOOL atom1_is_integer, atom2_is_integer;
                            ^~~~~~~~~~~~~~~~
quickjs/quickjs.c:7401:10: warning: variable 'atom1_is_integer' set but not used [-Wunused-but-set-variable]
     BOOL atom1_is_integer, atom2_is_integer;
          ^~~~~~~~~~~~~~~~
quickjs/quickjs.c: In function 'js_ecvt':
quickjs/quickjs.c:11320:66: error: 'FE_DOWNWARD' undeclared (first use in this function); did you mean 'FE_TONEAREST'?
                 js_ecvt1(d, n_digits + 1, &decpt1, &sign1, buf1, FE_DOWNWARD,
                                                                  ^~~~~~~~~~~
                                                                  FE_TONEAREST
quickjs/quickjs.c:11320:66: note: each undeclared identifier is reported only once for each function it appears in
quickjs/quickjs.c:11322:66: error: 'FE_UPWARD' undeclared (first use in this function)
                 js_ecvt1(d, n_digits + 1, &decpt2, &sign2, buf2, FE_UPWARD,
                                                                  ^~~~~~~~~
quickjs/quickjs.c: In function 'js_fcvt':
quickjs/quickjs.c:11371:64: error: 'FE_DOWNWARD' undeclared (first use in this function); did you mean 'FE_TONEAREST'?
             n1 = js_fcvt1(buf1, sizeof(buf1), d, n_digits + 1, FE_DOWNWARD);
                                                                ^~~~~~~~~~~
                                                                FE_TONEAREST
quickjs/quickjs.c:11372:64: error: 'FE_UPWARD' undeclared (first use in this function)
             n2 = js_fcvt1(buf2, sizeof(buf2), d, n_digits + 1, FE_UPWARD);
                                                                ^~~~~~~~~
quickjs/quickjs.c: In function 'JS_CompactBigInt1':
quickjs/quickjs.c:12290:21: warning: unused variable 'p' [-Wunused-variable]
         JSBigFloat *p = JS_VALUE_GET_PTR(val);
                     ^
quickjs/quickjs.c: In function 'JS_EvalThis':
quickjs/quickjs.c:33625:9: warning: unused variable 'eval_type' [-Wunused-variable]
     int eval_type = eval_flags & JS_EVAL_TYPE_MASK;
         ^~~~~~~~~
quickjs/quickjs.c: In function 'reset_weak_ref':
quickjs/quickjs.c:45605:17: warning: variable 's' set but not used [-Wunused-but-set-variable]
     JSMapState *s;
                 ^
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:49: /openwrt/build_dir/target-mips_24kc_musl/quickjspp-2021-03-23-1aa63ac1/.built] Error 1
```
