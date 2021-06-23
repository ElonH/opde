---
title: "compile.41"
date: 2021-06-23 23:11:37.902215
hidden: false
draft: false
weight: -41
---

build number: `41`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/perl/compile -j$(nproc) || make package/feeds/packages/perl/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-macos_11_support.patch using plaintext: 
File hints/darwin.sh is read-only; trying to patch anyway
patching file hints/darwin.sh

Applying ./patches/002-add-Internals-getcwd.patch using plaintext: 
File MANIFEST is read-only; trying to patch anyway
patching file MANIFEST
patching file t/io/getcwd.t
File universal.c is read-only; trying to patch anyway
patching file universal.c

Applying ./patches/003-fallback-to-the-built-in-getcwd-if-we-ca.patch using plaintext: 
File dist/PathTools/Cwd.pm is read-only; trying to patch anyway
patching file dist/PathTools/Cwd.pm
File dist/PathTools/t/cwd.t is read-only; trying to patch anyway
patching file dist/PathTools/t/cwd.t

Applying ./patches/010-musl-compat.patch using plaintext: 
File perl.c is read-only; trying to patch anyway
patching file perl.c

Applying ./patches/020-storables-stacksize.patch using plaintext: 
File dist/Storable/Makefile.PL is read-only; trying to patch anyway
patching file dist/Storable/Makefile.PL
File dist/Storable/stacksize is read-only; trying to patch anyway
patching file dist/Storable/stacksize

Applying ./patches/100-fix-cross-compile-endianness-detection.patch using plaintext: 
File config_h.SH is read-only; trying to patch anyway
patching file config_h.SH

Applying ./patches/110-always_use_miniperl.patch using plaintext: 
File Makefile.SH is read-only; trying to patch anyway
patching file Makefile.SH

Applying ./patches/120-remove-build-timestamp.patch using plaintext: 
File perl.c is read-only; trying to patch anyway
patching file perl.c

Applying ./patches/300-add-relink-hack.patch using plaintext: 
patching file relink/Makefile.PL

Applying ./patches/301-fix_macos_static_linking.patch using plaintext: 
File cpan/ExtUtils-MakeMaker/lib/ExtUtils/MM_Unix.pm is read-only; trying to patch anyway
patching file cpan/ExtUtils-MakeMaker/lib/ExtUtils/MM_Unix.pm

Applying ./patches/320-copy-pod-hack.patch using plaintext: 
File cpan/podlators/Makefile.PL is read-only; trying to patch anyway
patching file cpan/podlators/Makefile.PL

Applying ./patches/710-threads_join-skip_ps_on_busybox.patch using plaintext: 
File dist/threads/t/join.t is read-only; trying to patch anyway
patching file dist/threads/t/join.t

Applying ./patches/900-use-rm-force.patch using plaintext: 
File Makefile.SH is read-only; trying to patch anyway
patching file Makefile.SH

Applying ./patches/910-miniperl-needs-inc-dot.patch using plaintext: 
File Makefile.SH is read-only; trying to patch anyway
patching file Makefile.SH

Applying ./patches/920-fix-no-locale.patch using plaintext: 
File embed.fnc is read-only; trying to patch anyway
patching file embed.fnc
patching file embed.h
File locale.c is read-only; trying to patch anyway
patching file locale.c
File makedef.pl is read-only; trying to patch anyway
patching file makedef.pl
File perl.h is read-only; trying to patch anyway
patching file perl.h
patching file proto.h
File sv.c is read-only; trying to patch anyway
patching file sv.c
File t/lib/warnings/regexec is read-only; trying to patch anyway
patching file t/lib/warnings/regexec

Applying ./patches/998-Errno_errno.h_path.patch using plaintext: 
File ext/Errno/Errno_pm.PL is read-only; trying to patch anyway
patching file ext/Errno/Errno_pm.PL

Applying ./patches/999-fix-build-failure-against-gcc-10.patch using plaintext: 
File Configure is read-only; trying to patch anyway
patching file Configure
File cflags.SH is read-only; trying to patch anyway
patching file cflags.SH
 
Fetching answers from config.sh...
 
Doing variable substitutions on .SH files...
Extracting config.h (with variable substitutions)
cflags.SH: Adding -std=c89.
cflags.SH: Adding -Werror=declaration-after-statement.
cflags.SH: Adding -Werror=pointer-arith.
cflags.SH: Adding -Wextra.
cflags.SH: Adding -Wc++-compat.
cflags.SH: Adding -Wwrite-strings.
cflags.SH: cc       = ccache_cc
cflags.SH: ccflags  = -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include
cflags.SH: stdflags =  -std=c89
cflags.SH: optimize = -O2
cflags.SH: warn     =  -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings
Extracting cflags (with variable substitutions)
Not re-extracting config.h
Extracting makedepend (with variable substitutions)
Extracting Makefile (with variable substitutions)
Extracting myconfig (with variable substitutions)
Extracting pod/Makefile (with variable substitutions)
Extracting Policy.sh (with variable substitutions)
Extracting runtests (with variable substitutions)
Extraction done.
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1'
make depend MAKEDEPEND=
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1'
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC generate_uudmap.c
/bin/ln -s /openwrt/staging_dir/hostpkg/usr/bin/generate_uudmap generate_uudmap
./generate_uudmap uudmap.h bitcount.h mg_data.h
sh ./makedepend MAKE="make" cflags
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1'
rm -f opmini.c
/bin/ln -s op.c opmini.c
rm -f perlmini.c
/bin/ln -s perl.c perlmini.c
echo av.c scope.c op.c doop.c doio.c dump.c gv.c hv.c mg.c reentr.c mro_core.c perl.c perly.c pp.c pp_hot.c pp_ctl.c pp_sys.c regcomp.c regexec.c utf8.c sv.c taint.c toke.c util.c deb.c run.c universal.c pad.c globals.c keywords.c perlio.c perlapi.c numeric.c mathoms.c locale.c pp_pack.c pp_sort.c caretx.c dquote.c time64.c  miniperlmain.c opmini.c perlmini.c | tr ' ' '\n' >.clist
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1'
Finding dependencies for av.o
Finding dependencies for scope.o
Finding dependencies for op.o
Finding dependencies for doop.o
Finding dependencies for doio.o
Finding dependencies for dump.o
Finding dependencies for gv.o
Finding dependencies for hv.o
Finding dependencies for mg.o
Finding dependencies for reentr.o
Finding dependencies for mro_core.o
Finding dependencies for perl.o
Finding dependencies for perly.o
Finding dependencies for pp.o
Finding dependencies for pp_hot.o
Finding dependencies for pp_ctl.o
Finding dependencies for pp_sys.o
Finding dependencies for regcomp.o
Finding dependencies for regexec.o
Finding dependencies for utf8.o
Finding dependencies for sv.o
Finding dependencies for taint.o
Finding dependencies for toke.o
Finding dependencies for util.o
Finding dependencies for deb.o
Finding dependencies for run.o
Finding dependencies for universal.o
Finding dependencies for pad.o
Finding dependencies for globals.o
Finding dependencies for keywords.o
Finding dependencies for perlio.o
Finding dependencies for perlapi.o
Finding dependencies for numeric.o
Finding dependencies for mathoms.o
Finding dependencies for locale.o
Finding dependencies for pp_pack.o
Finding dependencies for pp_sort.o
Finding dependencies for caretx.o
Finding dependencies for dquote.o
Finding dependencies for time64.o
Finding dependencies for miniperlmain.o
Finding dependencies for opmini.o
Finding dependencies for perlmini.o
Updating makefile...
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1'
rm -f opmini.c
/bin/ln -s op.c opmini.c
echo @`sh  cflags "optimize='-O2'" perlmini.o` -fPIC -DPERL_IS_MINIPERL -DPERL_EXTERNAL_GLOB perlmini.c
@ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC -DPERL_IS_MINIPERL -DPERL_EXTERNAL_GLOB perlmini.c
In file included from perl.c:37:
perl.c: In function 'Perl_sys_init':
perl.h:2645:51: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
 #    define PERL_FPU_INIT       PL_sigfpe_saved = (Sighandler_t) signal(SIGFPE, SIG_IGN)
                                                   ^
unixish.h:150:29: note: in expansion of macro 'PERL_FPU_INIT'
  MALLOC_CHECK_TAINT2(*c,*v) PERL_FPU_INIT; PERLIO_INIT; MALLOC_INIT
                             ^~~~~~~~~~~~~
perl.c:124:5: note: in expansion of macro 'PERL_SYS_INIT_BODY'
     PERL_SYS_INIT_BODY(argc, argv);
     ^~~~~~~~~~~~~~~~~~
perl.c: In function 'Perl_sys_init3':
perl.h:2645:51: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
 #    define PERL_FPU_INIT       PL_sigfpe_saved = (Sighandler_t) signal(SIGFPE, SIG_IGN)
                                                   ^
unixish.h:150:29: note: in expansion of macro 'PERL_FPU_INIT'
  MALLOC_CHECK_TAINT2(*c,*v) PERL_FPU_INIT; PERLIO_INIT; MALLOC_INIT
                             ^~~~~~~~~~~~~
perl.h:2695:49: note: in expansion of macro 'PERL_SYS_INIT_BODY'
 #  define PERL_SYS_INIT3_BODY(argvp,argcp,envp) PERL_SYS_INIT_BODY(argvp,argcp)
                                                 ^~~~~~~~~~~~~~~~~~
perl.c:137:5: note: in expansion of macro 'PERL_SYS_INIT3_BODY'
     PERL_SYS_INIT3_BODY(argc, argv, env);
     ^~~~~~~~~~~~~~~~~~~
perl.c: In function 'S_parse_body':
perl.c:2367:22: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
      if (sigstate == (Sighandler_t) SIG_IGN) {
                      ^
In file included from perl.h:5310,
                 from perl.c:37:
perl.c:2370:26: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
   (void)rsignal(SIGCHLD, (Sighandler_t)SIG_DFL);
                          ^
embed.h:638:44: note: in definition of macro 'rsignal'
 #define rsignal(a,b)  Perl_rsignal(aTHX_ a,b)
                                            ^
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC gv.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC toke.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC perly.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC pad.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC regcomp.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC dump.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC util.c
util.c: In function 'Perl_rsignal':
util.c:2667:9: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
  return (Sighandler_t) SIG_ERR;
         ^
util.c:2670:22: warning: cast between incompatible function types from 'Sighandler_t' {aka 'void (*)(int,  struct <anonymous> *, void *)'} to 'void (*)(int)' [-Wcast-function-type]
     act.sa_handler = (void(*)(int))handler;
                      ^
util.c:2678:40: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
     if (signo == SIGCHLD && handler == (Sighandler_t) SIG_IGN)
                                        ^
util.c:2682:13: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
      return (Sighandler_t) SIG_ERR;
             ^
util.c:2684:13: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
      return (Sighandler_t) oact.sa_handler;
             ^
util.c: In function 'Perl_rsignal_state':
util.c:2694:9: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
  return (Sighandler_t) SIG_ERR;
         ^
util.c:2696:9: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
  return (Sighandler_t) oact.sa_handler;
         ^
util.c: In function 'Perl_rsignal_save':
util.c:2715:22: warning: cast between incompatible function types from 'Sighandler_t' {aka 'void (*)(int,  struct <anonymous> *, void *)'} to 'void (*)(int)' [-Wcast-function-type]
     act.sa_handler = (void(*)(int))handler;
                      ^
util.c:2723:40: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
     if (signo == SIGCHLD && handler == (Sighandler_t) SIG_IGN)
                                        ^
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC mg.c
mg.c: In function 'Perl_magic_getsig':
mg.c:1459:25: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
          if(sigstate == (Sighandler_t) SIG_IGN)
                         ^
In file included from perl.h:5310,
                 from mg.c:43:
mg.c: In function 'Perl_magic_setsig':
mg.c:1736:20: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
   (void)rsignal(i, (Sighandler_t) SIG_IGN);
                    ^
embed.h:638:44: note: in definition of macro 'rsignal'
 #define rsignal(a,b)  Perl_rsignal(aTHX_ a,b)
                                            ^
mg.c:1746:20: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
   (void)rsignal(i, (Sighandler_t) SIG_DFL);
                    ^
embed.h:638:44: note: in definition of macro 'rsignal'
 #define rsignal(a,b)  Perl_rsignal(aTHX_ a,b)
                                            ^
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC reentr.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC mro_core.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC keywords.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC hv.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC av.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC run.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC pp_hot.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC sv.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC pp.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC scope.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC pp_ctl.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC pp_sys.c
In file included from perl.h:5310,
                 from pp_sys.c:31:
pp_sys.c: In function 'Perl_pp_system':
pp_sys.c:4474:28: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
      rsignal_save(SIGINT,  (Sighandler_t) SIG_IGN, &ihand);
                            ^
embed.h:1556:55: note: in definition of macro 'rsignal_save'
 #define rsignal_save(a,b,c) Perl_rsignal_save(aTHX_ a,b,c)
                                                       ^
pp_sys.c:4475:28: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
      rsignal_save(SIGQUIT, (Sighandler_t) SIG_IGN, &qhand);
                            ^
embed.h:1556:55: note: in definition of macro 'rsignal_save'
 #define rsignal_save(a,b,c) Perl_rsignal_save(aTHX_ a,b,c)
                                                       ^
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC doop.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC doio.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC regexec.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC utf8.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC taint.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC deb.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC universal.c
/bin/ln -s /openwrt/staging_dir/hostpkg/usr/bin/generate_uudmap generate_uudmap
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC perlio.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC perlapi.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC numeric.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC mathoms.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC locale.c
locale.c: In function 'Perl_setlocale':
locale.c:2158:18: warning: unused variable 'newlocale' [-Wunused-variable]
     const char * newlocale;
                  ^~~~~~~~~
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC pp_pack.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC pp_sort.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC caretx.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC dquote.c
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC time64.c
time64.c: In function 'S_copy_little_tm_to_big_TM':
time64.c:283:25: warning: assignment discards 'const' qualifier from pointer target type [-Wdiscarded-qualifiers]
     dest->tm_zone       = src->tm_zone;
                         ^
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC miniperlmain.c
In file included from perl.h:5310,
                 from miniperlmain.c:52:
miniperlmain.c: In function 'main':
miniperlmain.c:134:29: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
      rsignal(PL_sig_num[i], (Sighandler_t) SIG_DFL);
                             ^
embed.h:638:44: note: in definition of macro 'rsignal'
 #define rsignal(a,b)  Perl_rsignal(aTHX_ a,b)
                                            ^
rm -f pod/perl5281delta.pod
/bin/ln -s perldelta.pod pod/perl5281delta.pod
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC op.c
op.c: In function 'S_fold_constants':
op.c:5469:34: warning: argument 'o' might be clobbered by 'longjmp' or 'vfork' [-Wclobbered]
 S_fold_constants(pTHX_ OP *const o)
                        ~~~~~~~~~~^
echo @`sh  cflags "optimize='-O2'" opmini.o` -fPIC -DPERL_IS_MINIPERL -DPERL_EXTERNAL_GLOB opmini.c
@ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC -DPERL_IS_MINIPERL -DPERL_EXTERNAL_GLOB opmini.c
op.c: In function 'S_fold_constants':
op.c:5469:34: warning: argument 'o' might be clobbered by 'longjmp' or 'vfork' [-Wclobbered]
 S_fold_constants(pTHX_ OP *const o)
                        ~~~~~~~~~~^
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC globals.c
/bin/ln -s /openwrt/staging_dir/hostpkg/usr/bin/perl miniperl
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -w -Ilib -I. -Idist/Exporter/lib -MExporter -e '<?>' || sh -c 'echo >&2 Failed to build miniperl.  Please run make minitest; exit 1'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. -f write_buildcustomize.pl 'osname' "linux"
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. autodoc.pl
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. pod/perlmodlib.PL -q
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_patchnum.pl
Updating 'git_version.h' and 'lib/Config_git.pl'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. configpm
written lib/Config.pod
updated lib/Config.pm
updated lib/Config_heavy.pl
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC perl.c
In file included from perl.c:37:
perl.c: In function 'Perl_sys_init':
perl.h:2645:51: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
 #    define PERL_FPU_INIT       PL_sigfpe_saved = (Sighandler_t) signal(SIGFPE, SIG_IGN)
                                                   ^
unixish.h:150:29: note: in expansion of macro 'PERL_FPU_INIT'
  MALLOC_CHECK_TAINT2(*c,*v) PERL_FPU_INIT; PERLIO_INIT; MALLOC_INIT
                             ^~~~~~~~~~~~~
perl.c:124:5: note: in expansion of macro 'PERL_SYS_INIT_BODY'
     PERL_SYS_INIT_BODY(argc, argv);
     ^~~~~~~~~~~~~~~~~~
perl.c: In function 'Perl_sys_init3':
perl.h:2645:51: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
 #    define PERL_FPU_INIT       PL_sigfpe_saved = (Sighandler_t) signal(SIGFPE, SIG_IGN)
                                                   ^
unixish.h:150:29: note: in expansion of macro 'PERL_FPU_INIT'
  MALLOC_CHECK_TAINT2(*c,*v) PERL_FPU_INIT; PERLIO_INIT; MALLOC_INIT
                             ^~~~~~~~~~~~~
perl.h:2695:49: note: in expansion of macro 'PERL_SYS_INIT_BODY'
 #  define PERL_SYS_INIT3_BODY(argvp,argcp,envp) PERL_SYS_INIT_BODY(argvp,argcp)
                                                 ^~~~~~~~~~~~~~~~~~
perl.c:137:5: note: in expansion of macro 'PERL_SYS_INIT3_BODY'
     PERL_SYS_INIT3_BODY(argc, argv, env);
     ^~~~~~~~~~~~~~~~~~~
perl.c: In function 'S_parse_body':
perl.c:2367:22: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
      if (sigstate == (Sighandler_t) SIG_IGN) {
                      ^
In file included from perl.h:5310,
                 from perl.c:37:
perl.c:2370:26: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
   (void)rsignal(SIGCHLD, (Sighandler_t)SIG_DFL);
                          ^
embed.h:638:44: note: in definition of macro 'rsignal'
 #define rsignal(a,b)  Perl_rsignal(aTHX_ a,b)
                                            ^
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Archive-Tar/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for Archive::Tar
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Archive-Tar'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Archive-Tar'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Attribute-Handlers/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Attribute-Handlers directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/AutoLoader/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/AutoLoader directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/B-Debug/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/B-Debug directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/CPAN/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for CPAN
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/CPAN'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/CPAN'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/CPAN-Meta/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for CPAN::Meta
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/CPAN-Meta'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/CPAN-Meta'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/CPAN-Meta-Requirements/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/CPAN-Meta-Requirements directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/CPAN-Meta-YAML/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/CPAN-Meta-YAML directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Carp/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Carp directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Config-Perl-V/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Config-Perl-V directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Devel-SelfStubber/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Devel-SelfStubber directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Digest/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Digest directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Dumpvalue/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Dumpvalue directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Env/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Env directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl ext/Errno/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for Errno
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Errno'
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" Errno_pm.PL Errno.pm
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Errno'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Exporter/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Exporter directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/ExtUtils-CBuilder/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/ExtUtils-CBuilder directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/ExtUtils-Constant/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/ExtUtils-Constant directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/ExtUtils-Install/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/ExtUtils-Install directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/ExtUtils-MakeMaker/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for ExtUtils::MakeMaker
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/ExtUtils-MakeMaker'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/ExtUtils-MakeMaker'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/ExtUtils-Manifest/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/ExtUtils-Manifest directly
Generating a Unix-style Makefile
Writing Makefile for ExtUtils::Manifest
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/ExtUtils-Manifest'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/ExtUtils-Manifest'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl ext/ExtUtils-Miniperl/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for ext/ExtUtils-Miniperl directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/ExtUtils-ParseXS/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/ExtUtils-ParseXS directly
Generating a Unix-style Makefile
Writing Makefile for ExtUtils::ParseXS
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/ExtUtils-ParseXS'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/ExtUtils-ParseXS'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/File-Fetch/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/File-Fetch directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl ext/File-Find/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for ext/File-Find directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/File-Path/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/File-Path directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/File-Temp/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/File-Temp directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl ext/FileCache/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for ext/FileCache directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Filter-Simple/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Filter-Simple directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Getopt-Long/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Getopt-Long directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/HTTP-Tiny/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for HTTP::Tiny
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/HTTP-Tiny'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/HTTP-Tiny'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/I18N-Collate/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/I18N-Collate directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/I18N-LangTags/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/I18N-LangTags directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/lib/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for lib
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/lib'
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" lib_pm.PL lib.pm
Extracting lib.pm (with variable substitutions)
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/lib'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/IO-Socket-IP/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/IO-Socket-IP directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/IO-Zlib/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/IO-Zlib directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/IPC-Cmd/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/IPC-Cmd directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl ext/IPC-Open3/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for ext/IPC-Open3 directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/JSON-PP/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for JSON::PP
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/JSON-PP'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/JSON-PP'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Locale-Codes/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Locale-Codes directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Locale-Maketext/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Locale-Maketext directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Locale-Maketext-Simple/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Locale-Maketext-Simple directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Math-BigInt/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Math-BigInt directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Math-BigRat/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Math-BigRat directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Math-Complex/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Math-Complex directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Memoize/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Memoize directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Module-CoreList/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for Module::CoreList
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Module-CoreList'
cp corelist blib/script/corelist
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Module-CoreList/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/corelist
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Module-CoreList'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Module-Load/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Module-Load directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Module-Load-Conditional/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Module-Load-Conditional directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Module-Loaded/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Module-Loaded directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Module-Metadata/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for Module::Metadata
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Module-Metadata'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Module-Metadata'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/NEXT/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/NEXT directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Net-Ping/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Net-Ping directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Params-Check/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Params-Check directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Perl-OSType/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Perl-OSType directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/PerlIO-via-QuotedPrint/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/PerlIO-via-QuotedPrint directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Pod-Checker/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for Pod::Checker
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Pod-Checker'
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "-I../../lib" podchecker.PL podchecker
Extracting podchecker (with variable substitutions)
cp podchecker blib/script/podchecker
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Pod-Checker/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/podchecker
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Pod-Checker'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Pod-Escapes/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Pod-Escapes directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Pod-Simple/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Pod-Simple directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl ext/Pod-Html/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
/bin/sh: 1: ./miniperl: Text file busy
make[4]: *** [Makefile:585: ext/Pod-Html/pm_to_blib] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1'
make[3]: *** [Makefile:150: /openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/.built] Error 2
```
