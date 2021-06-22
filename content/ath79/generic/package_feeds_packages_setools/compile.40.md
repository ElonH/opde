---
title: "compile.40"
date: 2021-06-22 10:48:13.522033
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
make package/feeds/packages/setools/compile -j$(nproc) || make package/feeds/packages/setools/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/030-remove-host-paths.patch using plaintext: 
patching file setup.py
Collecting Cython==0.29.21
  Downloading Cython-0.29.21.tar.gz (2.1 MB)
Skipping wheel build for Cython, due to binaries being disabled for it.
Installing collected packages: Cython
    Running setup.py install for Cython: started
    Running setup.py install for Cython: still running...
    Running setup.py install for Cython: finished with status 'done'
Successfully installed Cython-0.29.21
Compiling setools/policyrep.pyx because it changed.
[1/1] Cythonizing setools/policyrep.pyx
running install
running build
running build_py
creating build
creating build/lib.-3.9
creating build/lib.-3.9/setools
copying setools/permmap.py -> build/lib.-3.9/setools
copying setools/typequery.py -> build/lib.-3.9/setools
copying setools/userquery.py -> build/lib.-3.9/setools
copying setools/defaultquery.py -> build/lib.-3.9/setools
copying setools/fsusequery.py -> build/lib.-3.9/setools
copying setools/nodeconquery.py -> build/lib.-3.9/setools
copying setools/polcapquery.py -> build/lib.-3.9/setools
copying setools/ibpkeyconquery.py -> build/lib.-3.9/setools
copying setools/sensitivityquery.py -> build/lib.-3.9/setools
copying setools/dta.py -> build/lib.-3.9/setools
copying setools/rolequery.py -> build/lib.-3.9/setools
copying setools/categoryquery.py -> build/lib.-3.9/setools
copying setools/portconquery.py -> build/lib.-3.9/setools
copying setools/query.py -> build/lib.-3.9/setools
copying setools/boolquery.py -> build/lib.-3.9/setools
copying setools/infoflow.py -> build/lib.-3.9/setools
copying setools/ioportconquery.py -> build/lib.-3.9/setools
copying setools/commonquery.py -> build/lib.-3.9/setools
copying setools/netifconquery.py -> build/lib.-3.9/setools
copying setools/__init__.py -> build/lib.-3.9/setools
copying setools/genfsconquery.py -> build/lib.-3.9/setools
copying setools/iomemconquery.py -> build/lib.-3.9/setools
copying setools/typeattrquery.py -> build/lib.-3.9/setools
copying setools/ibendportconquery.py -> build/lib.-3.9/setools
copying setools/pcideviceconquery.py -> build/lib.-3.9/setools
copying setools/exception.py -> build/lib.-3.9/setools
copying setools/terulequery.py -> build/lib.-3.9/setools
copying setools/initsidquery.py -> build/lib.-3.9/setools
copying setools/pirqconquery.py -> build/lib.-3.9/setools
copying setools/util.py -> build/lib.-3.9/setools
copying setools/boundsquery.py -> build/lib.-3.9/setools
copying setools/descriptors.py -> build/lib.-3.9/setools
copying setools/mlsrulequery.py -> build/lib.-3.9/setools
copying setools/mixins.py -> build/lib.-3.9/setools
copying setools/constraintquery.py -> build/lib.-3.9/setools
copying setools/rbacrulequery.py -> build/lib.-3.9/setools
copying setools/objclassquery.py -> build/lib.-3.9/setools
copying setools/devicetreeconquery.py -> build/lib.-3.9/setools
creating build/lib.-3.9/setools/checker
copying setools/checker/checkermodule.py -> build/lib.-3.9/setools/checker
copying setools/checker/roexec.py -> build/lib.-3.9/setools/checker
copying setools/checker/emptyattr.py -> build/lib.-3.9/setools/checker
copying setools/checker/globalkeys.py -> build/lib.-3.9/setools/checker
copying setools/checker/__init__.py -> build/lib.-3.9/setools/checker
copying setools/checker/util.py -> build/lib.-3.9/setools/checker
copying setools/checker/checker.py -> build/lib.-3.9/setools/checker
copying setools/checker/descriptors.py -> build/lib.-3.9/setools/checker
copying setools/checker/assertte.py -> build/lib.-3.9/setools/checker
copying setools/checker/assertrbac.py -> build/lib.-3.9/setools/checker
creating build/lib.-3.9/setools/diff
copying setools/diff/rbacrules.py -> build/lib.-3.9/setools/diff
copying setools/diff/users.py -> build/lib.-3.9/setools/diff
copying setools/diff/commons.py -> build/lib.-3.9/setools/diff
copying setools/diff/bounds.py -> build/lib.-3.9/setools/diff
copying setools/diff/difference.py -> build/lib.-3.9/setools/diff
copying setools/diff/default.py -> build/lib.-3.9/setools/diff
copying setools/diff/constraints.py -> build/lib.-3.9/setools/diff
copying setools/diff/fsuse.py -> build/lib.-3.9/setools/diff
copying setools/diff/properties.py -> build/lib.-3.9/setools/diff
copying setools/diff/bool.py -> build/lib.-3.9/setools/diff
copying setools/diff/objclass.py -> build/lib.-3.9/setools/diff
copying setools/diff/roles.py -> build/lib.-3.9/setools/diff
copying setools/diff/terules.py -> build/lib.-3.9/setools/diff
copying setools/diff/__init__.py -> build/lib.-3.9/setools/diff
copying setools/diff/genfscon.py -> build/lib.-3.9/setools/diff
copying setools/diff/typing.py -> build/lib.-3.9/setools/diff
copying setools/diff/ibpkeycon.py -> build/lib.-3.9/setools/diff
copying setools/diff/ibendportcon.py -> build/lib.-3.9/setools/diff
copying setools/diff/mlsrules.py -> build/lib.-3.9/setools/diff
copying setools/diff/conditional.py -> build/lib.-3.9/setools/diff
copying setools/diff/netifcon.py -> build/lib.-3.9/setools/diff
copying setools/diff/nodecon.py -> build/lib.-3.9/setools/diff
copying setools/diff/typeattr.py -> build/lib.-3.9/setools/diff
copying setools/diff/descriptors.py -> build/lib.-3.9/setools/diff
copying setools/diff/initsid.py -> build/lib.-3.9/setools/diff
copying setools/diff/types.py -> build/lib.-3.9/setools/diff
copying setools/diff/context.py -> build/lib.-3.9/setools/diff
copying setools/diff/mls.py -> build/lib.-3.9/setools/diff
copying setools/diff/portcon.py -> build/lib.-3.9/setools/diff
copying setools/diff/polcap.py -> build/lib.-3.9/setools/diff
creating build/lib.-3.9/setoolsgui
copying setoolsgui/commonmodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/defaultmodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/rbacrulemodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/constraintmodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/boolmodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/terulemodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/widget.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/mlsrulemodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/treeview.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/listview.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/netifconmodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/typeattrmodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/boundsmodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/rolemodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/nodeconmodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/__init__.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/objclassmodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/getdetailslist.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/details.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/portconmodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/usermodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/ibpkeyconmodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/models.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/tableview.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/initsidmodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/typemodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/genfsconmodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/ibendportconmodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/fsusemodel.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/logtosignal.py -> build/lib.-3.9/setoolsgui
copying setoolsgui/mlsmodel.py -> build/lib.-3.9/setoolsgui
creating build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/typequery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/userquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/defaultquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/excludetypes.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/fsusequery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/nodeconquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/permmapedit.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/workspace.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/ibpkeyconquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/sensitivityquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/dta.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/chooseanalysis.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/rolequery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/categoryquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/portconquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/boolquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/infoflow.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/commonquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/config.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/netifconquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/__init__.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/genfsconquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/typeattrquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/ibendportconquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/analysistab.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/exception.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/terulequery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/summary.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/initsidquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/boundsquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/mainwindow.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/mlsrulequery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/queryupdater.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/constraintquery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/rbacrulequery.py -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/objclassquery.py -> build/lib.-3.9/setoolsgui/apol
copying setools/perm_map -> build/lib.-3.9/setools
copying setoolsgui/detail_popup.ui -> build/lib.-3.9/setoolsgui
copying setoolsgui/apol/mlsrulequery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/apol.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/choose_analysis.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/initsidquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/exclude_types.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/portconquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/ibpkeyconquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/typeattrquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/rbacrulequery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/sensitivityquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/boundsquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/genfsconquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/permmap_editor.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/nodeconquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/netifconquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/userquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/typequery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/summary.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/infoflow.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/boolquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/commonquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/constraintquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/dta.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/fsusequery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/objclassquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/rolequery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/ibendportconquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/permmapping.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/terulequery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/categoryquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/defaultquery.ui -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/apol.qhc -> build/lib.-3.9/setoolsgui/apol
copying setoolsgui/apol/apol.qch -> build/lib.-3.9/setoolsgui/apol
warning: build_py: byte-compiling is disabled, skipping.

running build_ext
building 'setools.policyrep' extension
creating build/temp.-3.9
creating build/temp.-3.9/setools
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/setools=setools -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c setools/policyrep.c -o build/temp.-3.9/setools/policyrep.o -Wextra -Waggregate-return -Wfloat-equal -Wformat -Wformat=2 -Winit-self -Wmissing-format-attribute -Wmissing-include-dirs -Wnested-externs -Wold-style-definition -Wpointer-arith -Wstrict-prototypes -Wunknown-pragmas -Wwrite-strings -fno-exceptions
cc1: warning: /openwrt/staging_dir/target-mips_24kc_musl/host/include: No such file or directory [-Wmissing-include-dirs]
cc1: warning: /openwrt/staging_dir/target-mips_24kc_musl/host/include: No such file or directory [-Wmissing-include-dirs]
cc1: warning: /openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9: No such file or directory [-Wmissing-include-dirs]
cc1: warning: /openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9: No such file or directory [-Wmissing-include-dirs]
setools/policyrep.c:44:10: fatal error: Python.h: No such file or directory
 #include "Python.h"
          ^~~~~~~~~~
compilation terminated.
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:46: /openwrt/build_dir/target-mips_24kc_musl/setools/.built] Error 1
```
