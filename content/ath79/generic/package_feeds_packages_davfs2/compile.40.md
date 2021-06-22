---
title: "compile.40"
date: 2021-06-22 10:37:31.208482
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
make package/feeds/packages/davfs2/compile -j$(nproc) || make package/feeds/packages/davfs2/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-main_code_fix.patch using plaintext: 
patching file src/webdav.c

Applying ./patches/030-realpath.patch using plaintext: 
patching file src/mount_davfs.c
patching file src/umount_davfs.c

Applying ./patches/040-sys-select.patch using plaintext: 
patching file src/dav_fuse.c

Applying ./patches/050-sys-types.patch using plaintext: 
patching file src/kernel_interface.c

Applying ./patches/060-paths.patch using plaintext: 
patching file src/mount_davfs.c

Applying ./patches/070-no-error.patch using plaintext: 
patching file configure.ac
patching file src/cache.c
patching file src/compat.h
patching file src/kernel_interface.c
patching file src/mount_davfs.c
patching file src/umount_davfs.c
patching file src/webdav.c
Copying file ABOUT-NLS
Copying file config/config.rpath
Copying file config/gettext.m4
Copying file config/host-cpu-c-abi.m4
Copying file config/iconv.m4
Copying file config/intlmacosx.m4
Copying file config/lib-ld.m4
Copying file config/lib-link.m4
Copying file config/lib-prefix.m4
Copying file config/nls.m4
Copying file config/po.m4
Copying file config/progtest.m4
Copying file po/Makefile.in.in
Copying file po/Makevars.template
Copying file po/Rules-quot
Copying file po/en@boldquot.header
Copying file po/en@quot.header
Copying file po/insert-header.sin
Copying file po/remove-potcdate.sin
autoreconf: Entering directory `.'
autoreconf: running: true --force
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I config
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
man/Makefile.am:53: warning: '%'-style pattern rules are a GNU make extension
man/de/Makefile.am:52: warning: '%'-style pattern rules are a GNU make extension
man/es/Makefile.am:53: warning: '%'-style pattern rules are a GNU make extension
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
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
checking for style of include used by make... GNU
checking dependency style of ccache_cc... gcc3
checking whether ln -s works... yes
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking whether NLS is requested... no
checking for msgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for gmsgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for xgettext... /openwrt/staging_dir/hostpkg/bin/xgettext
checking for msgmerge... /openwrt/staging_dir/hostpkg/bin/msgmerge
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking for ld... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for shared library run path origin... done
checking 32-bit host C ABI... yes
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for ELF binary format... yes
checking for the common suffixes of directories in the library search path... lib,lib32,lib
checking for CFPreferencesCopyAppValue... no
checking for CFLocaleCopyPreferredLanguages... no
checking whether to use NLS... no
checking for neon library in /openwrt/staging_dir/target-mips_24kc_musl/usr... not found
configure: error: could not find neon
make[3]: *** [Makefile:76: /openwrt/build_dir/target-mips_24kc_musl/davfs2-1.6.0/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
