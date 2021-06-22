---
title: "compile.40"
date: 2021-06-22 10:47:21.973347
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
make package/feeds/packages/snort/compile -j$(nproc) || make package/feeds/packages/snort/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-compile.patch using plaintext: 
File configure.in is read-only; trying to patch anyway
patching file configure.in

Applying ./patches/002-fix_include.patch using plaintext: 
File configure.in is read-only; trying to patch anyway
patching file configure.in

Applying ./patches/003-include-tirpc.patch using plaintext: 
patching file src/dynamic-preprocessors/appid/service_plugins/service_rpc.c
autoreconf: Entering directory `.'
autoreconf: configure.in: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force 
aclocal.real: warning: autoconf input should be named 'configure.ac', not 'configure.in'
autoreconf: configure.in: tracing
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in `.'.
OpenWrt-libtoolize: linking file `./config.guess'
OpenWrt-libtoolize: linking file `./config.sub'
OpenWrt-libtoolize: linking file `./install-sh'
OpenWrt-libtoolize: linking file `./ltmain.sh'
OpenWrt-libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.in and
OpenWrt-libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
OpenWrt-libtoolize: Consider adding `-I m4' to ACLOCAL_AMFLAGS in Makefile.am.
OpenWrt-libtoolize: `AC_PROG_RANLIB' is rendered obsolete by `LT_INIT'
aclocal.real: warning: autoconf input should be named 'configure.ac', not 'configure.in'
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
automake: warning: autoconf input should be named 'configure.ac', not 'configure.in'
configure.in:8: warning: AM_INIT_AUTOMAKE: two- and three-arguments forms are deprecated.  For more info, see:
configure.in:8: http://www.gnu.org/software/automake/manual/automake.html#Modernize-AM_005fINIT_005fAUTOMAKE-invocation
Makefile.am:5: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
automake: warning: autoconf input should be named 'configure.ac', not 'configure.in'
configure.in:1576: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
configure.in:1576: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
configure.in:1576: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
configure.in:1576: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
configure.in:1576: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/Makefile.am:97: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/control/Makefile.am:7: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/detection-plugins/Makefile.am:126: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-examples/Makefile.am:343: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-examples/dynamic-preprocessor/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-examples/dynamic-rule/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
configure.in:1576: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-output/libs/Makefile.am:3: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-output/plugins/Makefile.am:18: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-plugins/Makefile.am:28: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-plugins/sf_engine/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-plugins/sf_engine/examples/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
configure.in:1576: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/Makefile.am:14: warning: source file 'ssl_common/ssl.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:14: but option 'subdir-objects' is disabled
automake: warning: possible forward-incompatibility.
automake: At least a source file is in a subdirectory, but the 'subdir-objects'
automake: automake option hasn't been enabled.  For now, the corresponding output
automake: object file(s) will be placed in the top-level directory.  However,
automake: this behaviour will change in future Automake versions: they will
automake: unconditionally cause object files to be placed in the same subdirectory
automake: of the corresponding sources.
automake: You are advised to start using 'subdir-objects' option throughout your
automake: project, to avoid future incompatibilities.
src/dynamic-preprocessors/Makefile.am:14: warning: source file 'ssl_common/ssl_config.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:14: warning: source file 'ssl_common/ssl_inspect.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:14: warning: source file 'ssl_common/ssl_ha.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'include/sf_ip.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'include/sfrt.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'include/sfrt_dir.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'include/sfrt_flat.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'include/sfrt_flat_dir.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'include/segment_mem.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'include/mempool.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'include/sf_sdlist.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'include/util_unfold.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'include/sf_base64decode.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'include/sf_email_attach_decode.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'include/reg_test.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:20: warning: source file 'libs/sfparser.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:20: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:106: warning: source file 'include/sfmemcap.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:106: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:111: warning: source file 'include/appdata_adjuster.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:111: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:111: warning: source file 'include/sfxhash.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:111: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:111: warning: source file 'include/sfhashfcn.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:111: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:111: warning: source file 'include/sfmemcap.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:111: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:111: warning: source file 'include/sfprimetable.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:111: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:111: warning: source file 'include/reg_test.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:111: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:106: warning: source file 'include/sfprimetable.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:106: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:106: warning: source file 'include/sfxhash.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:106: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:106: warning: source file 'include/sfghash.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:106: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:106: warning: source file 'include/sfhashfcn.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:106: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:106: warning: source file 'include/sflsq.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:106: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/Makefile.am:106: warning: source file 'include/md5.c' is in a subdirectory,
src/dynamic-preprocessors/Makefile.am:106: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile_defs:3: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/commonAppMatcher.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/flow.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/fw_appid.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/hostPortAppCache.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/luaDetectorApi.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/luaDetectorFlowApi.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/luaDetectorModule.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_state.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/spp_appid.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/appId.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/appId_ss.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/appIdApi.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/appInfoTable.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/appIdStats.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/appIdConfig.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/app_forecast.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/lengthAppCache.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/thirdparty_appid_utils.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/client_plugins/client_app_base.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/client_plugins/client_app_ym.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/client_plugins/client_app_msn.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/client_plugins/client_app_aim.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/client_plugins/client_app_bit.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/client_plugins/client_app_bit_tracker.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/client_plugins/client_app_rtp.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/client_plugins/client_app_ssh.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/client_plugins/client_app_timbuktu.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/client_plugins/client_app_tns.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/client_plugins/client_app_vnc.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_base.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/dcerpc.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_mysql.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_radius.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_telnet.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_bootp.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_ntp.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_flap.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_rshell.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_netbios.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_snmp.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_battle_field.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_rexec.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_rfb.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_rpc.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_bgp.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_direct_connect.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_irc.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_ssh.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_tftp.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_ftp.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_rsync.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_rlogin.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_lpr.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_nntp.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_MDNS.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_dcerpc.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_ssl.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_bit.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_timbuktu.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_tns.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/service_plugins/service_rtmp.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/detector_plugins/detector_base.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/detector_plugins/http_url_patterns.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/detector_plugins/detector_http.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/detector_plugins/detector_imap.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/detector_plugins/detector_kerberos.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/detector_plugins/detector_pop3.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/detector_plugins/detector_smtp.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/detector_plugins/detector_sip.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/detector_plugins/detector_pattern.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/detector_plugins/detector_dns.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/detector_plugins/detector_cip.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/util/common_util.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/util/sf_multi_mpse.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/util/sf_mlmp.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/util/fw_avltree.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/util/OutputFile.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/util/NetworkSet.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/util/ip_funcs.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile_defs:10: warning: source file '$(APPID_SRC_DIR)/util/sfutil.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile_defs:10: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:4:   'src/dynamic-preprocessors/appid/Makefile_defs' included from here
src/dynamic-preprocessors/appid/Makefile.am:15: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile.am:15: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:15: warning: source file '../include/sf_ip.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile.am:15: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:15: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile.am:15: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:15: warning: source file '../include/sfxhash.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile.am:15: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:15: warning: source file '../include/sfghash.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile.am:15: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:15: warning: source file '../include/sflsq.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile.am:15: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:15: warning: source file '../include/sfhashfcn.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile.am:15: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:15: warning: source file '../include/sfmemcap.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile.am:15: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/appid/Makefile.am:15: warning: source file '../include/sfprimetable.c' is in a subdirectory,
src/dynamic-preprocessors/appid/Makefile.am:15: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dcerpc2/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/dcerpc2/Makefile.am:17: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/dcerpc2/Makefile.am:17: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dcerpc2/Makefile.am:17: warning: source file '../include/sf_ip.c' is in a subdirectory,
src/dynamic-preprocessors/dcerpc2/Makefile.am:17: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dcerpc2/Makefile.am:17: warning: source file '../include/sfrt.c' is in a subdirectory,
src/dynamic-preprocessors/dcerpc2/Makefile.am:17: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dcerpc2/Makefile.am:17: warning: source file '../include/sfrt_dir.c' is in a subdirectory,
src/dynamic-preprocessors/dcerpc2/Makefile.am:17: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dcerpc2/Makefile.am:17: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/dcerpc2/Makefile.am:17: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dcerpc2/Makefile.am:24: warning: source file '../include/appdata_adjuster.c' is in a subdirectory,
src/dynamic-preprocessors/dcerpc2/Makefile.am:24: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dcerpc2/Makefile.am:24: warning: source file '../include/sfxhash.c' is in a subdirectory,
src/dynamic-preprocessors/dcerpc2/Makefile.am:24: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dcerpc2/Makefile.am:24: warning: source file '../include/sfhashfcn.c' is in a subdirectory,
src/dynamic-preprocessors/dcerpc2/Makefile.am:24: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dcerpc2/Makefile.am:24: warning: source file '../include/sfmemcap.c' is in a subdirectory,
src/dynamic-preprocessors/dcerpc2/Makefile.am:24: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dcerpc2/Makefile.am:24: warning: source file '../include/sfprimetable.c' is in a subdirectory,
src/dynamic-preprocessors/dcerpc2/Makefile.am:24: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dcerpc2/Makefile.am:24: warning: source file '../include/reg_test.c' is in a subdirectory,
src/dynamic-preprocessors/dcerpc2/Makefile.am:24: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dnp3/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/dnp3/Makefile.am:17: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/dnp3/Makefile.am:17: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dnp3/Makefile.am:17: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/dnp3/Makefile.am:17: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dnp3/Makefile.am:17: warning: source file '../include/mempool.c' is in a subdirectory,
src/dynamic-preprocessors/dnp3/Makefile.am:17: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dnp3/Makefile.am:17: warning: source file '../include/sf_sdlist.c' is in a subdirectory,
src/dynamic-preprocessors/dnp3/Makefile.am:17: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dnp3/Makefile.am:23: warning: source file '../include/appdata_adjuster.c' is in a subdirectory,
src/dynamic-preprocessors/dnp3/Makefile.am:23: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dnp3/Makefile.am:23: warning: source file '../include/sfxhash.c' is in a subdirectory,
src/dynamic-preprocessors/dnp3/Makefile.am:23: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dnp3/Makefile.am:23: warning: source file '../include/sfhashfcn.c' is in a subdirectory,
src/dynamic-preprocessors/dnp3/Makefile.am:23: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dnp3/Makefile.am:23: warning: source file '../include/sfmemcap.c' is in a subdirectory,
src/dynamic-preprocessors/dnp3/Makefile.am:23: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dnp3/Makefile.am:23: warning: source file '../include/sfprimetable.c' is in a subdirectory,
src/dynamic-preprocessors/dnp3/Makefile.am:23: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dnp3/Makefile.am:23: warning: source file '../include/reg_test.c' is in a subdirectory,
src/dynamic-preprocessors/dnp3/Makefile.am:23: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dns/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/dns/Makefile.am:14: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/dns/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/dns/Makefile.am:14: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/dns/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/file/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/file/Makefile.am:19: warning: source file './include/output_lib.c' is in a subdirectory,
src/dynamic-preprocessors/file/Makefile.am:19: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/file/Makefile.am:19: warning: source file './include/circular_buffer.c' is in a subdirectory,
src/dynamic-preprocessors/file/Makefile.am:19: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/file/Makefile.am:14: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/file/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/file/Makefile.am:14: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/file/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ftptelnet/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: warning: source file '../include/sf_ip.c' is in a subdirectory,
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: warning: source file '../include/sfrt.c' is in a subdirectory,
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: warning: source file '../include/sfrt_dir.c' is in a subdirectory,
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: warning: source file '../include/sfmemcap.c' is in a subdirectory,
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: warning: source file '../ssl_common/ssl.c' is in a subdirectory,
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: warning: source file '../ssl_common/ssl_config.c' is in a subdirectory,
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: warning: source file '../ssl_common/ssl_inspect.c' is in a subdirectory,
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: warning: source file '../libs/sfparser.c' is in a subdirectory,
src/dynamic-preprocessors/ftptelnet/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/gtp/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/gtp/Makefile.am:14: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/gtp/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/gtp/Makefile.am:14: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/gtp/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/imap/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/imap/Makefile.am:14: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/imap/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/imap/Makefile.am:14: warning: source file '../include/mempool.c' is in a subdirectory,
src/dynamic-preprocessors/imap/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/imap/Makefile.am:14: warning: source file '../include/sf_sdlist.c' is in a subdirectory,
src/dynamic-preprocessors/imap/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/imap/Makefile.am:14: warning: source file '../include/sf_base64decode.c' is in a subdirectory,
src/dynamic-preprocessors/imap/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/imap/Makefile.am:14: warning: source file '../include/util_unfold.c' is in a subdirectory,
src/dynamic-preprocessors/imap/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/imap/Makefile.am:14: warning: source file '../include/sf_email_attach_decode.c' is in a subdirectory,
src/dynamic-preprocessors/imap/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/imap/Makefile.am:14: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/imap/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/imap/Makefile.am:14: warning: source file '../ssl_common/ssl.c' is in a subdirectory,
src/dynamic-preprocessors/imap/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/imap/Makefile.am:14: warning: source file '../ssl_common/ssl_config.c' is in a subdirectory,
src/dynamic-preprocessors/imap/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/imap/Makefile.am:14: warning: source file '../ssl_common/ssl_inspect.c' is in a subdirectory,
src/dynamic-preprocessors/imap/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/imap/Makefile.am:14: warning: source file '../libs/sfparser.c' is in a subdirectory,
src/dynamic-preprocessors/imap/Makefile.am:14: but option 'subdir-objects' is disabled
configure.in:1576: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/modbus/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/modbus/Makefile.am:14: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/modbus/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/modbus/Makefile.am:14: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/modbus/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/pop/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/pop/Makefile.am:14: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/pop/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/pop/Makefile.am:14: warning: source file '../include/mempool.c' is in a subdirectory,
src/dynamic-preprocessors/pop/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/pop/Makefile.am:14: warning: source file '../include/sf_sdlist.c' is in a subdirectory,
src/dynamic-preprocessors/pop/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/pop/Makefile.am:14: warning: source file '../include/util_unfold.c' is in a subdirectory,
src/dynamic-preprocessors/pop/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/pop/Makefile.am:14: warning: source file '../include/sf_base64decode.c' is in a subdirectory,
src/dynamic-preprocessors/pop/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/pop/Makefile.am:14: warning: source file '../include/sf_email_attach_decode.c' is in a subdirectory,
src/dynamic-preprocessors/pop/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/pop/Makefile.am:14: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/pop/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/pop/Makefile.am:14: warning: source file '../ssl_common/ssl.c' is in a subdirectory,
src/dynamic-preprocessors/pop/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/pop/Makefile.am:14: warning: source file '../ssl_common/ssl_config.c' is in a subdirectory,
src/dynamic-preprocessors/pop/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/pop/Makefile.am:14: warning: source file '../ssl_common/ssl_inspect.c' is in a subdirectory,
src/dynamic-preprocessors/pop/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/pop/Makefile.am:14: warning: source file '../libs/sfparser.c' is in a subdirectory,
src/dynamic-preprocessors/pop/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/reputation/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/reputation/Makefile.am:46: warning: source file './shmem/sflinux_helpers.c' is in a subdirectory,
src/dynamic-preprocessors/reputation/Makefile.am:46: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/reputation/Makefile.am:46: warning: source file './shmem/shmem_config.c' is in a subdirectory,
src/dynamic-preprocessors/reputation/Makefile.am:46: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/reputation/Makefile.am:46: warning: source file './shmem/shmem_datamgmt.c' is in a subdirectory,
src/dynamic-preprocessors/reputation/Makefile.am:46: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/reputation/Makefile.am:46: warning: source file './shmem/shmem_lib.c' is in a subdirectory,
src/dynamic-preprocessors/reputation/Makefile.am:46: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/reputation/Makefile.am:46: warning: source file './shmem/shmem_mgmt.c' is in a subdirectory,
src/dynamic-preprocessors/reputation/Makefile.am:46: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/reputation/Makefile.am:14: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/reputation/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/reputation/Makefile.am:14: warning: source file '../include/sf_ip.c' is in a subdirectory,
src/dynamic-preprocessors/reputation/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/reputation/Makefile.am:14: warning: source file '../include/sfrt.c' is in a subdirectory,
src/dynamic-preprocessors/reputation/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/reputation/Makefile.am:14: warning: source file '../include/sfrt_dir.c' is in a subdirectory,
src/dynamic-preprocessors/reputation/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/reputation/Makefile.am:14: warning: source file '../include/sfrt_flat.c' is in a subdirectory,
src/dynamic-preprocessors/reputation/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/reputation/Makefile.am:14: warning: source file '../include/sfrt_flat_dir.c' is in a subdirectory,
src/dynamic-preprocessors/reputation/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/reputation/Makefile.am:14: warning: source file '../include/segment_mem.c' is in a subdirectory,
src/dynamic-preprocessors/reputation/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/reputation/Makefile.am:14: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/reputation/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/s7commplus/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/s7commplus/Makefile.am:14: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/s7commplus/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/s7commplus/Makefile.am:14: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/s7commplus/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/sdf/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/sdf/Makefile.am:14: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/sdf/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/sdf/Makefile.am:14: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/sdf/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/sip/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/sip/Makefile.am:17: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/sip/Makefile.am:17: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/sip/Makefile.am:17: warning: source file '../include/sf_ip.c' is in a subdirectory,
src/dynamic-preprocessors/sip/Makefile.am:17: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/sip/Makefile.am:17: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/sip/Makefile.am:17: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/sip/Makefile.am:22: warning: source file '../include/appdata_adjuster.c' is in a subdirectory,
src/dynamic-preprocessors/sip/Makefile.am:22: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/sip/Makefile.am:22: warning: source file '../include/sfxhash.c' is in a subdirectory,
src/dynamic-preprocessors/sip/Makefile.am:22: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/sip/Makefile.am:22: warning: source file '../include/sfhashfcn.c' is in a subdirectory,
src/dynamic-preprocessors/sip/Makefile.am:22: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/sip/Makefile.am:22: warning: source file '../include/sfmemcap.c' is in a subdirectory,
src/dynamic-preprocessors/sip/Makefile.am:22: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/sip/Makefile.am:22: warning: source file '../include/sfprimetable.c' is in a subdirectory,
src/dynamic-preprocessors/sip/Makefile.am:22: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/sip/Makefile.am:22: warning: source file '../include/reg_test.c' is in a subdirectory,
src/dynamic-preprocessors/sip/Makefile.am:22: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/smtp/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/smtp/Makefile.am:14: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/smtp/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/smtp/Makefile.am:14: warning: source file '../include/mempool.c' is in a subdirectory,
src/dynamic-preprocessors/smtp/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/smtp/Makefile.am:14: warning: source file '../include/sf_sdlist.c' is in a subdirectory,
src/dynamic-preprocessors/smtp/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/smtp/Makefile.am:14: warning: source file '../include/sf_base64decode.c' is in a subdirectory,
src/dynamic-preprocessors/smtp/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/smtp/Makefile.am:14: warning: source file '../include/util_unfold.c' is in a subdirectory,
src/dynamic-preprocessors/smtp/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/smtp/Makefile.am:14: warning: source file '../include/sf_email_attach_decode.c' is in a subdirectory,
src/dynamic-preprocessors/smtp/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/smtp/Makefile.am:14: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/smtp/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/smtp/Makefile.am:14: warning: source file '../ssl_common/ssl.c' is in a subdirectory,
src/dynamic-preprocessors/smtp/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/smtp/Makefile.am:14: warning: source file '../ssl_common/ssl_ha.c' is in a subdirectory,
src/dynamic-preprocessors/smtp/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/smtp/Makefile.am:14: warning: source file '../ssl_common/ssl_config.c' is in a subdirectory,
src/dynamic-preprocessors/smtp/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/smtp/Makefile.am:14: warning: source file '../ssl_common/ssl_inspect.c' is in a subdirectory,
src/dynamic-preprocessors/smtp/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/smtp/Makefile.am:14: warning: source file '../libs/sfparser.c' is in a subdirectory,
src/dynamic-preprocessors/smtp/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ssh/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/ssh/Makefile.am:14: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/ssh/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ssh/Makefile.am:14: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/ssh/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ssl/Makefile.am:4: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/dynamic-preprocessors/ssl/Makefile.am:14: warning: source file '../include/sf_dynamic_preproc_lib.c' is in a subdirectory,
src/dynamic-preprocessors/ssl/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ssl/Makefile.am:14: warning: source file '../include/sfPolicyUserData.c' is in a subdirectory,
src/dynamic-preprocessors/ssl/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ssl/Makefile.am:14: warning: source file '../ssl_common/ssl.c' is in a subdirectory,
src/dynamic-preprocessors/ssl/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ssl/Makefile.am:14: warning: source file '../ssl_common/ssl_config.c' is in a subdirectory,
src/dynamic-preprocessors/ssl/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ssl/Makefile.am:14: warning: source file '../ssl_common/ssl_inspect.c' is in a subdirectory,
src/dynamic-preprocessors/ssl/Makefile.am:14: but option 'subdir-objects' is disabled
src/dynamic-preprocessors/ssl/Makefile.am:14: warning: source file '../libs/sfparser.c' is in a subdirectory,
src/dynamic-preprocessors/ssl/Makefile.am:14: but option 'subdir-objects' is disabled
src/file-process/Makefile.am:29: warning: whitespace following trailing backslash
src/file-process/Makefile.am:33: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/file-process/Makefile.am:5: warning: source file '../sfutil/sf_email_attach_decode.c' is in a subdirectory,
src/file-process/Makefile.am:5: but option 'subdir-objects' is disabled
src/file-process/libs/Makefile.am:13: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/output-plugins/Makefile.am:23: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/parser/Makefile.am:7: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/preprocessors/HttpInspect/Makefile.am:41: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/preprocessors/HttpInspect/anomaly_detection/Makefile.am:8: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/preprocessors/HttpInspect/client/Makefile.am:9: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/preprocessors/HttpInspect/event_output/Makefile.am:8: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/preprocessors/HttpInspect/files/Makefile.am:10: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
configure.in:1576: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/preprocessors/HttpInspect/mode_inspection/Makefile.am:8: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/preprocessors/HttpInspect/normalization/Makefile.am:8: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/preprocessors/HttpInspect/server/Makefile.am:9: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/preprocessors/HttpInspect/session_inspection/Makefile.am:8: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/preprocessors/HttpInspect/user_interface/Makefile.am:10: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/preprocessors/HttpInspect/utils/Makefile.am:20: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/preprocessors/Makefile.am:36: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/preprocessors/Session/Makefile.am:26: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/preprocessors/Stream6/Makefile.am:28: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/reload-adjust/Makefile.am:9: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/sfutil/Makefile.am:71: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/side-channel/Makefile.am:9: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
configure.in:1576: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/side-channel/plugins/Makefile.am:9: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
src/target-based/Makefile.am:5: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
configure.in:1576: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
configure.in:1576: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
tools/Makefile.am:17: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
tools/control/Makefile.am:12: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
tools/file_server/Makefile.am:9: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
tools/u2boat/Makefile.am:10: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
tools/u2openappid/Makefile.am:9: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
tools/u2spewfoo/Makefile.am:11: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
tools/u2streamer/Makefile.am:9: warning: 'INCLUDES' is the old name for 'AM_CPPFLAGS' (or '*_CPPFLAGS')
autoreconf: Leaving directory `.'
configure: WARNING: unrecognized options: --disable-nls, --enable-flexresp
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for style of include used by make... GNU
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... no
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking dependency style of ccache_cc... gcc3
checking for ccache_cc option to accept ISO C99... none needed
checking for ccache_cc option to accept ISO Standard C... (cached) none needed
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) no
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) gcc3
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... mips-openwrt-linux-musl-gcc-nm
checking the name lister (mips-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 3145728
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to mips-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for mips-openwrt-linux-musl-ld option to reload object files... -r
checking for mips-openwrt-linux-objdump... mips-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for mips-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for mips-openwrt-linux-strip... (cached) mips-openwrt-linux-musl-strip
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking command to parse mips-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for mips-openwrt-linux-mt... no
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
checking whether the ccache_cc linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking for mips-openwrt-linux-ranlib... (cached) mips-openwrt-linux-musl-gcc-ranlib
checking whether byte ordering is bigendian... (cached) yes
checking for inline... inline
checking for stdbool.h that conforms to C99... yes
checking for _Bool... yes
checking for bison... bison
checking for flex... flex
checking for inttypes.h... (cached) yes
checking math.h usability... yes
checking math.h presence... yes
checking for math.h... yes
checking paths.h usability... yes
checking paths.h presence... yes
checking for paths.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking for strings.h... (cached) yes
checking for unistd.h... (cached) yes
checking wchar.h usability... yes
checking wchar.h presence... yes
checking for wchar.h... yes
checking sys/sockio.h usability... no
checking sys/sockio.h presence... no
checking for sys/sockio.h... no
checking for floor in -lm... yes
checking for ceil in -lm... yes
checking uuid/uuid.h usability... yes
checking uuid/uuid.h presence... yes
checking for uuid/uuid.h... yes
checking for uuid_parse in -luuid... yes
checking for inet_ntoa in -lnsl... no
checking for socket in -lsocket... no
checking whether printf must be declared... no
checking whether fprintf must be declared... no
checking whether syslog must be declared... no
checking whether puts must be declared... no
checking whether fputs must be declared... no
checking whether fputc must be declared... no
checking whether fopen must be declared... no
checking whether fclose must be declared... no
checking whether fwrite must be declared... no
checking whether fflush must be declared... no
checking whether getopt must be declared... no
checking whether bzero must be declared... no
checking whether bcopy must be declared... no
checking whether memset must be declared... no
checking whether strtol must be declared... no
checking whether strcasecmp must be declared... no
checking whether strncasecmp must be declared... no
checking whether strerror must be declared... no
checking whether perror must be declared... no
checking whether socket must be declared... no
checking whether sendto must be declared... no
checking whether vsnprintf must be declared... no
checking whether snprintf must be declared... no
checking whether strtoul must be declared... no
checking for sigaction... yes
checking for strlcpy... yes
checking for strlcat... yes
checking for strerror... (cached) yes
checking for vswprintf... yes
checking for wprintf... yes
checking for memrchr... yes
checking for inet_ntop... yes
checking for gettid... no
checking for snprintf... yes
checking for malloc_trim... no
checking for mallinfo... no
checking size of char... (cached) 1
checking size of short... (cached) 2
checking size of int... (cached) 4
checking size of long int... (cached) 4
checking size of long long int... 8
checking size of unsigned int... (cached) 4
checking size of unsigned long int... 4
checking size of unsigned long long int... 8
checking for u_int8_t... yes
checking for u_int16_t... yes
checking for u_int32_t... yes
checking for u_int64_t... yes
checking for uint8_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for int8_t... yes
checking for int16_t... yes
checking for int32_t... yes
checking for int64_t... yes
checking for boolean... no
yes
checking for __FUNCTION__... yes
checking for pcap_datalink in -lpcap... yes
yes
checking for pcap_lib_version... yes
checking pcre.h usability... yes
checking pcre.h presence... yes
checking for pcre.h... yes
checking for pcre_compile in -lpcre... yes
checking for libpcre version 6.0 or greater... yes
checking for SHA256_Init in -lcrypto... no
checking for MD5_Init in -lcrypto... no
checking dnet.h usability... yes
checking dnet.h presence... yes
checking for dnet.h... yes
checking dumbnet.h usability... no
checking dumbnet.h presence... no
checking for dumbnet.h... no
checking for eth_set in -ldnet... yes
checking for eth_set in -ldumbnet... no
checking for dlsym in -ldl... yes
checking for daq_load_modules in -ldaq... yes
checking for daq_hup_apply... yes
checking for daq_acquire_with_meta... yes
checking for daq_dp_add_dc... yes

checking whether DAQ_PKT_FLAG_DECRYPTED_SSL is declared... no
checking whether DAQ_PKT_FLAG_LOCALLY_ORIGINATED is declared... yes
checking whether DAQ_PKT_FLAG_LOCALLY_DESTINED is declared... yes
checking for struct _DAQ_DP_key_t.sa.src_ip4... yes
yes
yes
yes
no
yes
yes
checking for DAQ_VERDICT_RETRY... yes
no
DAQ version doesn't support packet trace.
no
DAQ version doesn't support tracing verdict reason.
checking for sparc... no
checking for visibility support... yes
checking zlib.h usability... yes
checking zlib.h presence... yes
checking for zlib.h... yes
checking for inflate in -lz... yes
checking for pthread_tryjoin_np... yes
checking pkg-config is at least version 0.9.0... yes
checking for luajit... yes
checking openssl/x509.h usability... no
checking openssl/x509.h presence... no
checking for openssl/x509.h... no

   ERROR!  openssl/x509.h or openssl library not found.
   Try compiling without openAppId using '--disable-open-appid'
configure: error: "Fatal!"
make[3]: *** [Makefile:162: /openwrt/build_dir/target-mips_24kc_musl/snort/snort-2.9.17.1/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
