---
title: "compile.40"
date: 2021-06-22 10:38:26.236998
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
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force 
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
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: running: /openwrt/staging_dir/host/bin/autoheader --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
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
OpenWrt-libtoolize:   `/openwrt/staging_dir/target-mips_24kc_musl/../host/share/aclocal/libtool.m4'
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
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force -I build
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
configure: loading site script /openwrt/include/site/mips
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
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
checking dependency style of ccache_cc... none
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
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
checking whether to build static libraries... no
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
checking LUA_CFLAGS... -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include 
checking LUA_LIBS... -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -llua -lm 
checking for alMidiGainSOFT in -lopenal... no
checking for jack... checking for snd_pcm_open in -lasound... yes
checking for uuid >= 1.41.2... yes
checking LIBUUID_CFLAGS... -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/uuid 
checking LIBUUID_LIBS... -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -luuid 
checking for pg_config... /openwrt/staging_dir/target-mips_24kc_musl/usr/bin/pg_config
checking for pkg-config... /openwrt/staging_dir/host/bin/pkg-config
checking for PostgreSQL libraries via pkg_config... -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib 
checking for PQgetvalue in -lpq... yes
checking for libmariadb >= 3.0.9... checking for mariadb >= 3.0.9... no
checking for spandsp3 >= 3.0... yes
checking SPANDSP_CFLAGS... -I/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/spandsp3/include 
checking SPANDSP_LIBS... -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib/spandsp3/lib -l:libspandsp.so.3 
checking for sofia-sip-ua >= 1.13.3... configure: error: no usable sofia-sip; please install sofia-sip-ua devel package or equivalent
make[3]: *** [Makefile:1144: /openwrt/build_dir/target-mips_24kc_musl/freeswitch-1.10.6.-release/.configured_b1e0b13d899af1fa68548d011fddf86f] Error 1
```
