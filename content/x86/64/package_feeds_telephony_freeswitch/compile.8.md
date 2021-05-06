---
title: "compile.8"
date: 2021-05-06 05:08:02.037173
hidden: false
draft: false
weight: -8
---

build number: `8`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/telephony/freeswitch/compile -j$(nproc) || make package/feeds/telephony/freeswitch/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/003-modmake-fix.patch using plaintext: 
patching file build/modmake.rulesam

Applying ./patches/010-fix-zrtp-cflags.patch using plaintext: 
patching file libs/libzrtp/configure.ac

Applying ./patches/030-fix-configure-ac.patch using plaintext: 
patching file configure.ac

Applying ./patches/110-apr-add-cache-for-strerror_r.patch using plaintext: 
patching file libs/apr-util/build/apr_common.m4
patching file libs/apr/build/apr_common.m4
patching file libs/unimrcp/build/acmacros/apr_common.m4

Applying ./patches/120-fix-copts.patch using plaintext: 
patching file configure.ac
patching file libs/apr-util/configure.ac
patching file libs/apr/configure.ac
patching file libs/iksemel/configure.ac
patching file libs/libdingaling/configure.ac
patching file libs/srtp/configure.ac

Applying ./patches/130-fix-iksemel-copts.patch using plaintext: 
patching file libs/iksemel/src/Makefile.am

Applying ./patches/140-libvpx-cross.patch using plaintext: 
patching file Makefile.am

Applying ./patches/150-erlang-m4.patch using plaintext: 
patching file build/config/erlang.m4

Applying ./patches/170-mod_random.patch using plaintext: 
patching file src/mod/applications/mod_random/Makefile.am

Applying ./patches/180-mod_perl.patch using plaintext: 
patching file src/mod/languages/mod_perl/Makefile.am

Applying ./patches/190-mod_pocketsphinx.patch using plaintext: 
patching file src/mod/asr_tts/mod_pocketsphinx/Makefile.am

Applying ./patches/200-mod_verto-fix-copts.patch using plaintext: 
patching file src/mod/endpoints/mod_verto/Makefile.am

Applying ./patches/210-esl-perl-fix-copts.patch using plaintext: 
patching file libs/esl/perl/Makefile.am

Applying ./patches/230-mod_radius_cdr.patch using plaintext: 
patching file src/mod/event_handlers/mod_radius_cdr/Makefile.am
patching file src/mod/event_handlers/mod_radius_cdr/freeradius-client-1.1.6-configure-in.diff

Applying ./patches/260-mod_event_zmq-fix-build-with-fortify-headers.patch using plaintext: 
patching file src/mod/event_handlers/mod_event_zmq/Makefile.am

Applying ./patches/280-tone-down-freetdm-COMP_VENDOR_CFLAGS.patch using plaintext: 
patching file libs/freetdm/configure.ac

Applying ./patches/290-fix-mod_freetdm-copts.patch using plaintext: 
patching file libs/freetdm/mod_freetdm/Makefile.in

Applying ./patches/320-workaround-format-truncation-error-in-mod_cdr_mongodb.patch using plaintext: 
patching file configure.ac

Applying ./patches/330-do-not-install-freetdm-twice.patch using plaintext: 
patching file libs/freetdm/mod_freetdm/Makefile.in

Applying ./patches/360-fix-APR_TRY_COMPILE_NO_WARNING.patch using plaintext: 
patching file libs/apr-util/build/apr_common.m4
patching file libs/apr/build/apr_common.m4

Applying ./patches/370-procd-compat.patch using plaintext: 
patching file src/switch_console.c

Applying ./patches/380-disable-luajit.patch using plaintext: 
patching file configure.ac

Applying ./patches/390-spandsp3-pkg-config.patch using plaintext: 
patching file configure.ac

Applying ./patches/400-fix-pc-file.patch using plaintext: 
patching file build/freeswitch.pc.in
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force 
autoreconf: configure.ac: tracing
autoreconf: configure.ac: adding subdirectory libs/srtp to autoreconf
autoreconf: Entering directory `libs/srtp'
autoreconf: running: /openwrt/staging_dir/host/bin/libtoolize --install --force
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build'.
OpenWrt-libtoolize: linking file `build/config.guess'
OpenWrt-libtoolize: linking file `build/config.sub'
OpenWrt-libtoolize: linking file `build/install-sh'
OpenWrt-libtoolize: linking file `build/ltmain.sh'
OpenWrt-libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.ac and
OpenWrt-libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
OpenWrt-libtoolize: Consider adding `-I m4' to ACLOCAL_AMFLAGS in Makefile.am.
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-x86_64_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/automake --add-missing --force-missing
test/Makefile.am:11: warning: source file 'crypto/aes_calc.c' is in a subdirectory,
test/Makefile.am:11: but option 'subdir-objects' is disabled
automake: warning: possible forward-incompatibility.
automake: At least a source file is in a subdirectory, but the 'subdir-objects'
automake: automake option hasn't been enabled.  For now, the corresponding output
automake: object file(s) will be placed in the top-level directory.  However,
automake: this behaviour will change in future Automake versions: they will
automake: unconditionally cause object files to be placed in the same subdirectory
automake: of the corresponding sources.
automake: You are advised to start using 'subdir-objects' option throughout your
automake: project, to avoid future incompatibilities.
test/Makefile.am:9: warning: source file 'crypto/cipher_driver.c' is in a subdirectory,
test/Makefile.am:9: but option 'subdir-objects' is disabled
test/Makefile.am:12: warning: source file 'crypto/datatypes_driver.c' is in a subdirectory,
test/Makefile.am:12: but option 'subdir-objects' is disabled
test/Makefile.am:10: warning: source file 'crypto/kernel_driver.c' is in a subdirectory,
test/Makefile.am:10: but option 'subdir-objects' is disabled
test/Makefile.am:13: warning: source file 'crypto/sha1_driver.c' is in a subdirectory,
test/Makefile.am:13: but option 'subdir-objects' is disabled
test/Makefile.am:14: warning: source file 'crypto/stat_driver.c' is in a subdirectory,
test/Makefile.am:14: but option 'subdir-objects' is disabled
autoreconf: Leaving directory `libs/srtp'
autoreconf: configure.ac: adding subdirectory libs/apr to autoreconf
autoreconf: Entering directory `libs/apr'
configure.ac:149: warning: AC_COMPILE_IFELSE was called before AC_USE_SYSTEM_EXTENSIONS
../../lib/autoconf/specific.m4:436: AC_AIX is expanded from...
configure.ac:149: the top level
configure.ac:149: warning: AC_COMPILE_IFELSE was called before AC_USE_SYSTEM_EXTENSIONS
../../lib/autoconf/specific.m4:436: AC_AIX is expanded from...
configure.ac:149: the top level
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build'.
OpenWrt-libtoolize: linking file `build/config.guess'
OpenWrt-libtoolize: linking file `build/config.sub'
OpenWrt-libtoolize: linking file `build/install-sh'
OpenWrt-libtoolize: linking file `build/ltmain.sh'
OpenWrt-libtoolize: You should add the contents of the following files to `aclocal.m4':
OpenWrt-libtoolize:   `/openwrt/staging_dir/target-x86_64_musl/../host/share/aclocal/libtool.m4'
OpenWrt-libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.ac and
OpenWrt-libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
OpenWrt-libtoolize: Consider adding `-I m4' to ACLOCAL_AMFLAGS in Makefile.am.
OpenWrt-libtoolize: `AC_PROG_RANLIB' is rendered obsolete by `LT_INIT'
configure.ac:149: warning: AC_COMPILE_IFELSE was called before AC_USE_SYSTEM_EXTENSIONS
../../lib/autoconf/specific.m4:436: AC_AIX is expanded from...
configure.ac:149: the top level
configure.ac:149: warning: AC_COMPILE_IFELSE was called before AC_USE_SYSTEM_EXTENSIONS
../../lib/autoconf/specific.m4:436: AC_AIX is expanded from...
configure.ac:149: the top level
configure.ac:149: warning: AC_COMPILE_IFELSE was called before AC_USE_SYSTEM_EXTENSIONS
../../lib/autoconf/specific.m4:436: AC_AIX is expanded from...
configure.ac:149: the top level
autoreconf: configure.ac: not using Automake
autoreconf: Leaving directory `libs/apr'
autoreconf: configure.ac: adding subdirectory libs/apr-util to autoreconf
autoreconf: Entering directory `libs/apr-util'
autoreconf: configure.ac: not using Libtool
autoreconf: Leaving directory `libs/apr-util'
autoreconf: configure.ac: adding subdirectory libs/iksemel to autoreconf
autoreconf: Entering directory `libs/iksemel'
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build'.
OpenWrt-libtoolize: linking file `build/config.guess'
OpenWrt-libtoolize: linking file `build/config.sub'
OpenWrt-libtoolize: linking file `build/install-sh'
OpenWrt-libtoolize: linking file `build/ltmain.sh'
OpenWrt-libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.ac and
OpenWrt-libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
OpenWrt-libtoolize: Consider adding `-I m4' to ACLOCAL_AMFLAGS in Makefile.am.
autoreconf: Leaving directory `libs/iksemel'
autoreconf: configure.ac: adding subdirectory libs/libdingaling to autoreconf
autoreconf: Entering directory `libs/libdingaling'
aclocal.m4:9578: warning: file `build/config/ac_gcc_x86_cpuid.m4' included several times
aclocal.m4:9579: warning: file `build/config/ac_gcc_archflag.m4' included several times
aclocal.m4:9580: warning: file `build/config/ax_check_compiler_flags.m4' included several times
aclocal.m4:9581: warning: file `build/config/ax_cc_maxopt.m4' included several times
aclocal.m4:9582: warning: file `build/config/ax_cflags_warn_all_ansi.m4' included several times
aclocal.m4:9583: warning: file `build/config/ax_compiler_vendor.m4' included several times
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build'.
OpenWrt-libtoolize: linking file `build/config.guess'
OpenWrt-libtoolize: linking file `build/config.sub'
OpenWrt-libtoolize: linking file `build/install-sh'
OpenWrt-libtoolize: linking file `build/ltmain.sh'
OpenWrt-libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.ac and
OpenWrt-libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
OpenWrt-libtoolize: Consider adding `-I m4' to ACLOCAL_AMFLAGS in Makefile.am.
aclocal.m4:9578: warning: file `build/config/ac_gcc_x86_cpuid.m4' included several times
aclocal.m4:9579: warning: file `build/config/ac_gcc_archflag.m4' included several times
aclocal.m4:9580: warning: file `build/config/ax_check_compiler_flags.m4' included several times
aclocal.m4:9581: warning: file `build/config/ax_cc_maxopt.m4' included several times
aclocal.m4:9582: warning: file `build/config/ax_cflags_warn_all_ansi.m4' included several times
aclocal.m4:9583: warning: file `build/config/ax_compiler_vendor.m4' included several times
aclocal.m4:9578: warning: file `build/config/ac_gcc_x86_cpuid.m4' included several times
aclocal.m4:9579: warning: file `build/config/ac_gcc_archflag.m4' included several times
aclocal.m4:9580: warning: file `build/config/ax_check_compiler_flags.m4' included several times
aclocal.m4:9581: warning: file `build/config/ax_cc_maxopt.m4' included several times
aclocal.m4:9582: warning: file `build/config/ax_cflags_warn_all_ansi.m4' included several times
aclocal.m4:9583: warning: file `build/config/ax_compiler_vendor.m4' included several times
aclocal.m4:9578: warning: file `build/config/ac_gcc_x86_cpuid.m4' included several times
aclocal.m4:9579: warning: file `build/config/ac_gcc_archflag.m4' included several times
aclocal.m4:9580: warning: file `build/config/ax_check_compiler_flags.m4' included several times
aclocal.m4:9581: warning: file `build/config/ax_cc_maxopt.m4' included several times
aclocal.m4:9582: warning: file `build/config/ax_cflags_warn_all_ansi.m4' included several times
aclocal.m4:9583: warning: file `build/config/ax_compiler_vendor.m4' included several times
Makefile.am:17: warning: source file 'src/libdingaling.c' is in a subdirectory,
Makefile.am:17: but option 'subdir-objects' is disabled
automake: warning: possible forward-incompatibility.
automake: At least a source file is in a subdirectory, but the 'subdir-objects'
automake: automake option hasn't been enabled.  For now, the corresponding output
automake: object file(s) will be placed in the top-level directory.  However,
automake: this behaviour will change in future Automake versions: they will
automake: unconditionally cause object files to be placed in the same subdirectory
automake: of the corresponding sources.
automake: You are advised to start using 'subdir-objects' option throughout your
automake: project, to avoid future incompatibilities.
Makefile.am:17: warning: source file 'src/sha1.c' is in a subdirectory,
Makefile.am:17: but option 'subdir-objects' is disabled
autoreconf: Leaving directory `libs/libdingaling'
autoreconf: configure.ac: adding subdirectory libs/freetdm to autoreconf
autoreconf: Entering directory `libs/freetdm'
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-x86_64_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-x86_64_musl/usr/share/aclocal -I m4 -I . --force -I build
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build'.
OpenWrt-libtoolize: linking file `build/config.guess'
OpenWrt-libtoolize: linking file `build/config.sub'
OpenWrt-libtoolize: linking file `build/install-sh'
OpenWrt-libtoolize: linking file `build/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `build'.
OpenWrt-libtoolize: linking file `build/libtool.m4'
OpenWrt-libtoolize: linking file `build/ltoptions.m4'
OpenWrt-libtoolize: linking file `build/ltsugar.m4'
OpenWrt-libtoolize: linking file `build/ltversion.m4'
OpenWrt-libtoolize: linking file `build/lt~obsolete.m4'
autoreconf: configure.ac: not using Autoheader
Makefile.am:157: warning: source file '$(SRC)/ftmod/ftmod_analog/ftmod_analog.c' is in a subdirectory,
Makefile.am:157: but option 'subdir-objects' is disabled
automake: warning: possible forward-incompatibility.
automake: At least a source file is in a subdirectory, but the 'subdir-objects'
automake: automake option hasn't been enabled.  For now, the corresponding output
automake: object file(s) will be placed in the top-level directory.  However,
automake: this behaviour will change in future Automake versions: they will
automake: unconditionally cause object files to be placed in the same subdirectory
automake: of the corresponding sources.
automake: You are advised to start using 'subdir-objects' option throughout your
automake: project, to avoid future incompatibilities.
Makefile.am:162: warning: source file '$(SRC)/ftmod/ftmod_analog_em/ftmod_analog_em.c' is in a subdirectory,
Makefile.am:162: but option 'subdir-objects' is disabled
Makefile.am:256: warning: source file '$(SRC)/ftmod/ftmod_gsm/ftmod_gsm.c' is in a subdirectory,
Makefile.am:256: but option 'subdir-objects' is disabled
Makefile.am:179: warning: source file '$(SRC)/ftmod/ftmod_isdn/ftmod_isdn.c' is in a subdirectory,
Makefile.am:179: but option 'subdir-objects' is disabled
Makefile.am:187: warning: source file '$(SRC)/ftmod/ftmod_libpri/ftmod_libpri.c' is in a subdirectory,
Makefile.am:187: but option 'subdir-objects' is disabled
Makefile.am:187: warning: source file '$(SRC)/ftmod/ftmod_libpri/lpwrap_pri.c' is in a subdirectory,
Makefile.am:187: but option 'subdir-objects' is disabled
Makefile.am:264: warning: source file '$(SRC)/ftmod/ftmod_misdn/ftmod_misdn.c' is in a subdirectory,
Makefile.am:264: but option 'subdir-objects' is disabled
Makefile.am:195: warning: source file '$(SRC)/ftmod/ftmod_pritap/ftmod_pritap.c' is in a subdirectory,
Makefile.am:195: but option 'subdir-objects' is disabled
Makefile.am:248: warning: source file '$(SRC)/ftmod/ftmod_r2/ftmod_r2.c' is in a subdirectory,
Makefile.am:248: but option 'subdir-objects' is disabled
Makefile.am:248: warning: source file '$(SRC)/ftmod/ftmod_r2/ftmod_r2_io_mf_lib.c' is in a subdirectory,
Makefile.am:248: but option 'subdir-objects' is disabled
Makefile.am:228: warning: source file '$(SRC)/ftmod/ftmod_sangoma_isdn/ftmod_sangoma_isdn.c' is in a subdirectory,
Makefile.am:228: but option 'subdir-objects' is disabled
Makefile.am:228: warning: source file '$(SRC)/ftmod/ftmod_sangoma_isdn/ftmod_sangoma_isdn_cfg.c' is in a subdirectory,
Makefile.am:228: but option 'subdir-objects' is disabled
Makefile.am:228: warning: source file '$(SRC)/ftmod/ftmod_sangoma_isdn/ftmod_sangoma_isdn_cntrl.c' is in a subdirectory,
Makefile.am:228: but option 'subdir-objects' is disabled
Makefile.am:228: warning: source file '$(SRC)/ftmod/ftmod_sangoma_isdn/ftmod_sangoma_isdn_trace.c' is in a subdirectory,
Makefile.am:228: but option 'subdir-objects' is disabled
Makefile.am:228: warning: source file '$(SRC)/ftmod/ftmod_sangoma_isdn/ftmod_sangoma_isdn_transfer.c' is in a subdirectory,
Makefile.am:228: but option 'subdir-objects' is disabled
Makefile.am:228: warning: source file '$(SRC)/ftmod/ftmod_sangoma_isdn/ftmod_sangoma_isdn_support.c' is in a subdirectory,
Makefile.am:228: but option 'subdir-objects' is disabled
Makefile.am:228: warning: source file '$(SRC)/ftmod/ftmod_sangoma_isdn/ftmod_sangoma_isdn_stack_cntrl.c' is in a subdirectory,
Makefile.am:228: but option 'subdir-objects' is disabled
Makefile.am:228: warning: source file '$(SRC)/ftmod/ftmod_sangoma_isdn/ftmod_sangoma_isdn_stack_cfg.c' is in a subdirectory,
Makefile.am:228: but option 'subdir-objects' is disabled
Makefile.am:228: warning: source file '$(SRC)/ftmod/ftmod_sangoma_isdn/ftmod_sangoma_isdn_stack_rcv.c' is in a subdirectory,
Makefile.am:228: but option 'subdir-objects' is disabled
Makefile.am:228: warning: source file '$(SRC)/ftmod/ftmod_sangoma_isdn/ftmod_sangoma_isdn_stack_hndl.c' is in a subdirectory,
Makefile.am:228: but option 'subdir-objects' is disabled
Makefile.am:228: warning: source file '$(SRC)/ftmod/ftmod_sangoma_isdn/ftmod_sangoma_isdn_stack_out.c' is in a subdirectory,
Makefile.am:228: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_support.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_main.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_handle.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_in.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_out.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_cntrl.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_xml.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_timers.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_cli.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_cfg.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_sta.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_sts.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_logger.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_m2ua_xml.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_m2ua.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:203: warning: source file '$(SRC)/ftmod/ftmod_sangoma_ss7/ftmod_sangoma_ss7_relay.c' is in a subdirectory,
Makefile.am:203: but option 'subdir-objects' is disabled
Makefile.am:152: warning: source file '$(SRC)/ftmod/ftmod_skel/ftmod_skel.c' is in a subdirectory,
Makefile.am:152: but option 'subdir-objects' is disabled
Makefile.am:169: warning: source file '$(SRC)/ftmod/ftmod_wanpipe/ftmod_wanpipe.c' is in a subdirectory,
Makefile.am:169: but option 'subdir-objects' is disabled
Makefile.am:147: warning: source file '$(SRC)/ftmod/ftmod_zt/ftmod_zt.c' is in a subdirectory,
Makefile.am:147: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/hashtable.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/hashtable_itr.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/ftdm_io.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/ftdm_state.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/ftdm_queue.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/ftdm_sched.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/ftdm_call_utils.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/ftdm_variables.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/ftdm_config.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/ftdm_callerid.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/fsk.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/uart.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/g711.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/libteletone_detect.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/libteletone_generate.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/ftdm_buffer.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/ftdm_threadmutex.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/ftdm_dso.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/ftdm_cpu_monitor.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:63: warning: source file '$(SRC)/ftdm_backtrace.c' is in a subdirectory,
Makefile.am:63: but option 'subdir-objects' is disabled
Makefile.am:122: warning: source file '$(SRC)/detect_dtmf.c' is in a subdirectory,
Makefile.am:122: but option 'subdir-objects' is disabled
Makefile.am:118: warning: source file '$(SRC)/detect_tones.c' is in a subdirectory,
Makefile.am:118: but option 'subdir-objects' is disabled
Makefile.am:138: warning: source file '$(SRC)/testanalog.c' is in a subdirectory,
Makefile.am:138: but option 'subdir-objects' is disabled
Makefile.am:106: warning: source file '$(SRC)/testapp.c' is in a subdirectory,
Makefile.am:106: but option 'subdir-objects' is disabled
Makefile.am:110: warning: source file '$(SRC)/testcid.c' is in a subdirectory,
Makefile.am:110: but option 'subdir-objects' is disabled
Makefile.am:130: warning: source file '$(SRC)/testpri.c' is in a subdirectory,
Makefile.am:130: but option 'subdir-objects' is disabled
Makefile.am:134: warning: source file '$(SRC)/testr2.c' is in a subdirectory,
Makefile.am:134: but option 'subdir-objects' is disabled
Makefile.am:114: warning: source file '$(SRC)/testtones.c' is in a subdirectory,
Makefile.am:114: but option 'subdir-objects' is disabled
autoreconf: Leaving directory `libs/freetdm'
autoreconf: configure.ac: adding subdirectory libs/unimrcp to autoreconf
autoreconf: Entering directory `libs/unimrcp'
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build'.
OpenWrt-libtoolize: linking file `build/config.guess'
OpenWrt-libtoolize: linking file `build/config.sub'
OpenWrt-libtoolize: linking file `build/install-sh'
OpenWrt-libtoolize: linking file `build/ltmain.sh'
OpenWrt-libtoolize: putting macros in AC_CONFIG_MACRO_DIR, `build/acmacros'.
OpenWrt-libtoolize: linking file `build/acmacros/libtool.m4'
OpenWrt-libtoolize: You should add the contents of `build/acmacros/libtool.m4' to `aclocal.m4'.
OpenWrt-libtoolize: linking file `build/acmacros/ltoptions.m4'
OpenWrt-libtoolize: You should add the contents of `build/acmacros/ltoptions.m4' to `aclocal.m4'.
OpenWrt-libtoolize: linking file `build/acmacros/ltsugar.m4'
OpenWrt-libtoolize: You should add the contents of `build/acmacros/ltsugar.m4' to `aclocal.m4'.
OpenWrt-libtoolize: linking file `build/acmacros/ltversion.m4'
OpenWrt-libtoolize: You should add the contents of `build/acmacros/ltversion.m4' to `aclocal.m4'.
OpenWrt-libtoolize: linking file `build/acmacros/lt~obsolete.m4'
OpenWrt-libtoolize: You should add the contents of `build/acmacros/lt~obsolete.m4' to `aclocal.m4'.
OpenWrt-libtoolize: Consider adding `-I build/acmacros' to ACLOCAL_AMFLAGS in Makefile.am.
autoreconf: Leaving directory `libs/unimrcp'
autoreconf: configure.ac: adding subdirectory libs/libzrtp to autoreconf
autoreconf: Entering directory `libs/libzrtp'
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
automake: warning: possible forward-incompatibility.
automake: At least a source file is in a subdirectory, but the 'subdir-objects'
automake: automake option hasn't been enabled.  For now, the corresponding output
automake: object file(s) will be placed in the top-level directory.  However,
automake: this behaviour will change in future Automake versions: they will
automake: unconditionally cause object files to be placed in the same subdirectory
automake: of the corresponding sources.
automake: You are advised to start using 'subdir-objects' option throughout your
automake: project, to avoid future incompatibilities.
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_crc.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_crypto_aes.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_crypto_atl.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_crypto_ec.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_crypto_ecdh.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_crypto_hash.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_crypto_pk.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_crypto_sas.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_datatypes.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_engine.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_iface_scheduler.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_iface_sys.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_initiator.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_legal.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_list.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_log.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_pbx.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_protocol.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_responder.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_rng.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_srtp_builtin.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_string.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_utils.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_utils_proto.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/third_party/bgaes/aes_modes.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/third_party/bgaes/aescrypt.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/third_party/bgaes/aeskey.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/third_party/bgaes/aestab.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/third_party/bgaes/sha1.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/third_party/bgaes/sha2.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:54: warning: source file '$(top_srcdir)/src/zrtp_iface_cache.c' is in a subdirectory,
Makefile.am:54: but option 'subdir-objects' is disabled
Makefile.am:99: warning: source file '$(top_srcdir)/test/cmockery/cmockery.c' is in a subdirectory,
Makefile.am:99: but option 'subdir-objects' is disabled
Makefile.am:99: warning: source file '$(top_srcdir)/test/cache_test.c' is in a subdirectory,
Makefile.am:99: but option 'subdir-objects' is disabled
autoreconf: Leaving directory `libs/libzrtp'
OpenWrt-libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, `build/config'.
OpenWrt-libtoolize: linking file `build/config/config.guess'
OpenWrt-libtoolize: linking file `build/config/config.sub'
OpenWrt-libtoolize: linking file `build/config/install-sh'
OpenWrt-libtoolize: linking file `build/config/ltmain.sh'
OpenWrt-libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.ac and
OpenWrt-libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
OpenWrt-libtoolize: Consider adding `-I m4' to ACLOCAL_AMFLAGS in Makefile.am.
autoreconf: Leaving directory `.'
configure: loading site script /openwrt/include/site/x86_64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
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
checking dependency style of ccache_cc... none
checking for x86_64-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking dependency style of ccache_cc... (cached) none
checking whether we are using the GNU C++ compiler... yes
checking whether ccache_cxx accepts -g... yes
checking dependency style of ccache_cxx... none
checking whether the C++ compiler works... yes
checking for gawk... (cached) gawk
checking whether make sets $(MAKE)... (cached) yes
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
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
checking whether the ccache_cc linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... no
checking how to run the C++ preprocessor... ccache_cxx -E
checking for ld used by ccache_cxx... x86_64-openwrt-linux-musl-ld -m elf_x86_64
checking if the linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) is GNU ld... yes
checking whether the ccache_cxx linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) supports shared libraries... yes
checking for ccache_cxx option to produce PIC... -fPIC -DPIC
checking if ccache_cxx PIC flag -fPIC -DPIC works... yes
checking if ccache_cxx static flag -static works... yes
checking if ccache_cxx supports -c -o file.o... yes
checking if ccache_cxx supports -c -o file.o... (cached) yes
checking whether the ccache_cxx linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking for C compiler vendor... gnu
checking libtool major version... 2
using libtool library extension... la
checking whether compiler supports -Wno-unused-result... yes
yes
checking whether compiler supports -Wno-misleading-indentation... yes
yes
checking whether compiler supports -Wno-error=format-truncation... yes
yes
  adding "-fPIC" to SWITCH_AM_CFLAGS
  adding "-ffast-math" to SWITCH_AM_CFLAGS
  adding "-fPIC" to SWITCH_AM_CXXFLAGS
  adding "-ffast-math" to SWITCH_AM_CXXFLAGS
  adding "-Werror" to SWITCH_AM_CFLAGS
  adding "-Wno-unused-result" to SWITCH_AM_CFLAGS
  adding "-Wno-misleading-indentation" to SWITCH_AM_CFLAGS
  adding "-Wno-error=format-truncation" to SWITCH_AM_CFLAGS
checking whether the compiler supports -fvisibility=hidden... yes
  adding "-fvisibility=hidden" to SWITCH_AM_CFLAGS
  adding "-DSWITCH_API_VISIBILITY=1" to SWITCH_AM_CFLAGS
  adding "-DCJSON_API_VISIBILITY=1" to SWITCH_AM_CFLAGS
  adding "-DHAVE_VISIBILITY=1" to SWITCH_AM_CFLAGS
  adding "-fvisibility=hidden" to SWITCH_AM_CXXFLAGS
  adding "-DSWITCH_API_VISIBILITY=1" to SWITCH_AM_CXXFLAGS
  adding "-DCJSON_API_VISIBILITY=1" to SWITCH_AM_CXXFLAGS
  adding "-DHAVE_VISIBILITY=1" to SWITCH_AM_CXXFLAGS
checking for lua5.2... checking for lua-5.2... checking for lua52... checking for lua5.1... checking for lua-5.1... checking for lua... yes
checking LUA_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking LUA_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -llua -lm 
checking for alMidiGainSOFT in -lopenal... no
  adding "-DENABLE_ZRTP" to SWITCH_AM_CFLAGS
checking for jack... checking for snd_pcm_open in -lasound... yes
checking size of long... (cached) 8
checking what directory libraries are found in... lib64
checking whether to include odbc... yes
checking for uuid >= 1.41.2... yes
checking LIBUUID_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include/uuid 
checking LIBUUID_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -luuid 
checking for pg_config... /openwrt/staging_dir/target-x86_64_musl/usr/bin/pg_config
checking for pkg-config... /openwrt/staging_dir/host/bin/pkg-config
checking for PostgreSQL libraries via pkg_config... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib 
checking for PQgetvalue in -lpq... yes
checking for libmariadb >= 3.0.9... yes
checking MARIADB_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include/mysql/ 
checking MARIADB_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/ -lmariadb 
checking for spandsp3 >= 3.0... yes
checking SPANDSP_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/spandsp3/include 
checking SPANDSP_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/spandsp3/lib -l:libspandsp.so.3 
checking for sofia-sip-ua >= 1.13.3... yes
checking SOFIA_SIP_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include/sofia-sip-1.13 
checking SOFIA_SIP_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lsofia-sip-ua 
  setting PLATFORM_CORE_LIBS to "-ldl -lcrypt -lrt"
checking for inflateReset in -lz... yes
  adding "-lz" to PLATFORM_CORE_LIBS
checking for libmpg123 >= 1.16.0... yes
checking MPG123_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking MPG123_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lmpg123 
checking for opencore-amrnb >= 0.1.0... no
checking for opencore-amrwb >= 0.1.0 vo-amrwbenc >= 0.1.0... no
checking for apr_pool_mutex_set in -lapr-1... no
checking for apr_queue_pop_timeout in -laprutil-1... no
checking for jpeg_std_error in -ljpeg... yes
checking for jbg_enc_out in -ljbig... no
checking for lzma_code in -llzma... yes
checking for res_init in -lresolv... yes
  adding "-lresolv" to SWITCH_AM_LDFLAGS
checking for dirent.h that defines DIR... yes
checking for library containing opendir... none required
checking for ANSI C header files... (cached) yes
checking for sys/types.h... (cached) yes
checking sys/resource.h usability... yes
checking sys/resource.h presence... yes
checking for sys/resource.h... yes
checking sched.h usability... yes
checking sched.h presence... yes
checking for sched.h... yes
checking wchar.h usability... yes
checking wchar.h presence... yes
checking for wchar.h... yes
checking sys/filio.h usability... no
checking sys/filio.h presence... no
checking for sys/filio.h... no
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/prctl.h usability... yes
checking sys/prctl.h presence... yes
checking for sys/prctl.h... yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking execinfo.h usability... no
checking execinfo.h presence... no
checking for execinfo.h... no
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking for size_t... yes
checking whether time.h and sys/time.h may both be included... yes
checking whether struct tm is in sys/time.h or time.h... time.h
checking whether ccache_cc needs -traditional... no
checking for stdlib.h... (cached) yes
checking for GNU libc compatible malloc... (cached) yes
checking return type of signal handlers... void
checking for strftime... (cached) yes
checking for gethostname... yes
checking for vasprintf... yes
checking for mmap... yes
checking for mlock... yes
checking for mlockall... yes
checking for usleep... yes
checking for getifaddrs... yes
checking for timerfd_create... yes
checking for getdtablesize... yes
checking for posix_openpt... yes
checking for poll... yes
checking for sched_setscheduler... yes
checking for setpriority... yes
checking for setrlimit... yes
checking for setgroups... yes
checking for initgroups... yes
checking for getrusage... yes
checking for wcsncmp... yes
checking for setgroups... (cached) yes
checking for asprintf... yes
checking for setenv... yes
checking for pselect... yes
checking for gettimeofday... (cached) yes
checking for localtime_r... yes
checking for gmtime_r... yes
checking for strcasecmp... yes
checking for stricmp... no
checking for _stricmp... no
checking whether strerror_r is declared... yes
checking for strerror_r... yes
checking whether strerror_r returns char *... no
checking for sched_setaffinity... yes
checking for sched_getaffinity... yes
checking whether the CPU_SET and CPU_ZERO macros are defined... yes
checking for clock_gettime in -lrt... yes
checking for clock_getres in -lrt... yes
checking for clock_nanosleep in -lrt... yes
checking for pthread_setschedparam in -lpthread... yes
checking for socket... yes
checking for /dev/ptmx... (cached) yes
checking for openpty in -lutil... yes
checking for struct tm.tm_gmtoff... yes
checking for struct tm.tm_zone... yes
checking whether RLIMIT_MEMLOCK is declared... yes
checking whether SCHED_RR is declared... yes
checking whether SCHED_FIFO is declared... yes
checking whether to use mlockall... yes
checking for setenv... (cached) yes
checking for strtoll... yes
checking for strtoull... yes
checking for strtoq... no
checking for strtouq... no
checking for __strtoll... no
checking for __strtoull... no
checking whether va_list is an array... yes
checking whether compiler has __attribute__... yes
checking whether compiler supports -Wdeclaration-after-statement... yes
yes
  setting SWITCH_ANSI_CFLAGS to "-Wdeclaration-after-statement"
checking whether byte ordering is bigendian... (cached) no
checking size of char... (cached) 1
checking size of int... (cached) 4
checking size of long... (cached) 8
checking size of short... (cached) 2
checking size of long long... (cached) 8
checking for size_t... (cached) yes
checking for ssize_t... yes
checking size of void*... 8
checking size of ssize_t... (cached) 8
checking size of size_t... (cached) 8
checking for gunzip... /usr/bin/gunzip
checking for bzip2... /openwrt/staging_dir/hostpkg/bin/bzip2
checking for xz... /openwrt/staging_dir/host/bin/xz
checking for gtar... no
checking for tar... /openwrt/staging_dir/host/bin/tar
checking for wget... /openwrt/staging_dir/host/bin/wget
checking for curl... /usr/bin/curl
checking for libpng >= 1.6.16... yes
checking LIBPNG_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include/libpng16 -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking LIBPNG_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lpng16 
checking for freetype2 >= 2.4.9... yes
checking FREETYPE_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include/freetype2 -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/libpng16 
checking FREETYPE_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lfreetype 
checking for gumbo >= 0.10.1... no
checking for libfvad >= 1.0... no
checking for libtpl >= 1.5... no
checking for sqlite3 >= 3.6.20... yes
checking SQLITE_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking SQLITE_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lsqlite3 
checking for libcurl >= 7.19... yes
checking CURL_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking CURL_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lcurl 
checking for libpcre >= 7.8... yes
checking PCRE_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking PCRE_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lpcre 
checking for speex >= 1.2rc1 speexdsp >= 1.2rc1... yes
checking SPEEX_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking SPEEX_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lspeex -lspeexdsp 
checking for yaml-0.1 >= 0.1.4... yes
checking YAML_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking YAML_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lyaml 
checking for portaudio-2.0 >= 19... yes
checking PORTAUDIO_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking PORTAUDIO_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lportaudio -lasound -lm -lpthread 
checking for libldns-fs >= 1.6.6... checking for libldns >= 1.6.6... yes
checking LDNS_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking LDNS_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lldns 
checking for sndfile >= 1.0.20... yes
checking SNDFILE_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking SNDFILE_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lsndfile 
checking for libmpg123 >= 1.16.0... yes
checking MPG123_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking MPG123_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lmpg123 
checking for shout >= 2.2.2... yes
checking SHOUT_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking SHOUT_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lshout 
checking for lame_init in -lmp3lame... yes
checking lame/lame.h usability... yes
checking lame/lame.h presence... yes
checking for lame/lame.h... yes
checking for libavcodec >= 53.35.0... yes
checking AVCODEC_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking AVCODEC_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lavcodec 
checking for x264 >= 0.142.2431... no
checking for libavformat >= 53.21.1... yes
checking AVFORMAT_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking AVFORMAT_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lavformat 
checking for libavutil >= 54.3.0... yes
checking AVUTIL_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking AVUTIL_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lavutil 
checking for libavresample >= 2.1.0... no
checking for libswresample >= 2.1.0... yes
checking SWRESAMPLE_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking SWRESAMPLE_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lswresample 
checking for libswscale >= 3.0.0... yes
checking SWSCALE_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking SWSCALE_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lswscale 
checking for libvlc >= 2.1.0... no
checking for opencv >= 2.4.5... no
checking for opusfile >= 0.5... yes
checking OPUSFILE_DECODE_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include/opus -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking OPUSFILE_DECODE_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lopusfile 
checking for libopusenc >= 0.1... yes
checking OPUSFILE_ENCODE_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include/opus 
checking OPUSFILE_ENCODE_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lopusenc 
checking for ImageMagick >= 6.0.0... no
checking for ImageMagick >= 7.0.0... no
checking for silk >= 1.0.8... no
checking for broadvoice >= 0.1.0... no
checking for ilbc2 >= 0.0.1... checking for ilbc >= 0.0.1... no
checking for g722_1 >= 0.2.0... no
checking for codec2 >= 0.5... checking for codec2_create in -lcodec2... no
checking for opus >= 1.1... yes
checking OPUS_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include/opus 
checking OPUS_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lopus 
checking for soundtouch >= 1.7.0... no
checking for flite >= 2... checking for flite_init in -lflite... no
checking for libmongoc-1.0 >= 1.0.8... no
checking for libmemcached >= 0.31... no
checking for v8-6.1_static >= 6.1.298... checking for v8fs_static >= 6.1.298... checking for v8 >= 6.1.298... no
checking for libks >= 1.1.0... yes
checking KS_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include/libks 
checking KS_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lks 
checking for signalwire_client >= 1.0.0... yes
checking SIGNALWIRE_CLIENT_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking SIGNALWIRE_CLIENT_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lsignalwire_client 
checking for librabbitmq >= 0.5.2... no
checking for libh2o-evloop >= 0.11.0... no
checking for libbrotlienc >= 0.1.0... no
checking for libbrotlidec >= 0.1.0... no
checking for tap >= 0.1.0... no
checking for libsmpp34 >= 1.10... no
checking for hiredis >= 0.10.0... yes
checking HIREDIS_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include/hiredis -D_FILE_OFFSET_BITS=64 
checking HIREDIS_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lhiredis 
checking for libedit >= 2.11... yes
checking LIBEDIT_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include -I/openwrt/staging_dir/target-x86_64_musl/usr/include/editline 
checking LIBEDIT_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -ledit 
checking for ldap_search in -lldap... yes
checking for ber_pvt_opt_on in -llber... yes
checking whether EL_PROMPT_ESC is declared... yes
checking whether EL_REFRESH is declared... yes
checking for el_wset... yes
checking for openssl... yes
checking openssl_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking openssl_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lssl -lcrypto 
  adding "-DHAVE_OPENSSL" to SWITCH_AM_CFLAGS
checking for SSL_CTX_set_tlsext_use_srtp in -lssl... yes
checking for DTLSv1_method in -lssl... yes
checking for DTLSv1_2_method in -lssl... yes
checking for JAVA installation at ... 
configure: cannot find the java directory, assuming it is specified in CFLAGS
checking if JAVA package is complete... no
checking for perl... (cached) false
checking for php... (cached) false
checking for php-config... (cached) false
configure: WARNING: python support disabled, building mod_python will fail!
checking for net-snmp-config... /openwrt/staging_dir/target-x86_64_musl/host/bin/net-snmp-config
checking for Net-SNMP libraries via net-snmp-config... checking for erl... /openwrt/staging_dir/hostpkg/bin/erl
checking erlang version... 11.0
checking erlang libdir... /openwrt/staging_dir/target-x86_64_musl/usr/lib
checking erlang incdir... /openwrt/staging_dir/target-x86_64_musl/usr/include
checking ei.h usability... yes
checking ei.h presence... yes
checking for ei.h... yes
checking for ei_encode_version in -lei... yes
checking for ei_link_unlink in -lei... no
configure: Your erlang seems OK, do not forget to enable mod_erlang_event in modules.conf
  setting CONFIGURE_CFLAGS to "-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include "
  setting CONFIGURE_CPPFLAGS to "-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include "
  setting CONFIGURE_CXXFLAGS to "-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include "
  setting CONFIGURE_LDFLAGS to "-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib "
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating src/include/switch_version.h.in
config.status: creating Makefile
config.status: creating build/Makefile
config.status: creating tests/unit/Makefile
config.status: creating src/Makefile
config.status: creating src/mod/Makefile
config.status: creating src/mod/applications/mod_abstraction/Makefile
config.status: creating src/mod/applications/mod_avmd/Makefile
config.status: creating src/mod/applications/mod_bert/Makefile
config.status: creating src/mod/applications/mod_blacklist/Makefile
config.status: creating src/mod/applications/mod_callcenter/Makefile
config.status: creating src/mod/applications/mod_cidlookup/Makefile
config.status: creating src/mod/applications/mod_cluechoo/Makefile
config.status: creating src/mod/applications/mod_commands/Makefile
config.status: creating src/mod/applications/mod_conference/Makefile
config.status: creating src/mod/applications/mod_curl/Makefile
config.status: creating src/mod/applications/mod_cv/Makefile
config.status: creating src/mod/applications/mod_db/Makefile
config.status: creating src/mod/applications/mod_directory/Makefile
config.status: creating src/mod/applications/mod_distributor/Makefile
config.status: creating src/mod/applications/mod_dptools/Makefile
config.status: creating src/mod/applications/mod_easyroute/Makefile
config.status: creating src/mod/applications/mod_enum/Makefile
config.status: creating src/mod/applications/mod_esf/Makefile
config.status: creating src/mod/applications/mod_esl/Makefile
config.status: creating src/mod/applications/mod_expr/Makefile
config.status: creating src/mod/applications/mod_fifo/Makefile
config.status: creating src/mod/applications/mod_fsk/Makefile
config.status: creating src/mod/applications/mod_fsv/Makefile
config.status: creating src/mod/applications/mod_hash/Makefile
config.status: creating src/mod/applications/mod_hiredis/Makefile
config.status: creating src/mod/applications/mod_httapi/Makefile
config.status: creating src/mod/applications/mod_http_cache/Makefile
config.status: creating src/mod/applications/mod_ladspa/Makefile
config.status: creating src/mod/applications/mod_lcr/Makefile
config.status: creating src/mod/applications/mod_limit/Makefile
config.status: creating src/mod/applications/mod_memcache/Makefile
config.status: creating src/mod/applications/mod_mongo/Makefile
config.status: creating src/mod/applications/mod_mp4/Makefile
config.status: creating src/mod/applications/mod_mp4v2/Makefile
config.status: creating src/mod/applications/mod_nibblebill/Makefile
config.status: creating src/mod/applications/mod_oreka/Makefile
config.status: creating src/mod/applications/mod_osp/Makefile
config.status: creating src/mod/applications/mod_prefix/Makefile
config.status: creating src/mod/applications/mod_rad_auth/Makefile
config.status: creating src/mod/applications/mod_random/Makefile
config.status: creating src/mod/applications/mod_redis/Makefile
config.status: creating src/mod/applications/mod_rss/Makefile
config.status: creating src/mod/applications/mod_skel/Makefile
config.status: creating src/mod/applications/mod_signalwire/Makefile
config.status: creating src/mod/applications/mod_sms/Makefile
config.status: creating src/mod/applications/mod_sms_flowroute/Makefile
config.status: creating src/mod/applications/mod_snapshot/Makefile
config.status: creating src/mod/applications/mod_snom/Makefile
config.status: creating src/mod/applications/mod_sonar/Makefile
config.status: creating src/mod/applications/mod_soundtouch/Makefile
config.status: creating src/mod/applications/mod_spandsp/Makefile
config.status: creating src/mod/applications/mod_spy/Makefile
config.status: creating src/mod/applications/mod_stress/Makefile
config.status: creating src/mod/applications/mod_test/Makefile
config.status: creating src/mod/applications/mod_translate/Makefile
config.status: creating src/mod/applications/mod_valet_parking/Makefile
config.status: creating src/mod/applications/mod_vmd/Makefile
config.status: creating src/mod/applications/mod_voicemail/Makefile
config.status: creating src/mod/applications/mod_voicemail_ivr/Makefile
config.status: creating src/mod/asr_tts/mod_cepstral/Makefile
config.status: creating src/mod/asr_tts/mod_flite/Makefile
config.status: creating src/mod/asr_tts/mod_pocketsphinx/Makefile
config.status: creating src/mod/asr_tts/mod_tts_commandline/Makefile
config.status: creating src/mod/asr_tts/mod_unimrcp/Makefile
config.status: creating src/mod/codecs/mod_amr/Makefile
config.status: creating src/mod/codecs/mod_amrwb/Makefile
config.status: creating src/mod/codecs/mod_b64/Makefile
config.status: creating src/mod/codecs/mod_bv/Makefile
config.status: creating src/mod/codecs/mod_clearmode/Makefile
config.status: creating src/mod/codecs/mod_codec2/Makefile
config.status: creating src/mod/codecs/mod_com_g729/Makefile
config.status: creating src/mod/codecs/mod_dahdi_codec/Makefile
config.status: creating src/mod/codecs/mod_g723_1/Makefile
config.status: creating src/mod/codecs/mod_g729/Makefile
config.status: creating src/mod/codecs/mod_h26x/Makefile
config.status: creating src/mod/codecs/mod_ilbc/Makefile
config.status: creating src/mod/codecs/mod_isac/Makefile
config.status: creating src/mod/codecs/mod_mp4v/Makefile
config.status: creating src/mod/codecs/mod_opus/Makefile
config.status: creating src/mod/codecs/mod_openh264/Makefile
config.status: creating src/mod/codecs/mod_sangoma_codec/Makefile
config.status: creating src/mod/codecs/mod_silk/Makefile
config.status: creating src/mod/codecs/mod_siren/Makefile
config.status: creating src/mod/codecs/mod_skel_codec/Makefile
config.status: creating src/mod/codecs/mod_theora/Makefile
config.status: creating src/mod/databases/mod_mariadb/Makefile
config.status: creating src/mod/databases/mod_pgsql/Makefile
config.status: creating src/mod/dialplans/mod_dialplan_asterisk/Makefile
config.status: creating src/mod/dialplans/mod_dialplan_directory/Makefile
config.status: creating src/mod/dialplans/mod_dialplan_xml/Makefile
config.status: creating src/mod/directories/mod_ldap/Makefile
config.status: creating src/mod/endpoints/mod_alsa/Makefile
config.status: creating src/mod/endpoints/mod_dingaling/Makefile
config.status: creating src/mod/endpoints/mod_gsmopen/Makefile
config.status: creating src/mod/endpoints/mod_h323/Makefile
config.status: creating src/mod/endpoints/mod_khomp/Makefile
config.status: creating src/mod/endpoints/mod_loopback/Makefile
config.status: creating src/mod/endpoints/mod_opal/Makefile
config.status: creating src/mod/endpoints/mod_portaudio/Makefile
config.status: creating src/mod/endpoints/mod_reference/Makefile
config.status: creating src/mod/endpoints/mod_rtmp/Makefile
config.status: creating src/mod/endpoints/mod_skinny/Makefile
config.status: creating src/mod/endpoints/mod_sofia/Makefile
config.status: creating src/mod/endpoints/mod_unicall/Makefile
config.status: creating src/mod/endpoints/mod_rtc/Makefile
config.status: creating src/mod/endpoints/mod_verto/Makefile
config.status: creating src/mod/event_handlers/mod_amqp/Makefile
config.status: creating src/mod/event_handlers/mod_cdr_csv/Makefile
config.status: creating src/mod/event_handlers/mod_cdr_mongodb/Makefile
config.status: creating src/mod/event_handlers/mod_cdr_pg_csv/Makefile
config.status: creating src/mod/event_handlers/mod_cdr_sqlite/Makefile
config.status: creating src/mod/event_handlers/mod_erlang_event/Makefile
config.status: creating src/mod/event_handlers/mod_event_multicast/Makefile
config.status: creating src/mod/event_handlers/mod_event_socket/Makefile
config.status: creating src/mod/event_handlers/mod_event_test/Makefile
config.status: creating src/mod/event_handlers/mod_fail2ban/Makefile
config.status: creating src/mod/event_handlers/mod_format_cdr/Makefile
config.status: creating src/mod/event_handlers/mod_json_cdr/Makefile
config.status: creating src/mod/event_handlers/mod_kazoo/Makefile
config.status: creating src/mod/event_handlers/mod_radius_cdr/Makefile
config.status: creating src/mod/event_handlers/mod_odbc_cdr/Makefile
config.status: creating src/mod/event_handlers/mod_rayo/Makefile
config.status: creating src/mod/event_handlers/mod_smpp/Makefile
config.status: creating src/mod/event_handlers/mod_snmp/Makefile
config.status: creating src/mod/event_handlers/mod_event_zmq/Makefile
config.status: creating src/mod/formats/mod_imagick/Makefile
config.status: creating src/mod/formats/mod_local_stream/Makefile
config.status: creating src/mod/formats/mod_native_file/Makefile
config.status: creating src/mod/formats/mod_opusfile/Makefile
config.status: creating src/mod/formats/mod_png/Makefile
config.status: creating src/mod/formats/mod_shell_stream/Makefile
config.status: creating src/mod/formats/mod_shout/Makefile
config.status: creating src/mod/formats/mod_sndfile/Makefile
config.status: creating src/mod/formats/mod_ssml/Makefile
config.status: creating src/mod/formats/mod_tone_stream/Makefile
config.status: creating src/mod/formats/mod_vlc/Makefile
config.status: creating src/mod/formats/mod_portaudio_stream/Makefile
config.status: creating src/mod/languages/mod_java/Makefile
config.status: creating src/mod/languages/mod_lua/Makefile
config.status: creating src/mod/languages/mod_managed/Makefile
config.status: creating src/mod/languages/mod_perl/Makefile
config.status: creating src/mod/languages/mod_python/Makefile
config.status: creating src/mod/languages/mod_v8/Makefile
config.status: creating src/mod/languages/mod_yaml/Makefile
config.status: creating src/mod/languages/mod_basic/Makefile
config.status: creating src/mod/loggers/mod_console/Makefile
config.status: creating src/mod/loggers/mod_graylog2/Makefile
config.status: creating src/mod/loggers/mod_logfile/Makefile
config.status: creating src/mod/loggers/mod_syslog/Makefile
config.status: creating src/mod/loggers/mod_raven/Makefile
config.status: creating src/mod/say/mod_say_de/Makefile
config.status: creating src/mod/say/mod_say_en/Makefile
config.status: creating src/mod/say/mod_say_es/Makefile
config.status: creating src/mod/say/mod_say_es_ar/Makefile
config.status: creating src/mod/say/mod_say_fa/Makefile
config.status: creating src/mod/say/mod_say_fr/Makefile
config.status: creating src/mod/say/mod_say_he/Makefile
config.status: creating src/mod/say/mod_say_hr/Makefile
config.status: creating src/mod/say/mod_say_hu/Makefile
config.status: creating src/mod/say/mod_say_it/Makefile
config.status: creating src/mod/say/mod_say_ja/Makefile
config.status: creating src/mod/say/mod_say_nl/Makefile
config.status: creating src/mod/say/mod_say_pl/Makefile
config.status: creating src/mod/say/mod_say_pt/Makefile
config.status: creating src/mod/say/mod_say_ru/Makefile
config.status: creating src/mod/say/mod_say_sv/Makefile
config.status: creating src/mod/say/mod_say_th/Makefile
config.status: creating src/mod/say/mod_say_zh/Makefile
config.status: creating src/mod/timers/mod_posix_timer/Makefile
config.status: creating src/mod/timers/mod_timerfd/Makefile
config.status: creating src/mod/xml_int/mod_xml_cdr/Makefile
config.status: creating src/mod/xml_int/mod_xml_curl/Makefile
config.status: creating src/mod/xml_int/mod_xml_ldap/Makefile
config.status: creating src/mod/xml_int/mod_xml_radius/Makefile
config.status: creating src/mod/xml_int/mod_xml_rpc/Makefile
config.status: creating src/mod/xml_int/mod_xml_scgi/Makefile
config.status: creating src/mod/applications/mod_av/Makefile
config.status: creating src/mod/applications/mod_video_filter/Makefile
config.status: creating src/include/switch_am_config.h
config.status: creating build/getsounds.sh
config.status: creating build/getlib.sh
config.status: creating build/getg729.sh
config.status: creating build/freeswitch.pc
config.status: creating build/standalone_module/freeswitch.pc
config.status: creating build/modmake.rules
config.status: creating libs/esl/Makefile
config.status: creating libs/esl/perl/Makefile
config.status: creating libs/esl/php/Makefile
config.status: creating libs/xmlrpc-c/include/xmlrpc-c/config.h
config.status: creating libs/xmlrpc-c/xmlrpc_config.h
config.status: creating libs/xmlrpc-c/config.mk
config.status: creating libs/xmlrpc-c/srcdir.mk
config.status: creating libs/xmlrpc-c/stamp-h
config.status: creating scripts/gentls_cert
config.status: creating src/include/switch_private.h
config.status: creating libs/esl/src/include/esl_config_auto.h
config.status: creating libs/xmlrpc-c/xmlrpc_amconfig.h
config.status: executing depfiles commands
config.status: executing libtool commands
=== configuring in libs/srtp (/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release/libs/srtp)
configure: running /bin/bash ./configure.gnu --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '--disable-dependency-tracking' '--disable-static' '--disable-system-xmlrpc-c' '--enable-core-libedit-support' '--enable-fhs' '--with-cachedir=/tmp/freeswitch/cache' '--with-dbdir=/tmp/freeswitch/db' '--with-imagesdir=/usr/share/freeswitch/images' '--with-logfiledir=/tmp/freeswitch/log' '--with-python=no' '--with-recordingsdir=/tmp/freeswitch/recordings' '--with-storagedir=/tmp/freeswitch/storage' '--disable-debug' '--enable-libyuv' '--enable-core-odbc-support' '--enable-srtp' '--enable-libvpx' '--enable-zrtp' '--with-odbc-lib=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-odbc=/openwrt/staging_dir/target-x86_64_musl/usr' '--with-libpri=/openwrt/staging_dir/target-x86_64_musl/usr' '--with-pritap' '--without-pgsql' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib ' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' '--with-modinstdir=/usr/lib/freeswitch/mod' 'CONFIGURE_CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib ' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
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
checking for style of include used by make... GNU
checking dependency style of ccache_cc... none
checking for gawk... (cached) gawk
checking whether make sets $(MAKE)... (cached) yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld -m elf_x86_64
checking if the linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... x86_64-openwrt-linux-musl-gcc-nm
checking the name lister (x86_64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 1572864
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to x86_64-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for x86_64-openwrt-linux-musl-ld -m elf_x86_64 option to reload object files... -r
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
checking whether the ccache_cc linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64 -m elf_x86_64) supports shared libraries... yes
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... no
checking whether to build static libraries... yes
checking for C compiler vendor... gnu
checking whether to build for Linux kernel context... no
checking for /dev/urandom... (cached) yes
checking for ANSI C header files... (cached) yes
checking for stdlib.h... (cached) yes
checking for unistd.h... (cached) yes
checking for stdint.h... (cached) yes
checking sys/uio.h usability... yes
checking sys/uio.h presence... yes
checking for sys/uio.h... yes
checking for inttypes.h... (cached) yes
checking for sys/types.h... (cached) yes
checking machine/types.h usability... no
checking machine/types.h presence... no
checking for machine/types.h... no
checking sys/int_types.h usability... no
checking sys/int_types.h presence... no
checking for sys/int_types.h... no
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking windows.h usability... no
checking windows.h presence... no
checking for windows.h... no
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking for int8_t... yes
checking for uint8_t... yes
checking for int16_t... yes
checking for uint16_t... yes
checking for int32_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking size of unsigned long... (cached) 8
checking size of unsigned long long... (cached) 8
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking for size_t... yes
checking for socket... yes
checking for inet_aton... yes
checking for usleep... yes
checking for sigaction... yes
checking whether byte ordering is bigendian... (cached) no
checking whether to compile in debugging... no
checking whether to use ISMAcryp code... no
checking whether to leverage OpenSSL crypto... yes
checking for EVP_EncryptInit in -lcrypto... yes
checking for EVP_aes_128_ctr in -lcrypto... yes
checking for EVP_aes_128_gcm in -lcrypto... yes
yes
checking whether to use syslog for error reporting... no
checking whether to use stdout for error reporting... yes
checking whether to use /dev/console for error reporting... no
checking whether to use GDOI key management... no
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating crypto/Makefile
config.status: creating doc/Makefile
config.status: creating test/Makefile
config.status: creating libsrtp2.pc
config.status: creating crypto/include/config.h
config.status: executing depfiles commands
config.status: executing libtool commands
=== configuring in libs/apr (/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release/libs/apr)
configure: running /bin/bash ./configure.gnu --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '--disable-dependency-tracking' '--disable-static' '--disable-system-xmlrpc-c' '--enable-core-libedit-support' '--enable-fhs' '--with-cachedir=/tmp/freeswitch/cache' '--with-dbdir=/tmp/freeswitch/db' '--with-imagesdir=/usr/share/freeswitch/images' '--with-logfiledir=/tmp/freeswitch/log' '--with-python=no' '--with-recordingsdir=/tmp/freeswitch/recordings' '--with-storagedir=/tmp/freeswitch/storage' '--disable-debug' '--enable-libyuv' '--enable-core-odbc-support' '--enable-srtp' '--enable-libvpx' '--enable-zrtp' '--with-odbc-lib=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-odbc=/openwrt/staging_dir/target-x86_64_musl/usr' '--with-libpri=/openwrt/staging_dir/target-x86_64_musl/usr' '--with-pritap' '--without-pgsql' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib ' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' '--with-modinstdir=/usr/lib/freeswitch/mod' 'CONFIGURE_CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib ' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking target system type... x86_64-openwrt-linux-gnu
Configuring APR library
Platform: x86_64-openwrt-linux-gnu
checking for working mkdir -p... yes
APR Version: 1.2.8
checking for chosen layout... apr
checking for x86_64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking for C compiler vendor... gnu
Applying APR hints file rules for x86_64-openwrt-linux-gnu
  adding "-D_REENTRANT" to CPPFLAGS
  adding "-D_GNU_SOURCE" to CPPFLAGS
(Default will be unix)
checking whether make sets $(MAKE)... yes
checking how to run the C preprocessor... ccache_cc -E
checking for gawk... gawk
checking whether ln -s works... yes
checking for x86_64-openwrt-linux-ranlib... x86_64-openwrt-linux-musl-gcc-ranlib
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking for rm... rm
checking for as... ccache_cc -c -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include
checking for cpp... cpp
checking for x86_64-openwrt-linux-ar... x86_64-openwrt-linux-musl-gcc-ar
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
checking for library containing strerror... none required
checking whether system uses EBCDIC... no
performing libtool configuration...
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld -m elf_x86_64
checking if the linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... x86_64-openwrt-linux-musl-gcc-nm
checking the name lister (x86_64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking the maximum length of command line arguments... 1572864
checking how to convert x86_64-pc-linux-gnu file names to x86_64-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for x86_64-openwrt-linux-musl-ld -m elf_x86_64 option to reload object files... -r
checking for x86_64-openwrt-linux-objdump... x86_64-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for x86_64-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for x86_64-openwrt-linux-ar... (cached) x86_64-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for x86_64-openwrt-linux-ranlib... (cached) x86_64-openwrt-linux-musl-gcc-ranlib
checking command to parse x86_64-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for a working dd... /usr/bin/dd
checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1
checking for x86_64-openwrt-linux-mt... no
checking for mt... no
checking if : is a manifest tool... no
checking for dlfcn.h... yes
checking for objdir... .libs
checking if ccache_cc supports -fno-rtti -fno-exceptions... no
checking for ccache_cc option to produce PIC... -fPIC -DPIC
checking if ccache_cc PIC flag -fPIC -DPIC works... yes
checking if ccache_cc static flag -static works... yes
checking if ccache_cc supports -c -o file.o... rm: cannot remove 'conftest*': No such file or directory
yes
checking if ccache_cc supports -c -o file.o... (cached) yes
checking whether the ccache_cc linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64 -m elf_x86_64) supports shared libraries... yes
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... no
checking whether to build static libraries... yes
grep: /openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release/libs/apr/libtool: No such file or directory

Check for compiler flags...
  adding "-g" to CFLAGS
  adding "-Wall" to CFLAGS
checking whether to enable -D_LARGEFILE64_SOURCE... no

Checking for libraries...
checking for library containing gethostbyname... none required
checking for library containing gethostname... none required
checking for library containing socket... none required
checking for library containing crypt... none required
checking for main in -ltruerand... no
checking for library containing modf... none required
checking for dlopen in -ldl... yes

Checking for Threads...
checking pthread.h usability... yes
checking pthread.h presence... yes
checking for pthread.h... yes
checking for CFLAGS needed for pthreads... 
checking for LIBS needed for pthreads... (cached) -lpthread
  adding "-lpthread" to LIBS
checking for pthread.h... (cached) yes
checking whether pthread_getspecific takes two arguments... no
checking whether pthread_attr_getdetachstate takes one argument... no
checking for recursive mutex support... (cached) yes
checking for pthread_key_delete... (cached) yes
checking for pthread_rwlock_init... (cached) yes
checking for pthread_attr_setguardsize... yes
checking for pthread_rwlock_t... (cached) yes
APR will use threads
checking for readdir in -lc_r... no
checking for gethostbyname in -lc_r... no
checking for gethostbyaddr in -lc_r... no
checking for gethostbyname_r... yes
checking for gethostbyaddr_r... yes
checking for sigsuspend... yes
checking for sigwait... yes
checking for poll... yes
checking for kqueue... no
checking for port_create... no
checking for epoll support... (cached) yes
checking for getpwnam_r... yes
checking for getpwuid_r... (cached) yes
checking for getgrnam_r... yes
checking for getgrgid_r... yes

Checking for Shared Memory Support...
checking for library containing shm_open... none required
checking for sys/types.h... (cached) yes
checking sys/mman.h usability... yes
checking sys/mman.h presence... yes
checking for sys/mman.h... yes
checking sys/ipc.h usability... yes
checking sys/ipc.h presence... yes
checking for sys/ipc.h... yes
checking sys/mutex.h usability... no
checking sys/mutex.h presence... no
checking for sys/mutex.h... no
checking sys/shm.h usability... yes
checking sys/shm.h presence... yes
checking for sys/shm.h... yes
checking sys/file.h usability... yes
checking sys/file.h presence... yes
checking for sys/file.h... yes
checking kernel/OS.h usability... no
checking kernel/OS.h presence... no
checking for kernel/OS.h... no
checking os2.h usability... no
checking os2.h presence... no
checking for os2.h... no
checking for mmap... yes
checking for munmap... yes
checking for shm_open... yes
checking for shm_unlink... yes
checking for shmget... yes
checking for shmat... yes
checking for shmdt... yes
checking for shmctl... yes
checking for create_area... no
checking for MAP_ANON in sys/mman.h... yes
checking for /dev/zero... (cached) yes
checking for mmap that can map /dev/zero... no
decision on anonymous shared memory allocation method... 4.4BSD-style mmap() via MAP_ANON
decision on namebased memory allocation method... SysV IPC shmget()
checking for alloca... no
checking for calloc... yes
checking for setsid... yes
checking for isinf... no
checking for isnan... no
checking for getenv... yes
checking for putenv... yes
checking for setenv... yes
checking for unsetenv... yes
checking for writev... yes
checking for getifaddrs... yes
checking for utime... yes
checking for utimes... (cached) yes
checking for setrlimit... yes
checking for getrlimit... yes
checking for sendfilev in -lsendfile... no
checking for sendfile... yes
checking for send_file... no
checking for sendfilev... no
checking for sigaction... yes
checking whether sys_siglist is declared... (cached) no
checking for fork... yes
checking for inet_addr... yes
checking for inet_network... yes
checking for _getch... no
checking for strerror_r... yes
checking whether return code from strerror_r has type int... (cached) yes
checking for mmap... (cached) yes
checking for memmove... yes
checking for getpass... yes
checking for getpassphrase... no
checking for gmtime_r... yes
checking for localtime_r... yes
checking for mkstemp... yes
checking whether sigwait takes one argument... no
checking for inode member of struct dirent... d_fileno
checking for file type member of struct dirent... d_type
checking for ANSI C header files... (cached) yes
checking alloca.h usability... yes
checking alloca.h presence... yes
checking for alloca.h... yes
checking ByteOrder.h usability... no
checking ByteOrder.h presence... no
checking for ByteOrder.h... no
checking conio.h usability... no
checking conio.h presence... no
checking for conio.h... no
checking crypt.h usability... yes
checking crypt.h presence... yes
checking for crypt.h... yes
checking ctype.h usability... yes
checking ctype.h presence... yes
checking for ctype.h... yes
checking dir.h usability... no
checking dir.h presence... no
checking for dir.h... no
checking dirent.h usability... yes
checking dirent.h presence... yes
checking for dirent.h... yes
checking dl.h usability... no
checking dl.h presence... no
checking for dl.h... no
checking for dlfcn.h... (cached) yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking grp.h usability... yes
checking grp.h presence... yes
checking for grp.h... yes
checking io.h usability... no
checking io.h presence... no
checking for io.h... no
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking mach-o/dyld.h usability... no
checking mach-o/dyld.h presence... no
checking for mach-o/dyld.h... no
checking malloc.h usability... yes
checking malloc.h presence... yes
checking for malloc.h... yes
checking for memory.h... (cached) yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking osreldate.h usability... no
checking osreldate.h presence... no
checking for osreldate.h... no
checking poll.h usability... yes
checking poll.h presence... yes
checking for poll.h... yes
checking process.h usability... no
checking process.h presence... no
checking for process.h... no
checking pwd.h usability... yes
checking pwd.h presence... yes
checking for pwd.h... yes
checking semaphore.h usability... yes
checking semaphore.h presence... yes
checking for semaphore.h... yes
checking signal.h usability... yes
checking signal.h presence... yes
checking for signal.h... yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking stdio.h usability... yes
checking stdio.h presence... yes
checking for stdio.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking for strings.h... (cached) yes
checking sysapi.h usability... no
checking sysapi.h presence... no
checking for sysapi.h... no
checking sysgtime.h usability... no
checking sysgtime.h presence... no
checking for sysgtime.h... no
checking termios.h usability... yes
checking termios.h presence... yes
checking for termios.h... yes
checking time.h usability... yes
checking time.h presence... yes
checking for time.h... yes
checking tpfeq.h usability... no
checking tpfeq.h presence... no
checking for tpfeq.h... no
checking tpfio.h usability... no
checking tpfio.h presence... no
checking for tpfio.h... no
checking for unistd.h... (cached) yes
checking unix.h usability... no
checking unix.h presence... no
checking for unix.h... no
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking for kernel/OS.h... (cached) no
checking net/errno.h usability... no
checking net/errno.h presence... no
checking for net/errno.h... no
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking for netinet/sctp.h... (cached) no
checking for netinet/sctp_uio.h... (cached) no
checking for sys/file.h... (cached) yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking for sys/mman.h... (cached) yes
checking sys/poll.h usability... yes
checking sys/poll.h presence... yes
checking for sys/poll.h... yes
checking sys/resource.h usability... yes
checking sys/resource.h presence... yes
checking for sys/resource.h... yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking sys/sem.h usability... yes
checking sys/sem.h presence... yes
checking for sys/sem.h... yes
checking sys/sendfile.h usability... yes
checking sys/sendfile.h presence... yes
checking for sys/sendfile.h... yes
checking sys/signal.h usability... yes
checking sys/signal.h presence... yes
checking for sys/signal.h... yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking sys/sockio.h usability... no
checking sys/sockio.h presence... no
checking for sys/sockio.h... no
checking for sys/stat.h... (cached) yes
checking sys/sysctl.h usability... no
checking sys/sysctl.h presence... no
checking for sys/sysctl.h... no
checking sys/syslimits.h usability... no
checking sys/syslimits.h presence... no
checking for sys/syslimits.h... no
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking for sys/types.h... (cached) yes
checking sys/uio.h usability... yes
checking sys/uio.h presence... yes
checking for sys/uio.h... yes
checking sys/un.h usability... yes
checking sys/un.h presence... yes
checking for sys/un.h... yes
checking sys/wait.h usability... yes
checking sys/wait.h presence... yes
checking for sys/wait.h... yes
checking for netinet/tcp.h... yes
checking for h_errno in netdb.h... yes
checking for off_t... yes
checking for pid_t... yes
checking for size_t... yes
checking for uid_t in sys/types.h... yes
checking for ssize_t... yes
checking for inline... inline
checking for an ANSI C-conforming const... yes
checking whether setpgrp takes no argument... (cached) yes
checking for socklen_t... yes
checking size of void*... 8
checking size of char... (cached) 1
checking size of int... (cached) 4
checking size of long... (cached) 8
checking size of short... (cached) 2
checking size of long long... (cached) 8
checking for INT64_C... yes
checking size of ssize_t... (cached) 8
checking size of size_t... (cached) 8
checking size of off_t... (cached) 8
checking which type to use for apr_off_t... off_t
checking size of pid_t... 8
checking whether byte ordering is bigendian... (cached) no
checking for strnicmp... no
checking for strncasecmp... yes
checking for stricmp... no
checking for strcasecmp... yes
checking for strdup... yes
checking for strstr... yes
checking for memchr... yes
checking for strtol... yes

Checking for DSO...
checking for NSLinkModule... no
checking for shl_load in -ldld... no
checking for dlopen... yes
checking for dlsym... yes

Checking for Processes...
checking for waitpid... yes
checking for Variable Length Arrays... yes
checking struct rlimit... (cached) yes

Checking for Locking...
checking for semget... yes
checking for semctl... yes
checking for flock... yes
checking for semaphore.h... (cached) yes
checking OS.h usability... no
checking OS.h presence... no
checking for OS.h... no
checking for sem_close... yes
checking for sem_unlink... yes
checking for sem_post... yes
checking for sem_wait... yes
checking for create_sem... no
checking for working sem_open... (cached) yes
checking for union semun in sys/sem.h... no
checking for LOCK_EX in sys/file.h... yes
checking for F_SETLK in fcntl.h... yes
checking for SEM_UNDO in sys/sem.h... yes
checking for POLLIN in poll.h sys/poll.h... yes
checking for PTHREAD_PROCESS_SHARED in pthread.h... yes
checking for pthread_mutexattr_setpshared... yes
checking for pthread_setschedparam in -lpthread... yes
checking for working PROCESS_SHARED locks... (cached) yes
checking for robust cross-process mutex support... (cached) no
decision on apr_lock implementation method... SysV IPC semget()
checking if all interprocess locks affect threads... no
checking if POSIX sems affect threads in the same process... no
checking if SysV sems affect threads in the same process... no
checking if fcntl locks affect threads in the same process... no
checking if flock locks affect threads in the same process... no
checking for entropy source... /dev/random

Checking for OS UUID Support...
checking uuid.h usability... no
checking uuid.h presence... no
checking for uuid.h... no
checking uuid/uuid.h usability... yes
checking uuid/uuid.h presence... yes
checking for uuid/uuid.h... yes
checking for library containing uuid_create... no
checking for library containing uuid_generate... -luuid
checking for uuid_create... no
checking for uuid_generate... yes
checking for os uuid usability... yes

Checking for Time Support...
checking for struct tm.tm_gmtoff... yes
checking for struct tm.__tm_gmtoff... yes

Checking for Networking support...
checking for in_addr in netinet/in.h... yes
checking if fd == socket on this platform... yes
checking style of gethostbyname_r routine... glibc2
checking 3rd argument to the gethostbyname_r routines... char
checking if TCP_NODELAY setting is inherited from listening sockets... yes
checking if O_NONBLOCK setting is inherited from listening sockets... (cached) no
checking whether TCP_NODELAY and TCP_CORK can both be enabled... (cached) yes
checking for TCP_CORK in netinet/tcp.h... yes
checking for TCP_NOPUSH in netinet/tcp.h... no
checking for SO_ACCEPTFILTER in sys/socket.h... no
checking whether SCTP is supported... no
checking for struct ip_mreq... yes
checking for set_h_errno... no

Checking for IPv6 Networking support...
checking for library containing getaddrinfo... none required
checking for library containing gai_strerror... none required
checking for library containing getnameinfo... none required
checking for gai_strerror... yes
checking for working getaddrinfo... yes
checking for negative error codes for getaddrinfo... (cached) yes
checking for working getnameinfo... yes
checking for sockaddr_in6... yes
checking for sockaddr_storage... yes
checking for working AI_ADDRCONFIG... (cached) yes
checking if APR supports IPv6... yes
checking langinfo.h usability... yes
checking langinfo.h presence... yes
checking for langinfo.h... yes
checking for nl_langinfo... yes

Restore user-defined environment settings...
  restoring CPPFLAGS to "-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include "
  setting EXTRA_CPPFLAGS to "-D_REENTRANT -D_GNU_SOURCE"
  restoring CFLAGS to "-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include "
  setting EXTRA_CFLAGS to "-g -Wall"
  restoring LDFLAGS to "-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib "
  setting EXTRA_LDFLAGS to ""
  restoring LIBS to ""
  setting EXTRA_LIBS to "-luuid -ldl  -lpthread"
  restoring INCLUDES to ""
  setting EXTRA_INCLUDES to ""
configure: creating ./config.status
config.status: creating Makefile
config.status: creating include/apr.h
config.status: creating build/apr_rules.mk
config.status: creating build/pkg/pkginfo
config.status: creating apr-1-config
config.status: WARNING:  'apr-config.in' seems to ignore the --datarootdir setting
config.status: creating apr.pc
config.status: creating test/Makefile
config.status: creating test/internal/Makefile
config.status: creating include/arch/unix/apr_private.h
config.status: executing libtool commands
rm: cannot remove 'libtoolT': No such file or directory
config.status: executing default commands
=== configuring in libs/apr-util (/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release/libs/apr-util)
configure: running /bin/bash ./configure.gnu --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '--disable-dependency-tracking' '--disable-static' '--disable-system-xmlrpc-c' '--enable-core-libedit-support' '--enable-fhs' '--with-cachedir=/tmp/freeswitch/cache' '--with-dbdir=/tmp/freeswitch/db' '--with-imagesdir=/usr/share/freeswitch/images' '--with-logfiledir=/tmp/freeswitch/log' '--with-python=no' '--with-recordingsdir=/tmp/freeswitch/recordings' '--with-storagedir=/tmp/freeswitch/storage' '--disable-debug' '--enable-libyuv' '--enable-core-odbc-support' '--enable-srtp' '--enable-libvpx' '--enable-zrtp' '--with-odbc-lib=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-odbc=/openwrt/staging_dir/target-x86_64_musl/usr' '--with-libpri=/openwrt/staging_dir/target-x86_64_musl/usr' '--with-pritap' '--without-pgsql' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib ' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' '--with-modinstdir=/usr/lib/freeswitch/mod' 'CONFIGURE_CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib ' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking target system type... x86_64-openwrt-linux-gnu
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking for working mkdir -p... yes
APR-util Version: 1.2.8
checking for chosen layout... apr-util
Applying apr-util hints file rules for x86_64-openwrt-linux-gnu
checking for APR... yes
  setting CPP to "ccache_cc -E"
  adding "-g" to CFLAGS
  adding "-Wall" to CFLAGS
  adding "-D_REENTRANT" to CPPFLAGS
  adding "-D_GNU_SOURCE" to CPPFLAGS
checking for x86_64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
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
checking for ldap support...
checking for default DBM... sdbm (default)
checking for dbd/apr_dbd_mysql.c... (cached) no
checking for Expat in xml/expat... yes
configuring package in xml/expat now
configure: loading site script /openwrt/include/site/x86_64
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking target system type... x86_64-openwrt-linux-gnu
checking how to print strings... printf
checking for x86_64-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld -m elf_x86_64
checking if the linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... x86_64-openwrt-linux-musl-gcc-nm
checking the name lister (x86_64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 1572864
checking how to convert x86_64-pc-linux-gnu file names to x86_64-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for x86_64-openwrt-linux-musl-ld -m elf_x86_64 option to reload object files... -r
checking for x86_64-openwrt-linux-objdump... x86_64-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for x86_64-openwrt-linux-dlltool... dlltool
checking how to associate runtime and link libraries... printf %s\n
checking for x86_64-openwrt-linux-ar... x86_64-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for x86_64-openwrt-linux-ranlib... x86_64-openwrt-linux-musl-gcc-ranlib
checking for gawk... gawk
checking command to parse x86_64-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for a working dd... /usr/bin/dd
checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1
checking for x86_64-openwrt-linux-mt... no
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
checking whether the ccache_cc linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64 -m elf_x86_64) supports shared libraries... yes
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... no
checking whether to build static libraries... yes
checking for x86_64-openwrt-linux-gcc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking for ANSI C header files... (cached) yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking for unistd.h... (cached) yes
checking for string.h... (cached) yes
checking for an ANSI C-conforming const... yes
checking for off_t... yes
checking for size_t... yes
checking for working memcmp... (cached) yes
checking for stdlib.h... (cached) yes
checking for unistd.h... (cached) yes
checking for sys/param.h... yes
checking for getpagesize... yes
checking for working mmap... (cached) yes
checking for memmove... yes
checking for bcopy... (cached) yes
configure: creating ./config.status
config.status: creating Makefile
config.status: WARNING:  'Makefile.in' seems to ignore the --datarootdir setting
config.status: creating lib/Makefile
config.status: WARNING:  'lib/Makefile.in' seems to ignore the --datarootdir setting
config.status: creating lib/expat.h
config.status: creating config.h
config.status: executing libtool commands
xml/expat configured properly
  setting APRUTIL_EXPORT_LIBS to "/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release/libs/apr-util/xml/expat/lib/libexpat.la"
  setting APRUTIL_INCLUDES to "-I/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release/libs/apr-util/xml/expat/lib"
  setting APRUTIL_LDFLAGS to "-L/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release/libs/apr-util/xml/expat/lib"
  setting APRUTIL_LIBS to "/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release/libs/apr-util/xml/expat/lib/libexpat.la"
checking iconv.h usability... yes
checking iconv.h presence... yes
checking for iconv.h... yes
  setting LIBS to "-liconv"
  adding "-liconv" to APRUTIL_LIBS
  adding "-liconv" to APRUTIL_EXPORT_LIBS
  nulling LIBS
checking for type of inbuf parameter to iconv... char **
checking for iconv.h... (cached) yes
checking langinfo.h usability... yes
checking langinfo.h presence... yes
checking for langinfo.h... yes
checking for nl_langinfo... yes
checking for CODESET in langinfo.h... yes
checking for library containing crypt... none required
checking if system crypt() function is threadsafe... no
checking for crypt_r... yes
checking style of crypt_r... struct_crypt_data
  adding "/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release/libs/apr/libapr-1.la" to APRUTIL_LIBS
  adding "-luuid" to APRUTIL_LIBS
  adding "-ldl" to APRUTIL_LIBS
  adding "-lpthread" to APRUTIL_LIBS
configure: creating ./config.status
config.status: creating Makefile
config.status: creating export_vars.sh
config.status: creating build/pkg/pkginfo
config.status: creating apr-util.pc
config.status: creating apu-1-config
config.status: creating include/private/apu_select_dbm.h
config.status: creating include/apr_ldap.h
config.status: creating include/apu.h
config.status: creating include/apu_want.h
config.status: creating test/Makefile
config.status: creating include/private/apu_config.h
config.status: executing default commands
=== configuring in libs/iksemel (/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release/libs/iksemel)
configure: running /bin/bash ./configure.gnu --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '--disable-dependency-tracking' '--disable-static' '--disable-system-xmlrpc-c' '--enable-core-libedit-support' '--enable-fhs' '--with-cachedir=/tmp/freeswitch/cache' '--with-dbdir=/tmp/freeswitch/db' '--with-imagesdir=/usr/share/freeswitch/images' '--with-logfiledir=/tmp/freeswitch/log' '--with-python=no' '--with-recordingsdir=/tmp/freeswitch/recordings' '--with-storagedir=/tmp/freeswitch/storage' '--disable-debug' '--enable-libyuv' '--enable-core-odbc-support' '--enable-srtp' '--enable-libvpx' '--enable-zrtp' '--with-odbc-lib=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-odbc=/openwrt/staging_dir/target-x86_64_musl/usr' '--with-libpri=/openwrt/staging_dir/target-x86_64_musl/usr' '--with-pritap' '--without-pgsql' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib ' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' '--with-modinstdir=/usr/lib/freeswitch/mod' 'CONFIGURE_CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib ' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
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
checking for style of include used by make... GNU
checking dependency style of ccache_cc... none
checking for x86_64-openwrt-linux-objdump... x86_64-openwrt-linux-musl-objdump
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld -m elf_x86_64
checking if the linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... x86_64-openwrt-linux-musl-gcc-nm
checking the name lister (x86_64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 1572864
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to x86_64-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for x86_64-openwrt-linux-musl-ld -m elf_x86_64 option to reload object files... -r
checking for x86_64-openwrt-linux-objdump... (cached) x86_64-openwrt-linux-musl-objdump
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
checking whether the ccache_cc linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64 -m elf_x86_64) supports shared libraries... yes
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... no
checking whether to build static libraries... yes
checking for ANSI C header files... (cached) yes
checking for unistd.h... (cached) yes
checking for strings.h... (cached) yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking for size_t... yes
checking for struct stat.st_blksize... yes
checking for library containing recv... none required
checking for getopt_long... yes
checking for getaddrinfo... (cached) yes
checking for openssl... yes
checking openssl_CFLAGS... -I/openwrt/staging_dir/target-x86_64_musl/usr/include 
checking openssl_LIBS... -L/openwrt/staging_dir/target-x86_64_musl/usr/lib -lssl -lcrypto 
checking for C compiler vendor... gnu
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating iksemel.pc
config.status: creating src/Makefile
config.status: creating include/Makefile
config.status: creating tools/Makefile
config.status: creating test/Makefile
config.status: creating doc/Makefile
config.status: creating include/config.h
config.status: executing depfiles commands
config.status: executing libtool commands
=== configuring in libs/libdingaling (/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release/libs/libdingaling)
configure: running /bin/bash ./configure.gnu --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '--disable-dependency-tracking' '--disable-static' '--disable-system-xmlrpc-c' '--enable-core-libedit-support' '--enable-fhs' '--with-cachedir=/tmp/freeswitch/cache' '--with-dbdir=/tmp/freeswitch/db' '--with-imagesdir=/usr/share/freeswitch/images' '--with-logfiledir=/tmp/freeswitch/log' '--with-python=no' '--with-recordingsdir=/tmp/freeswitch/recordings' '--with-storagedir=/tmp/freeswitch/storage' '--disable-debug' '--enable-libyuv' '--enable-core-odbc-support' '--enable-srtp' '--enable-libvpx' '--enable-zrtp' '--with-odbc-lib=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-odbc=/openwrt/staging_dir/target-x86_64_musl/usr' '--with-libpri=/openwrt/staging_dir/target-x86_64_musl/usr' '--with-pritap' '--without-pgsql' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib ' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' '--with-modinstdir=/usr/lib/freeswitch/mod' 'CONFIGURE_CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib ' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
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
checking for style of include used by make... GNU
checking dependency style of ccache_cc... none
checking whether make sets $(MAKE)... (cached) yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld -m elf_x86_64
checking if the linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... x86_64-openwrt-linux-musl-gcc-nm
checking the name lister (x86_64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 1572864
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to x86_64-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for x86_64-openwrt-linux-musl-ld -m elf_x86_64 option to reload object files... -r
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
checking whether the ccache_cc linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64 -m elf_x86_64) supports shared libraries... yes
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... no
checking whether to build static libraries... yes
checking for C compiler vendor... gnu
checking for dirent.h that defines DIR... yes
checking for library containing opendir... none required
checking for ANSI C header files... (cached) yes
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking for size_t... yes
checking whether time.h and sys/time.h may both be included... yes
checking whether struct tm is in sys/time.h or time.h... time.h
checking whether ccache_cc needs -traditional... no
checking return type of signal handlers... void
checking for strftime... (cached) yes
checking whether byte ordering is bigendian... (cached) no
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating src/config.h
config.status: executing depfiles commands
config.status: executing libtool commands
=== configuring in libs/freetdm (/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release/libs/freetdm)
configure: running /bin/bash ./configure.gnu --disable-option-checking '--prefix=/usr'  '--target=x86_64-openwrt-linux' '--host=x86_64-openwrt-linux' '--build=x86_64-pc-linux-gnu' '--program-prefix=' '--program-suffix=' '--exec-prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--libexecdir=/usr/lib' '--sysconfdir=/etc' '--datadir=/usr/share' '--localstatedir=/var' '--mandir=/usr/man' '--infodir=/usr/info' '--disable-nls' '--disable-dependency-tracking' '--disable-static' '--disable-system-xmlrpc-c' '--enable-core-libedit-support' '--enable-fhs' '--with-cachedir=/tmp/freeswitch/cache' '--with-dbdir=/tmp/freeswitch/db' '--with-imagesdir=/usr/share/freeswitch/images' '--with-logfiledir=/tmp/freeswitch/log' '--with-python=no' '--with-recordingsdir=/tmp/freeswitch/recordings' '--with-storagedir=/tmp/freeswitch/storage' '--disable-debug' '--enable-libyuv' '--enable-core-odbc-support' '--enable-srtp' '--enable-libvpx' '--enable-zrtp' '--with-odbc-lib=/openwrt/staging_dir/target-x86_64_musl/usr/lib' '--with-odbc=/openwrt/staging_dir/target-x86_64_musl/usr' '--with-libpri=/openwrt/staging_dir/target-x86_64_musl/usr' '--with-pritap' '--without-pgsql' 'build_alias=x86_64-pc-linux-gnu' 'host_alias=x86_64-openwrt-linux' 'target_alias=x86_64-openwrt-linux' 'CC=ccache_cc' 'CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib ' 'CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CXX=ccache_cxx' 'CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' '--with-modinstdir=/usr/lib/freeswitch/mod' 'CONFIGURE_CFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_CPPFLAGS=-I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_CXXFLAGS=-Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release=freeswitch-1.10.6.-release -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/include -I/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/include ' 'CONFIGURE_LDFLAGS=-L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libiconv-stub/lib -L/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib -Wl,-rpath-link=/openwrt/staging_dir/target-x86_64_musl/usr/lib/libintl-stub/lib ' --cache-file=/dev/null --srcdir=.
configure: loading site script /openwrt/include/site/x86_64
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for x86_64-openwrt-linux-strip... x86_64-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
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
checking for style of include used by make... GNU
checking dependency style of ccache_cc... none
checking whether make sets $(MAKE)... (cached) yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... x86_64-openwrt-linux-musl-ld -m elf_x86_64
checking if the linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... x86_64-openwrt-linux-musl-gcc-nm
checking the name lister (x86_64-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 1572864
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-pc-linux-gnu file names to x86_64-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for x86_64-openwrt-linux-musl-ld -m elf_x86_64 option to reload object files... -r
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
checking whether the ccache_cc linker (x86_64-openwrt-linux-musl-ld -m elf_x86_64 -m elf_x86_64) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... no
checking pkg-config is at least version 0.9.0... yes
checking for C compiler vendor... gnu
checking for dlopen in -ldl... yes
checking for pthread_create in -lpthread... yes
checking for cos in -lm... yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking execinfo.h usability... no
checking execinfo.h presence... no
checking for execinfo.h... no
checking for gethostbyname_r... yes
checking whether gethostbyname_r requires five arguments... no

<<>> Modules and optional features
checking for openr2_context_set_io_type in -lopenr2... no
checking whether to build ftmod_r2... no
checking for wat_version in -lwat... no
checking whether to build ftmod_wat... no

<<>> Digium libpri
checking whether libpri is usable... no
configure: error: libpri not found or unusable (see config.log for details)
configure: error: ./configure.gnu failed for libs/freetdm
make[3]: *** [Makefile:1147: /openwrt/build_dir/target-x86_64_musl/freeswitch-1.10.6.-release/.configured_fc63396012fcd097440a505ac68a2b2a] Error 1
```
