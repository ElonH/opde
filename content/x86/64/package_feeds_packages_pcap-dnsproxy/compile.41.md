---
title: "compile.41"
date: 2021-06-23 23:10:37.524666
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
make package/feeds/packages/pcap-dnsproxy/compile -j$(nproc) || make package/feeds/packages/pcap-dnsproxy/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/002-cmake-dependency-scanner-workaround.patch using plaintext: 
patching file Source/Pcap_DNSProxy/Platform.h
Hunk #1 succeeded at 380 with fuzz 1 (offset 1 line).
Hunk #2 succeeded at 394 (offset 1 line).
Hunk #3 succeeded at 572 (offset -3 lines).
CMake Warning (dev) in CMakeLists.txt:
  No project() command is present.  The top-level CMakeLists.txt file must
  contain a literal, direct call to the project() command.  Add a line of
  code such as

    project(ProjectName)

  near the top of the file, but after cmake_minimum_required().

  CMake is pretending there is a "project(Project)" command on the first
  line.
This warning is for project developers.  Use -Wno-dev to suppress it.

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
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Found OpenSSL: /openwrt/staging_dir/target-x86_64_musl/usr/lib/libcrypto.so (found version "1.1.1k")  
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


-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/pcap-dnsproxy-0.4.9.13-2019-05-05-bc9f540d
ninja: Entering directory `/openwrt/build_dir/target-x86_64_musl/pcap-dnsproxy-0.4.9.13-2019-05-05-bc9f540d'
[1/22] Building CXX object Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Base.cpp.o
FAILED: Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Base.cpp.o 
/openwrt/staging_dir/host/bin/ccache /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-g++ -DENABLE_LIBSODIUM -DENABLE_PCAP -DENABLE_TLS -DPLATFORM_OPENWRT  -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/pcap-dnsproxy-0.4.9.13-2019-05-05-bc9f540d=pcap-dnsproxy-0.4.9.13-2019-05-05-bc9f540d -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -Wall -Wextra -DPIC -fpic -O3 -std=c++14 -DNDEBUG -MD -MT Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Base.cpp.o -MF Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Base.cpp.o.d -o Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Base.cpp.o -c Source/Pcap_DNSProxy/Base.cpp
In file included from Source/Pcap_DNSProxy/Structure.h:23,
                 from Source/Pcap_DNSProxy/Definition.h:23,
                 from Source/Pcap_DNSProxy/Type.h:23,
                 from Source/Pcap_DNSProxy/Template.h:23,
                 from Source/Pcap_DNSProxy/Include.h:23,
                 from Source/Pcap_DNSProxy/Base.h:23,
                 from Source/Pcap_DNSProxy/Base.cpp:20:
Source/Pcap_DNSProxy/Platform.h:657:3: error: #error "The version of LibSodium is too old."
  #error "The version of LibSodium is too old."
   ^~~~~
In file included from Source/Pcap_DNSProxy/Base.cpp:20:
Source/Pcap_DNSProxy/Base.h:159:36: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(65538U),
                                    ^
Source/Pcap_DNSProxy/Base.h:160:37: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(196612U),
                                     ^
Source/Pcap_DNSProxy/Base.h:161:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(1507352U),
                                      ^
Source/Pcap_DNSProxy/Base.h:162:37: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(327686U),
                                     ^
Source/Pcap_DNSProxy/Base.h:163:37: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(720908U),
                                     ^
Source/Pcap_DNSProxy/Base.h:164:37: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(458760U),
                                     ^
Source/Pcap_DNSProxy/Base.h:165:37: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(589834U),
                                     ^
Source/Pcap_DNSProxy/Base.h:166:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2150662193U),
                                         ^
Source/Pcap_DNSProxy/Base.h:167:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2150793313U),
                                         ^
Source/Pcap_DNSProxy/Base.h:168:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2154004581U),
                                         ^
Source/Pcap_DNSProxy/Base.h:169:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2154397807U),
                                         ^
Source/Pcap_DNSProxy/Base.h:170:37: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(851982U),
                                     ^
Source/Pcap_DNSProxy/Base.h:171:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(1114130U),
                                      ^
Source/Pcap_DNSProxy/Base.h:172:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2155053172U),
                                         ^
Source/Pcap_DNSProxy/Base.h:173:37: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(983056U),
                                     ^
Source/Pcap_DNSProxy/Base.h:174:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2149613605U),
                                         ^
Source/Pcap_DNSProxy/Base.h:175:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2150465582U),
                                         ^
Source/Pcap_DNSProxy/Base.h:176:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(1245204U),
                                      ^
Source/Pcap_DNSProxy/Base.h:177:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(1376278U),
                                      ^
Source/Pcap_DNSProxy/Base.h:178:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2150596659U),
                                         ^
Source/Pcap_DNSProxy/Base.h:179:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2150924341U),
                                         ^
Source/Pcap_DNSProxy/Base.h:180:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2151055415U),
                                         ^
Source/Pcap_DNSProxy/Base.h:181:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2151186489U),
                                         ^
Source/Pcap_DNSProxy/Base.h:182:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(1638426U),
                                      ^
Source/Pcap_DNSProxy/Base.h:183:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2687018U),
                                      ^
Source/Pcap_DNSProxy/Base.h:184:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(1769500U),
                                      ^
Source/Pcap_DNSProxy/Base.h:185:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2162722U),
                                      ^
Source/Pcap_DNSProxy/Base.h:186:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(1900574U),
                                      ^
Source/Pcap_DNSProxy/Base.h:187:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2031648U),
                                      ^
Source/Pcap_DNSProxy/Base.h:188:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2151514177U),
                                         ^
Source/Pcap_DNSProxy/Base.h:189:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2153742434U),
                                         ^
Source/Pcap_DNSProxy/Base.h:190:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2154070118U),
                                         ^
Source/Pcap_DNSProxy/Base.h:191:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2154266728U),
                                         ^
Source/Pcap_DNSProxy/Base.h:192:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2293796U),
                                      ^
Source/Pcap_DNSProxy/Base.h:193:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2424870U),
                                      ^
Source/Pcap_DNSProxy/Base.h:194:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2154594413U),
                                         ^
Source/Pcap_DNSProxy/Base.h:195:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2154725488U),
                                         ^
Source/Pcap_DNSProxy/Base.h:196:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2154987637U),
                                         ^
Source/Pcap_DNSProxy/Base.h:197:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2555944U),
                                      ^
Source/Pcap_DNSProxy/Base.h:198:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2151317570U),
                                         ^
Source/Pcap_DNSProxy/Base.h:199:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2151907396U),
                                         ^
Source/Pcap_DNSProxy/Base.h:200:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2818092U),
                                      ^
Source/Pcap_DNSProxy/Base.h:201:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(3735610U),
                                      ^
Source/Pcap_DNSProxy/Base.h:202:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2949166U),
                                      ^
Source/Pcap_DNSProxy/Base.h:203:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(3342388U),
                                      ^
Source/Pcap_DNSProxy/Base.h:204:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(3080240U),
                                      ^
Source/Pcap_DNSProxy/Base.h:205:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(3211314U),
                                      ^
Source/Pcap_DNSProxy/Base.h:206:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2152038470U),
                                         ^
Source/Pcap_DNSProxy/Base.h:207:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2152169544U),
                                         ^
Source/Pcap_DNSProxy/Base.h:208:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2152300618U),
                                         ^
Source/Pcap_DNSProxy/Base.h:209:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2152431692U),
                                         ^
Source/Pcap_DNSProxy/Base.h:210:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(3473462U),
                                      ^
Source/Pcap_DNSProxy/Base.h:211:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(3604536U),
                                      ^
Source/Pcap_DNSProxy/Base.h:212:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2152562766U),
                                         ^
Source/Pcap_DNSProxy/Base.h:213:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2152693840U),
                                         ^
Source/Pcap_DNSProxy/Base.h:214:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2152824914U),
                                         ^
Source/Pcap_DNSProxy/Base.h:215:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2152955988U),
                                         ^
Source/Pcap_DNSProxy/Base.h:216:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(3866684U),
                                      ^
Source/Pcap_DNSProxy/Base.h:217:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(4259906U),
                                      ^
Source/Pcap_DNSProxy/Base.h:218:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(3997758U),
                                      ^
Source/Pcap_DNSProxy/Base.h:219:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(4128832U),
                                      ^
Source/Pcap_DNSProxy/Base.h:220:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2153087062U),
                                         ^
Source/Pcap_DNSProxy/Base.h:221:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2153218137U),
                                         ^
Source/Pcap_DNSProxy/Base.h:222:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2154463339U),
                                         ^
Source/Pcap_DNSProxy/Base.h:223:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2154922102U),
                                         ^
Source/Pcap_DNSProxy/Base.h:224:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(4390980U),
                                      ^
Source/Pcap_DNSProxy/Base.h:225:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(4522054U),
                                      ^
Source/Pcap_DNSProxy/Base.h:226:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2155315320U),
                                         ^
Source/Pcap_DNSProxy/Base.h:227:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2155446394U),
                                         ^
Source/Pcap_DNSProxy/Base.h:228:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(4653128U),
                                      ^
Source/Pcap_DNSProxy/Base.h:229:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(4784202U),
                                      ^
Source/Pcap_DNSProxy/Base.h:230:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2150006826U),
                                         ^
Source/Pcap_DNSProxy/Base.h:231:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2150400059U),
                                         ^
Source/Pcap_DNSProxy/Base.h:232:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2153283674U),
                                         ^
Source/Pcap_DNSProxy/Base.h:233:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(4915276U),
                                      ^
Source/Pcap_DNSProxy/Base.h:234:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(5046350U),
                                      ^
Source/Pcap_DNSProxy/Base.h:235:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(5177424U),
                                      ^
Source/Pcap_DNSProxy/Base.h:236:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2149679138U),
                                         ^
Source/Pcap_DNSProxy/Base.h:237:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2150137897U),
                                         ^
Source/Pcap_DNSProxy/Base.h:238:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2151612497U),
                                         ^
Source/Pcap_DNSProxy/Base.h:239:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(5374035U),
                                      ^
Source/Pcap_DNSProxy/Base.h:240:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2150072363U),
                                         ^
Source/Pcap_DNSProxy/Base.h:241:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2155610196U),
                                         ^
Source/Pcap_DNSProxy/Base.h:242:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(5570646U),
                                      ^
Source/Pcap_DNSProxy/Base.h:243:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2149810238U),
                                         ^
Source/Pcap_DNSProxy/Base.h:244:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(5701720U),
                                      ^
Source/Pcap_DNSProxy/Base.h:245:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(5832794U),
                                      ^
Source/Pcap_DNSProxy/Base.h:246:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2147516452U),
                                         ^
Source/Pcap_DNSProxy/Base.h:247:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2151710811U),
                                         ^
Source/Pcap_DNSProxy/Base.h:248:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2153611390U),
                                         ^
Source/Pcap_DNSProxy/Base.h:249:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(5963868U),
                                      ^
Source/Pcap_DNSProxy/Base.h:250:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2153676925U),
                                         ^
Source/Pcap_DNSProxy/Base.h:251:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(6094942U),
                                      ^
Source/Pcap_DNSProxy/Base.h:252:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2151448672U),
                                         ^
Source/Pcap_DNSProxy/Base.h:253:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2155544671U),
                                         ^
Source/Pcap_DNSProxy/Base.h:254:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(6291553U),
                                      ^
Source/Pcap_DNSProxy/Base.h:255:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(6422627U),
                                      ^
Source/Pcap_DNSProxy/Base.h:256:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(7274608U),
                                      ^
Source/Pcap_DNSProxy/Base.h:257:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(6553701U),
                                      ^
Source/Pcap_DNSProxy/Base.h:258:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(6750312U),
                                      ^
Source/Pcap_DNSProxy/Base.h:259:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2153545923U),
                                         ^
Source/Pcap_DNSProxy/Base.h:260:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2161115238U),
                                         ^
Source/Pcap_DNSProxy/Base.h:261:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2155905154U),
                                         ^
Source/Pcap_DNSProxy/Base.h:262:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(6881386U),
                                      ^
Source/Pcap_DNSProxy/Base.h:263:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(7012460U),
                                      ^
Source/Pcap_DNSProxy/Base.h:264:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2156101794U),
                                         ^
Source/Pcap_DNSProxy/Base.h:265:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2159575234U),
                                         ^
Source/Pcap_DNSProxy/Base.h:266:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2162196706U),
                                         ^
Source/Pcap_DNSProxy/Base.h:267:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(7143534U),
                                      ^
Source/Pcap_DNSProxy/Base.h:268:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2157543585U),
                                         ^
Source/Pcap_DNSProxy/Base.h:269:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2158461100U),
                                         ^
Source/Pcap_DNSProxy/Base.h:270:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(7405682U),
                                      ^
Source/Pcap_DNSProxy/Base.h:271:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(8781959U),
                                      ^
Source/Pcap_DNSProxy/Base.h:272:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(7536756U),
                                      ^
Source/Pcap_DNSProxy/Base.h:273:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(7929978U),
                                      ^
Source/Pcap_DNSProxy/Base.h:274:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(7667830U),
                                      ^
Source/Pcap_DNSProxy/Base.h:275:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(7798904U),
                                      ^
Source/Pcap_DNSProxy/Base.h:276:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2159050929U),
                                         ^
Source/Pcap_DNSProxy/Base.h:277:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2159247569U),
                                         ^
Source/Pcap_DNSProxy/Base.h:278:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2161672409U),
                                         ^
Source/Pcap_DNSProxy/Base.h:279:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2162393317U),
                                         ^
Source/Pcap_DNSProxy/Base.h:280:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(8061052U),
                                      ^
Source/Pcap_DNSProxy/Base.h:281:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(8388737U),
                                      ^
Source/Pcap_DNSProxy/Base.h:282:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2162557053U),
                                         ^
Source/Pcap_DNSProxy/Base.h:283:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(8257663U),
                                      ^
Source/Pcap_DNSProxy/Base.h:284:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2155970692U),
                                         ^
Source/Pcap_DNSProxy/Base.h:285:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2156232838U),
                                         ^
Source/Pcap_DNSProxy/Base.h:286:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2156429458U),
                                         ^
Source/Pcap_DNSProxy/Base.h:287:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(8519811U),
                                      ^
Source/Pcap_DNSProxy/Base.h:288:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(8650885U),
                                      ^
Source/Pcap_DNSProxy/Base.h:289:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2157609116U),
                                         ^
Source/Pcap_DNSProxy/Base.h:290:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2158002339U),
                                         ^
Source/Pcap_DNSProxy/Base.h:291:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2158264489U),
                                         ^
Source/Pcap_DNSProxy/Base.h:292:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2158657709U),
                                         ^
Source/Pcap_DNSProxy/Base.h:293:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(8913033U),
                                      ^
Source/Pcap_DNSProxy/Base.h:294:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(10092699U),
                                       ^
Source/Pcap_DNSProxy/Base.h:295:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(9044107U),
                                      ^
Source/Pcap_DNSProxy/Base.h:296:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(9437329U),
                                      ^
Source/Pcap_DNSProxy/Base.h:297:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(9175181U),
                                      ^
Source/Pcap_DNSProxy/Base.h:298:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(9306255U),
                                      ^
Source/Pcap_DNSProxy/Base.h:299:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2159182005U),
                                         ^
Source/Pcap_DNSProxy/Base.h:300:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2159640762U),
                                         ^
Source/Pcap_DNSProxy/Base.h:301:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2159771837U),
                                         ^
Source/Pcap_DNSProxy/Base.h:302:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2159968452U),
                                         ^
Source/Pcap_DNSProxy/Base.h:303:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(9568403U),
                                      ^
Source/Pcap_DNSProxy/Base.h:304:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(9699477U),
                                      ^
Source/Pcap_DNSProxy/Base.h:305:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2160492772U),
                                         ^
Source/Pcap_DNSProxy/Base.h:306:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2162721001U),
                                         ^
Source/Pcap_DNSProxy/Base.h:307:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(9830551U),
                                      ^
Source/Pcap_DNSProxy/Base.h:308:38: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(9961625U),
                                      ^
Source/Pcap_DNSProxy/Base.h:309:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2147582087U),
                                         ^
Source/Pcap_DNSProxy/Base.h:310:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2156494986U),
                                         ^
Source/Pcap_DNSProxy/Base.h:311:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2156626060U),
                                         ^
Source/Pcap_DNSProxy/Base.h:312:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2156757135U),
                                         ^
Source/Pcap_DNSProxy/Base.h:313:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(10223773U),
                                       ^
Source/Pcap_DNSProxy/Base.h:314:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(11141291U),
                                       ^
Source/Pcap_DNSProxy/Base.h:315:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(10354847U),
                                       ^
Source/Pcap_DNSProxy/Base.h:316:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(10748069U),
                                       ^
Source/Pcap_DNSProxy/Base.h:317:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(10485921U),
                                       ^
Source/Pcap_DNSProxy/Base.h:318:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(10616995U),
                                       ^
Source/Pcap_DNSProxy/Base.h:319:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2157150357U),
                                         ^
Source/Pcap_DNSProxy/Base.h:320:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2157346967U),
                                         ^
Source/Pcap_DNSProxy/Base.h:321:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2157478043U),
                                         ^
Source/Pcap_DNSProxy/Base.h:322:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2157805726U),
                                         ^
Source/Pcap_DNSProxy/Base.h:323:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(10879143U),
                                       ^
Source/Pcap_DNSProxy/Base.h:324:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(11010217U),
                                       ^
Source/Pcap_DNSProxy/Base.h:325:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2158330022U),
                                         ^
Source/Pcap_DNSProxy/Base.h:326:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2158526638U),
                                         ^
Source/Pcap_DNSProxy/Base.h:327:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2158985396U),
                                         ^
Source/Pcap_DNSProxy/Base.h:328:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2159444151U),
                                         ^
Source/Pcap_DNSProxy/Base.h:329:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(11272365U),
                                       ^
Source/Pcap_DNSProxy/Base.h:330:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(11862198U),
                                       ^
Source/Pcap_DNSProxy/Base.h:331:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(11403439U),
                                       ^
Source/Pcap_DNSProxy/Base.h:332:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(11534513U),
                                       ^
Source/Pcap_DNSProxy/Base.h:333:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2159837375U),
                                         ^
Source/Pcap_DNSProxy/Base.h:334:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2160427239U),
                                         ^
Source/Pcap_DNSProxy/Base.h:335:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2163146930U),
                                         ^
Source/Pcap_DNSProxy/Base.h:336:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(11731124U),
                                       ^
Source/Pcap_DNSProxy/Base.h:337:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2148106382U),
                                         ^
Source/Pcap_DNSProxy/Base.h:338:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2156953745U),
                                         ^
Source/Pcap_DNSProxy/Base.h:339:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2157215903U),
                                         ^
Source/Pcap_DNSProxy/Base.h:340:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(11993272U),
                                       ^
Source/Pcap_DNSProxy/Base.h:341:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(12517568U),
                                       ^
Source/Pcap_DNSProxy/Base.h:342:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(12124346U),
                                       ^
Source/Pcap_DNSProxy/Base.h:343:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(12255420U),
                                       ^
Source/Pcap_DNSProxy/Base.h:344:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2158723278U),
                                         ^
Source/Pcap_DNSProxy/Base.h:345:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2161606881U),
                                         ^
Source/Pcap_DNSProxy/Base.h:346:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2162983149U),
                                         ^
Source/Pcap_DNSProxy/Base.h:347:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(12386494U),
                                       ^
Source/Pcap_DNSProxy/Base.h:348:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2160558287U),
                                         ^
Source/Pcap_DNSProxy/Base.h:349:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2162852075U),
                                         ^
Source/Pcap_DNSProxy/Base.h:350:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(12648642U),
                                       ^
Source/Pcap_DNSProxy/Base.h:351:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(13631697U),
                                       ^
Source/Pcap_DNSProxy/Base.h:352:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(12779716U),
                                       ^
Source/Pcap_DNSProxy/Base.h:353:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(13172938U),
                                       ^
Source/Pcap_DNSProxy/Base.h:354:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(12910790U),
                                       ^
Source/Pcap_DNSProxy/Base.h:355:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(13041864U),
                                       ^
Source/Pcap_DNSProxy/Base.h:356:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2160099521U),
                                         ^
Source/Pcap_DNSProxy/Base.h:357:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2160623817U),
                                         ^
Source/Pcap_DNSProxy/Base.h:358:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2160754893U),
                                         ^
Source/Pcap_DNSProxy/Base.h:359:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2161279189U),
                                         ^
Source/Pcap_DNSProxy/Base.h:360:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(13304012U),
                                       ^
Source/Pcap_DNSProxy/Base.h:361:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(13435086U),
                                       ^
Source/Pcap_DNSProxy/Base.h:362:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2161803483U),
                                         ^
Source/Pcap_DNSProxy/Base.h:363:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2163114224U),
                                         ^
Source/Pcap_DNSProxy/Base.h:364:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2163376371U),
                                         ^
Source/Pcap_DNSProxy/Base.h:365:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2164195535U),
                                         ^
Source/Pcap_DNSProxy/Base.h:366:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2160820428U),
                                         ^
Source/Pcap_DNSProxy/Base.h:367:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(13762771U),
                                       ^
Source/Pcap_DNSProxy/Base.h:368:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(14680289U),
                                       ^
Source/Pcap_DNSProxy/Base.h:369:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(13893845U),
                                       ^
Source/Pcap_DNSProxy/Base.h:370:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(14287067U),
                                       ^
Source/Pcap_DNSProxy/Base.h:371:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(14024919U),
                                       ^
Source/Pcap_DNSProxy/Base.h:372:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(14155993U),
                                       ^
Source/Pcap_DNSProxy/Base.h:373:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2161344724U),
                                         ^
Source/Pcap_DNSProxy/Base.h:374:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2161541341U),
                                         ^
Source/Pcap_DNSProxy/Base.h:375:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2162065631U),
                                         ^
Source/Pcap_DNSProxy/Base.h:376:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2163310836U),
                                         ^
Source/Pcap_DNSProxy/Base.h:377:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(14418141U),
                                       ^
Source/Pcap_DNSProxy/Base.h:378:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(14549215U),
                                       ^
Source/Pcap_DNSProxy/Base.h:379:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2163572982U),
                                         ^
Source/Pcap_DNSProxy/Base.h:380:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2163704056U),
                                         ^
Source/Pcap_DNSProxy/Base.h:381:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2163900667U),
                                         ^
Source/Pcap_DNSProxy/Base.h:382:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2164031741U),
                                         ^
Source/Pcap_DNSProxy/Base.h:383:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(14811363U),
                                       ^
Source/Pcap_DNSProxy/Base.h:384:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(15663344U),
                                       ^
Source/Pcap_DNSProxy/Base.h:385:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(14942437U),
                                       ^
Source/Pcap_DNSProxy/Base.h:386:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(15270122U),
                                       ^
Source/Pcap_DNSProxy/Base.h:387:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2164130022U),
                                         ^
Source/Pcap_DNSProxy/Base.h:388:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(15139048U),
                                       ^
Source/Pcap_DNSProxy/Base.h:389:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2147647491U),
                                         ^
Source/Pcap_DNSProxy/Base.h:390:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2147778565U),
                                         ^
Source/Pcap_DNSProxy/Base.h:391:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2147909639U),
                                         ^
Source/Pcap_DNSProxy/Base.h:392:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(15401196U),
                                       ^
Source/Pcap_DNSProxy/Base.h:393:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(15532270U),
                                       ^
Source/Pcap_DNSProxy/Base.h:394:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2148040715U),
                                         ^
Source/Pcap_DNSProxy/Base.h:395:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2148302862U),
                                         ^
Source/Pcap_DNSProxy/Base.h:396:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2148499472U),
                                         ^
Source/Pcap_DNSProxy/Base.h:397:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2148630546U),
                                         ^
Source/Pcap_DNSProxy/Base.h:398:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(15794418U),
                                       ^
Source/Pcap_DNSProxy/Base.h:399:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(16187640U),
                                       ^
Source/Pcap_DNSProxy/Base.h:400:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(15925492U),
                                       ^
Source/Pcap_DNSProxy/Base.h:401:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(16056566U),
                                       ^
Source/Pcap_DNSProxy/Base.h:402:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2148761620U),
                                         ^
Source/Pcap_DNSProxy/Base.h:403:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2148892695U),
                                         ^
Source/Pcap_DNSProxy/Base.h:404:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2149089305U),
                                         ^
Source/Pcap_DNSProxy/Base.h:405:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2149220379U),
                                         ^
Source/Pcap_DNSProxy/Base.h:406:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(16318714U),
                                       ^
Source/Pcap_DNSProxy/Base.h:407:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(16449788U),
                                       ^
Source/Pcap_DNSProxy/Base.h:408:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2149351453U),
                                         ^
Source/Pcap_DNSProxy/Base.h:409:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2149482527U),
                                         ^
Source/Pcap_DNSProxy/Base.h:410:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2155839708U),
                                         ^
Source/Pcap_DNSProxy/Base.h:411:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2163802365U),
                                         ^
Source/Pcap_DNSProxy/Base.h:412:39: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(16646399U),
                                       ^
Source/Pcap_DNSProxy/Base.h:413:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2148171789U),
                                         ^
Source/Pcap_DNSProxy/Base.h:414:41: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  static_cast<const uint32_t>(2148958464U)
                                         ^
Source/Pcap_DNSProxy/Base.cpp: In function 'bool MBS_To_WCS_String(const uint8_t*, size_t, std::wstring&)':
Source/Pcap_DNSProxy/Base.cpp:112:152: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  if (mbstowcs(TargetBuffer.get(), reinterpret_cast<const char *>(Buffer), DataLength + NULL_TERMINATE_LENGTH) == static_cast<const size_t>(RETURN_ERROR))
                                                                                                                                                        ^
Source/Pcap_DNSProxy/Base.cpp: In function 'bool WCS_To_MBS_String(const wchar_t*, size_t, std::string&)':
Source/Pcap_DNSProxy/Base.cpp:157:146: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  if (wcstombs(reinterpret_cast<char *>(TargetBuffer.get()), Buffer, DataLength + NULL_TERMINATE_LENGTH) == static_cast<const size_t>(RETURN_ERROR))
                                                                                                                                                  ^
Source/Pcap_DNSProxy/Base.cpp: In function 'void CaseConvert(uint8_t*, size_t, bool)':
Source/Pcap_DNSProxy/Base.cpp:185:70: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
     Buffer[Index] = static_cast<const uint8_t>(toupper(Buffer[Index]));
                                                                      ^
Source/Pcap_DNSProxy/Base.cpp:188:70: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
     Buffer[Index] = static_cast<const uint8_t>(tolower(Buffer[Index]));
                                                                      ^
Source/Pcap_DNSProxy/Base.cpp: In function 'void CaseConvert(std::string&, bool)':
Source/Pcap_DNSProxy/Base.cpp:204:60: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    StringIter = static_cast<const char>(toupper(StringIter));
                                                            ^
Source/Pcap_DNSProxy/Base.cpp:207:60: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    StringIter = static_cast<const char>(tolower(StringIter));
                                                            ^
Source/Pcap_DNSProxy/Base.cpp: In function 'void CaseConvert(std::wstring&, bool)':
Source/Pcap_DNSProxy/Base.cpp:222:63: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    StringIter = static_cast<const wchar_t>(toupper(StringIter));
                                                               ^
Source/Pcap_DNSProxy/Base.cpp:225:63: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    StringIter = static_cast<const wchar_t>(tolower(StringIter));
                                                               ^
Source/Pcap_DNSProxy/Base.cpp: In function 'HUFFMAN_RETURN_TYPE HPACK_HuffmanEncoding(uint8_t*, size_t, size_t*, uint8_t*, size_t, size_t*)':
Source/Pcap_DNSProxy/Base.cpp:478:44: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
     Mask = static_cast<const uint64_t>(0xFF) << Shift;
                                            ^
Source/Pcap_DNSProxy/Base.cpp:480:56: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
     *Buffer = static_cast<const uint8_t>(Value >> Shift);
                                                        ^
Source/Pcap_DNSProxy/Base.cpp:497:42: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    Mask = (static_cast<const uint64_t>(1U) << Shift) - 1U;
                                          ^
Source/Pcap_DNSProxy/Base.cpp:498:67: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    *Buffer = static_cast<const uint8_t>((BitQueue << Shift) | Mask);
                                                                   ^
Source/Pcap_DNSProxy/Base.cpp: In function 'HUFFMAN_RETURN_TYPE HPACK_HuffmanDecoding(uint8_t*, size_t, size_t*, uint8_t*, size_t, size_t*)':
Source/Pcap_DNSProxy/Base.cpp:534:64: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
 #define ONE(TC)       static_cast<const uint16_t>((TC) & 0xFFFF)
                                                                ^
Source/Pcap_DNSProxy/Base.cpp:549:12: note: in expansion of macro 'ONE'
     Temp = ONE(TC);
            ^~~
Source/Pcap_DNSProxy/Base.cpp:533:62: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
 #define ZERO(TC)      static_cast<const uint16_t>((TC) >> 16U)
                                                              ^
Source/Pcap_DNSProxy/Base.cpp:551:12: note: in expansion of macro 'ZERO'
     Temp = ZERO(TC);
            ^~~~
Source/Pcap_DNSProxy/Base.cpp:562:54: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
       *TargetBuffer = static_cast<const uint8_t>(Temp);
                                                      ^
Source/Pcap_DNSProxy/Base.cpp: In function 'void GenerateRandomBuffer(void*, size_t, const void*, uint64_t, uint64_t)':
Source/Pcap_DNSProxy/Base.cpp:628:92: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    std::uniform_int_distribution<size_t> RandomDistribution(static_cast<const size_t>(Lower), static_cast<const size_t>(Upper));
                                                                                            ^
Source/Pcap_DNSProxy/Base.cpp:628:126: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    std::uniform_int_distribution<size_t> RandomDistribution(static_cast<const size_t>(Lower), static_cast<const size_t>(Upper));
                                                                                                                              ^
Source/Pcap_DNSProxy/Base.cpp:652:96: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    std::uniform_int_distribution<uint32_t> RandomDistribution(static_cast<const uint32_t>(Lower), static_cast<const uint32_t>(Upper));
                                                                                                ^
Source/Pcap_DNSProxy/Base.cpp:652:132: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    std::uniform_int_distribution<uint32_t> RandomDistribution(static_cast<const uint32_t>(Lower), static_cast<const uint32_t>(Upper));
                                                                                                                                    ^
Source/Pcap_DNSProxy/Base.cpp:664:96: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    std::uniform_int_distribution<uint16_t> RandomDistribution(static_cast<const uint16_t>(Lower), static_cast<const uint16_t>(Upper));
                                                                                                ^
Source/Pcap_DNSProxy/Base.cpp:664:132: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    std::uniform_int_distribution<uint16_t> RandomDistribution(static_cast<const uint16_t>(Lower), static_cast<const uint16_t>(Upper));
                                                                                                                                    ^
Source/Pcap_DNSProxy/Base.cpp:673:249: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    *reinterpret_cast<uint8_t *>(BufferPointer) = static_cast<const uint8_t>((*const_cast<std::uniform_int_distribution<uint16_t> *>(reinterpret_cast<const std::uniform_int_distribution<uint16_t> *>(Distribution)))(*GlobalRunningStatus.RandomEngine));
                                                                                                                                                                                                                                                         ^
Source/Pcap_DNSProxy/Base.cpp:676:95: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    std::uniform_int_distribution<uint16_t> RandomDistribution(static_cast<const uint8_t>(Lower), static_cast<const uint8_t>(Upper));
                                                                                               ^
Source/Pcap_DNSProxy/Base.cpp:676:130: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    std::uniform_int_distribution<uint16_t> RandomDistribution(static_cast<const uint8_t>(Lower), static_cast<const uint8_t>(Upper));
                                                                                                                                  ^
Source/Pcap_DNSProxy/Base.cpp:677:130: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    *reinterpret_cast<uint8_t *>(BufferPointer) = static_cast<const uint8_t>(RandomDistribution(*GlobalRunningStatus.RandomEngine));
                                                                                                                                  ^
Source/Pcap_DNSProxy/Base.cpp:703:159: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
     *(reinterpret_cast<uint8_t *>(BufferPointer) + Index * sizeof(uint8_t)) = static_cast<const uint8_t>(RandomDistribution(*GlobalRunningStatus.RandomEngine));
                                                                                                                                                               ^
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:153: /openwrt/build_dir/target-x86_64_musl/pcap-dnsproxy-0.4.9.13-2019-05-05-bc9f540d/.built] Error 1
```
