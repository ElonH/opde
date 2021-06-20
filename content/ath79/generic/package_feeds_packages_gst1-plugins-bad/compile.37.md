---
title: "compile.37"
date: 2021-06-20 22:22:44.136301
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
make package/feeds/packages/gst1-plugins-bad/compile -j$(nproc) || make package/feeds/packages/gst1-plugins-bad/compile V=s
```

#### Compile.txt

``` bash
Makefile:425: WARNING: skipping gstreamer1-plugins-bad -- package has no install section

Applying ./patches/010-distutils.patch using plaintext: 
patching file meson.build
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-mips_24kc_musl/gst-plugins-bad-1.18.4
Build dir: /openwrt/build_dir/target-mips_24kc_musl/gst-plugins-bad-1.18.4/openwrt-build
Build type: cross build
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: gst-plugins-bad
Project version: 1.18.4
C compiler for the host machine: ccache_cc (gcc 8.4.0 "mips-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-91deb05) 8.4.0")
C linker for the host machine: ccache_cc ld.bfd 2.34
C++ compiler for the host machine: ccache_cxx (gcc 8.4.0 "mips-openwrt-linux-musl-g++ (OpenWrt GCC 8.4.0 r0-91deb05) 8.4.0")
C++ linker for the host machine: ccache_cxx ld.bfd 2.34
C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C linker for the build machine: gcc ld.bfd 2.34
C++ compiler for the build machine: ccache g++ (gcc 9.3.0 "g++ (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C++ linker for the build machine: g++ ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: mips
Host machine cpu: generic
Target machine cpu family: mips
Target machine cpu: generic
Compiler for C++ supports arguments -Wno-non-virtual-dtor: YES 
Compiler for C supports link arguments -Wl,-Bsymbolic-functions: YES 
Compiler for C supports arguments -fvisibility=hidden: YES 
Compiler for C supports arguments -fno-strict-aliasing: YES 
Compiler for C++ supports arguments -fno-strict-aliasing: YES 
Message: Disabling GLib cast checks
Message: Disabling GLib asserts
Message: Disabling GLib checks
Has header "dlfcn.h" : YES 
Has header "fcntl.h" : YES 
Has header "inttypes.h" : YES 
Has header "memory.h" : YES 
Has header "netinet/in.h" : YES 
Has header "netinet/ip.h" : YES 
Has header "netinet/tcp.h" : YES 
Has header "pthread.h" : YES 
Has header "stdint.h" : YES 
Has header "stdlib.h" : YES 
Has header "strings.h" : YES 
Has header "string.h" : YES 
Has header "sys/param.h" : YES 
Has header "sys/socket.h" : YES 
Has header "sys/stat.h" : YES 
Has header "sys/time.h" : YES 
Has header "sys/types.h" : YES 
Has header "sys/utsname.h" : YES 
Has header "unistd.h" : YES 
Has header "windows.h" : NO 
Has header "winsock2.h" : NO 
Has header "ws2tcpip.h" : NO 
Checking for function "dcgettext" : YES 
Checking for function "getpagesize" : YES 
Checking for function "gmtime_r" : YES 
Checking for function "mmap" : YES 
Checking for function "pipe2" : YES 
Checking for function "getrusage" : YES 
Checking for size of "char" : 1
Checking for size of "int" : 4
Checking for size of "long" : 4
Checking for size of "short" : 2
Checking for size of "void*" : 4
Compiler for C supports arguments -Wmissing-prototypes: YES 
Compiler for C supports arguments -Wdeclaration-after-statement: YES 
Compiler for C supports arguments -Wold-style-definition: YES 
Compiler for C++ supports arguments -Wformat-nonliteral: YES 
Compiler for C supports arguments -Wmissing-declarations: YES 
Compiler for C++ supports arguments -Wmissing-declarations: YES 
Compiler for C supports arguments -Wredundant-decls: YES 
Compiler for C++ supports arguments -Wredundant-decls: YES 
Compiler for C supports arguments -Wwrite-strings: YES 
Compiler for C++ supports arguments -Wwrite-strings: YES 
Compiler for C supports arguments -Wformat: YES 
Compiler for C++ supports arguments -Wformat: YES 
Compiler for C supports arguments -Wformat-security: YES 
Compiler for C++ supports arguments -Wformat-security: YES 
Compiler for C supports arguments -Winit-self: YES 
Compiler for C++ supports arguments -Winit-self: YES 
Compiler for C supports arguments -Wmissing-include-dirs: YES 
Compiler for C++ supports arguments -Wmissing-include-dirs: YES 
Compiler for C supports arguments -Waddress: YES 
Compiler for C++ supports arguments -Waddress: YES 
Compiler for C supports arguments -Wno-multichar: YES 
Compiler for C++ supports arguments -Wno-multichar: YES 
Compiler for C supports arguments -Wvla: YES 
Compiler for C++ supports arguments -Wvla: YES 
Compiler for C supports arguments -Wpointer-arith: YES 
Compiler for C++ supports arguments -Wpointer-arith: YES 
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Run-time dependency gstreamer-1.0 found: YES 1.18.4
Run-time dependency gstreamer-base-1.0 found: YES 1.18.4
Run-time dependency gstreamer-net-1.0 found: YES 1.18.4
Run-time dependency gstreamer-controller-1.0 found: YES 1.18.4
Run-time dependency gstreamer-pbutils-1.0 found: YES 1.18.4
Run-time dependency gstreamer-allocators-1.0 found: YES 1.18.4
Run-time dependency gstreamer-app-1.0 found: YES 1.18.4
Run-time dependency gstreamer-audio-1.0 found: YES 1.18.4
Run-time dependency gstreamer-fft-1.0 found: YES 1.18.4
Run-time dependency gstreamer-riff-1.0 found: YES 1.18.4
Run-time dependency gstreamer-rtp-1.0 found: YES 1.18.4
Run-time dependency gstreamer-rtsp-1.0 found: YES 1.18.4
Run-time dependency gstreamer-sdp-1.0 found: YES 1.18.4
Run-time dependency gstreamer-tag-1.0 found: YES 1.18.4
Run-time dependency gstreamer-video-1.0 found: YES 1.18.4
Dependency gstreamer-check-1.0 skipped: feature tests disabled
Dependency gstreamer-gl-1.0 skipped: feature gl disabled
Dependency gstreamer-gl-prototypes-1.0 skipped: feature gl disabled
Library m found: YES
Run-time dependency glib-2.0 found: YES 2.68.1
Run-time dependency gmodule-2.0 found: YES 2.68.1
Run-time dependency gio-2.0 found: YES 2.68.1
Dependency x11 skipped: feature x11 disabled
Dependency orc-0.4 skipped: feature orc disabled
Program orcc skipped: feature orc disabled
Message: Orc Compiler not found or disabled, will use backup C code
Header <gst/gstconfig.h> has symbol "GST_DISABLE_GST_DEBUG" with dependency gstreamer-1.0: YES 
Message: GStreamer debug system is disabled
Compiler for C supports arguments -Wno-unused: YES 
Compiler for C++ supports arguments -Wno-unused: YES 
Program g-ir-scanner skipped: feature introspection disabled
Program glib-mkenums found: YES (/openwrt/staging_dir/hostpkg/bin/glib-mkenums)
Program glib-mkenums found: YES (/openwrt/staging_dir/hostpkg/bin/glib-mkenums)
Program glib-mkenums found: YES (/openwrt/staging_dir/hostpkg/bin/glib-mkenums)
Program glib-mkenums found: YES (/openwrt/staging_dir/hostpkg/bin/glib-mkenums)
Dependency wayland-client skipped: feature wayland disabled
Dependency libdrm skipped: feature wayland disabled
Dependency wayland-protocols skipped: feature wayland disabled
Program wayland-scanner skipped: feature wayland disabled
Program glib-mkenums found: YES (/openwrt/staging_dir/hostpkg/bin/glib-mkenums)
Program glib-mkenums found: YES (/openwrt/staging_dir/hostpkg/bin/glib-mkenums)
Compiler for C supports arguments -Wno-unknown-pragmas: YES 
Found CMake: NO
Run-time dependency ltc found: NO (tried pkgconfig and cmake)
Run-time dependency bluez found: YES 5.56
Run-time dependency gio-unix-2.0 found: YES 2.68.1
Program gdbus-codegen found: YES (/openwrt/staging_dir/hostpkg/bin/gdbus-codegen)
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Has header "linux/fb.h" : YES 
Dependency libdrm skipped: feature kms disabled
Library ml_audio skipped: feature magicleap disabled
Library lumin_rt_core_1_5 skipped: feature magicleap disabled
Library lumin_rt_app_1_5 skipped: feature magicleap disabled
Library rt found: YES
Has header "sys/socket.h" : YES (cached)
Dependency gudev-1.0 skipped: feature uvch264 disabled
Dependency libusb-1.0 skipped: feature uvch264 disabled
Has header "linux/uvcvideo.h" : YES 
Dependency gudev-1.0 skipped: feature v4l2codecs disabled
Message: V4L2 CODECs plugin is disabled
Run-time dependency libva found: NO (tried pkgconfig and cmake)
Run-time dependency libva-drm found: NO (tried pkgconfig and cmake)
Run-time dependency gudev-1.0 found: NO (tried pkgconfig and cmake)
Run-time dependency libdrm found: NO (tried pkgconfig and cmake)
Looking for a fallback subproject for the dependency libdrm
Neither a subproject directory nor a libdrm.wrap file was found.
Subproject  libdrm is buildable: NO (disabling)
Dependency libdrm from subproject subprojects/libdrm found: NO (subproject failed to configure)
Dependency libass skipped: feature assrender disabled
Dependency aom skipped: feature aom disabled
Dependency avtp skipped: feature avtp disabled
Dependency libbs2b skipped: feature bs2b disabled
Library bz2 skipped: feature bz2 disabled
Dependency libchromaprint skipped: feature chromaprint disabled
Dependency pangocairo skipped: feature closedcaption disabled
Dependency lcms2 skipped: feature colormanagement disabled
Dependency libcurl skipped: feature curl disabled
Dependency libxml-2.0 skipped: feature dash disabled
Dependency libdc1394-2 skipped: feature dc1394 disabled
Dependency directfb skipped: feature directfb disabled
Run-time dependency openssl found: NO (tried pkgconfig)

../../../../build_dir/target-mips_24kc_musl/gst-plugins-bad-1.18.4/ext/dtls/meson.build:14:0: ERROR: Dependency "openssl" not found, tried pkgconfig

A full log can be found at /openwrt/build_dir/target-mips_24kc_musl/gst-plugins-bad-1.18.4/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:313: /openwrt/build_dir/target-mips_24kc_musl/gst-plugins-bad-1.18.4/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
