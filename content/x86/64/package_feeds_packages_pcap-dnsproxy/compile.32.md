---
title: "compile.32"
date: 2021-06-11 17:53:58.904227
hidden: false
draft: false
weight: -32
---

build number: `32`

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
ninja: Entering directory `/openwrt/build_dir/target-x86_64_musl/pcap-dnsproxy-0.4.9.13-2019-05-05-bc9f540d/'
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
[2/22] Building CXX object Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Capture.cpp.o
FAILED: Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Capture.cpp.o 
/openwrt/staging_dir/host/bin/ccache /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-g++ -DENABLE_LIBSODIUM -DENABLE_PCAP -DENABLE_TLS -DPLATFORM_OPENWRT  -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/pcap-dnsproxy-0.4.9.13-2019-05-05-bc9f540d=pcap-dnsproxy-0.4.9.13-2019-05-05-bc9f540d -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -Wall -Wextra -DPIC -fpic -O3 -std=c++14 -DNDEBUG -MD -MT Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Capture.cpp.o -MF Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Capture.cpp.o.d -o Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Capture.cpp.o -c Source/Pcap_DNSProxy/Capture.cpp
In file included from Source/Pcap_DNSProxy/Structure.h:23,
                 from Source/Pcap_DNSProxy/Definition.h:23,
                 from Source/Pcap_DNSProxy/Type.h:23,
                 from Source/Pcap_DNSProxy/Template.h:23,
                 from Source/Pcap_DNSProxy/Include.h:23,
                 from Source/Pcap_DNSProxy/Capture.h:23,
                 from Source/Pcap_DNSProxy/Capture.cpp:20:
Source/Pcap_DNSProxy/Platform.h:657:3: error: #error "The version of LibSodium is too old."
  #error "The version of LibSodium is too old."
   ^~~~~
In file included from Source/Pcap_DNSProxy/Type.h:23,
                 from Source/Pcap_DNSProxy/Template.h:23,
                 from Source/Pcap_DNSProxy/Include.h:23,
                 from Source/Pcap_DNSProxy/Capture.h:23,
                 from Source/Pcap_DNSProxy/Capture.cpp:20:
Source/Pcap_DNSProxy/Capture.cpp: In function 'void CaptureInit()':
Source/Pcap_DNSProxy/Definition.h:381:136: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                                                                                                        ^
Source/Pcap_DNSProxy/Definition.h:382:94: note: in definition of macro 'usleep'
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                              ^~~~~~~~~~~
Source/Pcap_DNSProxy/Capture.cpp:62:4: note: in expansion of macro 'Sleep'
    Sleep(Parameter.FileRefreshTime);
    ^~~~~
Source/Pcap_DNSProxy/Definition.h:382:105: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                                         ^
Source/Pcap_DNSProxy/Definition.h:381:57: note: in expansion of macro 'usleep'
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                         ^~~~~~
Source/Pcap_DNSProxy/Capture.cpp:62:4: note: in expansion of macro 'Sleep'
    Sleep(Parameter.FileRefreshTime);
    ^~~~~
Source/Pcap_DNSProxy/Definition.h:381:136: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                                                                                                        ^
Source/Pcap_DNSProxy/Definition.h:382:94: note: in definition of macro 'usleep'
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                              ^~~~~~~~~~~
Source/Pcap_DNSProxy/Capture.cpp:70:4: note: in expansion of macro 'Sleep'
    Sleep(Parameter.FileRefreshTime);
    ^~~~~
Source/Pcap_DNSProxy/Definition.h:382:105: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                                         ^
Source/Pcap_DNSProxy/Definition.h:381:57: note: in expansion of macro 'usleep'
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                         ^~~~~~
Source/Pcap_DNSProxy/Capture.cpp:70:4: note: in expansion of macro 'Sleep'
    Sleep(Parameter.FileRefreshTime);
    ^~~~~
Source/Pcap_DNSProxy/Definition.h:381:136: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                                                                                                        ^
Source/Pcap_DNSProxy/Definition.h:382:94: note: in definition of macro 'usleep'
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                              ^~~~~~~~~~~
Source/Pcap_DNSProxy/Capture.cpp:150:3: note: in expansion of macro 'Sleep'
   Sleep(Parameter.FileRefreshTime);
   ^~~~~
Source/Pcap_DNSProxy/Definition.h:382:105: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                                         ^
Source/Pcap_DNSProxy/Definition.h:381:57: note: in expansion of macro 'usleep'
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                         ^~~~~~
Source/Pcap_DNSProxy/Capture.cpp:150:3: note: in expansion of macro 'Sleep'
   Sleep(Parameter.FileRefreshTime);
   ^~~~~
Source/Pcap_DNSProxy/Capture.cpp: In function 'bool Capture_MainProcess(const pcap_if*, bool)':
Source/Pcap_DNSProxy/Capture.cpp:419:51: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
   static_cast<const int>(Parameter.LargeBufferSize),
                                                   ^
Source/Pcap_DNSProxy/Capture.cpp:421:54: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
   static_cast<const int>(Parameter.PcapReadingTimeout),
                                                      ^
In file included from Source/Pcap_DNSProxy/Type.h:23,
                 from Source/Pcap_DNSProxy/Template.h:23,
                 from Source/Pcap_DNSProxy/Include.h:23,
                 from Source/Pcap_DNSProxy/Capture.h:23,
                 from Source/Pcap_DNSProxy/Capture.cpp:20:
Source/Pcap_DNSProxy/Definition.h:381:136: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                                                                                                        ^
Source/Pcap_DNSProxy/Definition.h:382:94: note: in definition of macro 'usleep'
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                              ^~~~~~~~~~~
Source/Pcap_DNSProxy/Capture.cpp:545:3: note: in expansion of macro 'Sleep'
   Sleep(Parameter.FileRefreshTime);
   ^~~~~
Source/Pcap_DNSProxy/Definition.h:382:105: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                                         ^
Source/Pcap_DNSProxy/Definition.h:381:57: note: in expansion of macro 'usleep'
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                         ^~~~~~
Source/Pcap_DNSProxy/Capture.cpp:545:3: note: in expansion of macro 'Sleep'
   Sleep(Parameter.FileRefreshTime);
   ^~~~~
Source/Pcap_DNSProxy/Capture.cpp: In function 'bool Capture_AnalyzeNetworkLayer(uint16_t, const uint8_t*, size_t, size_t)':
Source/Pcap_DNSProxy/Capture.cpp:688:81: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    ntoh16(IPv6_Header->PayloadLength) >= static_cast<const size_t>(PayloadOffset) + sizeof(icmpv6_hdr))
                                                                                 ^
Source/Pcap_DNSProxy/Capture.cpp:691:107: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    if (GetChecksum_ICMPv6(IPv6_Header, Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset), ntoh16(IPv6_Header->PayloadLength) - static_cast<const size_t>(PayloadOffset)) != CHECKSUM_SUCCESS)
                                                                                                           ^
Source/Pcap_DNSProxy/Capture.cpp:691:186: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    if (GetChecksum_ICMPv6(IPv6_Header, Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset), ntoh16(IPv6_Header->PayloadLength) - static_cast<const size_t>(PayloadOffset)) != CHECKSUM_SUCCESS)
                                                                                                                                                                                          ^
Source/Pcap_DNSProxy/Capture.cpp:694:110: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    else if (Capture_AnalyzeICMP(AF_INET6, Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset), ntoh16(IPv6_Header->PayloadLength) - static_cast<const size_t>(PayloadOffset)))
                                                                                                              ^
Source/Pcap_DNSProxy/Capture.cpp:694:189: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    else if (Capture_AnalyzeICMP(AF_INET6, Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset), ntoh16(IPv6_Header->PayloadLength) - static_cast<const size_t>(PayloadOffset)))
                                                                                                                                                                                             ^
Source/Pcap_DNSProxy/Capture.cpp:702:81: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    ntoh16(IPv6_Header->PayloadLength) >= static_cast<const size_t>(PayloadOffset) + sizeof(tcp_hdr))
                                                                                 ^
Source/Pcap_DNSProxy/Capture.cpp:708:99: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    else if (Capture_AnalyzeTCP(Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset)))
                                                                                                   ^
Source/Pcap_DNSProxy/Capture.cpp:716:81: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    ntoh16(IPv6_Header->PayloadLength) >= static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr) + DNS_PACKET_MINSIZE)
                                                                                 ^
Source/Pcap_DNSProxy/Capture.cpp:724:129: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    const auto UDP_Header = reinterpret_cast<const udp_hdr *>(Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset));
                                                                                                                                 ^
Source/Pcap_DNSProxy/Capture.cpp:733:80: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      memcmp(Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr), DNSCurveParameter.DNSCurve_Target_Server_Main_IPv6.ReceiveMagicNumber, DNSCURVE_MAGIC_QUERY_LEN) == 0) ||
                                                                                ^
Source/Pcap_DNSProxy/Capture.cpp:737:80: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      memcmp(Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr), DNSCurveParameter.DNSCurve_Target_Server_Alternate_IPv6.ReceiveMagicNumber, DNSCURVE_MAGIC_QUERY_LEN) == 0)))
                                                                                ^
Source/Pcap_DNSProxy/Capture.cpp:742:101: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
     size_t DataLength = ntoh16(IPv6_Header->PayloadLength) - static_cast<const size_t>(PayloadOffset) - sizeof(udp_hdr), PacketEDNS_Offset = 0, PacketEDNS_Length = 0;
                                                                                                     ^
Source/Pcap_DNSProxy/Capture.cpp:748:96: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
       const_cast<uint8_t *>(Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr)),
                                                                                                ^
Source/Pcap_DNSProxy/Capture.cpp:750:78: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
       BufferSize - sizeof(ipv6_hdr) - static_cast<const size_t>(PayloadOffset) - sizeof(udp_hdr),
                                                                              ^
Source/Pcap_DNSProxy/Capture.cpp:761:97: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
       if (Capture_AnalyzeDNS(Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr), BufferSize - (sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr)), IsRegisterStatus))
                                                                                                 ^
Source/Pcap_DNSProxy/Capture.cpp:761:190: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
       if (Capture_AnalyzeDNS(Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr), BufferSize - (sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr)), IsRegisterStatus))
                                                                                                                                                                                              ^
Source/Pcap_DNSProxy/Capture.cpp:766:134: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
        if (IsRegisterStatus && Capture_PacketStatusCheck(AF_INET6, Buffer, sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr), DataLength, PacketEDNS_Offset, PacketEDNS_Length, true, PacketSource))
                                                                                                                                      ^
Source/Pcap_DNSProxy/Capture.cpp:772:111: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
        !Capture_PacketStatusCheck(AF_INET6, Buffer, sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr), DataLength, PacketEDNS_Offset, PacketEDNS_Length, false, PacketSource))
                                                                                                               ^
Source/Pcap_DNSProxy/Capture.cpp:779:53: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv6_Header->HopLimit) + static_cast<const size_t>(Parameter.HopLimitsFluctuation) >= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv6_HeaderStatus.HopLimit_StaticLoad) &&
                                                     ^
Source/Pcap_DNSProxy/Capture.cpp:779:113: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv6_Header->HopLimit) + static_cast<const size_t>(Parameter.HopLimitsFluctuation) >= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv6_HeaderStatus.HopLimit_StaticLoad) &&
                                                                                                                 ^
Source/Pcap_DNSProxy/Capture.cpp:779:233: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv6_Header->HopLimit) + static_cast<const size_t>(Parameter.HopLimitsFluctuation) >= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv6_HeaderStatus.HopLimit_StaticLoad) &&
                                                                                                                                                                                                                                         ^
Source/Pcap_DNSProxy/Capture.cpp:780:53: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv6_Header->HopLimit) <= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv6_HeaderStatus.HopLimit_StaticLoad) + static_cast<const size_t>(Parameter.HopLimitsFluctuation)) ||
                                                     ^
Source/Pcap_DNSProxy/Capture.cpp:780:173: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv6_Header->HopLimit) <= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv6_HeaderStatus.HopLimit_StaticLoad) + static_cast<const size_t>(Parameter.HopLimitsFluctuation)) ||
                                                                                                                                                                             ^
Source/Pcap_DNSProxy/Capture.cpp:780:233: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv6_Header->HopLimit) <= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv6_HeaderStatus.HopLimit_StaticLoad) + static_cast<const size_t>(Parameter.HopLimitsFluctuation)) ||
                                                                                                                                                                                                                                         ^
Source/Pcap_DNSProxy/Capture.cpp:782:53: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv6_Header->HopLimit) + static_cast<const size_t>(Parameter.HopLimitsFluctuation) >= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv6_HeaderStatus.HopLimit_DynamicMark) &&
                                                     ^
Source/Pcap_DNSProxy/Capture.cpp:782:113: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv6_Header->HopLimit) + static_cast<const size_t>(Parameter.HopLimitsFluctuation) >= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv6_HeaderStatus.HopLimit_DynamicMark) &&
                                                                                                                 ^
Source/Pcap_DNSProxy/Capture.cpp:782:234: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv6_Header->HopLimit) + static_cast<const size_t>(Parameter.HopLimitsFluctuation) >= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv6_HeaderStatus.HopLimit_DynamicMark) &&
                                                                                                                                                                                                                                          ^
Source/Pcap_DNSProxy/Capture.cpp:783:53: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv6_Header->HopLimit) <= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv6_HeaderStatus.HopLimit_DynamicMark) + static_cast<const size_t>(Parameter.HopLimitsFluctuation)))
                                                     ^
Source/Pcap_DNSProxy/Capture.cpp:783:174: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv6_Header->HopLimit) <= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv6_HeaderStatus.HopLimit_DynamicMark) + static_cast<const size_t>(Parameter.HopLimitsFluctuation)))
                                                                                                                                                                              ^
Source/Pcap_DNSProxy/Capture.cpp:783:234: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv6_Header->HopLimit) <= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv6_HeaderStatus.HopLimit_DynamicMark) + static_cast<const size_t>(Parameter.HopLimitsFluctuation)))
                                                                                                                                                                                                                                          ^
Source/Pcap_DNSProxy/Capture.cpp:788:130: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
       const_cast<dns_hdr *>(reinterpret_cast<const dns_hdr *>(Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr)))->Flags = hton16(ntoh16(reinterpret_cast<const dns_hdr *>(Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr))->Flags) | DNS_FLAG_GET_BIT_TC);
                                                                                                                                  ^
Source/Pcap_DNSProxy/Capture.cpp:788:276: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
       const_cast<dns_hdr *>(reinterpret_cast<const dns_hdr *>(Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr)))->Flags = hton16(ntoh16(reinterpret_cast<const dns_hdr *>(Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr))->Flags) | DNS_FLAG_GET_BIT_TC);
                                                                                                                                                                                                                                                                                    ^
Source/Pcap_DNSProxy/Capture.cpp:802:107: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      Capture_MatchPortToSend(AF_INET6, Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr), DataLength, BufferSize - sizeof(ipv6_hdr) - static_cast<const size_t>(PayloadOffset) - sizeof(udp_hdr), UDP_Header->DestinationPort /* , IsNeedTruncated, PacketEDNS_Length */ );
                                                                                                           ^
Source/Pcap_DNSProxy/Capture.cpp:802:211: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      Capture_MatchPortToSend(AF_INET6, Buffer + sizeof(ipv6_hdr) + static_cast<const size_t>(PayloadOffset) + sizeof(udp_hdr), DataLength, BufferSize - sizeof(ipv6_hdr) - static_cast<const size_t>(PayloadOffset) - sizeof(udp_hdr), UDP_Header->DestinationPort /* , IsNeedTruncated, PacketEDNS_Length */ );
                                                                                                                                                                                                                   ^
Source/Pcap_DNSProxy/Capture.cpp:815:80: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
   if (ntoh16(IPv4_Header->Length) <= static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET || ntoh16(IPv4_Header->Length) > Length ||
                                                                                ^
Source/Pcap_DNSProxy/Capture.cpp:854:77: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    ntoh16(IPv4_Header->Length) >= static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(icmp_hdr))
                                                                             ^
Source/Pcap_DNSProxy/Capture.cpp:857:115: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    if (GetChecksum_Internet(reinterpret_cast<const uint16_t *>(Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET), ntoh16(IPv4_Header->Length) - static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET) != CHECKSUM_SUCCESS)
                                                                                                                   ^
Source/Pcap_DNSProxy/Capture.cpp:857:212: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    if (GetChecksum_Internet(reinterpret_cast<const uint16_t *>(Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET), ntoh16(IPv4_Header->Length) - static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET) != CHECKSUM_SUCCESS)
                                                                                                                                                                                                                    ^
Source/Pcap_DNSProxy/Capture.cpp:860:93: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    else if (Capture_AnalyzeICMP(AF_INET, Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET, ntoh16(IPv4_Header->Length) - static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET))
                                                                                             ^
Source/Pcap_DNSProxy/Capture.cpp:860:189: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    else if (Capture_AnalyzeICMP(AF_INET, Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET, ntoh16(IPv4_Header->Length) - static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET))
                                                                                                                                                                                             ^
Source/Pcap_DNSProxy/Capture.cpp:868:77: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    ntoh16(IPv4_Header->Length) >= static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(tcp_hdr))
                                                                             ^
Source/Pcap_DNSProxy/Capture.cpp:871:130: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    if (GetChecksum_TCP_UDP(AF_INET, IPPROTO_TCP, Buffer, ntoh16(IPv4_Header->Length) - static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET, 0) != CHECKSUM_SUCCESS)
                                                                                                                                  ^
Source/Pcap_DNSProxy/Capture.cpp:874:83: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    else if (Capture_AnalyzeTCP(Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET))
                                                                                   ^
Source/Pcap_DNSProxy/Capture.cpp:882:77: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    ntoh16(IPv4_Header->Length) >= static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr) + DNS_PACKET_MINSIZE)
                                                                             ^
Source/Pcap_DNSProxy/Capture.cpp:886:127: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
     GetChecksum_TCP_UDP(AF_INET, IPPROTO_UDP, Buffer, ntoh16(IPv4_Header->Length) - static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET, 0) != CHECKSUM_SUCCESS)
                                                                                                                               ^
Source/Pcap_DNSProxy/Capture.cpp:890:113: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
    const auto UDP_Header = reinterpret_cast<const udp_hdr *>(Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET);
                                                                                                                 ^
Source/Pcap_DNSProxy/Capture.cpp:899:64: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      memcmp(Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr), DNSCurveParameter.DNSCurve_Target_Server_Main_IPv4.ReceiveMagicNumber, DNSCURVE_MAGIC_QUERY_LEN) == 0) ||
                                                                ^
Source/Pcap_DNSProxy/Capture.cpp:903:64: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      memcmp(Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr), DNSCurveParameter.DNSCurve_Target_Server_Alternate_IPv4.ReceiveMagicNumber, DNSCURVE_MAGIC_QUERY_LEN) == 0)))
                                                                ^
Source/Pcap_DNSProxy/Capture.cpp:908:97: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
     size_t DataLength = ntoh16(IPv4_Header->Length) - static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET - sizeof(udp_hdr), PacketEDNS_Offset = 0, PacketEDNS_Length = 0;
                                                                                                 ^
Source/Pcap_DNSProxy/Capture.cpp:914:80: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
       const_cast<uint8_t *>(Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr)),
                                                                                ^
Source/Pcap_DNSProxy/Capture.cpp:916:62: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
       BufferSize - static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET - sizeof(udp_hdr),
                                                              ^
Source/Pcap_DNSProxy/Capture.cpp:927:81: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
       if (Capture_AnalyzeDNS(Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr), BufferSize - (static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr)), IsRegisterStatus))
                                                                                 ^
Source/Pcap_DNSProxy/Capture.cpp:927:179: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
       if (Capture_AnalyzeDNS(Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr), BufferSize - (static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr)), IsRegisterStatus))
                                                                                                                                                                                   ^
Source/Pcap_DNSProxy/Capture.cpp:932:117: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
        if (IsRegisterStatus && Capture_PacketStatusCheck(AF_INET, Buffer, static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr), DataLength, PacketEDNS_Offset, PacketEDNS_Length, true, PacketSource))
                                                                                                                     ^
Source/Pcap_DNSProxy/Capture.cpp:938:94: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
        !Capture_PacketStatusCheck(AF_INET, Buffer, static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr), DataLength, PacketEDNS_Offset, PacketEDNS_Length, false, PacketSource))
                                                                                              ^
Source/Pcap_DNSProxy/Capture.cpp:945:48: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv4_Header->TTL) + static_cast<const size_t>(Parameter.HopLimitsFluctuation) >= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv4_HeaderStatus.TTL_StaticLoad) &&
                                                ^
Source/Pcap_DNSProxy/Capture.cpp:945:108: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv4_Header->TTL) + static_cast<const size_t>(Parameter.HopLimitsFluctuation) >= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv4_HeaderStatus.TTL_StaticLoad) &&
                                                                                                            ^
Source/Pcap_DNSProxy/Capture.cpp:945:223: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv4_Header->TTL) + static_cast<const size_t>(Parameter.HopLimitsFluctuation) >= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv4_HeaderStatus.TTL_StaticLoad) &&
                                                                                                                                                                                                                               ^
Source/Pcap_DNSProxy/Capture.cpp:946:48: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv4_Header->TTL) <= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv4_HeaderStatus.TTL_StaticLoad) + static_cast<const size_t>(Parameter.HopLimitsFluctuation)) ||
                                                ^
Source/Pcap_DNSProxy/Capture.cpp:946:163: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv4_Header->TTL) <= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv4_HeaderStatus.TTL_StaticLoad) + static_cast<const size_t>(Parameter.HopLimitsFluctuation)) ||
                                                                                                                                                                   ^
Source/Pcap_DNSProxy/Capture.cpp:946:223: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv4_Header->TTL) <= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv4_HeaderStatus.TTL_StaticLoad) + static_cast<const size_t>(Parameter.HopLimitsFluctuation)) ||
                                                                                                                                                                                                                               ^
Source/Pcap_DNSProxy/Capture.cpp:948:48: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv4_Header->TTL) + static_cast<const size_t>(Parameter.HopLimitsFluctuation) >= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv4_HeaderStatus.TTL_DynamicMark) &&
                                                ^
Source/Pcap_DNSProxy/Capture.cpp:948:108: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv4_Header->TTL) + static_cast<const size_t>(Parameter.HopLimitsFluctuation) >= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv4_HeaderStatus.TTL_DynamicMark) &&
                                                                                                            ^
Source/Pcap_DNSProxy/Capture.cpp:948:224: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv4_Header->TTL) + static_cast<const size_t>(Parameter.HopLimitsFluctuation) >= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv4_HeaderStatus.TTL_DynamicMark) &&
                                                                                                                                                                                                                                ^
Source/Pcap_DNSProxy/Capture.cpp:949:48: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv4_Header->TTL) <= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv4_HeaderStatus.TTL_DynamicMark) + static_cast<const size_t>(Parameter.HopLimitsFluctuation)))
                                                ^
Source/Pcap_DNSProxy/Capture.cpp:949:164: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv4_Header->TTL) <= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv4_HeaderStatus.TTL_DynamicMark) + static_cast<const size_t>(Parameter.HopLimitsFluctuation)))
                                                                                                                                                                    ^
Source/Pcap_DNSProxy/Capture.cpp:949:224: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      static_cast<const size_t>(IPv4_Header->TTL) <= static_cast<const size_t>(PacketSource->ServerPacketStatus.NetworkLayerStatus.IPv4_HeaderStatus.TTL_DynamicMark) + static_cast<const size_t>(Parameter.HopLimitsFluctuation)))
                                                                                                                                                                                                                                ^
Source/Pcap_DNSProxy/Capture.cpp:954:114: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
       const_cast<dns_hdr *>(reinterpret_cast<const dns_hdr *>(Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr)))->Flags = hton16(ntoh16(reinterpret_cast<const dns_hdr *>(Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr))->Flags) | DNS_FLAG_GET_BIT_TC);
                                                                                                                  ^
Source/Pcap_DNSProxy/Capture.cpp:954:265: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
       const_cast<dns_hdr *>(reinterpret_cast<const dns_hdr *>(Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr)))->Flags = hton16(ntoh16(reinterpret_cast<const dns_hdr *>(Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr))->Flags) | DNS_FLAG_GET_BIT_TC);
                                                                                                                                                                                                                                                                         ^
Source/Pcap_DNSProxy/Capture.cpp:968:90: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      Capture_MatchPortToSend(AF_INET, Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr), DataLength, BufferSize - static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET - sizeof(udp_hdr), UDP_Header->DestinationPort /* , IsNeedTruncated, PacketEDNS_Length */ );
                                                                                          ^
Source/Pcap_DNSProxy/Capture.cpp:968:199: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      Capture_MatchPortToSend(AF_INET, Buffer + static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET + sizeof(udp_hdr), DataLength, BufferSize - static_cast<const size_t>(IPv4_Header->IHL) * IPV4_IHL_BYTES_SET - sizeof(udp_hdr), UDP_Header->DestinationPort /* , IsNeedTruncated, PacketEDNS_Length */ );
                                                                                                                                                                                                       ^
Source/Pcap_DNSProxy/Capture.cpp: In function 'ssize_t Capture_AnalyzeFragment(uint16_t, const uint8_t*, size_t, bool&)':
Source/Pcap_DNSProxy/Capture.cpp:1008:115: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
     if (Index + sizeof(ipv6_extension_hop_by_hop) + static_cast<const size_t>(IPv6_HopByHopHeader->ExtensionLength) * UNITS_IN_8_OCTETS <= Length)
                                                                                                                   ^
Source/Pcap_DNSProxy/Capture.cpp:1011:113: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      Index += sizeof(ipv6_extension_hop_by_hop) + static_cast<const size_t>(IPv6_HopByHopHeader->ExtensionLength) * UNITS_IN_8_OCTETS;
                                                                                                                 ^
Source/Pcap_DNSProxy/Capture.cpp:1022:111: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
     if (Index + sizeof(ipv6_extension_routing) + static_cast<const size_t>(IPv6_RoutingHeader->ExtensionLength) * UNITS_IN_8_OCTETS <= Length)
                                                                                                               ^
Source/Pcap_DNSProxy/Capture.cpp:1025:109: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      Index += sizeof(ipv6_extension_routing) + static_cast<const size_t>(IPv6_RoutingHeader->ExtensionLength) * UNITS_IN_8_OCTETS;
                                                                                                             ^
Source/Pcap_DNSProxy/Capture.cpp:1060:119: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
     if (Index + sizeof(ipv6_extension_destination) + static_cast<const size_t>(IPv6_DestinationHeader->ExtensionLength) * UNITS_IN_8_OCTETS <= Length)
                                                                                                                       ^
Source/Pcap_DNSProxy/Capture.cpp:1063:117: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      Index += sizeof(ipv6_extension_destination) + static_cast<const size_t>(IPv6_DestinationHeader->ExtensionLength) * UNITS_IN_8_OCTETS;
                                                                                                                     ^
Source/Pcap_DNSProxy/Capture.cpp:1074:101: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
     if (Index + sizeof(ipv6_extension_hip) + static_cast<const size_t>(IPv6_HIP_Header->HeaderLength) * UNITS_IN_8_OCTETS <= Length)
                                                                                                     ^
Source/Pcap_DNSProxy/Capture.cpp:1077:99: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      Index += sizeof(ipv6_extension_hip) + static_cast<const size_t>(IPv6_HIP_Header->HeaderLength) * UNITS_IN_8_OCTETS;
                                                                                                   ^
In file included from Source/Pcap_DNSProxy/Type.h:23,
                 from Source/Pcap_DNSProxy/Template.h:23,
                 from Source/Pcap_DNSProxy/Include.h:23,
                 from Source/Pcap_DNSProxy/Capture.h:23,
                 from Source/Pcap_DNSProxy/Capture.cpp:20:
Source/Pcap_DNSProxy/Capture.cpp: In function 'bool Capture_MatchPortToSend(uint16_t, const uint8_t*, size_t, size_t, uint16_t)':
Source/Pcap_DNSProxy/Definition.h:381:136: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                                                                                                        ^
Source/Pcap_DNSProxy/Definition.h:382:94: note: in definition of macro 'usleep'
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                              ^~~~~~~~~~~
Source/Pcap_DNSProxy/Capture.cpp:1445:2: note: in expansion of macro 'Sleep'
  Sleep(Parameter.ReceiveWaiting);
  ^~~~~
Source/Pcap_DNSProxy/Definition.h:382:105: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                                         ^
Source/Pcap_DNSProxy/Definition.h:381:57: note: in expansion of macro 'usleep'
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                         ^~~~~~
Source/Pcap_DNSProxy/Capture.cpp:1445:2: note: in expansion of macro 'Sleep'
  Sleep(Parameter.ReceiveWaiting);
  ^~~~~
[3/22] Building CXX object Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Configuration.cpp.o
FAILED: Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Configuration.cpp.o 
/openwrt/staging_dir/host/bin/ccache /openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/bin/x86_64-openwrt-linux-musl-g++ -DENABLE_LIBSODIUM -DENABLE_PCAP -DENABLE_TLS -DPLATFORM_OPENWRT  -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/pcap-dnsproxy-0.4.9.13-2019-05-05-bc9f540d=pcap-dnsproxy-0.4.9.13-2019-05-05-bc9f540d -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -Wall -Wextra -DPIC -fpic -O3 -std=c++14 -DNDEBUG -MD -MT Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Configuration.cpp.o -MF Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Configuration.cpp.o.d -o Source/Pcap_DNSProxy/CMakeFiles/Pcap_DNSProxy.dir/Configuration.cpp.o -c Source/Pcap_DNSProxy/Configuration.cpp
In file included from Source/Pcap_DNSProxy/Structure.h:23,
                 from Source/Pcap_DNSProxy/Definition.h:23,
                 from Source/Pcap_DNSProxy/Type.h:23,
                 from Source/Pcap_DNSProxy/Template.h:23,
                 from Source/Pcap_DNSProxy/Include.h:23,
                 from Source/Pcap_DNSProxy/Configuration.h:23,
                 from Source/Pcap_DNSProxy/Configuration.cpp:20:
Source/Pcap_DNSProxy/Platform.h:657:3: error: #error "The version of LibSodium is too old."
  #error "The version of LibSodium is too old."
   ^~~~~
Source/Pcap_DNSProxy/Configuration.cpp: In function 'bool ReadSupport_ReadText(const FILE*, READ_TEXT_TYPE, size_t)':
Source/Pcap_DNSProxy/Configuration.cpp:136:79: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      SingleText = ((static_cast<const uint16_t>(FileBuffer.get()[Index] & 0x0F)) << 12U) + ((static_cast<const uint16_t>(FileBuffer.get()[Index + 1U] & 0x3F)) << 6U) + static_cast<const uint16_t>(FileBuffer.get()[Index + 2U] & 0x3F);
                                                                               ^
Source/Pcap_DNSProxy/Configuration.cpp:136:157: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      SingleText = ((static_cast<const uint16_t>(FileBuffer.get()[Index] & 0x0F)) << 12U) + ((static_cast<const uint16_t>(FileBuffer.get()[Index + 1U] & 0x3F)) << 6U) + static_cast<const uint16_t>(FileBuffer.get()[Index + 2U] & 0x3F);
                                                                                                                                                             ^
Source/Pcap_DNSProxy/Configuration.cpp:136:232: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      SingleText = ((static_cast<const uint16_t>(FileBuffer.get()[Index] & 0x0F)) << 12U) + ((static_cast<const uint16_t>(FileBuffer.get()[Index + 1U] & 0x3F)) << 6U) + static_cast<const uint16_t>(FileBuffer.get()[Index + 2U] & 0x3F);
                                                                                                                                                                                                                                        ^
Source/Pcap_DNSProxy/Configuration.cpp:176:79: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      SingleText = ((static_cast<const uint16_t>(FileBuffer.get()[Index] & 0x1F)) << 6U) + static_cast<const uint16_t>(FileBuffer.get()[Index] & 0x3F);
                                                                               ^
Source/Pcap_DNSProxy/Configuration.cpp:176:149: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
      SingleText = ((static_cast<const uint16_t>(FileBuffer.get()[Index] & 0x1F)) << 6U) + static_cast<const uint16_t>(FileBuffer.get()[Index] & 0x3F);
                                                                                                                                                     ^
In file included from Source/Pcap_DNSProxy/Type.h:23,
                 from Source/Pcap_DNSProxy/Template.h:23,
                 from Source/Pcap_DNSProxy/Include.h:23,
                 from Source/Pcap_DNSProxy/Configuration.h:23,
                 from Source/Pcap_DNSProxy/Configuration.cpp:20:
Source/Pcap_DNSProxy/Definition.h:337:100: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
               (sizeof(uint8_t) * BYTES_TO_BITS) | (reinterpret_cast<const uint8_t *>(&(Value)))[1U]))
                                                                                                    ^
Source/Pcap_DNSProxy/Definition.h:338:55: note: in expansion of macro 'hton16_Force'
 #define ntoh16_Force                                  hton16_Force
                                                       ^~~~~~~~~~~~
Source/Pcap_DNSProxy/Configuration.cpp:218:20: note: in expansion of macro 'ntoh16_Force'
      *SingleText = ntoh16_Force(*SingleText);
                    ^~~~~~~~~~~~
Source/Pcap_DNSProxy/Definition.h:345:64: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
               (reinterpret_cast<const uint8_t *>(&(Value)))[3U]))
                                                                ^
Source/Pcap_DNSProxy/Definition.h:346:55: note: in expansion of macro 'hton32_Force'
 #define ntoh32_Force                                  hton32_Force
                                                       ^~~~~~~~~~~~
Source/Pcap_DNSProxy/Configuration.cpp:267:20: note: in expansion of macro 'ntoh32_Force'
      *SingleText = ntoh32_Force(*SingleText);
                    ^~~~~~~~~~~~
Source/Pcap_DNSProxy/Configuration.cpp: In function 'bool ReadParameter(bool)':
Source/Pcap_DNSProxy/Definition.h:381:136: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                                                                                                        ^
Source/Pcap_DNSProxy/Definition.h:382:94: note: in definition of macro 'usleep'
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                              ^~~~~~~~~~~
Source/Pcap_DNSProxy/Configuration.cpp:753:3: note: in expansion of macro 'Sleep'
   Sleep(Parameter.FileRefreshTime);
   ^~~~~
Source/Pcap_DNSProxy/Definition.h:382:105: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                                         ^
Source/Pcap_DNSProxy/Definition.h:381:57: note: in expansion of macro 'usleep'
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                         ^~~~~~
Source/Pcap_DNSProxy/Configuration.cpp:753:3: note: in expansion of macro 'Sleep'
   Sleep(Parameter.FileRefreshTime);
   ^~~~~
Source/Pcap_DNSProxy/Configuration.cpp: In function 'void ReadIPFilter()':
Source/Pcap_DNSProxy/Definition.h:381:136: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                                                                                                        ^
Source/Pcap_DNSProxy/Definition.h:382:94: note: in definition of macro 'usleep'
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                              ^~~~~~~~~~~
Source/Pcap_DNSProxy/Configuration.cpp:849:4: note: in expansion of macro 'Sleep'
    Sleep(Parameter.FileRefreshTime);
    ^~~~~
Source/Pcap_DNSProxy/Definition.h:382:105: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                                         ^
Source/Pcap_DNSProxy/Definition.h:381:57: note: in expansion of macro 'usleep'
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                         ^~~~~~
Source/Pcap_DNSProxy/Configuration.cpp:849:4: note: in expansion of macro 'Sleep'
    Sleep(Parameter.FileRefreshTime);
    ^~~~~
Source/Pcap_DNSProxy/Definition.h:381:136: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                                                                                                        ^
Source/Pcap_DNSProxy/Definition.h:382:94: note: in definition of macro 'usleep'
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                              ^~~~~~~~~~~
Source/Pcap_DNSProxy/Configuration.cpp:866:3: note: in expansion of macro 'Sleep'
   Sleep(Parameter.FileRefreshTime);
   ^~~~~
Source/Pcap_DNSProxy/Definition.h:382:105: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                                         ^
Source/Pcap_DNSProxy/Definition.h:381:57: note: in expansion of macro 'usleep'
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                         ^~~~~~
Source/Pcap_DNSProxy/Configuration.cpp:866:3: note: in expansion of macro 'Sleep'
   Sleep(Parameter.FileRefreshTime);
   ^~~~~
Source/Pcap_DNSProxy/Configuration.cpp: In function 'void ReadHosts()':
Source/Pcap_DNSProxy/Definition.h:381:136: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                                                                                                        ^
Source/Pcap_DNSProxy/Definition.h:382:94: note: in definition of macro 'usleep'
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                              ^~~~~~~~~~~
Source/Pcap_DNSProxy/Configuration.cpp:962:4: note: in expansion of macro 'Sleep'
    Sleep(Parameter.FileRefreshTime);
    ^~~~~
Source/Pcap_DNSProxy/Definition.h:382:105: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                                         ^
Source/Pcap_DNSProxy/Definition.h:381:57: note: in expansion of macro 'usleep'
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                         ^~~~~~
Source/Pcap_DNSProxy/Configuration.cpp:962:4: note: in expansion of macro 'Sleep'
    Sleep(Parameter.FileRefreshTime);
    ^~~~~
Source/Pcap_DNSProxy/Definition.h:381:136: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                                                                                                        ^
Source/Pcap_DNSProxy/Definition.h:382:94: note: in definition of macro 'usleep'
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                              ^~~~~~~~~~~
Source/Pcap_DNSProxy/Configuration.cpp:979:3: note: in expansion of macro 'Sleep'
   Sleep(Parameter.FileRefreshTime);
   ^~~~~
Source/Pcap_DNSProxy/Definition.h:382:105: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  #define usleep(Millisecond)                            usleep(static_cast<const useconds_t>(Millisecond))
                                                                                                         ^
Source/Pcap_DNSProxy/Definition.h:381:57: note: in expansion of macro 'usleep'
  #define Sleep(Millisecond)                             usleep(static_cast<const useconds_t>((Millisecond) * MICROSECOND_TO_MILLISECOND))
                                                         ^~~~~~
Source/Pcap_DNSProxy/Configuration.cpp:979:3: note: in expansion of macro 'Sleep'
   Sleep(Parameter.FileRefreshTime);
   ^~~~~
Source/Pcap_DNSProxy/Configuration.cpp: In function 'bool ReadSupport_FileAttributesLoop(READ_TEXT_TYPE, size_t, FILE_DATA&, bool&)':
Source/Pcap_DNSProxy/Configuration.cpp:1038:75: warning: type qualifiers ignored on cast result type [-Wignored-qualifiers]
  if (FileStatData.st_size >= static_cast<const off_t>(FILE_READING_MAXSIZE))
                                                                           ^
ninja: build stopped: subcommand failed.
make[3]: *** [Makefile:153: /openwrt/build_dir/target-x86_64_musl/pcap-dnsproxy-0.4.9.13-2019-05-05-bc9f540d/.built] Error 1
```
