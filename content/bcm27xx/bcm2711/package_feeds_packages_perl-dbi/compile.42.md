---
title: "compile.42"
date: 2021-06-29 09:28:26.559169
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
make package/feeds/packages/perl-dbi/compile -j$(nproc) || make package/feeds/packages/perl-dbi/compile V=s
```

#### Compile.txt

``` bash
Your perl was compiled with gcc (version 9.3.0), okay.
Creating test wrappers for DBD::Gofer:
t/zvg_01basics.t 
t/zvg_02dbidrv.t 
t/zvg_03handle.t 
t/zvg_04mods.t 
t/zvg_05concathash.t 
t/zvg_06attrs.t 
t/zvg_07kids.t 
t/zvg_08keeperr.t 
t/zvg_09trace.t 
t/zvg_10examp.t 
t/zvg_11fetch.t 
t/zvg_12quote.t 
t/zvg_13taint.t 
t/zvg_14utf8.t 
t/zvg_15array.t 
t/zvg_16destroy.t 
t/zvg_17handle_error.t 
t/zvg_19fhtrace.t 
t/zvg_20meta.t 
t/zvg_30subclass.t 
t/zvg_31methcache.t 
t/zvg_35thrclone.t 
t/zvg_40profile.t 
t/zvg_41prof_dump.t 
t/zvg_42prof_data.t 
t/zvg_43prof_env.t 
t/zvg_48dbi_dbd_sqlengine.t 
t/zvg_49dbd_file.t 
t/zvg_50dbm_simple.t 
t/zvg_51dbm_file.t 
t/zvg_52dbm_complex.t 
t/zvg_53sqlengine_adv.t 
t/zvg_54_dbd_mem.t 
t/zvg_60preparse.t 
t/zvg_65transact.t 
t/zvg_70callbacks.t 
t/zvg_72childhandles.t 
t/zvg_73cachedkids.t 
t/zvg_80proxy.t 
t/zvg_85gofer.t 
t/zvg_86gofer_fail.t 
t/zvg_87gofer_cache.t 
t/zvg_90sql_type_cast.t 
t/zvg_91_store_warning.t 
Creating test wrappers for DBI::SQL::Nano:
t/zvn_48dbi_dbd_sqlengine.t 
t/zvn_49dbd_file.t 
t/zvn_50dbm_simple.t 
t/zvn_51dbm_file.t 
t/zvn_52dbm_complex.t 
t/zvn_85gofer.t 
Creating test wrappers for DBI::PurePerl:
t/zvp_01basics.t 
t/zvp_02dbidrv.t 
t/zvp_03handle.t 
t/zvp_04mods.t 
t/zvp_05concathash.t 
t/zvp_06attrs.t 
t/zvp_07kids.t 
t/zvp_08keeperr.t 
t/zvp_09trace.t 
t/zvp_10examp.t 
t/zvp_11fetch.t 
t/zvp_12quote.t 
t/zvp_13taint.t 
t/zvp_14utf8.t 
t/zvp_15array.t 
t/zvp_16destroy.t 
t/zvp_17handle_error.t 
t/zvp_19fhtrace.t 
t/zvp_20meta.t 
t/zvp_30subclass.t 
t/zvp_31methcache.t 
t/zvp_35thrclone.t 
t/zvp_40profile.t 
t/zvp_41prof_dump.t 
t/zvp_42prof_data.t 
t/zvp_43prof_env.t 
t/zvp_48dbi_dbd_sqlengine.t 
t/zvp_49dbd_file.t 
t/zvp_50dbm_simple.t 
t/zvp_51dbm_file.t 
t/zvp_52dbm_complex.t 
t/zvp_53sqlengine_adv.t 
t/zvp_54_dbd_mem.t 
t/zvp_60preparse.t 
t/zvp_65transact.t 
t/zvp_70callbacks.t 
t/zvp_72childhandles.t 
t/zvp_73cachedkids.t 
t/zvp_80proxy.t 
t/zvp_85gofer.t 
t/zvp_86gofer_fail.t 
t/zvp_87gofer_cache.t 
t/zvp_90sql_type_cast.t 
t/zvp_91_store_warning.t 
Creating test wrappers for DBD::Gofer + DBI::SQL::Nano:
t/zvxgn_48dbi_dbd_sqlengine.t 
t/zvxgn_49dbd_file.t 
t/zvxgn_50dbm_simple.t 
t/zvxgn_51dbm_file.t 
t/zvxgn_52dbm_complex.t 
t/zvxgn_85gofer.t 
Creating test wrappers for DBD::Gofer + DBI::PurePerl:
t/zvxgp_01basics.t 
t/zvxgp_02dbidrv.t 
t/zvxgp_03handle.t 
t/zvxgp_04mods.t 
t/zvxgp_05concathash.t 
t/zvxgp_06attrs.t 
t/zvxgp_07kids.t 
t/zvxgp_08keeperr.t 
t/zvxgp_09trace.t 
t/zvxgp_10examp.t 
t/zvxgp_11fetch.t 
t/zvxgp_12quote.t 
t/zvxgp_13taint.t 
t/zvxgp_14utf8.t 
t/zvxgp_15array.t 
t/zvxgp_16destroy.t 
t/zvxgp_17handle_error.t 
t/zvxgp_19fhtrace.t 
t/zvxgp_20meta.t 
t/zvxgp_30subclass.t 
t/zvxgp_31methcache.t 
t/zvxgp_35thrclone.t 
t/zvxgp_40profile.t 
t/zvxgp_41prof_dump.t 
t/zvxgp_42prof_data.t 
t/zvxgp_43prof_env.t 
t/zvxgp_48dbi_dbd_sqlengine.t 
t/zvxgp_49dbd_file.t 
t/zvxgp_50dbm_simple.t 
t/zvxgp_51dbm_file.t 
t/zvxgp_52dbm_complex.t 
t/zvxgp_53sqlengine_adv.t 
t/zvxgp_54_dbd_mem.t 
t/zvxgp_60preparse.t 
t/zvxgp_65transact.t 
t/zvxgp_70callbacks.t 
t/zvxgp_72childhandles.t 
t/zvxgp_73cachedkids.t 
t/zvxgp_80proxy.t 
t/zvxgp_85gofer.t 
t/zvxgp_86gofer_fail.t 
t/zvxgp_87gofer_cache.t 
t/zvxgp_90sql_type_cast.t 
t/zvxgp_91_store_warning.t 
Creating test wrappers for DBI::SQL::Nano + DBI::PurePerl:
t/zvxnp_48dbi_dbd_sqlengine.t 
t/zvxnp_49dbd_file.t 
t/zvxnp_50dbm_simple.t 
t/zvxnp_51dbm_file.t 
t/zvxnp_52dbm_complex.t 
t/zvxnp_85gofer.t 
Creating test wrappers for DBD::Gofer + DBI::SQL::Nano + DBI::PurePerl:
t/zvxgnp_48dbi_dbd_sqlengine.t 
t/zvxgnp_49dbd_file.t 
t/zvxgnp_50dbm_simple.t 
t/zvxgnp_51dbm_file.t 
t/zvxgnp_52dbm_complex.t 
t/zvxgnp_85gofer.t 
Checking if your kit is complete...
Looks good

    I see you're using perl 5.028001 on x86_64-linux, okay.
    Remember to actually *read* the README file!
    Use  'make' to build the software (dmake or nmake on Windows).
    Then 'make test' to execute self tests.
    Then 'make install' to install the DBI and then delete this working
    directory before unpacking and building any DBD::* drivers.

Generating a Unix-style Makefile
Writing Makefile for DBI
Writing MYMETA.yml and MYMETA.json
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/perl/DBI-1.643'
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" -MExtUtils::Command -e 'mkpath' -- blib/lib/DBI
rm -f blib/lib/DBI/Changes.pm
cp Changes blib/lib/DBI/Changes.pm
cp lib/DBD/Gofer.pm blib/lib/DBD/Gofer.pm
cp lib/DBD/Gofer/Transport/Base.pm blib/lib/DBD/Gofer/Transport/Base.pm
cp lib/DBD/Gofer/Transport/null.pm blib/lib/DBD/Gofer/Transport/null.pm
cp lib/DBD/Sponge.pm blib/lib/DBD/Sponge.pm
cp lib/DBI/DBD/Metadata.pm blib/lib/DBI/DBD/Metadata.pm
cp DBI.pm blib/lib/DBI.pm
cp lib/DBD/Gofer/Transport/corostream.pm blib/lib/DBD/Gofer/Transport/corostream.pm
cp lib/DBD/Mem.pm blib/lib/DBD/Mem.pm
cp lib/DBD/Gofer/Policy/rush.pm blib/lib/DBD/Gofer/Policy/rush.pm
cp lib/DBI/Const/GetInfoReturn.pm blib/lib/DBI/Const/GetInfoReturn.pm
cp lib/DBD/Gofer/Policy/classic.pm blib/lib/DBD/Gofer/Policy/classic.pm
cp lib/DBI/DBD/SqlEngine/HowTo.pod blib/lib/DBI/DBD/SqlEngine/HowTo.pod
cp lib/DBD/File/Developers.pod blib/lib/DBD/File/Developers.pod
cp lib/DBD/Gofer/Policy/Base.pm blib/lib/DBD/Gofer/Policy/Base.pm
cp lib/DBD/Gofer/Transport/stream.pm blib/lib/DBD/Gofer/Transport/stream.pm
cp lib/DBD/Gofer/Transport/pipeone.pm blib/lib/DBD/Gofer/Transport/pipeone.pm
cp lib/DBI/Const/GetInfo/ODBC.pm blib/lib/DBI/Const/GetInfo/ODBC.pm
cp lib/DBI/Gofer/Response.pm blib/lib/DBI/Gofer/Response.pm
cp dbi_sql.h blib/arch/auto/DBI/dbi_sql.h
cp lib/DBI/DBD/SqlEngine.pm blib/lib/DBI/DBD/SqlEngine.pm
cp dbixs_rev.pl blib/lib/dbixs_rev.pl
cp lib/DBI/Const/GetInfoType.pm blib/lib/DBI/Const/GetInfoType.pm
cp lib/DBI/Gofer/Request.pm blib/lib/DBI/Gofer/Request.pm
cp Driver_xst.h blib/arch/auto/DBI/Driver_xst.h
cp dbd_xsh.h blib/arch/auto/DBI/dbd_xsh.h
cp dbipport.h blib/arch/auto/DBI/dbipport.h
cp dbixs_rev.h blib/arch/auto/DBI/dbixs_rev.h
cp lib/DBD/ExampleP.pm blib/lib/DBD/ExampleP.pm
cp lib/Bundle/DBI.pm blib/lib/Bundle/DBI.pm
cp lib/DBD/Proxy.pm blib/lib/DBD/Proxy.pm
cp DBIXS.h blib/arch/auto/DBI/DBIXS.h
cp lib/DBD/DBM.pm blib/lib/DBD/DBM.pm
cp lib/DBD/NullP.pm blib/lib/DBD/NullP.pm
cp lib/DBI/Gofer/Execute.pm blib/lib/DBI/Gofer/Execute.pm
cp dbivport.h blib/arch/auto/DBI/dbivport.h
cp Driver.xst blib/arch/auto/DBI/Driver.xst
cp lib/DBI/DBD/SqlEngine/Developers.pod blib/lib/DBI/DBD/SqlEngine/Developers.pod
cp lib/DBD/File/Roadmap.pod blib/lib/DBD/File/Roadmap.pod
cp lib/DBI/Const/GetInfo/ANSI.pm blib/lib/DBI/Const/GetInfo/ANSI.pm
cp lib/DBD/File/HowTo.pod blib/lib/DBD/File/HowTo.pod
cp lib/DBD/File.pm blib/lib/DBD/File.pm
cp lib/DBD/Gofer/Policy/pedantic.pm blib/lib/DBD/Gofer/Policy/pedantic.pm
cp lib/DBI/DBD.pm blib/lib/DBI/DBD.pm
cp lib/DBI/ProfileSubs.pm blib/lib/DBI/ProfileSubs.pm
cp lib/DBI/ProfileDumper.pm blib/lib/DBI/ProfileDumper.pm
cp lib/DBI/Gofer/Transport/pipeone.pm blib/lib/DBI/Gofer/Transport/pipeone.pm
cp lib/DBI/PurePerl.pm blib/lib/DBI/PurePerl.pm
cp lib/Win32/DBIODBC.pm blib/lib/Win32/DBIODBC.pm
cp lib/DBI/Gofer/Serializer/Base.pm blib/lib/DBI/Gofer/Serializer/Base.pm
cp lib/DBI/Util/_accessor.pm blib/lib/DBI/Util/_accessor.pm
cp lib/DBI/Profile.pm blib/lib/DBI/Profile.pm
cp lib/DBI/Gofer/Transport/stream.pm blib/lib/DBI/Gofer/Transport/stream.pm
cp lib/DBI/W32ODBC.pm blib/lib/DBI/W32ODBC.pm
cp lib/DBI/ProfileDumper/Apache.pm blib/lib/DBI/ProfileDumper/Apache.pm
cp lib/DBI/ProfileData.pm blib/lib/DBI/ProfileData.pm
cp lib/DBI/Util/CacheMemory.pm blib/lib/DBI/Util/CacheMemory.pm
cp lib/DBI/SQL/Nano.pm blib/lib/DBI/SQL/Nano.pm
cp lib/DBI/Gofer/Transport/Base.pm blib/lib/DBI/Gofer/Transport/Base.pm
cp lib/DBI/Gofer/Serializer/DataDumper.pm blib/lib/DBI/Gofer/Serializer/DataDumper.pm
cp lib/DBI/ProxyServer.pm blib/lib/DBI/ProxyServer.pm
cp lib/DBI/Gofer/Serializer/Storable.pm blib/lib/DBI/Gofer/Serializer/Storable.pm
Running Mkbootstrap for DBI ()
chmod 644 "DBI.bs"
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" -MExtUtils::Command::MM -e 'cp_nonempty' -- DBI.bs blib/arch/auto/DBI/DBI.bs 644
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" -p -e "s/~DRIVER~/Perl/g" ./Driver.xst > Perl.xsi
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" "/openwrt/staging_dir/hostpkg/usr/lib/perl5/5.28.1/ExtUtils/xsubpp"  -typemap '/openwrt/staging_dir/hostpkg/usr/lib/perl5/5.28.1/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-aarch64_cortex-a72_musl/perl/DBI-1.643/typemap'  Perl.xs > Perl.xsc
mv Perl.xsc Perl.c
aarch64-openwrt-linux-gcc -c   -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-aarch64_cortex-a72_musl/perl/DBI-1.643=DBI-1.643 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-aarch64_cortex-a72_gcc-8.4.0_musl/include -O2   -DVERSION=\"1.643\" -DXS_VERSION=\"1.643\" -fPIC "-I/openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/lib/perl5/5.28/CORE/"  -W -Wall -Wpointer-arith -Wbad-function-cast -Wno-comment -Wno-sign-compare -Wno-cast-qual -Wmissing-noreturn -Wno-unused-parameter -DDBI_NO_THREADS Perl.c
In file included from Perl.xs:7:
DBIXS.h:22:10: fatal error: EXTERN.h: No such file or directory
 #include <EXTERN.h>
          ^~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:510: Perl.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/perl/DBI-1.643'
make[3]: *** [Makefile:67: /openwrt/build_dir/target-aarch64_cortex-a72_musl/perl/DBI-1.643/.built] Error 2
```
