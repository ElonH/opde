---
title: "compile.40"
date: 2021-06-22 10:45:15.513968
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
make package/feeds/packages/minidlna/compile -j$(nproc) || make package/feeds/packages/minidlna/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-dont-build-po-files.patch using plaintext: 
patching file Makefile.am
patching file configure.ac

Applying ./patches/005-added-support-RMVB.patch using plaintext: 
patching file metadata.c
patching file upnpglobalvars.h
patching file utils.c

Applying ./patches/020-wrap_container_definitions_into_a_structure.patch using plaintext: 
patching file containers.c
patching file containers.h
patching file scanner.c

Applying ./patches/030-mark_all_instances_of_magic_container_s_as_const.patch using plaintext: 
patching file containers.c
patching file containers.h
patching file scanner.c
patching file upnpsoap.c

Applying ./patches/040-heroes.patch using plaintext: 
patching file utils.c

Applying ./patches/060-reduce_duplication_in_sql_c.patch using plaintext: 
patching file sql.c

Applying ./patches/070-return-void.patch using plaintext: 
patching file upnpdescgen.c
autoreconf: Entering directory `.'
autoreconf: running: true --force
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
Makefile.am:20: warning: AM_GNU_GETTEXT used but 'po' not in SUBDIRS
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/mips
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking target system type... mips-openwrt-linux-gnu
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
checking for style of include used by make... GNU
checking for mips-openwrt-linux-gcc... ccache_cc
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
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
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
checking minix/config.h usability... no
checking minix/config.h presence... no
checking for minix/config.h... no
checking whether it is safe to define __EXTENSIONS__... yes
checking for ld... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for shared library run path origin... done
checking 32-bit host C ABI... yes
checking for ELF binary format... yes
checking for the common suffixes of directories in the library search path... lib,lib32,lib
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar terminated with signal 13 [Broken pipe]
checking for iconv... yes
checking for working iconv... guessing yes
checking how to link with libiconv... /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libiconv-stub/lib/libiconv.a
checking for iconv declaration... 
         extern size_t iconv (iconv_t cd, char * *inbuf, size_t *inbytesleft, char * *outbuf, size_t *outbytesleft);
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking whether NLS is requested... no
checking for msgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for gmsgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for xgettext... /openwrt/staging_dir/hostpkg/bin/xgettext
checking for msgmerge... /openwrt/staging_dir/hostpkg/bin/msgmerge
checking for CFPreferencesCopyAppValue... no
checking for CFLocaleCopyPreferredLanguages... no
checking whether to use NLS... no
checking for gawk... (cached) gawk
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking whether ln -s works... yes
checking whether make sets $(MAKE)... (cached) yes
checking for inline... inline
checking for mode_t... yes
checking for off_t... yes
checking for pid_t... yes
checking for size_t... yes
checking for uint8_t... yes
checking for int32_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for ssize_t... yes
checking for dirent.h that defines DIR... yes
checking for library containing opendir... none required
checking for struct dirent.d_type... yes
checking for struct stat.st_blocks... yes
checking for stdbool.h that conforms to C99... yes
checking for _Bool... yes
checking whether byte ordering is bigendian... (cached) yes
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... cross
configure: WARNING: result yes guessed because of cross compilation
checking for working vfork... (cached) yes
checking whether lstat correctly handles trailing slash... (cached) yes
checking for gethostname... yes
checking for getifaddrs... yes
checking for gettimeofday... (cached) yes
checking for inet_ntoa... yes
checking for memmove... yes
checking for memset... yes
checking for mkdir... yes
checking for realpath... yes
checking for select... yes
checking for sendfile... yes
checking for setlocale... (cached) yes
checking for socket... yes
checking for strcasecmp... yes
checking for strchr... yes
checking for strdup... yes
checking for strerror... (cached) yes
checking for strncasecmp... yes
checking for strpbrk... yes
checking for strrchr... yes
checking for strstr... yes
checking for strtol... yes
checking for strtoul... yes
checking whether SEEK_HOLE is declared... no
checking for library containing clock_gettime... none required
checking for struct ip_mreqn... yes
checking syscall.h usability... yes
checking syscall.h presence... yes
checking for syscall.h... yes
checking sys/syscall.h usability... yes
checking sys/syscall.h presence... yes
checking for sys/syscall.h... yes
checking mach/mach_time.h usability... no
checking mach/mach_time.h presence... no
checking for mach/mach_time.h... no
checking for __NR_clock_gettime syscall... yes
checking for linux/netlink.h... yes
checking libavutil/avutil.h usability... no
checking libavutil/avutil.h presence... no
checking for libavutil/avutil.h... no
checking ffmpeg/libavutil/avutil.h usability... no
checking ffmpeg/libavutil/avutil.h presence... no
checking for ffmpeg/libavutil/avutil.h... no
checking libav/libavutil/avutil.h usability... no
checking libav/libavutil/avutil.h presence... no
checking for libav/libavutil/avutil.h... no
checking avutil.h usability... no
checking avutil.h presence... no
checking for avutil.h... no
checking ffmpeg/avutil.h usability... no
checking ffmpeg/avutil.h presence... no
checking for ffmpeg/avutil.h... no
checking libav/avutil.h usability... no
checking libav/avutil.h presence... no
checking for libav/avutil.h... no
checking libavutil/avutil.h usability... no
checking libavutil/avutil.h presence... no
checking for libavutil/avutil.h... no
checking ffmpeg/libavutil/avutil.h usability... no
checking ffmpeg/libavutil/avutil.h presence... no
checking for ffmpeg/libavutil/avutil.h... no
checking libav/libavutil/avutil.h usability... no
checking libav/libavutil/avutil.h presence... no
checking for libav/libavutil/avutil.h... no
checking avutil.h usability... no
checking avutil.h presence... no
checking for avutil.h... no
checking ffmpeg/avutil.h usability... no
checking ffmpeg/avutil.h presence... no
checking for ffmpeg/avutil.h... no
checking libav/avutil.h usability... no
checking libav/avutil.h presence... no
checking for libav/avutil.h... no
configure: error: libavutil headers not found or not usable
make[3]: *** [Makefile:72: /openwrt/build_dir/target-mips_24kc_musl/minidlna-1.3.0/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
