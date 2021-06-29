---
title: "compile.42"
date: 2021-06-29 09:35:35.006931
hidden: false
draft: false
weight: -42
---

build number: `42`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/bluez/compile -j$(nproc) || make package/feeds/packages/bluez/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-bcm43xx-Add-bcm43xx-3wire-variant.patch using plaintext: 
patching file tools/hciattach.c

Applying ./patches/002-bcm43xx-The-UART-speed-must-be-reset-after-the-firmw.patch using plaintext: 
patching file tools/hciattach_bcm43xx.c

Applying ./patches/003-Increase-firmware-load-timeout-to-30s.patch using plaintext: 
patching file tools/hciattach.c

Applying ./patches/004-Move-the-43xx-firmware-into-lib-firmware.patch using plaintext: 
patching file tools/hciattach_bcm43xx.c

Applying ./patches/201-readline.patch using plaintext: 
patching file Makefile.in

Applying ./patches/202-fix-endianness.patch using plaintext: 
patching file src/shared/util.h

Applying ./patches/203-obexd_without_systemd.patch using plaintext: 
patching file Makefile.obexd
patching file obexd/src/org.bluez.obex.service
patching file obexd/src/org.bluez.obex.service.in

Applying ./patches/205-refresh_adv_manager_for_non-LE_devices.patch using plaintext: 
patching file src/adapter.c
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/aarch64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for aarch64-openwrt-linux-strip... aarch64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking how to create a pax tar archive... gnutar
checking whether make supports nested variables... (cached) yes
checking whether to enable maintainer-specific portions of Makefiles... no
checking pkg-config is at least version 0.9.0... yes
checking whether make supports the include directive... yes (GNU style)
checking for aarch64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking dependency style of ccache_cc... gcc3
checking for C/C++ restrict keyword... __restrict
checking for aarch64-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking whether ccache_cc accepts -fPIE... no
checking build system type... x86_64-pc-linux-gnu
checking host system type... aarch64-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... aarch64-openwrt-linux-musl-ld
checking if the linker (aarch64-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... aarch64-openwrt-linux-musl-gcc-nm
checking the name lister (aarch64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 3145728
checking how to convert x86_64-pc-linux-gnu file names to aarch64-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for aarch64-openwrt-linux-musl-ld option to reload object files... -r
checking for aarch64-openwrt-linux-objdump... aarch64-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for aarch64-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for aarch64-openwrt-linux-ar... aarch64-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for aarch64-openwrt-linux-strip... (cached) aarch64-openwrt-linux-musl-strip
checking for aarch64-openwrt-linux-ranlib... aarch64-openwrt-linux-musl-gcc-ranlib
checking command to parse aarch64-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for a working dd... /usr/bin/dd
checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1
checking for aarch64-openwrt-linux-mt... no
checking for mt... no
checking if : is a manifest tool... no
checking how to run the C preprocessor... ccache_cc -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking for dlfcn.h... yes
checking for objdir... .libs
checking if ccache_cc supports -fno-rtti -fno-exceptions... no
checking for ccache_cc option to produce PIC... -fPIC -DPIC
checking if ccache_cc PIC flag -fPIC -DPIC works... yes
checking if ccache_cc static flag -static works... yes
checking if ccache_cc supports -c -o file.o... yes
checking if ccache_cc supports -c -o file.o... (cached) yes
checking whether the ccache_cc linker (aarch64-openwrt-linux-musl-ld) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking for explicit_bzero... yes
checking for rawmemchr... no
checking for signalfd... yes
checking for clock_gettime in -lrt... yes
checking for pthread_create in -lpthread... yes
checking for dlopen in -ldl... yes
checking linux/types.h usability... yes
checking linux/types.h presence... yes
checking for linux/types.h... yes
checking linux/if_alg.h usability... yes
checking linux/if_alg.h presence... yes
checking for linux/if_alg.h... yes
checking for GLIB... no
configure: error: GLib >= 2.28 is required
make[3]: *** [Makefile:158: /openwrt/build_dir/target-aarch64_cortex-a72_musl/bluez-5.56/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
