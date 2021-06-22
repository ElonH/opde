---
title: "compile.40"
date: 2021-06-22 10:48:13.515575
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
make package/feeds/packages/selinux-python/compile -j$(nproc) || make package/feeds/packages/selinux-python/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0001-sepolgen-adjust-data_dir.patch using plaintext: 
patching file sepolgen/src/sepolgen/defaults.py

Applying ./patches/0002-sepolgen-don-t-hardcode-search-for-ausearch-in-sbin.patch using plaintext: 
patching file sepolgen/src/sepolgen/audit.py
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/selinux-python-3.2'
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/selinux-python-3.2/sepolicy'
/openwrt/staging_dir/hostpkg/bin/python3.9 setup.py build
running build
running build_py
creating build
creating build/lib
creating build/lib/sepolicy
copying sepolicy/network.py -> build/lib/sepolicy
copying sepolicy/interface.py -> build/lib/sepolicy
copying sepolicy/communicate.py -> build/lib/sepolicy
copying sepolicy/__init__.py -> build/lib/sepolicy
copying sepolicy/manpage.py -> build/lib/sepolicy
copying sepolicy/gui.py -> build/lib/sepolicy
copying sepolicy/transition.py -> build/lib/sepolicy
copying sepolicy/sedbus.py -> build/lib/sepolicy
copying sepolicy/booleans.py -> build/lib/sepolicy
copying sepolicy/generate.py -> build/lib/sepolicy
creating build/lib/sepolicy/templates
copying sepolicy/templates/network.py -> build/lib/sepolicy/templates
copying sepolicy/templates/var_lib.py -> build/lib/sepolicy/templates
copying sepolicy/templates/test_module.py -> build/lib/sepolicy/templates
copying sepolicy/templates/user.py -> build/lib/sepolicy/templates
copying sepolicy/templates/var_spool.py -> build/lib/sepolicy/templates
copying sepolicy/templates/rw.py -> build/lib/sepolicy/templates
copying sepolicy/templates/executable.py -> build/lib/sepolicy/templates
copying sepolicy/templates/etc_rw.py -> build/lib/sepolicy/templates
copying sepolicy/templates/__init__.py -> build/lib/sepolicy/templates
copying sepolicy/templates/unit_file.py -> build/lib/sepolicy/templates
copying sepolicy/templates/boolean.py -> build/lib/sepolicy/templates
copying sepolicy/templates/script.py -> build/lib/sepolicy/templates
copying sepolicy/templates/spec.py -> build/lib/sepolicy/templates
copying sepolicy/templates/var_run.py -> build/lib/sepolicy/templates
copying sepolicy/templates/semodule.py -> build/lib/sepolicy/templates
copying sepolicy/templates/var_log.py -> build/lib/sepolicy/templates
copying sepolicy/templates/var_cache.py -> build/lib/sepolicy/templates
copying sepolicy/templates/tmp.py -> build/lib/sepolicy/templates
creating build/lib/sepolicy/help
copying sepolicy/help/__init__.py -> build/lib/sepolicy/help
copying sepolicy/sepolicy.glade -> build/lib/sepolicy
copying sepolicy/help/transition_from.txt -> build/lib/sepolicy/help
copying sepolicy/help/lockdown.txt -> build/lib/sepolicy/help
copying sepolicy/help/transition_from_boolean.txt -> build/lib/sepolicy/help
copying sepolicy/help/system_boot_mode.txt -> build/lib/sepolicy/help
copying sepolicy/help/booleans_toggled.txt -> build/lib/sepolicy/help
copying sepolicy/help/login_default.txt -> build/lib/sepolicy/help
copying sepolicy/help/files_exec.txt -> build/lib/sepolicy/help
copying sepolicy/help/lockdown_unconfined.txt -> build/lib/sepolicy/help
copying sepolicy/help/lockdown_permissive.txt -> build/lib/sepolicy/help
copying sepolicy/help/files_write.txt -> build/lib/sepolicy/help
copying sepolicy/help/system_policy_type.txt -> build/lib/sepolicy/help
copying sepolicy/help/users.txt -> build/lib/sepolicy/help
copying sepolicy/help/files_apps.txt -> build/lib/sepolicy/help
copying sepolicy/help/ports_outbound.txt -> build/lib/sepolicy/help
copying sepolicy/help/booleans.txt -> build/lib/sepolicy/help
copying sepolicy/help/system.txt -> build/lib/sepolicy/help
copying sepolicy/help/booleans_more_show.txt -> build/lib/sepolicy/help
copying sepolicy/help/transition_from_boolean_1.txt -> build/lib/sepolicy/help
copying sepolicy/help/start.txt -> build/lib/sepolicy/help
copying sepolicy/help/login.txt -> build/lib/sepolicy/help
copying sepolicy/help/system_relabel.txt -> build/lib/sepolicy/help
copying sepolicy/help/system_current_mode.txt -> build/lib/sepolicy/help
copying sepolicy/help/transition_from_boolean_2.txt -> build/lib/sepolicy/help
copying sepolicy/help/ports_inbound.txt -> build/lib/sepolicy/help
copying sepolicy/help/transition_to.txt -> build/lib/sepolicy/help
copying sepolicy/help/system_export.txt -> build/lib/sepolicy/help
copying sepolicy/help/booleans_more.txt -> build/lib/sepolicy/help
copying sepolicy/help/file_equiv.txt -> build/lib/sepolicy/help
copying sepolicy/help/lockdown_ptrace.txt -> build/lib/sepolicy/help
copying sepolicy/help/transition_file.txt -> build/lib/sepolicy/help
copying sepolicy/help/ports_inbound.png -> build/lib/sepolicy/help
copying sepolicy/help/system_boot_mode.png -> build/lib/sepolicy/help
copying sepolicy/help/system_current_mode.png -> build/lib/sepolicy/help
copying sepolicy/help/lockdown_ptrace.png -> build/lib/sepolicy/help
copying sepolicy/help/system_policy_type.png -> build/lib/sepolicy/help
copying sepolicy/help/files_apps.png -> build/lib/sepolicy/help
copying sepolicy/help/lockdown.png -> build/lib/sepolicy/help
copying sepolicy/help/login.png -> build/lib/sepolicy/help
copying sepolicy/help/files_exec.png -> build/lib/sepolicy/help
copying sepolicy/help/system_relabel.png -> build/lib/sepolicy/help
copying sepolicy/help/lockdown_unconfined.png -> build/lib/sepolicy/help
copying sepolicy/help/transition_from_boolean_1.png -> build/lib/sepolicy/help
copying sepolicy/help/transition_from_boolean.png -> build/lib/sepolicy/help
copying sepolicy/help/lockdown_permissive.png -> build/lib/sepolicy/help
copying sepolicy/help/transition_file.png -> build/lib/sepolicy/help
copying sepolicy/help/login_default.png -> build/lib/sepolicy/help
copying sepolicy/help/file_equiv.png -> build/lib/sepolicy/help
copying sepolicy/help/files_write.png -> build/lib/sepolicy/help
copying sepolicy/help/start.png -> build/lib/sepolicy/help
copying sepolicy/help/booleans_toggled.png -> build/lib/sepolicy/help
copying sepolicy/help/ports_outbound.png -> build/lib/sepolicy/help
copying sepolicy/help/system_export.png -> build/lib/sepolicy/help
copying sepolicy/help/booleans_more.png -> build/lib/sepolicy/help
copying sepolicy/help/transition_to.png -> build/lib/sepolicy/help
copying sepolicy/help/transition_from.png -> build/lib/sepolicy/help
copying sepolicy/help/users.png -> build/lib/sepolicy/help
copying sepolicy/help/booleans_more_show.png -> build/lib/sepolicy/help
copying sepolicy/help/transition_from_boolean_2.png -> build/lib/sepolicy/help
copying sepolicy/help/booleans.png -> build/lib/sepolicy/help
copying sepolicy/help/system.png -> build/lib/sepolicy/help
warning: build_py: byte-compiling is disabled, skipping.

make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/selinux-python-3.2/sepolicy'
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/selinux-python-3.2/audit2allow'
ccache_cc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/selinux-python-3.2=selinux-python-3.2 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9  -c -o sepolgen-ifgen-attr-helper.o sepolgen-ifgen-attr-helper.c
ccache_cc -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -lpython3.9 -o sepolgen-ifgen-attr-helper sepolgen-ifgen-attr-helper.o -l:libsepol.a -lselinux
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lpython3.9
collect2: error: ld returned 1 exit status
make[5]: *** [Makefile:22: sepolgen-ifgen-attr-helper] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/selinux-python-3.2/audit2allow'
make[4]: *** [Makefile:4: all] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/selinux-python-3.2'
make[3]: *** [Makefile:158: /openwrt/build_dir/target-mips_24kc_musl/selinux-python-3.2/.built] Error 2
```
