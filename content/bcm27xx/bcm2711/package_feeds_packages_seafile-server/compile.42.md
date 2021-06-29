---
title: "compile.42"
date: 2021-06-29 09:27:20.671761
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
make package/feeds/packages/seafile-server/compile -j$(nproc) || make package/feeds/packages/seafile-server/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-configure-libevent_openssl.patch using plaintext: 
patching file configure.ac

Applying ./patches/011-configure-liconv.patch using plaintext: 
patching file configure.ac

Applying ./patches/012-automake-no-python-compile.patch using plaintext: 
patching file python/seafile/Makefile.am
patching file python/seaserv/Makefile.am

Applying ./patches/020-installpath.patch using plaintext: 
patching file controller/seafile-controller.c
patching file scripts/reset-admin.sh
patching file scripts/seaf-fsck.sh
patching file scripts/seaf-fuse.sh
patching file scripts/seaf-gc.sh
patching file scripts/seafile.sh
patching file scripts/seahub.sh
patching file scripts/setup-seafile-mysql.sh
patching file scripts/setup-seafile.sh

Applying ./patches/021-bin-paths.patch using plaintext: 
patching file scripts/seaf-fsck.sh
patching file scripts/seaf-fuse.sh
patching file scripts/seaf-gc.sh
patching file scripts/seafile.sh
patching file scripts/seahub.sh
patching file scripts/setup-seafile-mysql.py
patching file scripts/setup-seafile.sh

Applying ./patches/022-uci-conf.patch using plaintext: 
patching file common/seaf-utils.c
patching file controller/seafile-controller.c
patching file python/seaserv/service.py
patching file scripts/check_init_admin.py
patching file scripts/reset-admin.sh
patching file scripts/seaf-fsck.sh
patching file scripts/seaf-fuse.sh
patching file scripts/seaf-gc.sh
patching file scripts/seafile.sh
patching file scripts/seahub.sh
patching file scripts/setup-seafile-mysql.py
patching file scripts/setup-seafile-mysql.sh
patching file scripts/setup-seafile.sh
patching file scripts/sqlite2mysql.sh
patching file scripts/upgrade/minor-upgrade.sh
patching file server/seaf-server.c

Applying ./patches/023-pgrep-patterns.patch using plaintext: 
patching file scripts/seaf-gc.sh
patching file scripts/seafile.sh
patching file scripts/seahub.sh

Applying ./patches/024-seahub-pyc.patch using plaintext: 
patching file scripts/reset-admin.sh
patching file scripts/seahub.sh
patching file scripts/setup-seafile-mysql.py
patching file scripts/setup-seafile.sh

Applying ./patches/025-command-names.patch using plaintext: 
patching file scripts/reset-admin.sh
patching file scripts/seaf-fsck.sh
patching file scripts/seaf-fuse.sh
patching file scripts/seaf-gc.sh
patching file scripts/seafile.sh
patching file scripts/seahub.sh
patching file scripts/setup-seafile-mysql.py
patching file scripts/setup-seafile.sh

Applying ./patches/030-controller-pid-dir-permissions.patch using plaintext: 
patching file controller/seafile-controller.c

Applying ./patches/031-sqlite2mysql-bash-python3.patch using plaintext: 
patching file scripts/sqlite2mysql.sh

Applying ./patches/032-seafile-no-stat.patch using plaintext: 
patching file scripts/seafile.sh

Applying ./patches/033-seahub-do-not-create-admin.patch using plaintext: 
patching file scripts/check_init_admin.py
patching file scripts/seahub.sh

Applying ./patches/034-seaf-fuse-no-fuse_opt_h.patch using plaintext: 
patching file fuse/seaf-fuse.c

Applying ./patches/040-setup-skip-dir-check.patch using plaintext: 
patching file scripts/setup-seafile-mysql.py
patching file scripts/setup-seafile.sh

Applying ./patches/041-setup-add-custom-seahub-settings.patch using plaintext: 
patching file scripts/setup-seafile-mysql.py
patching file scripts/setup-seafile.sh

Applying ./patches/042-setup-skip-user-manuals.patch using plaintext: 
patching file scripts/setup-seafile-mysql.py
patching file scripts/setup-seafile.sh

Applying ./patches/043-setup-skip-server-symlink.patch using plaintext: 
patching file scripts/setup-seafile-mysql.py
patching file scripts/setup-seafile.sh
patching file scripts/upgrade/minor-upgrade.sh

Applying ./patches/044-setup-sleep-whole-number.patch using plaintext: 
patching file scripts/setup-seafile.sh

Applying ./patches/045-setup-copy-default-avatars.patch using plaintext: 
patching file scripts/setup-seafile-mysql.py
patching file scripts/setup-seafile.sh

Applying ./patches/046-setup-show-create-admin-message.patch using plaintext: 
patching file scripts/setup-seafile-mysql.py
patching file scripts/setup-seafile.sh

Applying ./patches/050-libseafile-makefile-fixes.patch using plaintext: 
patching file lib/Makefile.am

Applying ./patches/060-timestamps-as-int64.patch using plaintext: 
patching file lib/repo.vala

Applying ./patches/110-libevhtp-linking.patch using plaintext: 
patching file configure.ac
patching file server/Makefile.am

Applying ./patches/120-recent-libevhtp.patch using plaintext: 
patching file server/access-file.c
patching file server/upload-file.c

Applying ./patches/130-newer-libevhtp.patch using plaintext: 
patching file server/upload-file.c
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: linking file `./config.guess'
OpenWrt-libtoolize: linking file `./config.sub'
OpenWrt-libtoolize: linking file `./install-sh'
OpenWrt-libtoolize: linking file `./ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:21: installing './compile'
configure.ac:10: installing './missing'
common/cdc/Makefile.am: installing './depcomp'
controller/Makefile.am:16: warning: source file '../common/log.c' is in a subdirectory,
controller/Makefile.am:16: but option 'subdir-objects' is disabled
automake: warning: possible forward-incompatibility.
automake: At least a source file is in a subdirectory, but the 'subdir-objects'
automake: automake option hasn't been enabled.  For now, the corresponding output
automake: object file(s) will be placed in the top-level directory.  However,
automake: this behaviour will change in future Automake versions: they will
automake: unconditionally cause object files to be placed in the same subdirectory
automake: of the corresponding sources.
automake: You are advised to start using 'subdir-objects' option throughout your
automake: project, to avoid future incompatibilities.
fuse/Makefile.am:19: warning: source file '../common/block-mgr.c' is in a subdirectory,
fuse/Makefile.am:19: but option 'subdir-objects' is disabled
fuse/Makefile.am:19: warning: source file '../common/block-backend.c' is in a subdirectory,
fuse/Makefile.am:19: but option 'subdir-objects' is disabled
fuse/Makefile.am:19: warning: source file '../common/block-backend-fs.c' is in a subdirectory,
fuse/Makefile.am:19: but option 'subdir-objects' is disabled
fuse/Makefile.am:19: warning: source file '../common/branch-mgr.c' is in a subdirectory,
fuse/Makefile.am:19: but option 'subdir-objects' is disabled
fuse/Makefile.am:19: warning: source file '../common/commit-mgr.c' is in a subdirectory,
fuse/Makefile.am:19: but option 'subdir-objects' is disabled
fuse/Makefile.am:19: warning: source file '../common/fs-mgr.c' is in a subdirectory,
fuse/Makefile.am:19: but option 'subdir-objects' is disabled
fuse/Makefile.am:19: warning: source file '../common/log.c' is in a subdirectory,
fuse/Makefile.am:19: but option 'subdir-objects' is disabled
fuse/Makefile.am:19: warning: source file '../common/seaf-db.c' is in a subdirectory,
fuse/Makefile.am:19: but option 'subdir-objects' is disabled
fuse/Makefile.am:19: warning: source file '../common/seaf-utils.c' is in a subdirectory,
fuse/Makefile.am:19: but option 'subdir-objects' is disabled
fuse/Makefile.am:19: warning: source file '../common/obj-store.c' is in a subdirectory,
fuse/Makefile.am:19: but option 'subdir-objects' is disabled
fuse/Makefile.am:19: warning: source file '../common/obj-backend-fs.c' is in a subdirectory,
fuse/Makefile.am:19: but option 'subdir-objects' is disabled
fuse/Makefile.am:19: warning: source file '../common/obj-backend-riak.c' is in a subdirectory,
fuse/Makefile.am:19: but option 'subdir-objects' is disabled
fuse/Makefile.am:19: warning: source file '../common/seafile-crypt.c' is in a subdirectory,
fuse/Makefile.am:19: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/seaf-db.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/branch-mgr.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/fs-mgr.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/config-mgr.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/commit-mgr.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/log.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/object-list.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/rpc-service.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/vc-common.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/seaf-utils.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/obj-store.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/obj-backend-fs.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/seafile-crypt.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/diff-simple.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/mq-mgr.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/block-mgr.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/block-backend.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/block-backend-fs.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/merge-new.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/Makefile.am:38: warning: source file '../common/block-tx-utils.c' is in a subdirectory,
server/Makefile.am:38: but option 'subdir-objects' is disabled
server/gc/Makefile.am:25: warning: source file '../../common/seaf-db.c' is in a subdirectory,
server/gc/Makefile.am:25: but option 'subdir-objects' is disabled
server/gc/Makefile.am:25: warning: source file '../../common/branch-mgr.c' is in a subdirectory,
server/gc/Makefile.am:25: but option 'subdir-objects' is disabled
server/gc/Makefile.am:25: warning: source file '../../common/fs-mgr.c' is in a subdirectory,
server/gc/Makefile.am:25: but option 'subdir-objects' is disabled
server/gc/Makefile.am:25: warning: source file '../../common/block-mgr.c' is in a subdirectory,
server/gc/Makefile.am:25: but option 'subdir-objects' is disabled
server/gc/Makefile.am:25: warning: source file '../../common/block-backend.c' is in a subdirectory,
server/gc/Makefile.am:25: but option 'subdir-objects' is disabled
server/gc/Makefile.am:25: warning: source file '../../common/block-backend-fs.c' is in a subdirectory,
server/gc/Makefile.am:25: but option 'subdir-objects' is disabled
server/gc/Makefile.am:25: warning: source file '../../common/commit-mgr.c' is in a subdirectory,
server/gc/Makefile.am:25: but option 'subdir-objects' is disabled
server/gc/Makefile.am:25: warning: source file '../../common/log.c' is in a subdirectory,
server/gc/Makefile.am:25: but option 'subdir-objects' is disabled
server/gc/Makefile.am:25: warning: source file '../../common/seaf-utils.c' is in a subdirectory,
server/gc/Makefile.am:25: but option 'subdir-objects' is disabled
server/gc/Makefile.am:25: warning: source file '../../common/obj-store.c' is in a subdirectory,
server/gc/Makefile.am:25: but option 'subdir-objects' is disabled
server/gc/Makefile.am:25: warning: source file '../../common/obj-backend-fs.c' is in a subdirectory,
server/gc/Makefile.am:25: but option 'subdir-objects' is disabled
server/gc/Makefile.am:25: warning: source file '../../common/seafile-crypt.c' is in a subdirectory,
server/gc/Makefile.am:25: but option 'subdir-objects' is disabled
server/gc/Makefile.am:25: warning: source file '../../common/config-mgr.c' is in a subdirectory,
server/gc/Makefile.am:25: but option 'subdir-objects' is disabled
tools/Makefile.am:6: warning: source file '../common/seaf-db.c' is in a subdirectory,
tools/Makefile.am:6: but option 'subdir-objects' is disabled
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/aarch64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for aarch64-openwrt-linux-strip... aarch64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking build system type... x86_64-pc-linux-gnu
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
checking for style of include used by make... GNU
checking dependency style of ccache_cc... gcc3
checking for an ANSI C-conforming const... yes
checking whether make sets $(MAKE)... (cached) yes
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
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
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
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for WIN32... no
checking for Mac... no
checking for Linux... compile in linux
checking for uuid_generate in -luuid... yes
found library uuid
checking for pthread_create in -lpthread... yes
found library pthread
checking for sqlite3_open in -lsqlite3... yes
found library sqlite3
checking for SHA1_Init in -lcrypto... yes
found library crypto
checking pkg-config is at least version 0.9.0... yes
checking for SSL... yes
checking for GLIB2... no
configure: error: Package requirements (glib-2.0 >= 2.16.0) were not met:

Package 'glib-2.0', required by 'virtual:world', not found

Consider adjusting the PKG_CONFIG_PATH environment variable if you
installed software in a non-standard prefix.

Alternatively, you may set the environment variables GLIB2_CFLAGS
and GLIB2_LIBS to avoid the need to call pkg-config.
See the pkg-config man page for more details.
make[3]: *** [Makefile:238: /openwrt/build_dir/target-aarch64_cortex-a72_musl/seafile-server-7.1.5-server/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
