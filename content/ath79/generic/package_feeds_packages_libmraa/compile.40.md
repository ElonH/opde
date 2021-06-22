---
title: "compile.40"
date: 2021-06-22 10:45:15.532766
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
make package/feeds/packages/libmraa/compile -j$(nproc) || make package/feeds/packages/libmraa/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-version.patch using plaintext: 
patching file CMakeLists.txt

Applying ./patches/020-support_v12.patch using plaintext: 
patching file api/mraa/gpio.hpp

Applying ./patches/030-gcc10.patch using plaintext: 
patching file include/version.h
CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- The CXX compiler identification is GNU 8.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test HAS_C__Wall
-- Performing Test HAS_C__Wall - Success
-- Performing Test HAS_C__Werror_main
-- Performing Test HAS_C__Werror_main - Success
-- Performing Test HAS_C__Wformat
-- Performing Test HAS_C__Wformat - Success
-- Performing Test HAS_C__Wmain
-- Performing Test HAS_C__Wmain - Success
-- Performing Test HAS_C__Wuninitialized
-- Performing Test HAS_C__Wuninitialized - Success
-- Performing Test HAS_C__Winit_self
-- Performing Test HAS_C__Winit_self - Success
-- Performing Test HAS_C__Werror_implicit
-- Performing Test HAS_C__Werror_implicit - Success
-- Performing Test HAS_C__Werror_missing_parameter_type
-- Performing Test HAS_C__Werror_missing_parameter_type - Success
-- Performing Test HAS_CXX__Wall
-- Performing Test HAS_CXX__Wall - Success
-- Performing Test HAS_CXX__Werror_main
-- Performing Test HAS_CXX__Werror_main - Success
-- Performing Test HAS_CXX__Wformat
-- Performing Test HAS_CXX__Wformat - Success
-- Performing Test HAS_CXX__Wmain
-- Performing Test HAS_CXX__Wmain - Success
-- Performing Test HAS_CXX__Wuninitialized
-- Performing Test HAS_CXX__Wuninitialized - Success
-- Performing Test HAS_CXX__Winit_self
-- Performing Test HAS_CXX__Winit_self - Success
-- Performing Test HAS_CXX__Wnon_virtual_dtor
-- Performing Test HAS_CXX__Wnon_virtual_dtor - Success
-- Performing Test HAS_CXX__Woverloaded_virtual
-- Performing Test HAS_CXX__Woverloaded_virtual - Success
-- Performing Test HAS_CXX__Wreorder
-- Performing Test HAS_CXX__Wreorder - Success
-- INFO - libmraa Version v2.2.0
-- INFO - cmake Version 3.20.3
-- INFO - Target arch is mips
-- Found PythonInterp: /usr/bin/python2.7 (found suitable version "2.7.18", minimum required is "2.7") 
-- Could NOT find PythonLibs (missing: PYTHON_LIBRARIES PYTHON_INCLUDE_DIRS) (Required is at least version "2.7")
-- Found PythonInterp: /openwrt/staging_dir/hostpkg/bin/python3 (found suitable version "3.9.5", minimum required is "3") 
-- Could NOT find PythonLibs (missing: PYTHON_LIBRARIES PYTHON_INCLUDE_DIRS) (Required is at least version "3.9")
-- INFO - Adding firmata backend support
-- INFO - Adding onewire backend support
-- INFO - Adding support for platform ALL
-- INFO - Adding support for all platforms
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
INFO - Adding MIPS platforms
-- Found SWIG: /openwrt/staging_dir/hostpkg/bin/swig (found version "4.0.2")  
-- Could NOT find GTest (missing: GTEST_LIBRARY GTEST_INCLUDE_DIR GTEST_MAIN_LIBRARY) 
-- Install Google Test to enable additional unit testing
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
    CMAKE_MODULE_LINKER_FLAGS
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0'
[1/27] Building C object src/CMakeFiles/mraa.dir/mraa.c.o
src/mraa.c: In function 'mraa_find_uart_bus_pci':
src/mraa.c:1157:50: warning: '%s' directive output may be truncated writing up to 255 bytes into a region of size 11 [-Wformat-truncation=]
     snprintf(*dev_name, max_allowable_len, "/dev/%s", namelist[n - 1]->d_name);
                                                  ^~
src/mraa.c:1157:5: note: 'snprintf' output between 6 and 261 bytes into a destination of size 16
     snprintf(*dev_name, max_allowable_len, "/dev/%s", namelist[n - 1]->d_name);
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[2/27] Building C object src/CMakeFiles/mraa.dir/gpio/gpio.c.o
[3/27] Building C object src/CMakeFiles/mraa.dir/gpio/gpio_chardev.c.o
[4/27] Building C object src/CMakeFiles/mraa.dir/i2c/i2c.c.o
In file included from src/i2c/i2c.c:19:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
[5/27] Building C object src/CMakeFiles/mraa.dir/pwm/pwm.c.o
[6/27] Building C object src/CMakeFiles/mraa.dir/spi/spi.c.o
[7/27] Building C object src/CMakeFiles/mraa.dir/aio/aio.c.o
[8/27] Building C object src/CMakeFiles/mraa.dir/uart/uart.c.o
[9/27] Building C object src/CMakeFiles/mraa.dir/led/led.c.o
In file included from src/led/led.c:17:
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/sys/errno.h:1:2: warning: #warning redirecting incorrect #include <sys/errno.h> to <errno.h> [-Wcpp]
 #warning redirecting incorrect #include <sys/errno.h> to <errno.h>
  ^~~~~~~
src/led/led.c: In function 'mraa_led_init':
src/led/led.c:148:59: warning: argument to 'sizeof' in 'strncpy' call is the same expression as the source; did you mean to use the size of the destination? [-Wsizeof-pointer-memaccess]
     strncpy(dev->led_path, (const char*) directory, sizeof(directory));
                                                           ^
src/led/led.c: In function 'mraa_led_init_raw':
src/led/led.c:179:59: warning: argument to 'sizeof' in 'strncpy' call is the same expression as the source; did you mean to use the size of the destination? [-Wsizeof-pointer-memaccess]
     strncpy(dev->led_path, (const char*) directory, sizeof(directory));
                                                           ^
src/led/led.c: In function 'mraa_led_get_brightfd':
src/led/led.c:44:33: warning: '%s' directive output may be truncated writing 10 bytes into a region of size between 0 and 63 [-Wformat-truncation=]
     snprintf(buf, MAX_SIZE, "%s/%s", dev->led_path, "brightness");
                                 ^~                  ~~~~~~~~~~~~
src/led/led.c:44:5: note: 'snprintf' output between 12 and 75 bytes into a destination of size 64
     snprintf(buf, MAX_SIZE, "%s/%s", dev->led_path, "brightness");
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
src/led/led.c: In function 'mraa_led_read_max_brightness':
src/led/led.c:59:33: warning: '%s' directive output may be truncated writing 14 bytes into a region of size between 0 and 63 [-Wformat-truncation=]
     snprintf(buf, MAX_SIZE, "%s/%s", dev->led_path, "max_brightness");
                                 ^~                  ~~~~~~~~~~~~~~~~
src/led/led.c:59:5: note: 'snprintf' output between 16 and 79 bytes into a destination of size 64
     snprintf(buf, MAX_SIZE, "%s/%s", dev->led_path, "max_brightness");
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
src/led/led.c: In function 'mraa_led_set_trigger':
src/led/led.c:29:33: warning: '%s' directive output may be truncated writing 7 bytes into a region of size between 0 and 63 [-Wformat-truncation=]
     snprintf(buf, MAX_SIZE, "%s/%s", dev->led_path, "trigger");
                                 ^~                  ~~~~~~~~~
src/led/led.c:29:5: note: 'snprintf' output between 9 and 72 bytes into a destination of size 64
     snprintf(buf, MAX_SIZE, "%s/%s", dev->led_path, "trigger");
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[10/27] Building C object src/CMakeFiles/mraa.dir/initio/initio.c.o
[11/27] Building C object src/CMakeFiles/mraa.dir/grovepi/grovepi.c.o
[12/27] Building C object src/CMakeFiles/mraa.dir/firmata/firmata.c.o
[13/27] Building C object src/CMakeFiles/mraa.dir/firmata/firmata_mraa.c.o
[14/27] Building C object src/CMakeFiles/mraa.dir/uart_ow/uart_ow.c.o
[15/27] Building C object src/CMakeFiles/mraa.dir/iio/iio.c.o
src/iio/iio.c: In function 'mraa_iio_get_channel_data':
src/iio/iio.c:165:44: warning: format '%d' expects a matching 'int' argument [-Wformat=]
             syslog(LOG_ERR, "iio: Channel %d with channel bytes value <= 0");
                                           ~^
src/iio/iio.c:23:26: warning: '%s' directive output may be truncated writing up to 255 bytes into a region of size between 71 and 81 [-Wformat-truncation=]
 #define IIO_SYSFS_DEVICE "/sys/bus/iio/devices/" IIO_DEVICE
                          ^~~~~~~~~~~~~~~~~~~~~~~
src/iio/iio.c:96:37: note: in expansion of macro 'IIO_SYSFS_DEVICE'
             snprintf(buf, MAX_SIZE, IIO_SYSFS_DEVICE "%d/" IIO_SCAN_ELEM "/%s", dev->num, ent->d_name);
                                     ^~~~~~~~~~~~~~~~
src/iio/iio.c:595:80: note: format string is defined here
                 snprintf(buf, MAX_SIZE, IIO_SYSFS_DEVICE "%d/" IIO_SCAN_ELEM "/%s", dev->num, ent->d_name);
                                                                                ^~
src/iio/iio.c:96:13: note: 'snprintf' output between 48 and 313 bytes into a destination of size 128
             snprintf(buf, MAX_SIZE, IIO_SYSFS_DEVICE "%d/" IIO_SCAN_ELEM "/%s", dev->num, ent->d_name);
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
src/iio/iio.c: In function 'mraa_iio_get_event_data':
src/iio/iio.c:23:26: warning: '%s' directive output may be truncated writing up to 255 bytes into a region of size between 78 and 88 [-Wformat-truncation=]
 #define IIO_SYSFS_DEVICE "/sys/bus/iio/devices/" IIO_DEVICE
                          ^~~~~~~~~~~~~~~~~~~~~~~
src/iio/iio.c:399:41: note: in expansion of macro 'IIO_SYSFS_DEVICE'
                 snprintf(buf, MAX_SIZE, IIO_SYSFS_DEVICE "%d/" IIO_EVENTS "/%s", dev->num, ent->d_name);
                                         ^~~~~~~~~~~~~~~~
src/iio/iio.c:21:31: note: format string is defined here
 #define IIO_SCAN_ELEM "scan_elements"
                               ^~
src/iio/iio.c:399:17: note: 'snprintf' output between 41 and 306 bytes into a destination of size 128
                 snprintf(buf, MAX_SIZE, IIO_SYSFS_DEVICE "%d/" IIO_EVENTS "/%s", dev->num, ent->d_name);
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
src/iio/iio.c: In function 'mraa_iio_update_channels':
src/iio/iio.c:23:26: warning: '%s' directive output may be truncated writing up to 255 bytes into a region of size between 71 and 81 [-Wformat-truncation=]
 #define IIO_SYSFS_DEVICE "/sys/bus/iio/devices/" IIO_DEVICE
                          ^~~~~~~~~~~~~~~~~~~~~~~
src/iio/iio.c:595:41: note: in expansion of macro 'IIO_SYSFS_DEVICE'
                 snprintf(buf, MAX_SIZE, IIO_SYSFS_DEVICE "%d/" IIO_SCAN_ELEM "/%s", dev->num, ent->d_name);
                                         ^~~~~~~~~~~~~~~~
src/iio/iio.c:595:80: note: format string is defined here
                 snprintf(buf, MAX_SIZE, IIO_SYSFS_DEVICE "%d/" IIO_SCAN_ELEM "/%s", dev->num, ent->d_name);
                                                                                ^~
src/iio/iio.c:595:17: note: 'snprintf' output between 48 and 313 bytes into a destination of size 128
                 snprintf(buf, MAX_SIZE, IIO_SYSFS_DEVICE "%d/" IIO_SCAN_ELEM "/%s", dev->num, ent->d_name);
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[16/27] Building C object src/CMakeFiles/mraa.dir/json/jsonplatform.c.o
[17/27] Building C object src/CMakeFiles/mraa.dir/mips/mips.c.o
[18/27] Building C object src/CMakeFiles/mraa.dir/mips/mediatek.c.o
src/mips/mediatek.c: In function 'mtk_common.constprop':
src/mips/mediatek.c:422:60: warning: '%d' directive output may be truncated writing between 1 and 10 bytes into a region of size 8 [-Wformat-truncation=]
         snprintf(b->pins[i].name, MRAA_PIN_NAME_SIZE, "GPIO%d", i);
                                                            ^~
src/mips/mediatek.c:422:55: note: directive argument in the range [0, 2147483647]
         snprintf(b->pins[i].name, MRAA_PIN_NAME_SIZE, "GPIO%d", i);
                                                       ^~~~~~~~
src/mips/mediatek.c:422:9: note: 'snprintf' output between 6 and 15 bytes into a destination of size 12
         snprintf(b->pins[i].name, MRAA_PIN_NAME_SIZE, "GPIO%d", i);
         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[19/27] Building C object src/CMakeFiles/mraa.dir/version.c.o
[20/27] Linking C shared library src/libmraa.so.2.2.0
[21/27] Creating library symlink src/libmraa.so.2 src/libmraa.so
[22/27] Building C object tools/CMakeFiles/mraa-uart.dir/mraa-uart.c.o
[23/27] Linking C executable tools/mraa-uart
[24/27] Building C object tools/CMakeFiles/mraa-i2c.dir/mraa-i2c.c.o
[25/27] Linking C executable tools/mraa-i2c
[26/27] Building C object tools/CMakeFiles/mraa-gpio.dir/mraa-gpio.c.o
tools/mraa-gpio.c: In function 'gpio_set':
tools/mraa-gpio.c:99:13: warning: 'mraa_gpio_use_mmaped' is deprecated [-Wdeprecated-declarations]
             if (mraa_gpio_use_mmaped(gpio, 1) != MRAA_SUCCESS) {
             ^~
In file included from tools/mraa-gpio.c:13:
api/mraa/gpio.h:289:26: note: declared here
 DEPRECATED mraa_result_t mraa_gpio_use_mmaped(mraa_gpio_context dev, mraa_boolean_t mmap);
                          ^~~~~~~~~~~~~~~~~~~~
tools/mraa-gpio.c: In function 'gpio_get':
tools/mraa-gpio.c:117:13: warning: 'mraa_gpio_use_mmaped' is deprecated [-Wdeprecated-declarations]
             if (mraa_gpio_use_mmaped(gpio, 1) != MRAA_SUCCESS) {
             ^~
In file included from tools/mraa-gpio.c:13:
api/mraa/gpio.h:289:26: note: declared here
 DEPRECATED mraa_result_t mraa_gpio_use_mmaped(mraa_gpio_context dev, mraa_boolean_t mmap);
                          ^~~~~~~~~~~~~~~~~~~~
[27/27] Linking C executable tools/mraa-gpio
ninja: Entering directory `/openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0'
[0/1] Install the project...
-- Install configuration: "Release"
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/spi.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/i2c.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/uart_ow.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/common.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/types.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/firmata.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/pwm.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/iio.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/i2c.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/gpio.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/uart.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/gpio.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/led.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/pwm.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/uart.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/iio.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/aio.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/aio.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/uart_ow.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/types.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/spi.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/initio.hpp
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/iio_kernel_headers.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/led.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/common.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/include/mraa/initio.h
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/lib/pkgconfig/mraa.pc
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/lib/libmraa.so.2.2.0
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/lib/libmraa.so.2
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/lib/libmraa.so
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/bin/mraa-gpio
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/bin/mraa-i2c
-- Installing: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/bin/mraa-uart
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-mips_24kc/libmraa/usr/bin/mraa-i2c: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-mips_24kc/libmraa/usr/bin/mraa-uart: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-mips_24kc/libmraa/usr/bin/mraa-gpio: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-mips_24kc/libmraa/usr/lib/libmraa.so.2.2.0: shared object
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-mips_24kc/libmraa into /openwrt/bin/packages/mips_24kc/packages/libmraa_2.2.0-3_mips_24kc.ipk
cp: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/mraa-2.2.0/ipkg-install/usr/lib/python3.9/site-packages/*': No such file or directory
make[3]: *** [Makefile:94: /openwrt/bin/packages/mips_24kc/packages/libmraa-python3_2.2.0-3_mips_24kc.ipk] Error 1
```
