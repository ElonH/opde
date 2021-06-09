---
title: "compile.30"
date: 2021-06-09 21:56:39.869327
hidden: false
draft: false
weight: -30
---

build number: `30`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/perl-device-usb/compile -j$(nproc) || make package/feeds/packages/perl-device-usb/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-fix_buildsystem.patch using plaintext: 
patching file Makefile.PL

Applying ./patches/110-just_assume_libusb_is_there.patch using plaintext: 
patching file Makefile.PL

Applying ./patches/120-use_libusb_0_1.patch using plaintext: 
patching file lib/Device/USB.pm

Applying ./patches/130-provide-proper-library-paths.patch using plaintext: 
patching file lib/Device/USB.pm

Applying ./patches/140-avoid-libusb-name-conflicts.patch using plaintext: 
patching file lib/Device/USB.pm
Checking if your kit is complete...
Warning: the following files are missing in your kit:
	USB.pm
Please inform the author.
Generating a Unix-style Makefile
Writing Makefile for Device::USB
Writing MYMETA.yml and MYMETA.json
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38'
cp lib/Device/USB/FAQ.pod blib/lib/Device/USB/FAQ.pod
cp lib/Device/USB/DevEndpoint.pm blib/lib/Device/USB/DevEndpoint.pm
cp lib/Device/USB/Device.pm blib/lib/Device/USB/Device.pm
cp lib/Device/USB.pm blib/lib/Device/USB.pm
cp lib/Device/USB/DevConfig.pm blib/lib/Device/USB/DevConfig.pm
cp lib/Device/USB/DevInterface.pm blib/lib/Device/USB/DevInterface.pm
cp lib/Device/USB/Bus.pm blib/lib/Device/USB/Bus.pm
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" -Mblib -MInline=NOISY,_INSTALL_ -MDevice::USB::Bus -e"my %A = (modinlname => 'Device-USB-Bus.inl', module => 'Device::USB::Bus'); my %S = (API => \%A); Inline::satisfy_makefile_dep(\%S);" 0.38 blib/arch
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" -Mblib -MInline=NOISY,_INSTALL_ -MDevice::USB -e"my %A = (modinlname => 'Device-USB.inl', module => 'Device::USB'); my %S = (API => \%A); Inline::satisfy_makefile_dep(\%S);" 0.38 blib/arch
validate Stage
Starting Build Preprocess Stage
get_maps Stage
Finished Build Preprocess Stage

Starting Build Parse Stage
Finished Build Parse Stage

Starting Build Glue 1 Stage
Finished Build Glue 1 Stage

Starting Build Glue 2 Stage
Finished Build Glue 2 Stage

Starting Build Glue 3 Stage
Finished Build Glue 3 Stage

"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" -Mblib -MInline=NOISY,_INSTALL_ -MDevice::USB::Device -e"my %A = (modinlname => 'Device-USB-Device.inl', module => 'Device::USB::Device'); my %S = (API => \%A); Inline::satisfy_makefile_dep(\%S);" 0.38 blib/arch
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" -Mblib -MInline=NOISY,_INSTALL_ -MDevice::USB::DevEndpoint -e"my %A = (modinlname => 'Device-USB-DevEndpoint.inl', module => 'Device::USB::DevEndpoint'); my %S = (API => \%A); Inline::satisfy_makefile_dep(\%S);" 0.38 blib/arch
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" -Mblib -MInline=NOISY,_INSTALL_ -MDevice::USB::DevConfig -e"my %A = (modinlname => 'Device-USB-DevConfig.inl', module => 'Device::USB::DevConfig'); my %S = (API => \%A); Inline::satisfy_makefile_dep(\%S);" 0.38 blib/arch
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" -Mblib -MInline=NOISY,_INSTALL_ -MDevice::USB::DevInterface -e"my %A = (modinlname => 'Device-USB-DevInterface.inl', module => 'Device::USB::DevInterface'); my %S = (API => \%A); Inline::satisfy_makefile_dep(\%S);" 0.38 blib/arch
cp bin/dump_usb.pl blib/script/dump_usb.pl
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/dump_usb.pl
Manifying 1 pod document
Manifying 7 pod documents
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/lib/perl5/5.28/Device/USB.pm
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/lib/perl5/5.28/Device/USB/DevEndpoint.pm
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/lib/perl5/5.28/Device/USB/Device.pm
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/lib/perl5/5.28/Device/USB/DevConfig.pm
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/lib/perl5/5.28/Device/USB/Bus.pm
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/lib/perl5/5.28/Device/USB/DevInterface.pm
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/lib/perl5/5.28/Device/USB/FAQ.pod
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/man/man1/dump_usb.pl.0
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/man/man3/Device::USB::DevEndpoint.0
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/man/man3/Device::USB::Bus.0
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/man/man3/Device::USB.0
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/man/man3/Device::USB::DevInterface.0
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/man/man3/Device::USB::DevConfig.0
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/man/man3/Device::USB::Device.0
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/man/man3/Device::USB::FAQ.0
Installing /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/bin/dump_usb.pl
Appending installation info to /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/lib/perl5/5.28/perllocal.pod
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38'
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38'
Manifying 1 pod document
Manifying 7 pod documents
Appending installation info to /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/ipkg-install/usr/lib/perl5/5.28/perllocal.pod
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38'
Typemap /openwrt/staging_dir/target-x86_64_musl/usr/lib/perl5/5.28/ExtUtils/typemap not found.
Generating a Unix-style Makefile
Writing Makefile for Device::USB
Writing MYMETA.yml and MYMETA.json
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/_Inline/build/Device/USB'
Running Mkbootstrap for USB ()
chmod 644 "USB.bs"
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" -MExtUtils::Command::MM -e 'cp_nonempty' -- USB.bs blib/arch/auto/Device/USB/USB.bs 644
"/openwrt/staging_dir/hostpkg/usr/bin/perl5.28.1" "/openwrt/staging_dir/hostpkg/usr/lib/perl5/5.28.1/ExtUtils/xsubpp"  -typemap '/openwrt/staging_dir/hostpkg/usr/lib/perl5/5.28.1/ExtUtils/typemap'  USB.xs > USB.xsc
mv USB.xsc USB.c
x86_64-openwrt-linux-gcc -c  -iquote"/openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38" -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -fmacro-prefix-map=/openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38=Device-USB-0.38 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -D_REENTRANT -D_GNU_SOURCE -O2   -DVERSION=\"0.38\" -DXS_VERSION=\"0.38\" -fPIC "-I/openwrt/staging_dir/target-x86_64_musl/usr/lib/perl5/5.28/CORE/"   USB.c
USB.xs:1:10: fatal error: EXTERN.h: No such file or directory
 #include "EXTERN.h"
          ^~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:335: USB.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/_Inline/build/Device/USB'
make[3]: *** [Makefile:76: /openwrt/build_dir/target-x86_64_musl/perl/Device-USB-0.38/.built] Error 2
```
