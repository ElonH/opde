---
title: "compile.37"
date: 2021-06-20 22:39:07.423209
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
make package/feeds/packages/gnutls/compile -j$(nproc) || make package/feeds/packages/gnutls/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-m4.patch using plaintext: 
patching file m4/stdint.m4
patching file m4/vasnprintf.m4
patching file m4/wchar_t.m4
patching file m4/wint_t.m4
patching file src/gl/m4/gnulib-comp.m4
autopoint: using AM_GNU_GETTEXT_REQUIRE_VERSION instead of AM_GNU_GETTEXT_VERSION
Copying file build-aux/config.rpath
Copying file m4/gettext.m4
Copying file m4/intlmacosx.m4
Copying file m4/nls.m4
Copying file m4/po.m4
Copying file m4/progtest.m4
Copying file po/Makefile.in.in
Copying file po/Makevars.template
autoreconf: Entering directory `.'
autoreconf: running: true --force
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . -I lib --force -I m4 -I src/libopts/m4 -I src/gl/m4 -I lib/unistring/m4 --install
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
aclocal.real: installing '/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal/wint_t.m4' from '/openwrt/staging_dir/target-mips_24kc_musl/../host/share/aclocal/wint_t.m4'
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
autoreconf: configure.ac: tracing
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build-aux'.
OpenWrt-libtoolize: linking file `build-aux/config.guess'
OpenWrt-libtoolize: linking file `build-aux/config.sub'
OpenWrt-libtoolize: linking file `build-aux/install-sh'
OpenWrt-libtoolize: linking file `build-aux/ltmain.sh'
OpenWrt-libtoolize: putting macros in `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
OpenWrt-libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.ac and
OpenWrt-libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --include=lib --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --include=lib --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
aminclude_static.am:52: warning: if $(CODE_COVERAGE_BRANCH_COVERAGE: non-POSIX variable name
aminclude_static.am:52: (probably a GNU make extension)
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:59: warning: if $(CODE_COVERAGE_BRANCH_COVERAGE: non-POSIX variable name
aminclude_static.am:59: (probably a GNU make extension)
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:64: warning: code_coverage_v_lcov_cap_$(V: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:65: warning: code_coverage_v_lcov_cap_$(AM_DEFAULT_VERBOSITY: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:67: warning: code_coverage_v_lcov_ign_$(V: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:68: warning: code_coverage_v_lcov_ign_$(AM_DEFAULT_VERBOSITY: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:70: warning: code_coverage_v_genhtml_$(V: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:71: warning: code_coverage_v_genhtml_$(AM_DEFAULT_VERBOSITY: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:73: warning: code_coverage_quiet_$(V: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:74: warning: code_coverage_quiet_$(AM_DEFAULT_VERBOSITY: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:78: warning: subst -,_,$(subst .,_,$(1: non-POSIX variable name
aminclude_static.am:78: (probably a GNU make extension)
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:87: warning: addprefix --directory ,$(CODE_COVERAGE_DIRECTORY: non-POSIX variable name
aminclude_static.am:87: (probably a GNU make extension)
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:87: warning: call code_coverage_sanitize,$(PACKAGE_NAME: non-POSIX variable name
aminclude_static.am:87: (probably a GNU make extension)
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:88: warning: addprefix --directory ,$(CODE_COVERAGE_DIRECTORY: non-POSIX variable name
aminclude_static.am:88: (probably a GNU make extension)
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:90: warning: addprefix --prefix ,$(CODE_COVERAGE_DIRECTORY: non-POSIX variable name
aminclude_static.am:90: (probably a GNU make extension)
Makefile.am:176:   'aminclude_static.am' included from here
guile/Makefile.am:68: warning: AM_V_GUILEC_$(V: non-POSIX recursive variable expansion
guile/Makefile.am:69: warning: AM_V_GUILEC_$(AM_DEFAULT_VERBOSITY: non-POSIX recursive variable expansion
guile/Makefile.am:83: warning: '%'-style pattern rules are a GNU make extension
guile/src/Makefile.am:117: warning: '%'-style pattern rules are a GNU make extension
autoreconf: Leaving directory `.'
autoreconf: Entering directory `.'
autoreconf: running: true --force
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . -I lib --force -I m4 -I src/libopts/m4 -I src/gl/m4 -I lib/unistring/m4 --install
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
autoreconf: configure.ac: tracing
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build-aux'.
OpenWrt-libtoolize: linking file `build-aux/config.guess'
OpenWrt-libtoolize: linking file `build-aux/config.sub'
OpenWrt-libtoolize: linking file `build-aux/install-sh'
OpenWrt-libtoolize: linking file `build-aux/ltmain.sh'
OpenWrt-libtoolize: putting macros in `m4'.
OpenWrt-libtoolize: linking file `m4/libtool.m4'
OpenWrt-libtoolize: linking file `m4/ltoptions.m4'
OpenWrt-libtoolize: linking file `m4/ltsugar.m4'
OpenWrt-libtoolize: linking file `m4/ltversion.m4'
OpenWrt-libtoolize: linking file `m4/lt~obsolete.m4'
OpenWrt-libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.ac and
OpenWrt-libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --include=lib --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --include=lib --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:467: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
m4/gnulib-comp.m4:172: gl_INIT is expanded from...
configure.ac:467: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:33: gl_PREREQ_PRINTF_ARGS is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
m4/vasnprintf.m4:40: gl_PREREQ_PRINTF_PARSE is expanded from...
m4/vasnprintf.m4:15: gl_REPLACE_VASNPRINTF is expanded from...
m4/vasnprintf.m4:7: gl_FUNC_VASNPRINTF is expanded from...
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
configure.ac:468: warning: gt_TYPE_WCHAR_T is m4_require'd but not m4_defun'd
src/gl/m4/gnulib-comp.m4:411: ggl_INIT is expanded from...
configure.ac:468: the top level
aminclude_static.am:52: warning: if $(CODE_COVERAGE_BRANCH_COVERAGE: non-POSIX variable name
aminclude_static.am:52: (probably a GNU make extension)
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:59: warning: if $(CODE_COVERAGE_BRANCH_COVERAGE: non-POSIX variable name
aminclude_static.am:59: (probably a GNU make extension)
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:64: warning: code_coverage_v_lcov_cap_$(V: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:65: warning: code_coverage_v_lcov_cap_$(AM_DEFAULT_VERBOSITY: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:67: warning: code_coverage_v_lcov_ign_$(V: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:68: warning: code_coverage_v_lcov_ign_$(AM_DEFAULT_VERBOSITY: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:70: warning: code_coverage_v_genhtml_$(V: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:71: warning: code_coverage_v_genhtml_$(AM_DEFAULT_VERBOSITY: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:73: warning: code_coverage_quiet_$(V: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:74: warning: code_coverage_quiet_$(AM_DEFAULT_VERBOSITY: non-POSIX recursive variable expansion
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:78: warning: subst -,_,$(subst .,_,$(1: non-POSIX variable name
aminclude_static.am:78: (probably a GNU make extension)
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:87: warning: addprefix --directory ,$(CODE_COVERAGE_DIRECTORY: non-POSIX variable name
aminclude_static.am:87: (probably a GNU make extension)
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:87: warning: call code_coverage_sanitize,$(PACKAGE_NAME: non-POSIX variable name
aminclude_static.am:87: (probably a GNU make extension)
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:88: warning: addprefix --directory ,$(CODE_COVERAGE_DIRECTORY: non-POSIX variable name
aminclude_static.am:88: (probably a GNU make extension)
Makefile.am:176:   'aminclude_static.am' included from here
aminclude_static.am:90: warning: addprefix --prefix ,$(CODE_COVERAGE_DIRECTORY: non-POSIX variable name
aminclude_static.am:90: (probably a GNU make extension)
Makefile.am:176:   'aminclude_static.am' included from here
guile/Makefile.am:68: warning: AM_V_GUILEC_$(V: non-POSIX recursive variable expansion
guile/Makefile.am:69: warning: AM_V_GUILEC_$(AM_DEFAULT_VERBOSITY: non-POSIX recursive variable expansion
guile/Makefile.am:83: warning: '%'-style pattern rules are a GNU make extension
guile/src/Makefile.am:117: warning: '%'-style pattern rules are a GNU make extension
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/mips
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
***
*** Checking for compilation programs...

checking pkg-config is at least version 0.9.0... yes
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to enable C11 features... none needed
checking whether the compiler is clang... no
checking for compiler option needed when checking for declarations... none
checking for style of include used by make... GNU
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
checking for wchar.h... yes
checking for minix/config.h... no
checking for sys/socket.h... yes
checking for arpa/inet.h... yes
checking for features.h... yes
checking for unistd.h... (cached) yes
checking for sys/stat.h... (cached) yes
checking for sys/time.h... yes
checking for netdb.h... yes
checking for netinet/in.h... yes
checking for limits.h... yes
checking for inttypes.h... (cached) yes
checking for sys/types.h... (cached) yes
checking for stdint.h... (cached) yes
checking for sys/mman.h... yes
checking for sys/param.h... yes
checking for strings.h... (cached) yes
checking for sys/uio.h... yes
checking for threads.h... yes
checking for crtdefs.h... no
checking for stdio_ext.h... yes
checking for termios.h... yes
checking for sys/select.h... yes
checking for langinfo.h... yes
checking for xlocale.h... no
checking for semaphore.h... yes
checking for pthread.h... yes
checking for sys/cdefs.h... yes
checking for sys/wait.h... yes
checking for sys/ioctl.h... yes
checking whether it is safe to define __EXTENSIONS__... yes
checking whether _XOPEN_SOURCE should be defined... no
checking for Minix Amsterdam compiler... no
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking the archiver (mips-openwrt-linux-musl-gcc-ar) interface... ar
checking for mips-openwrt-linux-ar... (cached) mips-openwrt-linux-musl-gcc-ar
checking for _LARGEFILE_SOURCE value needed for large files... no
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking dependency style of ccache_cc... gcc3
checking for mips-openwrt-linux-ar... (cached) mips-openwrt-linux-musl-gcc-ar
checking the archiver (mips-openwrt-linux-musl-gcc-ar) interface... (cached) ar
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking for ccache_cxx option to enable C++11 features... none needed
checking dependency style of ccache_cxx... gcc3
checking for bison... bison -y
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking whether to build with code coverage support... no
checking whether to enable maintainer-specific portions of Makefiles... yes
checking for inline... inline
checking for ANSI C header files... (cached) yes
checking for __get_cpuid_count... no
checking for struct iovec.iov_base... yes
checking netinet/tcp.h usability... yes
checking netinet/tcp.h presence... yes
checking for netinet/tcp.h... yes
checking stdatomic.h usability... yes
checking stdatomic.h presence... yes
checking for stdatomic.h... yes
checking for library containing __atomic_load_4... -latomic
checking for threads.h... (cached) yes
checking valgrind/memcheck.h usability... no
checking valgrind/memcheck.h presence... no
checking for valgrind/memcheck.h... no
checking for getrandom... yes
checking for KERN_ARND... no
checking for getentropy... no
checking for NETTLE... yes
checking for HOGWEED... yes
checking for __gmpz_cmp in -lgmp... yes
checking whether to use the included minitasn1... yes
checking whether C99 macros are supported... yes
checking whether to disable strict DER time encodings for backwards compatibility... no
checking whether to allow SHA1 as an acceptable hash for cert digital signatures... yes
checking whether to disable the SSL 3.0 protocol... yes
checking whether to disable the SSL 2.0 client hello... yes
checking whether to disable DTLS-SRTP extension... no
checking whether to disable ALPN extension... no
checking whether to enable TLS heartbeat support... yes
checking whether to disable SRP authentication support... yes
checking whether to disable PSK authentication support... no
checking whether to disable anonymous authentication support... no
checking whether to disable DHE support... no
checking whether to disable ECDHE support... no
checking whether to disable GOST support... no
checking whether to add cryptodev support... yes
checking whether to add AF_ALG support... no
checking whether to disable OCSP support... no
checking size of void *... (cached) 4
checking size of long long... (cached) 8
checking size of long... (cached) 4
checking size of int... (cached) 4
checking for library containing setsockopt... none needed
checking whether to build OpenSSL compatibility layer... no
checking for gtk-doc... no
configure: WARNING:
  You will not be able to create source packages with 'make dist'
  because gtk-doc >= 1.14 is not found.
checking for gtkdoc-check... no
checking for gtkdoc-check... no
checking for gtkdoc-rebase... no
checking for gtkdoc-mkpdf... no
checking whether to build gtk-doc documentation... no
checking for GTKDOC_DEPS... yes
checking whether NLS is requested... no
checking for msgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for gmsgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for xgettext... /openwrt/staging_dir/hostpkg/bin/xgettext
checking for msgmerge... /openwrt/staging_dir/hostpkg/bin/msgmerge
checking for ld... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for shared library run path origin... done
checking 32-bit host C ABI... yes
checking for ELF binary format... yes
checking for the common suffixes of directories in the library search path... lib,lib32,lib
checking for CFPreferencesCopyAppValue... no
checking for CFLocaleCopyPreferredLanguages... no
checking whether to use NLS... no
checking whether byte ordering is bigendian... (cached) yes
checking for fork... yes
checking for setitimer... yes
checking for getrusage... yes
checking for getpwuid_r... (cached) yes
checking for nanosleep... yes
checking for daemon... yes
checking for getpid... yes
checking for localtime... yes
checking for mmap... yes
checking for clock_gettime... yes
checking for fmemopen... yes
checking for __register_atfork... no
checking for secure_getenv... yes
checking for getauxval... yes
checking for libseccomp... no
checking for libcrypto... no
checking for librt... no
checking for pthread_mutex_lock... yes
checking for size_t... yes
checking for working alloca.h... yes
checking for alloca... yes
checking whether the preprocessor supports include_next... yes
checking whether source code line length is unlimited... yes
checking for _set_invalid_parameter_handler... no
checking for explicit_bzero... yes
checking for memset_s... no
checking for fcntl... yes
checking for symlink... yes
checking for getdelim... yes
checking for getdtablesize... yes
checking for gettimeofday... (cached) yes
checking for mprotect... yes
checking for lstat... (cached) yes
checking for secure_getenv... (cached) yes
checking for getuid... yes
checking for geteuid... yes
checking for getgid... yes
checking for getegid... yes
checking for snprintf... yes
checking for strndup... yes
checking for localtime_r... yes
checking for vasnprintf... no
checking for getpass... yes
checking for __fsetlocking... yes
checking for getprogname... no
checking for getexecname... no
checking for setenv... yes
checking for strerror_r... yes
checking for __xpg_strerror_r... yes
checking for timegm... yes
checking for ftruncate... yes
checking for isblank... yes
checking for newlocale... yes
checking for uselocale... yes
checking for duplocale... yes
checking for freelocale... yes
checking for pipe... yes
checking for pthread_sigmask... yes
checking for sigaction... yes
checking for sigaltstack... yes
checking for siginterrupt... yes
checking for sleep... yes
checking for catgets... yes
checking for shutdown... yes
checking for usleep... yes
checking for mquery... no
checking for pstat_getprocvm... no
checking for complete errno.h... yes
checking for working fcntl.h... cross-compiling
checking for pid_t... yes
checking for mode_t... yes
checking whether stat file-mode macros are broken... no
checking for C/C++ restrict keyword... __restrict__
checking for nlink_t... yes
checking whether stdin defaults to large file offsets... yes
checking whether ftello is declared... yes
checking whether ungetc works on arbitrary bytes... guessing yes
checking for ftello... yes
checking whether ftello works... guessing yes
checking whether getdelim is declared... yes
checking whether getdtablesize is declared... yes
checking whether getline is declared... yes
checking for struct timeval... yes
checking for wide-enough struct timeval.tv_sec member... yes
checking whether <sys/socket.h> is self-contained... yes
checking for shutdown... (cached) yes
checking whether <sys/socket.h> defines the SHUT_* macros... yes
checking for struct sockaddr_storage... yes
checking for sa_family_t... yes
checking for struct sockaddr_storage.ss_family... yes
checking for IPv4 sockets... yes
checking for IPv6 sockets... yes
checking whether limits.h has LLONG_MAX, WORD_BIT, ULLONG_WIDTH etc.... no
checking for wint_t... yes
checking whether wint_t is large enough... yes
checking whether the compiler produces multi-arch binaries... no
checking whether stdint.h conforms to C99... guessing yes
checking whether stdint.h works without ISO C predefines... yes
checking whether stdint.h has UINTMAX_WIDTH etc.... no
checking whether malloc is ptrdiff_t safe... no
checking whether malloc, realloc, calloc set errno on failure... yes
checking whether malloc (0) returns nonnull... (cached) yes
checking for mmap... (cached) yes
checking for MAP_ANONYMOUS... yes
checking whether memchr works... guessing no
checking whether memmem is declared... yes
checking whether <limits.h> defines MIN and MAX... no
checking whether <sys/param.h> defines MIN and MAX... yes
checking for O_CLOEXEC... yes
checking for promoted mode_t type... mode_t
checking whether snprintf returns a byte count as in C99... guessing yes
checking whether snprintf is declared... yes
checking for stdbool.h that conforms to C99... yes
checking for _Bool... yes
./configure: line 25948: gt_TYPE_WCHAR_T: command not found
checking for good max_align_t... yes
./configure: line 26001: test: =: unary operator expected
checking whether NULL can be used in arbitrary expressions... yes
checking whether fcloseall is declared... no
checking which flavor of printf attribute matches inttypes macros... system
checking whether ecvt is declared... yes
checking whether fcvt is declared... yes
checking whether gcvt is declared... yes
checking whether strdup is declared... yes
checking whether strndup is declared... yes
checking whether strnlen is declared... yes
checking whether strtok_r is declared... yes
checking whether imported symbols can be declared weak... guessing yes
checking for pthread.h... (cached) yes
checking for pthread_kill in -lpthread... yes
checking whether POSIX threads API is available... yes
checking for multithread API to use... posix
checking for struct timespec in <time.h>... yes
checking for TIME_UTC in <time.h>... yes
checking whether execvpe is declared... yes
./configure: line 28215: gt_TYPE_WCHAR_T: command not found
./configure: line 28216: gt_TYPE_WCHAR_T: command not found
checking for inttypes.h... yes
checking for stdint.h... yes
checking for intmax_t... yes
./configure: line 28338: gt_TYPE_WCHAR_T: command not found
checking where to find the exponent in a 'double'... (cached) word 0 bit 20
checking whether snprintf truncates the result as in C99... guessing yes
checking for snprintf... (cached) yes
checking for strnlen... yes
checking for wcslen... yes
checking for wcsnlen... yes
checking for mbrtowc... yes
checking for wcrtomb... yes
checking whether _snprintf is declared... no
checking whether vsnprintf is declared... yes
checking whether <wchar.h> uses 'inline' correctly... yes
checking for wint_t... (cached) yes
checking whether wcsdup is declared... yes
checking for alloca as a compiler built-in... yes
checking for __builtin_expect... yes
checking byteswap.h usability... yes
checking byteswap.h presence... yes
checking for byteswap.h... yes
checking whether dup2 works... guessing yes
checking whether fcntl handles F_DUPFD correctly... guessing yes
checking whether fcntl understands F_DUPFD_CLOEXEC... guessing no
checking whether conversion from 'int' to 'long double' works... guessing yes
checking whether fopen recognizes a trailing slash... guessing yes
checking whether fopen supports the mode character 'x'... guessing yes
checking whether fopen supports the mode character 'e'... guessing yes
checking whether free is known to preserve errno... no
checking for ftello... (cached) yes
checking whether ftello works... (cached) guessing yes
checking whether __func__ is available... yes
checking for working getdelim function... guessing no
checking for flockfile... yes
checking for funlockfile... yes
checking whether getc_unlocked is declared... yes
checking whether getdtablesize works... guessing yes
checking for getline... yes
checking for working getline function... guessing no
checking for gettimeofday with POSIX signature... yes
checking for library containing inet_ntop... none required
checking whether inet_ntop is declared... yes
checking for library containing inet_pton... none required
checking whether inet_pton is declared... yes
checking for mips-openwrt-linux-objdump... mips-openwrt-linux-musl-objdump
checking if gcc/ld supports -Wl,--output-def... no
checking if LD -Wl,--version-script works... yes
checking whether the compiler supports the __inline keyword... yes
checking whether lseek detects pipes... yes
checking bp-sym.h usability... no
checking bp-sym.h presence... no
checking for bp-sym.h... no
checking for memmem... yes
checking whether memmem works... guessing yes
checking whether <netinet/in.h> is self-contained... yes
checking whether open recognizes a trailing slash... guessing yes
checking for pmccabe... false
checking for stdint.h... (cached) yes
checking for SIZE_MAX... yes
checking for snprintf... (cached) yes
checking whether snprintf respects a size of 1... guessing yes
checking whether printf supports POSIX/XSI format strings with positions... guessing yes
checking for socklen_t... yes
checking for ssize_t... yes
checking whether stat handles trailing slashes on files... guessing yes
checking for struct stat.st_atim.tv_nsec... yes
checking whether struct stat.st_atim is of type struct timespec... yes
checking for struct stat.st_birthtimespec.tv_nsec... no
checking for struct stat.st_birthtimensec... no
checking for struct stat.st_birthtim.tv_nsec... no
checking for working stdalign.h... yes
checking for stpcpy... yes
checking for strcasecmp... yes
checking for strncasecmp... yes
checking whether strncasecmp is declared... yes
checking for working strndup... guessing yes
checking for working strnlen... yes
checking for strtok_r... yes
checking whether strtok_r works... guessing no
checking for strverscmp... yes
checking whether localtime_r is declared... yes
checking whether localtime_r is compatible with its POSIX signature... yes
checking for ptrdiff_t... yes
checking for vasprintf... yes
checking for vsnprintf... (cached) yes
checking whether snprintf respects a size of 1... (cached) guessing yes
checking whether printf supports POSIX/XSI format strings with positions... (cached) guessing yes
checking for stdint.h... (cached) yes
checking if environ is properly declared... yes
checking whether strerror_r is declared... yes
checking for strerror_r... (cached) yes
checking whether strerror_r returns char *... no
checking whether fseeko is declared... yes
checking for fseeko... yes
checking for library containing gethostbyname... none required
checking for gethostbyname... yes
checking for library containing getservbyname... none required
checking for getservbyname... yes
checking whether fflush_unlocked is declared... yes
checking whether flockfile is declared... yes
checking whether fputs_unlocked is declared... yes
checking whether funlockfile is declared... yes
checking whether putc_unlocked is declared... yes
checking whether INT32_MAX < INTMAX_MAX... yes
checking whether INT64_MAX == LONG_MAX... no
checking whether UINT32_MAX < UINTMAX_MAX... yes
checking whether UINT64_MAX == ULONG_MAX... no
checking whether time_t is signed... yes
checking whether alarm is declared... yes
checking for working mktime... guessing no
checking whether struct tm is in sys/time.h or time.h... time.h
checking for struct tm.tm_zone... yes
checking for struct tm.tm_gmtoff... yes
checking for compound literals... yes
checking whether <sys/select.h> is self-contained... yes
checking whether setenv is declared... yes
checking search.h usability... yes
checking search.h presence... yes
checking for search.h... yes
checking for tsearch... yes
checking for sigset_t... yes
checking for uid_t in sys/types.h... yes
checking for volatile sig_atomic_t... yes
checking for sighandler_t... yes
checking whether strerror(0) succeeds... guessing yes
checking for strerror_r with POSIX signature... yes
checking whether strerror_r works... guessing yes
checking whether unsetenv is declared... yes
./configure: line 38381: gt_TYPE_WCHAR_T: command not found
./configure: line 38382: gt_TYPE_WCHAR_T: command not found
checking for nl_langinfo and CODESET... yes
checking whether getcwd (NULL, 0) allocates memory for result... guessing yes
checking for getcwd with POSIX signature... yes
checking for off_t... yes
checking whether langinfo.h defines CODESET... yes
checking whether langinfo.h defines T_FMT_AMPM... yes
checking whether langinfo.h defines ALTMON_1... no
checking whether langinfo.h defines ERA... yes
checking whether langinfo.h defines YESEXPR... yes
checking whether locale.h defines locale_t... yes
checking whether locale.h conforms to POSIX:2001... yes
checking whether struct lconv is properly defined... yes
checking for LC_MESSAGES... yes
checking whether uselocale works... guessing yes
checking for fake locale system (OpenBSD)... guessing no
checking for Solaris 11.4 locale system... no
checking for getlocalename_l... no
checking for library needed for semaphore functions... none
checking whether lstat correctly handles trailing slash... guessing yes
checking whether strerror_r is declared... (cached) yes
checking for pthread_t... yes
checking for pthread_spinlock_t... yes
checking for PTHREAD_CREATE_DETACHED... yes
checking for PTHREAD_MUTEX_RECURSIVE... yes
checking for PTHREAD_MUTEX_ROBUST... yes
checking for PTHREAD_PROCESS_SHARED... yes
checking for sched.h... yes
checking for struct sched_param... yes
checking whether setlocale (LC_ALL, NULL) is multithread-safe... yes
checking whether setlocale (category, NULL) is multithread-safe... yes
./configure: line 40879: gt_TYPE_WCHAR_T: command not found
checking whether <sys/ioctl.h> declares ioctl... yes
checking for alloca as a compiler built-in... (cached) yes
checking for __builtin_expect... (cached) yes
checking for byteswap.h... (cached) yes
checking for library containing clock_gettime... none required
checking for clock_gettime... (cached) yes
checking for clock_settime... yes
checking whether // is distinct from /... unknown, assuming no
checking whether dup2 works... (cached) guessing yes
checking for error_at_line... no
checking whether fcntl handles F_DUPFD correctly... (cached) guessing yes
checking whether fcntl understands F_DUPFD_CLOEXEC... (cached) guessing no
checking for flexible array member... yes
checking whether conversion from 'int' to 'long double' works... (cached) guessing yes
checking whether fopen recognizes a trailing slash... (cached) guessing yes
checking whether fopen supports the mode character 'x'... (cached) guessing yes
checking whether fopen supports the mode character 'e'... (cached) guessing yes
checking for __fpending... yes
checking whether __fpending is declared... yes
checking whether free is known to preserve errno... (cached) no
checking for fseeko... (cached) yes
checking for ftello... (cached) yes
checking whether ftello works... (cached) guessing yes
checking whether __func__ is available... (cached) yes
checking for library containing getaddrinfo... none required
checking for getaddrinfo... yes
checking whether gai_strerror is declared... yes
checking whether gai_strerrorA is declared... no
checking for gai_strerror with POSIX signature... yes
checking for struct sockaddr.sa_len... no
checking whether getaddrinfo is declared... yes
checking whether freeaddrinfo is declared... yes
checking whether getnameinfo is declared... yes
checking for struct addrinfo... yes
checking for working getdelim function... (cached) guessing no
checking for flockfile... (cached) yes
checking for funlockfile... (cached) yes
checking whether getc_unlocked is declared... (cached) yes
checking whether getdtablesize works... (cached) guessing yes
checking for getline... (cached) yes
checking for working getline function... (cached) guessing no
checking whether program_invocation_name is declared... yes
checking whether program_invocation_short_name is declared... yes
checking whether __argv is declared... no
checking for gettimeofday with POSIX signature... (cached) yes
checking for library containing gethostbyname... (cached) none required
checking for gethostbyname... (cached) yes
checking for library containing inet_ntop... (cached) none required
checking whether inet_ntop is declared... (cached) yes
checking for library containing inet_pton... (cached) none required
checking whether inet_pton is declared... (cached) yes
checking whether the compiler supports the __inline keyword... (cached) yes
checking whether lseek detects pipes... (cached) yes
checking for bp-sym.h... (cached) no
checking for memmem... (cached) yes
checking whether memmem works... (cached) guessing yes
checking for __mktime_internal... no
checking whether <netinet/in.h> is self-contained... (cached) yes
checking whether open recognizes a trailing slash... (cached) guessing yes
checking for bison... bison
checking for bison 2.4 or newer... 3.7.4, ok
checking for struct tm.tm_zone... (cached) yes
checking whether program_invocation_name is declared... (cached) yes
checking whether program_invocation_short_name is declared... (cached) yes
checking for reallocarray... no
checking whether select supports a 0 argument... guessing yes
checking whether select detects invalid fds... guessing yes
checking for library containing getservbyname... (cached) none required
checking for getservbyname... (cached) yes
checking whether setenv validates arguments... guessing yes
checking for stdint.h... (cached) yes
checking for SIZE_MAX... (cached) yes
checking for snprintf... (cached) yes
checking whether snprintf respects a size of 1... (cached) guessing yes
checking whether printf supports POSIX/XSI format strings with positions... (cached) guessing yes
checking for socklen_t... (cached) yes
checking for ssize_t... (cached) yes
checking whether stat handles trailing slashes on files... (cached) guessing yes
checking for struct stat.st_atim.tv_nsec... (cached) yes
checking whether struct stat.st_atim is of type struct timespec... (cached) yes
checking for struct stat.st_birthtimespec.tv_nsec... (cached) no
checking for struct stat.st_birthtimensec... (cached) no
checking for struct stat.st_birthtim.tv_nsec... (cached) no
checking for working stdalign.h... (cached) yes
checking for stpcpy... (cached) yes
checking for strcasecmp... (cached) yes
checking for strncasecmp... (cached) yes
checking whether strncasecmp is declared... (cached) yes
checking for working strerror function... guessing yes
checking for working strndup... (cached) guessing yes
checking for working strnlen... (cached) yes
checking for strtok_r... (cached) yes
checking whether strtok_r works... (cached) guessing no
checking for strverscmp... (cached) yes
checking whether localtime_r is declared... (cached) yes
checking whether localtime_r is compatible with its POSIX signature... (cached) yes
checking whether localtime works even near extrema... guessing yes
checking for timezone_t... no
checking for unsetenv... yes
checking for unsetenv() return type... int
checking whether unsetenv obeys POSIX... guessing yes
checking for ptrdiff_t... (cached) yes
checking for vasprintf... (cached) yes
checking for vsnprintf... (cached) yes
checking whether snprintf respects a size of 1... (cached) guessing yes
checking whether printf supports POSIX/XSI format strings with positions... (cached) guessing yes
checking for stdint.h... (cached) yes
checking for atoll... yes
checking for a traditional french locale... none
checking for a turkish Unicode locale... none
checking whether fdopen sets errno... guessing yes
checking for getpagesize... yes
checking whether getpagesize is declared... yes
checking whether byte ordering is bigendian... (cached) yes
checking whether byte ordering is bigendian... (cached) yes
checking for ioctl... yes
checking for ioctl with POSIX signature... yes
checking for pthread_rwlock_t... yes
checking whether pthread_rwlock_rdlock prefers a writer to a reader... guessing no
checking for library containing nanosleep... none required
checking for working nanosleep... guessing no (mishandles large arguments)
checking whether perror matches strerror... guessing no
checking whether pthread_create exists as a global function... yes
checking whether pthread_sigmask is a macro... no
checking whether pthread_sigmask works without -lpthread... guessing yes
checking whether pthread_sigmask returns error numbers... guessing yes
checking whether pthread_sigmask unblocks signals correctly... guessing yes
checking for putenv compatible with GNU and SVID... guessing yes
checking for raise... yes
checking for sigprocmask... yes
checking whether sched_yield is declared... yes
checking whether setlocale supports the C locale... guessing yes
checking whether setlocale (LC_ALL, NULL) is multithread-safe... (cached) yes
checking whether setlocale (category, NULL) is multithread-safe... (cached) yes
checking for a traditional french locale... (cached) none
checking for a french Unicode locale... none
checking for a traditional japanese locale... none
checking for a transitional chinese locale... none
checking for struct sigaction.sa_sigaction... yes
checking for sigprocmask... (cached) yes
checking whether sleep is declared... yes
checking for working sleep... guessing yes
checking for strtoll... yes
checking whether strtoll works... guessing no
checking whether symlink handles trailing slash correctly... guessing yes
checking for pthread_atfork... yes
checking sys/single_threaded.h usability... no
checking sys/single_threaded.h presence... no
checking for sys/single_threaded.h... no
checking for useconds_t... yes
checking whether usleep allows large arguments... guessing yes
checking whether the compiler generally respects inline... yes
checking for ssize_t... (cached) yes
checking for python... /openwrt/staging_dir/host/bin/python
checking for python version... 3.8
checking for python platform... linux
checking for python script directory... ${prefix}/lib/python3.8/site-packages
checking for python extension module directory... ${exec_prefix}/lib/python3.8/site-packages
checking for libev... yes
checking how to link with libev... -lev
checking whether C compiler handles -fno-builtin-strcmp... yes
checking whether ln -s works... yes
checking how to print strings... printf
checking for a sed that does not truncate output... (cached) /openwrt/staging_dir/host/bin/sed
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... mips-openwrt-linux-musl-gcc-nm
checking the name lister (mips-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking the maximum length of command line arguments... 3145728
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to mips-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for mips-openwrt-linux-musl-ld option to reload object files... -r
checking for mips-openwrt-linux-objdump... (cached) mips-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for mips-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for mips-openwrt-linux-ar... (cached) mips-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for mips-openwrt-linux-strip... (cached) mips-openwrt-linux-musl-strip
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking command to parse mips-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for mips-openwrt-linux-mt... no
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
checking whether the ccache_cc linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking how to run the C++ preprocessor... ccache_cxx -E
checking for ld used by ccache_cxx... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking whether the ccache_cxx linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking for ccache_cxx option to produce PIC... -fPIC -DPIC
checking if ccache_cxx PIC flag -fPIC -DPIC works... yes
checking if ccache_cxx static flag -static works... yes
checking if ccache_cxx supports -c -o file.o... yes
checking if ccache_cxx supports -c -o file.o... (cached) yes
checking whether the ccache_cxx linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking for libdl... no
checking for CMOCKA... no
checking for nettle_get_secp_192r1 in -lhogweed... yes
checking for nettle_rsa_sec_decrypt... yes
checking for nettle_gost28147_set_key... no
checking for nettle_streebog512_update... no
checking for nettle_magma_set_key... no
checking for nettle_kuznyechik_set_key... no
checking for nettle_cmac_magma_update... no
checking for nettle_cmac_kuznyechik_update... no
checking gmp soname... libgmp.so.10
checking nettle soname... libnettle.so.8
checking hogweed soname... libhogweed.so.6
checking whether to build libdane... yes
checking for unbound library... no
configure: WARNING:
***
*** libunbound was not found. Libdane will not be built.
*** 
checking for autogen... no
configure: WARNING:
***
*** autogen not found. Will not link against system libopts.
*** 
checking for dirent.h that defines DIR... yes
checking for library containing opendir... none required
checking for sys/mman.h... (cached) yes
checking for sys/param.h... (cached) yes
checking sys/poll.h usability... yes
checking sys/poll.h presence... yes
checking for sys/poll.h... yes
checking sys/procset.h usability... no
checking sys/procset.h presence... no
checking for sys/procset.h... no
checking for sys/select.h... (cached) yes
checking for sys/socket.h... (cached) yes
checking sys/stropts.h usability... yes
checking sys/stropts.h presence... yes
checking for sys/stropts.h... yes
checking for sys/time.h... (cached) yes
checking sys/un.h usability... yes
checking sys/un.h presence... yes
checking for sys/un.h... yes
checking for sys/wait.h... (cached) yes
checking for dlfcn.h... (cached) yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking libgen.h usability... yes
checking libgen.h presence... yes
checking for libgen.h... yes
checking libintl.h usability... yes
checking libintl.h presence... yes
checking for libintl.h... yes
checking for memory.h... (cached) yes
checking for netinet/in.h... (cached) yes
checking setjmp.h usability... yes
checking setjmp.h presence... yes
checking for setjmp.h... yes
checking for stdbool.h... (cached) yes
checking sysexits.h usability... yes
checking sysexits.h presence... yes
checking for sysexits.h... yes
checking for unistd.h... (cached) yes
checking utime.h usability... yes
checking utime.h presence... yes
checking for utime.h... yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking for string.h... (cached) yes
checking for limits.h... (cached) yes
checking for inttypes.h... (cached) yes
checking for working stdnoreturn.h... yes
checking for runetype.h... no
checking for wchar.h... (cached) yes
checking for wchar_t... yes
checking for wint_t... yes
checking for int8_t... yes
checking for uint8_t... yes
checking for int16_t... yes
checking for uint16_t... yes
checking for int32_t... yes
checking for uint32_t... yes
checking for intptr_t... yes
checking for uintptr_t... yes
checking for uint_t... no
checking for pid_t... (cached) yes
checking for size_t... (cached) yes
checking for ptrdiff_t... (cached) yes
checking size of char *... 4
checking size of int... (cached) 4
checking size of long... (cached) 4
checking size of short... (cached) 2
checking for pathfind in -lgen... no
checking for gettext in -lintl... no
checking for vprintf... yes
checking for _doprnt... no
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... (cached) yes
checking for vfork... yes
checking for working fork... cross
configure: WARNING: result yes guessed because of cross compilation
checking for working vfork... (cached) yes
checking for mmap... (cached) yes
checking for canonicalize_file_name... no
checking for snprintf... (cached) yes
checking for strdup... yes
checking for strchr... yes
checking for strrchr... yes
checking for strsignal... yes
checking for fchmod... (cached) yes
checking for fstat... yes
checking for chmod... yes
checking for a sed that does not truncate output... (cached) /openwrt/staging_dir/host/bin/sed
configure: Using supplied libopts tearoff
checking whether a reg expr header is specified... no
checking whether with-libregex was specified... no
checking whether with-libregex-cflags was specified... no
checking whether with-libregex-libs was specified... no
checking whether libregex functions properly... no
checking whether pathfind(3) works... no
checking whether /dev/zero is readable device... crw-rw-rw- 1 root root 1, 5 Jun 20 18:34 /dev/zero
checking whether we have a functional realpath(3C)... no
checking whether strftime() works... no
checking whether fopen accepts "b" mode... no
checking whether fopen accepts "t" mode... no
checking whether not wanting optional option args... yes
checking size of unsigned long int... 4
checking size of unsigned int... (cached) 4
checking size of time_t... 4
checking whether building Guile bindings... no
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating ldd.sh
config.status: creating src/libopts/Makefile
config.status: creating guile/pre-inst-guile
config.status: creating Makefile
config.status: creating doc/Makefile
config.status: creating doc/credentials/Makefile
config.status: creating doc/credentials/srp/Makefile
config.status: creating doc/credentials/x509/Makefile
config.status: creating doc/doxygen/Doxyfile
config.status: creating doc/examples/Makefile
config.status: creating doc/latex/Makefile
config.status: creating doc/manpages/Makefile
config.status: creating doc/reference/Makefile
config.status: creating doc/reference/version.xml
config.status: creating doc/scripts/Makefile
config.status: creating extra/Makefile
config.status: creating extra/includes/Makefile
config.status: creating libdane/Makefile
config.status: creating libdane/includes/Makefile
config.status: creating libdane/gnutls-dane.pc
config.status: creating gl/Makefile
config.status: creating guile/Makefile
config.status: creating guile/src/Makefile
config.status: creating lib/Makefile
config.status: creating lib/accelerated/Makefile
config.status: creating lib/accelerated/x86/Makefile
config.status: creating lib/accelerated/aarch64/Makefile
config.status: creating lib/algorithms/Makefile
config.status: creating lib/auth/Makefile
config.status: creating lib/ext/Makefile
config.status: creating lib/extras/Makefile
config.status: creating lib/gnutls.pc
config.status: creating lib/includes/Makefile
config.status: creating lib/includes/gnutls/gnutls.h
config.status: creating lib/minitasn1/Makefile
config.status: creating lib/nettle/Makefile
config.status: creating lib/x509/Makefile
config.status: creating lib/unistring/Makefile
config.status: creating po/Makefile.in
config.status: creating src/Makefile
config.status: creating src/args-std.def
config.status: creating src/gl/Makefile
config.status: creating src/gl/tests/Makefile
config.status: creating tests/Makefile
config.status: creating tests/windows/Makefile
config.status: creating tests/cert-tests/Makefile
config.status: creating tests/slow/Makefile
config.status: creating tests/suite/Makefile
config.status: creating fuzz/Makefile
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing po-directories commands
config.status: creating po/POTFILES
config.status: creating po/Makefile
config.status: executing libtool commands
configure: summary of build options:

  version:              3.7.2 shared 60:0:30
  Host/Target system:   mips-openwrt-linux-gnu
  Build system:         x86_64-pc-linux-gnu
  Install prefix:       /usr
  Compiler:             ccache_cc
  Valgrind:             no 
  CFlags:               -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2=gnutls-3.7.2 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro 
  Library types:        Shared=yes, Static=yes
  Local libopts:        yes
  Local libtasn1:       yes
  Local unistring:      yes
  Use nettle-mini:      no
  Documentation:        no (manpages: no)

configure: External hardware support:

  /dev/crypto:          yes
  AF_ALG support:       no
  Hardware accel:       none
  Padlock accel:        no
  Random gen. variant:  getrandom
  PKCS#11 support:      no
  TPM support:          no

configure: Optional features:
(note that included applications might not compile properly
if features are disabled)

  SSL3.0 support:       no
  SSL2.0 client hello:  no
  Allow SHA1 sign:      no
  DTLS-SRTP support:    yes
  ALPN support:         yes
  OCSP support:         yes
  SRP support:          no
  PSK support:          yes
  DHE support:          yes
  ECDHE support:        yes
  GOST support:         yes
  Anon auth support:    yes
  Heartbeat support:    yes
  IDNA support:         no
  Non-SuiteB curves:    yes
  FIPS140 mode:         no
  Strict DER time:	yes

configure: Optional libraries:

  Guile wrappers:       no
  C++ library:          yes
  DANE library:         no
  OpenSSL compat:       no

configure: System files:

  Trust store pkcs11:   
  Trust store dir:      /etc/ssl/certs/
  Trust store file:     
  Blacklist file:       
  CRL file:             
  Configuration file:   
  DNSSEC root key file: /etc/unbound/root.key

configure: WARNING:
***
*** The DNSSEC root key file in /etc/unbound/root.key was not found.
*** This file is needed for the verification of DNSSEC responses.
*** Use the command: unbound-anchor -a "/etc/unbound/root.key"
*** to generate or update it.
*** 
configure: WARNING:
*** GnuTLS will be build as a static library. That means that library
*** constructors for gnutls_global_init will not be made available to
*** linking applications. If you are building that library for arbitrary
*** applications to link, do not enable static linking.

make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2'
Making all in gl
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/gl'
  GEN      alloca.h
  GEN      arpa/inet.h
  GEN      fcntl.h
  GEN      inttypes.h
  GEN      limits.h
  GEN      netdb.h
  GEN      stdint.h
  GEN      stdio.h
  GEN      stdlib.h
  GEN      string.h
  GEN      strings.h
  GEN      sys/socket.h
  GEN      sys/stat.h
  GEN      sys/time.h
  GEN      sys/types.h
  GEN      sys/uio.h
  GEN      time.h
  GEN      unistd.h
  GEN      wchar.h
make  all-recursive
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/gl'
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/gl'
  CC       bitrotate.lo
  CC       c-ctype.lo
  CC       c-strcasecmp.lo
  CC       c-strncasecmp.lo
  CC       cloexec.lo
  CC       fd-hook.lo
  CC       hash.lo
  CC       hash-pjw-bare.lo
  CC       malloca.lo
  CC       read-file.lo
  CC       stat-time.lo
  CC       sys_socket.lo
  CC       unistd.lo
  CC       xsize.lo
  CC       asnprintf.lo
  CC       fcntl.lo
  CC       free.lo
  CC       getdelim.lo
  CC       getline.lo
  CC       malloc.lo
  CC       memchr.lo
  CC       printf-args.lo
  CC       printf-parse.lo
  CC       realloc.lo
  CC       vasnprintf.lo
  CC       glthread/threadlib.lo
  CCLD     libgnu.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/gl'
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/gl'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/gl'
Making all in lib
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib'
make  all-recursive
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib'
Making all in includes
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/includes'
make[8]: Nothing to be done for 'all'.
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/includes'
Making all in x509
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/x509'
make  all-am
make[9]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/x509'
  CC       common.lo
  CC       key_encode.lo
  CC       key_decode.lo
  CC       time.lo
  CC       crl.lo
  CC       crl_write.lo
  CC       crq.lo
  CC       dn.lo
  CC       attributes.lo
  CC       prov-seed.lo
  CC       extensions.lo
  CC       mpi.lo
  CC       output.lo
  CC       pkcs12.lo
  CC       pkcs12_bag.lo
  CC       pkcs12_encr.lo
  CC       pkcs7.lo
  CC       pkcs7-attrs.lo
  CC       pkcs7-crypt.lo
  CC       privkey.lo
  CC       privkey_pkcs8.lo
  CC       privkey_pkcs8_pbes1.lo
  CC       privkey_openssl.lo
  CC       hostname-verify.lo
  CC       sign.lo
  CC       verify.lo
  CC       x509.lo
  CC       x509_dn.lo
  CC       x509_write.lo
  CC       name_constraints.lo
  CC       verify-high.lo
  CC       verify-high2.lo
  CC       x509_ext.lo
  CC       email-verify.lo
  CC       pkcs7-output.lo
  CC       virt-san.lo
  CC       spki.lo
  CC       tls_features.lo
  CC       krb5.lo
  CC       ip.lo
  CC       ocsp.lo
  CC       ocsp_output.lo
  CCLD     libgnutls_x509.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[9]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/x509'
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/x509'
Making all in auth
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/auth'
  CC       anon.lo
  CC       cert.lo
  CC       dh_common.lo
  CC       dhe.lo
  CC       rsa_psk.lo
  CC       dhe_psk.lo
  CC       psk.lo
  CC       psk_passwd.lo
  CC       rsa.lo
  CC       srp_kx.lo
  CC       srp_passwd.lo
  CC       srp_rsa.lo
  CC       srp_sb64.lo
  CC       anon_ecdh.lo
  CC       ecdhe.lo
  CC       vko_gost.lo
  CCLD     libgnutls_auth.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/auth'
Making all in ext
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/ext'
  CC       max_record.lo
  CC       server_name.lo
  CC       signature.lo
  CC       safe_renegotiation.lo
  CC       session_ticket.lo
  CC       srp.lo
  CC       heartbeat.lo
  CC       status_request.lo
  CC       dumbfw.lo
  CC       ext_master_secret.lo
  CC       etm.lo
  CC       supported_versions.lo
  CC       post_handshake.lo
  CC       key_share.lo
  CC       cookie.lo
  CC       psk_ke_modes.lo
  CC       pre_shared_key.lo
  CC       supported_groups.lo
  CC       ec_point_formats.lo
  CC       early_data.lo
  CC       record_size_limit.lo
  CC       client_cert_type.lo
  CC       server_cert_type.lo
  CC       alpn.lo
  CC       srtp.lo
  CCLD     libgnutls_ext.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/ext'
Making all in algorithms
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/algorithms'
  CC       cert_types.lo
  CC       ciphers.lo
  CC       ciphersuites.lo
  CC       ecc.lo
ecc.c: In function '_gnutls_ecc_curve_mark_disabled':
ecc.c:358:8: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
  for(p = ecc_curves; p->name != NULL; p++) {
        ^
  CC       kx.lo
  CC       mac.lo
  CC       protocols.lo
  CC       publickey.lo
  CC       secparams.lo
  CC       sign.lo
  CC       groups.lo
  CCLD     libgnutls_alg.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/algorithms'
Making all in extras
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/extras'
  CC       randomart.lo
  CC       hex.lo
  CCLD     libgnutls_extras.la
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ar: `u' modifier ignored since `D' is the default (see `U')
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/extras'
Making all in accelerated
make[8]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/accelerated'
make[9]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/accelerated'
  CC       accelerated.lo
  CC       cryptodev.lo
cryptodev.c:34:10: fatal error: crypto/cryptodev.h: No such file or directory
 #include <crypto/cryptodev.h>
          ^~~~~~~~~~~~~~~~~~~~
compilation terminated.
make[9]: *** [Makefile:2198: cryptodev.lo] Error 1
make[9]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/accelerated'
make[8]: *** [Makefile:2218: all-recursive] Error 1
make[8]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib/accelerated'
make[7]: *** [Makefile:2790: all-recursive] Error 1
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib'
make[6]: *** [Makefile:2405: all] Error 2
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/lib'
make[5]: *** [Makefile:2225: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2'
make[4]: *** [Makefile:2150: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2'
make[3]: *** [Makefile:265: /openwrt/build_dir/target-mips_24kc_musl/gnutls-3.7.2/.built] Error 2
```
