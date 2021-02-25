---
title: "compile.50"
date: 2021-02-25 14:20:49.083841
hidden: false
draft: false
weight: -50
---

build number: `50`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/mc/compile -j$(nproc) || make package/feeds/packages/mc/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-subshell.patch using plaintext: 
patching file src/subshell/common.c

Applying ./patches/020-fix-mouse-handling-newer-terminfo.patch using plaintext: 
patching file lib/tty/tty.c
autopoint: *** Missing version: please specify in configure.ac through a line 'AM_GNU_GETTEXT_VERSION(x.yy.zz)' the gettext version the package is using
autopoint: *** Stop.
autoreconf: Entering directory `.'
autoreconf: running: true --force
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: adding subdirectory src/vfs/smbfs/helpers to autoreconf
autoreconf: Entering directory `src/vfs/smbfs/helpers'
autoreconf: configure.ac: not using Gettext
autoreconf: configure.ac: not using aclocal
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: configure.ac: not using Automake
autoreconf: Leaving directory `src/vfs/smbfs/helpers'
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `config'.
OpenWrt-libtoolize: linking file `config/config.guess'
OpenWrt-libtoolize: linking file `config/config.sub'
OpenWrt-libtoolize: linking file `config/install-sh'
OpenWrt-libtoolize: linking file `config/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: You should add the contents of `m4/libtool.m4' to `aclocal.m4'.
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: You should add the contents of `m4/ltoptions.m4' to `aclocal.m4'.
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: You should add the contents of `m4/ltsugar.m4' to `aclocal.m4'.
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
OpenWrt-libtoolize: You should add the contents of `m4/lt~obsolete.m4' to `aclocal.m4'.
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:13: warning: AM_INIT_AUTOMAKE: two- and three-arguments forms are deprecated.  For more info, see:
configure.ac:13: http://www.gnu.org/software/automake/manual/automake.html#Modernize-AM_005fINIT_005fAUTOMAKE-invocation
autoreconf: Leaving directory `.'
autoreconf: Entering directory `.'
autoreconf: running: true --force
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force -I m4
autoreconf: configure.ac: tracing
autoreconf: configure.ac: adding subdirectory src/vfs/smbfs/helpers to autoreconf
autoreconf: Entering directory `src/vfs/smbfs/helpers'
autoreconf: configure.ac: not using Gettext
autoreconf: configure.ac: not using aclocal
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: configure.ac: not using Automake
autoreconf: Leaving directory `src/vfs/smbfs/helpers'
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `config'.
OpenWrt-libtoolize: linking file `config/config.guess'
OpenWrt-libtoolize: linking file `config/config.sub'
OpenWrt-libtoolize: linking file `config/install-sh'
OpenWrt-libtoolize: linking file `config/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: You should add the contents of `m4/libtool.m4' to `aclocal.m4'.
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: You should add the contents of `m4/ltoptions.m4' to `aclocal.m4'.
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: You should add the contents of `m4/ltsugar.m4' to `aclocal.m4'.
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
OpenWrt-libtoolize: You should add the contents of `m4/lt~obsolete.m4' to `aclocal.m4'.
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:13: warning: AM_INIT_AUTOMAKE: two- and three-arguments forms are deprecated.  For more info, see:
configure.ac:13: http://www.gnu.org/software/automake/manual/automake.html#Modernize-AM_005fINIT_005fAUTOMAKE-invocation
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/x86_64
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
checking whether to enable maintainer-specific portions of Makefiles... no
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking for style of include used by make... GNU
checking for x86_64-openwrt-linux-gcc... ccache_cc
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
checking for ccache_cc option to accept ISO C99... none needed
checking for ccache_cc option to accept ISO Standard C... (cached) none needed
checking whether ccache_cc accepts -Wassign-enum... no
checking whether ccache_cc accepts -Wbad-function-cast... yes
checking whether ccache_cc accepts -Wcomment... yes
checking whether ccache_cc accepts -Wconditional-uninitialized... no
checking whether ccache_cc accepts -Wdeclaration-after-statement... yes
checking whether ccache_cc accepts -Wfloat-conversion... yes
checking whether ccache_cc accepts -Wfloat-equal... yes
checking whether ccache_cc accepts -Wformat... yes
checking whether ccache_cc accepts -Wformat-security... yes
checking whether ccache_cc accepts -Wformat-signedness... yes
checking whether ccache_cc accepts -Wimplicit... yes
checking whether ccache_cc accepts -Wimplicit-fallthrough... yes
checking whether ccache_cc accepts -Wignored-qualifiers... yes
checking whether ccache_cc accepts -Wlogical-not-parentheses... yes
checking whether ccache_cc accepts -Wmaybe-uninitialized... yes
checking whether ccache_cc accepts -Wmissing-braces... yes
checking whether ccache_cc accepts -Wmissing-declarations... yes
checking whether ccache_cc accepts -Wmissing-field-initializers... yes
checking whether ccache_cc accepts -Wmissing-format-attribute... yes
checking whether ccache_cc accepts -Wmissing-parameter-type... yes
checking whether ccache_cc accepts -Wmissing-prototypes... yes
checking whether ccache_cc accepts -Wmissing-variable-declarations... no
checking whether ccache_cc accepts -Wnested-externs... yes
checking whether ccache_cc accepts -Wno-long-long... yes
checking whether ccache_cc accepts -Wno-unreachable-code... yes
checking whether ccache_cc accepts -Wparentheses... yes
checking whether ccache_cc accepts -Wpointer-arith... yes
checking whether ccache_cc accepts -Wpointer-sign... yes
checking whether ccache_cc accepts -Wredundant-decls... yes
checking whether ccache_cc accepts -Wreturn-type... yes
checking whether ccache_cc accepts -Wsequence-point... yes
checking whether ccache_cc accepts -Wshadow... yes
checking whether ccache_cc accepts -Wsign-compare... yes
checking whether ccache_cc accepts -Wstrict-prototypes... yes
checking whether ccache_cc accepts -Wswitch... yes
checking whether ccache_cc accepts -Wswitch-default... yes
checking whether ccache_cc accepts -Wtype-limits... yes
checking whether ccache_cc accepts -Wundef... yes
checking whether ccache_cc accepts -Wuninitialized... yes
checking whether ccache_cc accepts -Wunreachable-code... yes
checking whether ccache_cc accepts -Wunused-but-set-variable... yes
checking whether ccache_cc accepts -Wunused-function... yes
checking whether ccache_cc accepts -Wunused-label... yes
checking whether ccache_cc accepts -Wunused-parameter... yes
checking whether ccache_cc accepts -Wunused-result... yes
checking whether ccache_cc accepts -Wunused-value... yes
checking whether ccache_cc accepts -Wunused-variable... yes
checking whether ccache_cc accepts -Wwrite-strings... yes
checking for __attribute__((fallthrough))... no
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld
checking if the linker (x86_64-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... x86_64-openwrt-linux-musl-gcc-nm
checking the name lister (x86_64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 1572864
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to x86_64-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for x86_64-openwrt-linux-musl-ld option to reload object files... -r
checking for x86_64-openwrt-linux-objdump... x86_64-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for x86_64-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for x86_64-openwrt-linux-ar... x86_64-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for x86_64-openwrt-linux-strip... (cached) x86_64-openwrt-linux-musl-strip
checking for x86_64-openwrt-linux-ranlib... x86_64-openwrt-linux-musl-gcc-ranlib
checking command to parse x86_64-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for x86_64-openwrt-linux-mt... no
checking for mt... no
checking if : is a manifest tool... no
checking for dlfcn.h... yes
checking for objdir... .libs
checking if ccache_cc supports -fno-rtti -fno-exceptions... no
checking for ccache_cc option to produce PIC... -fPIC -DPIC
checking if ccache_cc PIC flag -fPIC -DPIC works... yes
checking if ccache_cc static flag -static works... yes
checking if ccache_cc supports -c -o file.o... yes
checking if ccache_cc supports -c -o file.o... (cached) yes
checking whether the ccache_cc linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking pkg-config is at least version 0.9.0... yes
checking whether ln -s works... yes
checking for nroff... false
checking for file... true
checking for -L option to file command... yes
checking for gnome-moz-remote... no
checking for mozilla... no
checking for firefox... no
checking for konqueror... no
checking for opera... no
checking for x86_64-openwrt-linux-ar... (cached) x86_64-openwrt-linux-musl-gcc-ar
checking for sighandler_t... yes
checking for GLIB... yes
checking for GMODULE... yes
checking for library containing addwstr... (cached) no
configure: WARNING: Cannot find ncurses library, that support wide characters
checking for library containing stdscr... -lncursesw
checking for library containing has_colors... -lncurses
checking for library containing stdscr... (cached) -lncursesw
checking ncursesw/curses.h usability... yes
checking ncursesw/curses.h presence... yes
checking for ncursesw/curses.h... yes
checking for ESCDELAY variable... yes
checking for resizeterm... yes
checking for X... disabled
checking for string.h... (cached) yes
checking for memory.h... (cached) yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking malloc.h usability... yes
checking malloc.h presence... yes
checking for malloc.h... yes
checking utime.h usability... yes
checking utime.h presence... yes
checking for utime.h... yes
checking sys/statfs.h usability... yes
checking sys/statfs.h presence... yes
checking for sys/statfs.h... yes
checking sys/vfs.h usability... yes
checking sys/vfs.h presence... yes
checking for sys/vfs.h... yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking stropts.h usability... yes
checking stropts.h presence... yes
checking for stropts.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking for sys/types.h... (cached) yes
checking for sys/param.h... yes
checking for stdlib.h... (cached) yes
checking for unistd.h... (cached) yes
checking for sys/statvfs.h... yes
checking for sys/vfs.h... (cached) yes
checking for sys/fs_types.h... no
checking for OS.h... no
checking for netinet/in.h... yes
checking sys/mkdev.h usability... no
checking sys/mkdev.h presence... no
checking for sys/mkdev.h... no
checking sys/sysmacros.h usability... yes
checking sys/sysmacros.h presence... yes
checking for sys/sysmacros.h... yes
checking size of long... (cached) 8
checking for unsigned long long int... yes
checking for uintmax_t... yes
checking size of uintmax_t... 8
checking for off_t... yes
checking size of off_t... (cached) 8
checking for mode_t... yes
checking for promoted mode_t type... mode_t
checking for pid_t... yes
checking for uid_t in sys/types.h... yes
checking for struct stat.st_blocks... yes
checking for struct stat.st_blksize... yes
checking for struct stat.st_rdev... yes
checking for struct stat.st_mtim... yes
checking for sig_atomic_t in signal.h... yes, non volatile
checking for strverscmp... yes
checking for strncasecmp... yes
checking for realpath... yes
checking for posix_openpt... yes
checking for grantpt... yes
checking for statlstat... no
checking for getpagesize... yes
checking for working mmap... no
checking for get_process_stats in -lseq... no
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking for utime.h... (cached) yes
checking for listmntent... no
checking for sys/ucred.h... no
checking for sys/mount.h... yes
checking mntent.h usability... yes
checking mntent.h presence... yes
checking for mntent.h... yes
checking for sys/fs_types.h... (cached) no
checking for struct fsstat.f_fstypename... no
checking for library containing getmntent... none required
checking for getmntent... yes
checking for mntctl function and struct vmount... no
checking for one-argument getmntent function... yes
checking for setmntent... yes
checking for endmntent... yes
checking for hasmntopt... yes
checking sys/mntent.h usability... no
checking sys/mntent.h presence... no
checking for sys/mntent.h... no
checking for sys/mkdev.h... (cached) no
checking for sys/sysmacros.h... (cached) yes
checking for struct statfs.f_fstypename... no
checking for sys/mount.h... (cached) yes
checking how to get file system space usage... checking for statvfs function (SVR4)... yes
checking whether to use statvfs64... no
checking for two-argument statfs with statfs.f_frsize member... no
checking sys/fs/s5param.h usability... no
checking sys/fs/s5param.h presence... no
checking for sys/fs/s5param.h... no
checking for sys/statfs.h... (cached) yes
checking for statfs that truncates block counts... no
checking for struct statfs.f_fstypename... (cached) no
checking nfs/vfs.h usability... no
checking nfs/vfs.h presence... no
checking for nfs/vfs.h... no
checking for struct statvfs.f_basetype... no
checking for struct statvfs.f_fstypename... no
checking for struct statvfs.f_type... no
checking for struct statfs.f_namelen... yes
checking for struct statfs.f_type... yes
checking for struct statfs.f_frsize... yes
checking for setlocale... (cached) yes
checking whether NLS is requested... no
checking for msgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for gmsgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for xgettext... /openwrt/staging_dir/hostpkg/bin/xgettext
checking for msgmerge... /openwrt/staging_dir/hostpkg/bin/msgmerge
checking for ld... x86_64-openwrt-linux-musl-ld -m elf_x86_64
checking if the linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) is GNU ld... yes
checking for shared library run path origin... done
checking 32-bit host C ABI... no
checking for ELF binary format... yes
checking for the common suffixes of directories in the library search path... lib,lib,lib64
checking for CFPreferencesCopyAppValue... no
checking for CFLocaleCopyPreferredLanguages... no
checking whether to use NLS... no
checking for perl... /openwrt/staging_dir/host/bin/perl
checking for python... /openwrt/staging_dir/host/bin/python
checking for ruby... /openwrt/staging_dir/hostpkg/bin/ruby
checking for AIX defines... no
checking for utimensat... yes
checking linux/fs.h usability... yes
checking linux/fs.h presence... yes
checking for linux/fs.h... yes
checking for Gpm_Repeat in -lgpm... no
configure: WARNING: libgpm is missing or older than 0.18
configure: using internal editor
checking for subshell support... checking pty.h usability... yes
checking pty.h presence... yes
checking for pty.h... yes
checking libutil.h usability... no
checking libutil.h presence... no
checking for libutil.h... no
checking util.h usability... no
checking util.h presence... no
checking for util.h... no
checking for openpty... yes
yes
checking for EXT2FS... yes
checking for E2P... no
configure: WARNING: e2p library not found or version too old (must be >= 1.42.4)
configure: Enabling VFS code
checking for zip... /openwrt/staging_dir/host/bin/zip
checking for unzip... /openwrt/staging_dir/host/bin/unzip
checking for zipinfo code in unzip... no
checking for LIBSSH... yes
checking for library containing socket... none required
checking for library containing gethostbyname... none required
checking for struct linger.l_linger... yes
checking for nlink_t... yes
checking for socklen_t... yes
checking for pmap_set... no
checking for pmap_set in -lrpc... yes
checking for pmap_getport... yes
checking for pmap_getmaps... yes
checking for rresvport... yes
checking for rpc/pmap_clnt.h... yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating src/man2hlp/man2hlp
config.status: creating Makefile
config.status: creating contrib/Makefile
config.status: creating contrib/dist/Makefile
config.status: creating contrib/dist/gentoo/Makefile
config.status: creating contrib/dist/redhat/Makefile
config.status: creating contrib/dist/redhat/mc.spec
config.status: creating contrib/dist/pkginfo
config.status: creating contrib/dist/prototype
config.status: creating misc/Makefile
config.status: creating misc/mc.charsets
config.status: creating misc/mc.menu
config.status: creating misc/mcedit.menu
config.status: creating misc/skins/Makefile
config.status: creating misc/ext.d/Makefile
config.status: creating misc/ext.d/doc.sh
config.status: creating misc/ext.d/misc.sh
config.status: creating misc/ext.d/text.sh
config.status: creating misc/ext.d/web.sh
config.status: creating misc/macros.d/Makefile
config.status: creating misc/mc.ext
config.status: creating src/Makefile
config.status: creating src/consaver/Makefile
config.status: creating src/editor/Makefile
config.status: creating src/man2hlp/Makefile
config.status: creating src/subshell/Makefile
config.status: creating src/viewer/Makefile
config.status: creating src/diffviewer/Makefile
config.status: creating src/filemanager/Makefile
config.status: creating src/vfs/Makefile
config.status: creating src/vfs/cpio/Makefile
config.status: creating src/vfs/extfs/Makefile
config.status: creating src/vfs/extfs/helpers/Makefile
config.status: creating src/vfs/extfs/helpers/a+
config.status: creating src/vfs/extfs/helpers/apt+
config.status: creating src/vfs/extfs/helpers/audio
config.status: creating src/vfs/extfs/helpers/deb
config.status: creating src/vfs/extfs/helpers/deba
config.status: creating src/vfs/extfs/helpers/debd
config.status: creating src/vfs/extfs/helpers/dpkg+
config.status: creating src/vfs/extfs/helpers/iso9660
config.status: creating src/vfs/extfs/helpers/hp48+
config.status: creating src/vfs/extfs/helpers/lslR
config.status: creating src/vfs/extfs/helpers/mailfs
config.status: creating src/vfs/extfs/helpers/patchfs
config.status: creating src/vfs/extfs/helpers/rpms+
config.status: creating src/vfs/extfs/helpers/s3+
config.status: creating src/vfs/extfs/helpers/uace
config.status: creating src/vfs/extfs/helpers/ualz
config.status: creating src/vfs/extfs/helpers/uar
config.status: creating src/vfs/extfs/helpers/uarc
config.status: creating src/vfs/extfs/helpers/uarj
config.status: creating src/vfs/extfs/helpers/ucab
config.status: creating src/vfs/extfs/helpers/uha
config.status: creating src/vfs/extfs/helpers/ulha
config.status: creating src/vfs/extfs/helpers/ulib
config.status: creating src/vfs/extfs/helpers/urar
config.status: creating src/vfs/extfs/helpers/uzip
config.status: creating src/vfs/extfs/helpers/uzoo
config.status: creating src/vfs/fish/Makefile
config.status: creating src/vfs/fish/helpers/Makefile
config.status: creating src/vfs/ftpfs/Makefile
config.status: creating src/vfs/sftpfs/Makefile
config.status: creating src/vfs/local/Makefile
config.status: creating src/vfs/sfs/Makefile
config.status: creating src/vfs/smbfs/Makefile
config.status: creating src/vfs/tar/Makefile
config.status: creating src/vfs/undelfs/Makefile
config.status: creating lib/Makefile
config.status: creating lib/event/Makefile
config.status: creating lib/filehighlight/Makefile
config.status: creating lib/mcconfig/Makefile
config.status: creating lib/search/Makefile
config.status: creating lib/skin/Makefile
config.status: creating lib/strutil/Makefile
config.status: creating lib/tty/Makefile
config.status: creating lib/vfs/Makefile
config.status: creating lib/widget/Makefile
config.status: creating misc/syntax/Makefile
config.status: creating misc/syntax/Syntax
config.status: creating doc/Makefile
config.status: creating doc/hints/Makefile
config.status: creating doc/hints/l10n/Makefile
config.status: creating doc/man/Makefile
config.status: creating doc/man/es/Makefile
config.status: creating doc/man/hu/Makefile
config.status: creating doc/man/it/Makefile
config.status: creating doc/man/pl/Makefile
config.status: creating doc/man/ru/Makefile
config.status: creating doc/man/sr/Makefile
config.status: creating doc/hlp/Makefile
config.status: creating doc/hlp/es/Makefile
config.status: creating doc/hlp/hu/Makefile
config.status: creating doc/hlp/it/Makefile
config.status: creating doc/hlp/pl/Makefile
config.status: creating doc/hlp/ru/Makefile
config.status: creating doc/hlp/sr/Makefile
config.status: creating po/Makefile.in
config.status: creating tests/Makefile
config.status: creating tests/lib/Makefile
config.status: creating tests/lib/mcconfig/Makefile
config.status: creating tests/lib/search/Makefile
config.status: creating tests/lib/strutil/Makefile
config.status: creating tests/lib/vfs/Makefile
config.status: creating tests/lib/widget/Makefile
config.status: creating tests/src/Makefile
config.status: creating tests/src/filemanager/Makefile
config.status: creating tests/src/editor/Makefile
config.status: creating tests/src/editor/test-data.txt
config.status: creating tests/src/vfs/Makefile
config.status: creating tests/src/vfs/extfs/Makefile
config.status: creating tests/src/vfs/extfs/helpers-list/Makefile
config.status: creating tests/src/vfs/extfs/helpers-list/data/config.sh
config.status: creating tests/src/vfs/extfs/helpers-list/misc/Makefile
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
config.status: executing po-directories commands
config.status: creating po/POTFILES
config.status: creating po/Makefile
configure:

Configuration:

  Source code location:           .
  Compiler:                       ccache_cc
  Compiler flags:                  -Wbad-function-cast -Wcomment -Wdeclaration-after-statement -Wfloat-conversion -Wfloat-equal -Wformat -Wformat-security -Wformat-signedness -Wimplicit -Wimplicit-fallthrough -Wignored-qualifiers -Wlogical-not-parentheses -Wmaybe-uninitialized -Wmissing-braces -Wmissing-declarations -Wmissing-field-initializers -Wmissing-format-attribute -Wmissing-parameter-type -Wmissing-prototypes -Wnested-externs -Wno-long-long -Wno-unreachable-code -Wparentheses -Wpointer-arith -Wpointer-sign -Wredundant-decls -Wreturn-type -Wsequence-point -Wshadow -Wsign-compare -Wstrict-prototypes -Wswitch -Wswitch-default -Wtype-limits -Wundef -Wuninitialized -Wunreachable-code -Wunused-but-set-variable -Wunused-function -Wunused-label -Wunused-parameter -Wunused-result -Wunused-value -Wunused-variable -Wwrite-strings  -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/mc-4.8.25=mc-4.8.25 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include 
  Assertions:                     yes
  Unit tests:                     no
  File system:                    Midnight Commander Virtual Filesystem
                                  cpio, extfs, fish, ftp, sfs, sftp, tar
  Screen library:                 NCurses
  Mouse support:                  xterm only
  X11 events support:             no
  With subshell support:          yes
  With background operations:     no
  With ext2fs attributes support: no
  Internal editor:                yes
  Diff viewer:                    no
  Support for charset:            yes
  Search type:                    glib-regexp

make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/mc-4.8.25'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/mc-4.8.25'
Making all in po
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/mc-4.8.25/po'
*** error: gettext infrastructure mismatch: using a Makefile.in.in from gettext version 0.18 but the autoconf macros are from gettext version 0.20
make[6]: *** [Makefile:249: check-macro-version] Error 1
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/mc-4.8.25/po'
make[5]: *** [Makefile:576: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/mc-4.8.25'
make[4]: *** [Makefile:506: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/mc-4.8.25'
make[3]: *** [Makefile:131: /openwrt/build_dir/target-x86_64_musl/mc-4.8.25/.built] Error 2
```
