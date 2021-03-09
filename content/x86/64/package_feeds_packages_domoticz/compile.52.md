---
title: "compile.52"
date: 2021-03-09 13:46:57.312716
hidden: false
draft: false
weight: -52
---

build number: `52`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/domoticz/compile -j$(nproc) || make package/feeds/packages/domoticz/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-boost-173.patch using plaintext: 
patching file hardware/ASyncSerial.cpp
patching file hardware/ASyncTCP.cpp
patching file hardware/Comm5Serial.cpp
patching file hardware/CurrentCostMeterSerial.cpp
patching file hardware/DavisLoggerSerial.cpp
patching file hardware/DenkoviUSBDevices.cpp
patching file hardware/EnOceanESP2.cpp
patching file hardware/EnOceanESP3.cpp
patching file hardware/EvohomeRadio.cpp
patching file hardware/EvohomeSerial.cpp
patching file hardware/KMTronic433.cpp
patching file hardware/KMTronicBase.cpp
patching file hardware/KMTronicSerial.cpp
patching file hardware/MQTT.cpp
patching file hardware/Meteostick.cpp
patching file hardware/MySensorsBase.cpp
patching file hardware/MySensorsSerial.cpp
patching file hardware/OTGWBase.cpp
patching file hardware/OTGWSerial.cpp
patching file hardware/OpenWebNetUSB.cpp
patching file hardware/P1MeterSerial.cpp
patching file hardware/Pinger.cpp
patching file hardware/RAVEn.cpp
patching file hardware/RFLinkSerial.cpp
patching file hardware/RFXComSerial.cpp
patching file hardware/RFXComTCP.cpp
patching file hardware/Rego6XXSerial.cpp
patching file hardware/S0MeterBase.cpp
patching file hardware/S0MeterSerial.cpp
patching file hardware/TCPProxy/tcpproxy_server.cpp
patching file hardware/TeleinfoSerial.cpp
patching file hardware/USBtin.cpp
patching file hardware/XiaomiGateway.cpp
patching file hardware/Yeelight.h
patching file hardware/ZiBlueSerial.cpp
patching file hardware/plugins/PluginTransports.cpp
patching file main/WebServer.cpp
patching file main/mainworker.cpp
patching file push/FibaroPush.cpp
patching file push/GooglePubSubPush.cpp
patching file push/HttpPush.cpp
patching file push/InfluxPush.cpp
patching file push/WebsocketPush.cpp
patching file tcpserver/TCPServer.cpp
patching file webserver/cWebem.cpp
patching file webserver/connection.cpp
patching file webserver/connection_manager.cpp
patching file webserver/proxyclient.cpp
patching file webserver/server.cpp

Applying ./patches/011-openzwave-include.patch using plaintext: 
patching file CMakeLists.txt
patching file hardware/OpenZWave.cpp
patching file hardware/openzwave/control_panel/ozwcp.cpp
patching file hardware/openzwave/control_panel/ozwcp.h

Applying ./patches/012-minizip-overflow.patch using plaintext: 
patching file main/unzip_stream.h

Applying ./patches/020-python39.patch using plaintext: 
patching file hardware/plugins/DelayedLink.h
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
fatal: not a git repository: './.git'
-- Failed to get ProjectRevision from git
-- Read ProjectRevision from History.txt
-- LUA library found at: /openwrt/staging_dir/target-x86_64_musl/usr/lib/liblua5.3.so
-- Found PythonInterp: /openwrt/staging_dir/hostpkg/bin/python3 (found suitable version "3.9.2", minimum required is "3.4") 
-- Found PythonLibs: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libpython3.9.so (found suitable version "3.9.2", minimum required is "3.4") 
-- Python3 includes found at: /openwrt/staging_dir/target-x86_64_musl/usr/include/python3.9
-- Looking for execinfo.h
-- Looking for execinfo.h - not found
-- Looking for 3 include files sys/types.h, ..., linux/i2c.h
-- Looking for 3 include files sys/types.h, ..., linux/i2c.h - found
-- Building with I2C support
-- Looking for include files sys/types.h, linux/spi/spidev.h
-- Looking for include files sys/types.h, linux/spi/spidev.h - found
-- Building with SPI support
-- ###########################
-- Compiling Revision #2
-- ###########################
-- Check if the system is big endian
-- Searching 16 bit integer
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Searching 16 bit integer - Using unsigned short
-- Check if the system is big endian - little endian
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
-- Checking for module 'jsoncpp'
--   Found jsoncpp, version 1.9.4
-- JSONCPP includes found at: /openwrt/staging_dir/target-x86_64_musl/usr/include
-- MQTT includes found at: /openwrt/staging_dir/target-x86_64_musl/usr/include
-- Found SQLite3: /openwrt/staging_dir/target-x86_64_musl/usr/include (found version "3.33.0") 
-- SQLite library found at: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libsqlite3.so
-- SQLite includes found at: /openwrt/staging_dir/target-x86_64_musl/usr/include
-- Checking for module 'minizip'
--   Found minizip, version 3.0.0
-- MINIZIP includes found at: /openwrt/staging_dir/target-x86_64_musl/usr/include/minizip;/openwrt/staging_dir/target-x86_64_musl/usr/include
-- Found OpenSSL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libcrypto.so (found version "1.1.1j")  
-- OPENSSL library found at: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libssl.so;/openwrt/staging_dir/target-x86_64_musl/usr/lib/libcrypto.so
-- Linking against boost dynamic libraries
CMake Warning at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1204 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1326 (_Boost_COMPONENT_DEPENDENCIES)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1935 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:614 (find_package)


CMake Warning at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1204 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1326 (_Boost_COMPONENT_DEPENDENCIES)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1935 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:614 (find_package)


CMake Warning at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1204 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1326 (_Boost_COMPONENT_DEPENDENCIES)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1935 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:614 (find_package)


CMake Warning at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1204 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1326 (_Boost_COMPONENT_DEPENDENCIES)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1935 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:614 (find_package)


CMake Warning at /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1204 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1326 (_Boost_COMPONENT_DEPENDENCIES)
  /openwrt/staging_dir/host/share/cmake-3.19/Modules/FindBoost.cmake:1935 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:614 (find_package)


-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Found Boost: /openwrt/staging_dir/target-x86_64_musl/usr/include (found version "1.75.0") found components: thread system chrono date_time atomic 
-- BOOST includes found at: /openwrt/staging_dir/target-x86_64_musl/usr/include
-- Found ZLIB: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libz.so (found version "1.2.11") 
-- ZLIB library found at: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libz.so
-- ZLIB includes found at: /openwrt/staging_dir/target-x86_64_musl/usr/include
-- Found CURL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libcurl.so (found version "7.75.0")  
-- Curl library found at: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libcurl.so
-- Curl includes found at: /openwrt/staging_dir/target-x86_64_musl/usr/include
-- CEREAL includes found at: /openwrt/staging_dir/target-x86_64_musl/usr/include
-- Checking for module 'libopenzwave'
--   Found libopenzwave, version 1.6
-- ==== OpenZWave package found!
-- OpenZWavelibraryfoundat:/openwrt/staging_dir/target-x86_64_musl/usr/lib/libopenzwave.so
-- OpenZWave library found at: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libopenzwave.so
-- OpenZWave includes found at: /openwrt/staging_dir/target-x86_64_musl/usr/include/openzwave/
-- GPIO is available
-- Found telldus-core (telldus-core.h) at : /openwrt/staging_dir/target-x86_64_musl/usr/include
-- Found libtelldus-core at : /openwrt/staging_dir/target-x86_64_musl/usr/lib/libtelldus-core.so, adding telldus support
-- Using precompiled headers
-- Using dynamic libgcc_s/libstdc++
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
    CMAKE_SHARED_LINKER_FLAGS
    DL_LIBRARY


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/domoticz-2020.2
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/domoticz-2020.2'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/domoticz-2020.2'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/domoticz-2020.2'
Scanning dependencies of target revisiontag
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/domoticz-2020.2'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/domoticz-2020.2'
-- Found Git: /openwrt/staging_dir/host/bin/git (found version "2.25.1") 
fatal: not a git repository: './.git'
-- Read ProjectRevision from History.txt
fatal: not a git repository: './.git'
-- Failed to get ProjectHash from git, set it to 0
fatal: not a git repository: './.git'
-- Failed to get ProjectDate from git, set it to 0
fatal: not a git repository: './.git'
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/domoticz-2020.2'
[  0%] Built target revisiontag
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/domoticz-2020.2'
Scanning dependencies of target domoticz
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/domoticz-2020.2'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/domoticz-2020.2'
[  0%] Building CXX object CMakeFiles/domoticz.dir/cmake_pch.hxx.gch
[  0%] Building CXX object CMakeFiles/domoticz.dir/main/stdafx.cpp.o
[  1%] Building CXX object CMakeFiles/domoticz.dir/main/BaroForecastCalculator.cpp.o
[  1%] Building CXX object CMakeFiles/domoticz.dir/main/CmdLine.cpp.o
[  2%] Building CXX object CMakeFiles/domoticz.dir/main/Camera.cpp.o
[  2%] Building CXX object CMakeFiles/domoticz.dir/main/domoticz.cpp.o
[  2%] Building CXX object CMakeFiles/domoticz.dir/main/dzVents.cpp.o
[  3%] Building CXX object CMakeFiles/domoticz.dir/main/EventSystem.cpp.o
[  3%] Building CXX object CMakeFiles/domoticz.dir/main/EventsPythonModule.cpp.o
[  4%] Building CXX object CMakeFiles/domoticz.dir/main/EventsPythonDevice.cpp.o
[  4%] Building CXX object CMakeFiles/domoticz.dir/main/Helper.cpp.o
[  4%] Building CXX object CMakeFiles/domoticz.dir/main/HTMLSanitizer.cpp.o
[  5%] Building CXX object CMakeFiles/domoticz.dir/main/IFTTT.cpp.o
[  5%] Building CXX object CMakeFiles/domoticz.dir/main/json_helper.cpp.o
[  6%] Building CXX object CMakeFiles/domoticz.dir/main/localtime_r.cpp.o
[  6%] Building CXX object CMakeFiles/domoticz.dir/main/Logger.cpp.o
[  6%] Building CXX object CMakeFiles/domoticz.dir/main/LuaCommon.cpp.o
[  7%] Building CXX object CMakeFiles/domoticz.dir/main/LuaHandler.cpp.o
[  7%] Building CXX object CMakeFiles/domoticz.dir/main/LuaTable.cpp.o
[  8%] Building CXX object CMakeFiles/domoticz.dir/main/mainworker.cpp.o
[  8%] Building CXX object CMakeFiles/domoticz.dir/main/mosquitto_helper.cpp.o
[  8%] Building CXX object CMakeFiles/domoticz.dir/main/NotificationObserver.cpp.o
[  9%] Building CXX object CMakeFiles/domoticz.dir/main/NotificationSystem.cpp.o
[  9%] Building CXX object CMakeFiles/domoticz.dir/main/RFXNames.cpp.o
[ 10%] Building CXX object CMakeFiles/domoticz.dir/main/Scheduler.cpp.o
[ 10%] Building CXX object CMakeFiles/domoticz.dir/main/SignalHandler.cpp.o
[ 11%] Building CXX object CMakeFiles/domoticz.dir/main/SQLHelper.cpp.o
In file included from /openwrt/build_dir/target-x86_64_musl/domoticz-2020.2/main/SQLHelper.cpp:16:
/openwrt/build_dir/target-x86_64_musl/domoticz-2020.2/main/clx_unzip.h:43:10: fatal error: minizip/unzip.h: No such file or directory
 #include <minizip/unzip.h>
          ^~~~~~~~~~~~~~~~~
compilation terminated.
make[6]: *** [CMakeFiles/domoticz.dir/build.make:473: CMakeFiles/domoticz.dir/main/SQLHelper.cpp.o] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/domoticz-2020.2'
make[5]: *** [CMakeFiles/Makefile2:124: CMakeFiles/domoticz.dir/all] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/domoticz-2020.2'
make[4]: *** [Makefile:171: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/domoticz-2020.2'
make[3]: *** [Makefile:132: /openwrt/build_dir/target-x86_64_musl/domoticz-2020.2/.built] Error 2
```
