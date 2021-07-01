---
title: "compile.43"
date: 2021-07-01 09:14:00.052340
hidden: false
draft: false
weight: -43
---

build number: `43`

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
Generating a Unix-style Makefile
Writing Makefile for Pod::Html
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Pod-Html'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Pod-Html'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Pod-Parser/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for Pod::Parser
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Pod-Parser'
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "-I../../lib" podselect.PL podselect
Extracting podselect (with variable substitutions)
cp podselect blib/script/podselect
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Pod-Parser/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/podselect
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Pod-Parser'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Pod-Perldoc/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for Pod::Perldoc
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Pod-Perldoc'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Pod-Perldoc'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Pod-Usage/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for Pod::Usage
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Pod-Usage'
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "-I../../lib" pod2usage.PL pod2usage
Extracting pod2usage (with variable substitutions)
cp pod2usage blib/script/pod2usage
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Pod-Usage/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/pod2usage
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Pod-Usage'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Safe/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Safe directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Search-Dict/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Search-Dict directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/SelfLoader/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/SelfLoader directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Term-ANSIColor/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Term-ANSIColor directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Term-Cap/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for Term::Cap
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Term-Cap'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Term-Cap'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Term-Complete/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Term-Complete directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Term-ReadLine/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Term-ReadLine directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Test/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Test directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Test-Harness/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for Test::Harness
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Test-Harness'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Test-Harness'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Test-Simple/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Test-Simple directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Text-Abbrev/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Text-Abbrev directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Text-Balanced/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Text-Balanced directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Text-ParseWords/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Text-ParseWords directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Text-Tabs/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Text-Tabs directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Thread-Queue/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Thread-Queue directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Thread-Semaphore/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Thread-Semaphore directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Tie-File/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/Tie-File directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl ext/Tie-Memoize/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for ext/Tie-Memoize directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Tie-RefHash/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Tie-RefHash directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/Time-Local/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/Time-Local directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/XSLoader/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for XSLoader
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/XSLoader'
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" XSLoader_pm.PL XSLoader.pm
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/XSLoader'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/autodie/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/autodie directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/autouse/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/autouse directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/base/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for base
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/base'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/base'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/bignum/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/bignum directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/constant/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/constant directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/encoding-warnings/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for dist/encoding-warnings directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/experimental/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/experimental directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/if/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for if
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/if'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/if'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/libnet/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for Net
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/libnet'
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/libnet'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/parent/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/parent directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/perlfaq/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/perlfaq directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/podlators/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for Pod
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/podlators'
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "-I../../lib" pod2man.PL pod2man
Extracting pod2man (with variable substitutions)
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "-I../../lib" pod2text.PL pod2text
Extracting pod2text (with variable substitutions)
cp pod2man blib/script/pod2man
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/podlators/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/pod2man
cp pod2text blib/script/pod2text
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/podlators/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/pod2text
Manifying 2 pod documents
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/podlators'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl dist/Unicode-Normalize/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Making header files for XS...
Generating a Unix-style Makefile
Writing Makefile for Unicode::Normalize
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Unicode-Normalize'
Running Mkbootstrap for Normalize ()
chmod 644 "Normalize.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Unicode-Normalize/../../lib/ExtUtils/typemap'  Normalize.xs > Normalize.xsc
mv Normalize.xsc Normalize.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.26\" -DXS_VERSION=\"1.26\" -fPIC "-I../.."   Normalize.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Unicode-Normalize/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Normalize.bs ../../lib/auto/Unicode/Normalize/Normalize.bs 644
rm -f ../../lib/auto/Unicode/Normalize/Normalize.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Normalize.o  -o ../../lib/auto/Unicode/Normalize/Normalize.so  \
      \
  
chmod 755 ../../lib/auto/Unicode/Normalize/Normalize.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Unicode-Normalize'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/version/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Running pm_to_blib for cpan/version directly
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. -MExtUtils::Miniperl -e 'writemain(\"perlmain.c", @ARGV)' DynaLoader 
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. utils/Makefile.PL
Extracting utils/Makefile (with variable substitutions)
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl cpan/IO-Compress/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for IO::Compress
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/IO-Compress'
cp bin/zipdetails blib/script/zipdetails
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/IO-Compress/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/zipdetails
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/IO-Compress'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl ext/Pod-Functions/pm_to_blib  MAKE="make" LIBPERL_A=libperl.so
Generating a Unix-style Makefile
Writing Makefile for Pod::Functions
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Pod-Functions'
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" Functions_pm.PL ../../pod/perlfunc.pod
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Pod-Functions'
ccache_cc -c -DPERL_CORE -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -std=c89 -O2 -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -fPIC perlmain.c
In file included from perl.h:5310,
                 from perlmain.c:46:
perlmain.c: In function 'main':
perlmain.c:128:29: warning: cast between incompatible function types from 'void (*)(int)' to 'void (*)(int,  siginfo_t *, void *)' {aka 'void (*)(int,  struct <anonymous> *, void *)'} [-Wcast-function-type]
      rsignal(PL_sig_num[i], (Sighandler_t) SIG_DFL);
                             ^
embed.h:638:44: note: in definition of macro 'rsignal'
 #define rsignal(a,b)  Perl_rsignal(aTHX_ a,b)
                                            ^
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl DynaLoader.o  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=static 
Generating a Unix-style Makefile
Writing Makefile for DynaLoader
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/DynaLoader'
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" DynaLoader_pm.PL DynaLoader.pm
rm -f DynaLoader.xs
cp dl_dlopen.xs DynaLoader.xs
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp" -noprototypes -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/DynaLoader/../../lib/ExtUtils/typemap'  DynaLoader.xs > DynaLoader.xsc
mv DynaLoader.xsc DynaLoader.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.45\" -DXS_VERSION=\"1.45\" -fPIC "-I../.."  -DLIBC="" DynaLoader.c
rm -rf ../../DynaLoader.o
cp DynaLoader.o ../../DynaLoader.o
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/DynaLoader'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. mkppport
running "/openwrt/staging_dir/hostpkg/usr/bin/perl" -I../../lib PPPort_pm.PL
including ppphdoc
including ppphbin
including version
including threads
including limits
including uv
including memory
including magic
including misc
including format
including mess
including variables
including mPUSH
including call
including newRV
including newCONSTSUB
including MY_CXT
including SvREFCNT
including newSV_type
including newSVpv
including SvPV
including Sv_set
including sv_xpvf
including shared_pv
including HvNAME
including gv
including warn
including pvs
including cop
including grok
including snprintf
including sprintf
including exception
including strlfuncs
including pv_tools
running "/openwrt/staging_dir/hostpkg/usr/bin/perl" -I../../lib ppport_h.PL
installing ppport.h for cpan/DB_File
installing ppport.h for cpan/IPC-SysV
installing ppport.h for cpan/Scalar-List-Utils
installing ppport.h for cpan/Win32API-File
installing ppport.h for dist/IO
installing ppport.h for dist/PathTools
installing ppport.h for dist/Time-HiRes
removing temporary file PPPort.pm
removing temporary file ppport.h
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. lib/unicore/mktables -C lib/unicore -P pod -maketest -makelist -p
Processing PropertyAliases.txt
Finishing property setup
Processing PropValueAliases.txt
Processing extracted/DGeneralCategory.txt
Processing extracted/DCombiningClass.txt
Processing extracted/DNumType.txt
Processing extracted/DEastAsianWidth.txt
Processing extracted/DLineBreak.txt
Processing extracted/DBidiClass.txt
Processing extracted/DDecompositionType.txt
Processing extracted/DBinaryProperties.txt
Processing extracted/DNumValues.txt
Processing extracted/DJoinGroup.txt
Processing extracted/DJoinType.txt
Processing Jamo.txt
Processing UnicodeData.txt
Processing ArabicShaping.txt
Processing Blocks.txt
Processing PropList.txt
Processing SpecialCasing.txt
Processing LineBreak.txt
Processing EastAsianWidth.txt
Processing CompositionExclusions.txt
Processing BidiMirroring.txt
Processing CaseFolding.txt
Processing DCoreProperties.txt
Processing Scripts.txt
Processing DNormalizationProps.txt
Processing DAge.txt
Processing HangulSyllableType.txt
Processing auxiliary/WordBreakProperty.txt
Processing auxiliary/GraphemeBreakProperty.txt
Processing auxiliary/GCBTest.txt
Processing auxiliary/SBTest.txt
Processing auxiliary/WBTest.txt
Processing auxiliary/SentenceBreakProperty.txt
Processing NamedSequences.txt
Processing NameAliases.txt
Processing auxiliary/LBTest.txt
Processing ScriptExtensions.txt
Processing IndicSyllabicCategory.txt
Processing BidiBrackets.txt
Processing IndicPositionalCategory.txt
Processing VerticalOrientation.txt
Finishing processing Unicode properties
Compiling Perl properties
Creating Perl synonyms
Writing tables
Making pod file
Making test script
Updating 'mktables.lst'
rm -f libperl.so
ccache_cc -o libperl.so -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro op.o     perl.o  gv.o toke.o perly.o pad.o regcomp.o dump.o util.o mg.o reentr.o mro_core.o keywords.o hv.o av.o run.o pp_hot.o sv.o pp.o scope.o pp_ctl.o pp_sys.o doop.o doio.o regexec.o utf8.o taint.o deb.o universal.o globals.o perlio.o perlapi.o numeric.o mathoms.o locale.o pp_pack.o pp_sort.o caretx.o dquote.o time64.o   DynaLoader.o -lpthread -ldl -lm -lcrypt -lutil -lc 
ccache_cc -o perl -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro -fPIC -rdynamic -Wl,-rpath,/usr/lib/perl5/5.28/CORE perlmain.o   libperl.so `cat ext.libs` -lpthread -ldl -lm -lcrypt -lutil -lc 
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/B/B.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for B
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/B'
Running Mkbootstrap for B ()
chmod 644 "B.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/B/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/B/typemap'  B.xs > B.xsc
mv B.xsc B.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.74\" -DXS_VERSION=\"1.74\" -fPIC "-I../.."   B.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/B/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- B.bs ../../lib/auto/B/B.bs 644
rm -f ../../lib/auto/B/B.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  B.o  -o ../../lib/auto/B/B.so  \
      \
  
chmod 755 ../../lib/auto/B/B.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/B'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Compress/Raw/Bzip2/Bzip2.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Compress::Raw::Bzip2
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Compress-Raw-Bzip2'
Running Mkbootstrap for Bzip2 ()
chmod 644 "Bzip2.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Compress-Raw-Bzip2/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Compress-Raw-Bzip2/typemap'  Bzip2.xs > Bzip2.xsc
mv Bzip2.xsc Bzip2.c
ccache_cc -c  -I. -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.074\" -DXS_VERSION=\"2.074\" -fPIC "-I../.."  -DBZ_NO_STDIO  blocksort.c
ccache_cc -c  -I. -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.074\" -DXS_VERSION=\"2.074\" -fPIC "-I../.."  -DBZ_NO_STDIO  bzlib.c
ccache_cc -c  -I. -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.074\" -DXS_VERSION=\"2.074\" -fPIC "-I../.."  -DBZ_NO_STDIO  compress.c
ccache_cc -c  -I. -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.074\" -DXS_VERSION=\"2.074\" -fPIC "-I../.."  -DBZ_NO_STDIO  crctable.c
ccache_cc -c  -I. -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.074\" -DXS_VERSION=\"2.074\" -fPIC "-I../.."  -DBZ_NO_STDIO  decompress.c
decompress.c: In function 'BZ2_decompress':
decompress.c:198:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (uc != BZ_HDR_B) RETURN(BZ_DATA_ERROR_MAGIC);
          ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:200:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_MAGIC_2, uc);
       ^~~~~~~~~
decompress.c:201:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (uc != BZ_HDR_Z) RETURN(BZ_DATA_ERROR_MAGIC);
          ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:203:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_MAGIC_3, uc)
       ^~~~~~~~~
decompress.c:204:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (uc != BZ_HDR_h) RETURN(BZ_DATA_ERROR_MAGIC);
          ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:206:7: note: in expansion of macro 'GET_BITS'
       GET_BITS(BZ_X_MAGIC_4, s->blockSize100k, 8)
       ^~~~~~~~
decompress.c:211:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (s->smallDecompress) {
          ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:222:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_BLKHDR_1, uc);
       ^~~~~~~~~
decompress.c:225:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (uc != 0x31) RETURN(BZ_DATA_ERROR);
          ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:226:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_BLKHDR_2, uc);
       ^~~~~~~~~
decompress.c:227:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (uc != 0x41) RETURN(BZ_DATA_ERROR);
          ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:228:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_BLKHDR_3, uc);
       ^~~~~~~~~
decompress.c:229:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (uc != 0x59) RETURN(BZ_DATA_ERROR);
          ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:230:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_BLKHDR_4, uc);
       ^~~~~~~~~
decompress.c:231:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (uc != 0x26) RETURN(BZ_DATA_ERROR);
          ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:232:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_BLKHDR_5, uc);
       ^~~~~~~~~
decompress.c:233:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (uc != 0x53) RETURN(BZ_DATA_ERROR);
          ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:234:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_BLKHDR_6, uc);
       ^~~~~~~~~
decompress.c:241:25: warning: this statement may fall through [-Wimplicit-fallthrough=]
       s->storedBlockCRC = 0;
       ~~~~~~~~~~~~~~~~~~^~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:242:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_BCRC_1, uc);
       ^~~~~~~~~
decompress.c:243:25: warning: this statement may fall through [-Wimplicit-fallthrough=]
       s->storedBlockCRC = (s->storedBlockCRC << 8) | ((UInt32)uc);
       ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:244:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_BCRC_2, uc);
       ^~~~~~~~~
decompress.c:245:25: warning: this statement may fall through [-Wimplicit-fallthrough=]
       s->storedBlockCRC = (s->storedBlockCRC << 8) | ((UInt32)uc);
       ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:246:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_BCRC_3, uc);
       ^~~~~~~~~
decompress.c:247:25: warning: this statement may fall through [-Wimplicit-fallthrough=]
       s->storedBlockCRC = (s->storedBlockCRC << 8) | ((UInt32)uc);
       ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:248:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_BCRC_4, uc);
       ^~~~~~~~~
decompress.c:249:25: warning: this statement may fall through [-Wimplicit-fallthrough=]
       s->storedBlockCRC = (s->storedBlockCRC << 8) | ((UInt32)uc);
       ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:251:7: note: in expansion of macro 'GET_BITS'
       GET_BITS(BZ_X_RANDBIT, s->blockRandomised, 1);
       ^~~~~~~~
decompress.c:253:18: warning: this statement may fall through [-Wimplicit-fallthrough=]
       s->origPtr = 0;
       ~~~~~~~~~~~^~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:254:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_ORIGPTR_1, uc);
       ^~~~~~~~~
decompress.c:255:18: warning: this statement may fall through [-Wimplicit-fallthrough=]
       s->origPtr = (s->origPtr << 8) | ((Int32)uc);
       ~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:256:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_ORIGPTR_2, uc);
       ^~~~~~~~~
decompress.c:257:18: warning: this statement may fall through [-Wimplicit-fallthrough=]
       s->origPtr = (s->origPtr << 8) | ((Int32)uc);
       ~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:258:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_ORIGPTR_3, uc);
       ^~~~~~~~~
decompress.c:284:17: warning: this statement may fall through [-Wimplicit-fallthrough=]
       alphaSize = s->nInUse+2;
       ~~~~~~~~~~^~~~~~~~~~~~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:287:7: note: in expansion of macro 'GET_BITS'
       GET_BITS(BZ_X_SELECTOR_1, nGroups, 3);
       ^~~~~~~~
decompress.c:288:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (nGroups < 2 || nGroups > 6) RETURN(BZ_DATA_ERROR);
          ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:289:7: note: in expansion of macro 'GET_BITS'
       GET_BITS(BZ_X_SELECTOR_2, nSelectors, 15);
       ^~~~~~~~
decompress.c:292:12: warning: this statement may fall through [-Wimplicit-fallthrough=]
          j = 0;
          ~~^~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:71:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,1)
    ^~~~~~~~
decompress.c:294:13: note: in expansion of macro 'GET_BIT'
             GET_BIT(BZ_X_SELECTOR_3, uc);
             ^~~~~~~
decompress.c:321:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
                if (curr < 1 || curr > 20) RETURN(BZ_DATA_ERROR);
                   ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:71:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,1)
    ^~~~~~~~
decompress.c:322:16: note: in expansion of macro 'GET_BIT'
                GET_BIT(BZ_X_CODING_2, uc);
                ^~~~~~~
decompress.c:323:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
                if (uc == 0) break;
                   ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:71:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,1)
    ^~~~~~~~
decompress.c:324:16: note: in expansion of macro 'GET_BIT'
                GET_BIT(BZ_X_CODING_3, uc);
                ^~~~~~~
decompress.c:88:7: warning: this statement may fall through [-Wimplicit-fallthrough=]
    zn = gMinlen;                                  \
    ~~~^~~~~~~~~
decompress.c:373:7: note: in expansion of macro 'GET_MTF_VAL'
       GET_MTF_VAL(BZ_X_MTF_1, BZ_X_MTF_2, nextSym);
       ^~~~~~~~~~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:89:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(label1, zvec, zn);                    \
    ^~~~~~~~
decompress.c:373:7: note: in expansion of macro 'GET_MTF_VAL'
       GET_MTF_VAL(BZ_X_MTF_1, BZ_X_MTF_2, nextSym);
       ^~~~~~~~~~~
decompress.c:94:9: warning: this statement may fall through [-Wimplicit-fallthrough=]
       zn++;                                       \
       ~~^~
decompress.c:373:7: note: in expansion of macro 'GET_MTF_VAL'
       GET_MTF_VAL(BZ_X_MTF_1, BZ_X_MTF_2, nextSym);
       ^~~~~~~~~~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:71:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,1)
    ^~~~~~~~
decompress.c:95:7: note: in expansion of macro 'GET_BIT'
       GET_BIT(label2, zj);                        \
       ^~~~~~~
decompress.c:373:7: note: in expansion of macro 'GET_MTF_VAL'
       GET_MTF_VAL(BZ_X_MTF_1, BZ_X_MTF_2, nextSym);
       ^~~~~~~~~~~
decompress.c:88:7: warning: this statement may fall through [-Wimplicit-fallthrough=]
    zn = gMinlen;                                  \
    ~~~^~~~~~~~~
decompress.c:483:13: note: in expansion of macro 'GET_MTF_VAL'
             GET_MTF_VAL(BZ_X_MTF_5, BZ_X_MTF_6, nextSym);
             ^~~~~~~~~~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:89:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(label1, zvec, zn);                    \
    ^~~~~~~~
decompress.c:483:13: note: in expansion of macro 'GET_MTF_VAL'
             GET_MTF_VAL(BZ_X_MTF_5, BZ_X_MTF_6, nextSym);
             ^~~~~~~~~~~
decompress.c:94:9: warning: this statement may fall through [-Wimplicit-fallthrough=]
       zn++;                                       \
       ~~^~
decompress.c:483:13: note: in expansion of macro 'GET_MTF_VAL'
             GET_MTF_VAL(BZ_X_MTF_5, BZ_X_MTF_6, nextSym);
             ^~~~~~~~~~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:71:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,1)
    ^~~~~~~~
decompress.c:95:7: note: in expansion of macro 'GET_BIT'
       GET_BIT(label2, zj);                        \
       ^~~~~~~
decompress.c:483:13: note: in expansion of macro 'GET_MTF_VAL'
             GET_MTF_VAL(BZ_X_MTF_5, BZ_X_MTF_6, nextSym);
             ^~~~~~~~~~~
decompress.c:585:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (uc != 0x72) RETURN(BZ_DATA_ERROR);
          ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:586:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_ENDHDR_3, uc);
       ^~~~~~~~~
decompress.c:587:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (uc != 0x45) RETURN(BZ_DATA_ERROR);
          ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:588:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_ENDHDR_4, uc);
       ^~~~~~~~~
decompress.c:589:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (uc != 0x38) RETURN(BZ_DATA_ERROR);
          ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:590:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_ENDHDR_5, uc);
       ^~~~~~~~~
decompress.c:591:10: warning: this statement may fall through [-Wimplicit-fallthrough=]
       if (uc != 0x50) RETURN(BZ_DATA_ERROR);
          ^
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:592:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_ENDHDR_6, uc);
       ^~~~~~~~~
decompress.c:595:28: warning: this statement may fall through [-Wimplicit-fallthrough=]
       s->storedCombinedCRC = 0;
       ~~~~~~~~~~~~~~~~~~~~~^~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:596:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_CCRC_1, uc);
       ^~~~~~~~~
decompress.c:597:28: warning: this statement may fall through [-Wimplicit-fallthrough=]
       s->storedCombinedCRC = (s->storedCombinedCRC << 8) | ((UInt32)uc);
       ~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:598:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_CCRC_2, uc);
       ^~~~~~~~~
decompress.c:599:28: warning: this statement may fall through [-Wimplicit-fallthrough=]
       s->storedCombinedCRC = (s->storedCombinedCRC << 8) | ((UInt32)uc);
       ~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:600:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_CCRC_3, uc);
       ^~~~~~~~~
decompress.c:601:28: warning: this statement may fall through [-Wimplicit-fallthrough=]
       s->storedCombinedCRC = (s->storedCombinedCRC << 8) | ((UInt32)uc);
       ~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
decompress.c:44:4: note: here
    case lll: s->state = lll;                      \
    ^~~~
decompress.c:68:4: note: in expansion of macro 'GET_BITS'
    GET_BITS(lll,uuu,8)
    ^~~~~~~~
decompress.c:602:7: note: in expansion of macro 'GET_UCHAR'
       GET_UCHAR(BZ_X_CCRC_4, uc);
       ^~~~~~~~~
ccache_cc -c  -I. -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.074\" -DXS_VERSION=\"2.074\" -fPIC "-I../.."  -DBZ_NO_STDIO  huffman.c
ccache_cc -c  -I. -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.074\" -DXS_VERSION=\"2.074\" -fPIC "-I../.."  -DBZ_NO_STDIO  randtable.c
ccache_cc -c  -I. -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.074\" -DXS_VERSION=\"2.074\" -fPIC "-I../.."  -DBZ_NO_STDIO  Bzip2.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Compress-Raw-Bzip2/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Bzip2.bs ../../lib/auto/Compress/Raw/Bzip2/Bzip2.bs 644
rm -f ../../lib/auto/Compress/Raw/Bzip2/Bzip2.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Bzip2.o blocksort.o bzlib.o compress.o crctable.o decompress.o huffman.o randtable.o   -o ../../lib/auto/Compress/Raw/Bzip2/Bzip2.so  \
      \
  
chmod 755 ../../lib/auto/Compress/Raw/Bzip2/Bzip2.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Compress-Raw-Bzip2'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Compress/Raw/Zlib/Zlib.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Parsing config.in...
Building Zlib enabled
Auto Detect Gzip OS Code..
Setting Gzip OS Code to 3 [Unix/Default]
Looks Good.
Generating a Unix-style Makefile
Writing Makefile for Compress::Raw::Zlib
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Compress-Raw-Zlib'
Running Mkbootstrap for Zlib ()
chmod 644 "Zlib.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Compress-Raw-Zlib/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Compress-Raw-Zlib/typemap'  Zlib.xs > Zlib.xsc
mv Zlib.xsc Zlib.c
ccache_cc -c  -I./zlib-src -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.076\" -DXS_VERSION=\"2.076\" -fPIC "-I../.."  -DNO_VIZ -DZ_SOLO   -DGZIP_OS_CODE=3  adler32.c
ccache_cc -c  -I./zlib-src -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.076\" -DXS_VERSION=\"2.076\" -fPIC "-I../.."  -DNO_VIZ -DZ_SOLO   -DGZIP_OS_CODE=3  compress.c
ccache_cc -c  -I./zlib-src -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.076\" -DXS_VERSION=\"2.076\" -fPIC "-I../.."  -DNO_VIZ -DZ_SOLO   -DGZIP_OS_CODE=3  crc32.c
ccache_cc -c  -I./zlib-src -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.076\" -DXS_VERSION=\"2.076\" -fPIC "-I../.."  -DNO_VIZ -DZ_SOLO   -DGZIP_OS_CODE=3  deflate.c
deflate.c: In function 'deflateParams':
deflate.c:602:28: warning: macro expands to multiple statements [-Wmultistatement-macros]
                 CLEAR_HASH(s);
                            ^
deflate.c:193:5: note: in definition of macro 'CLEAR_HASH'
     s->head[s->hash_size-1] = NIL; \
     ^
deflate.c:601:13: note: some parts of macro expansion are not guarded by this 'else' clause
             else
             ^~~~
ccache_cc -c  -I./zlib-src -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.076\" -DXS_VERSION=\"2.076\" -fPIC "-I../.."  -DNO_VIZ -DZ_SOLO   -DGZIP_OS_CODE=3  infback.c
ccache_cc -c  -I./zlib-src -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.076\" -DXS_VERSION=\"2.076\" -fPIC "-I../.."  -DNO_VIZ -DZ_SOLO   -DGZIP_OS_CODE=3  inffast.c
ccache_cc -c  -I./zlib-src -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.076\" -DXS_VERSION=\"2.076\" -fPIC "-I../.."  -DNO_VIZ -DZ_SOLO   -DGZIP_OS_CODE=3  inflate.c
ccache_cc -c  -I./zlib-src -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.076\" -DXS_VERSION=\"2.076\" -fPIC "-I../.."  -DNO_VIZ -DZ_SOLO   -DGZIP_OS_CODE=3  inftrees.c
ccache_cc -c  -I./zlib-src -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.076\" -DXS_VERSION=\"2.076\" -fPIC "-I../.."  -DNO_VIZ -DZ_SOLO   -DGZIP_OS_CODE=3  trees.c
ccache_cc -c  -I./zlib-src -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.076\" -DXS_VERSION=\"2.076\" -fPIC "-I../.."  -DNO_VIZ -DZ_SOLO   -DGZIP_OS_CODE=3  uncompr.c
ccache_cc -c  -I./zlib-src -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.076\" -DXS_VERSION=\"2.076\" -fPIC "-I../.."  -DNO_VIZ -DZ_SOLO   -DGZIP_OS_CODE=3  zutil.c
ccache_cc -c  -I./zlib-src -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.076\" -DXS_VERSION=\"2.076\" -fPIC "-I../.."  -DNO_VIZ -DZ_SOLO   -DGZIP_OS_CODE=3  Zlib.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Compress-Raw-Zlib/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Zlib.bs ../../lib/auto/Compress/Raw/Zlib/Zlib.bs 644
rm -f ../../lib/auto/Compress/Raw/Zlib/Zlib.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Zlib.o adler32.o compress.o crc32.o deflate.o infback.o inffast.o inflate.o inftrees.o trees.o uncompr.o zutil.o   -o ../../lib/auto/Compress/Raw/Zlib/Zlib.so  \
      \
  
chmod 755 ../../lib/auto/Compress/Raw/Zlib/Zlib.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Compress-Raw-Zlib'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Cwd/Cwd.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Cwd
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/PathTools'
Running Mkbootstrap for Cwd ()
chmod 644 "Cwd.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/PathTools/../../lib/ExtUtils/typemap'  Cwd.xs > Cwd.xsc
mv Cwd.xsc Cwd.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"3.74\" -DXS_VERSION=\"3.74\" -fPIC "-I../.."  -DDOUBLE_SLASHES_SPECIAL=0 -DNO_PPPORT_H Cwd.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/PathTools/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Cwd.bs ../../lib/auto/Cwd/Cwd.bs 644
rm -f ../../lib/auto/Cwd/Cwd.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Cwd.o  -o ../../lib/auto/Cwd/Cwd.so  \
      \
  
chmod 755 ../../lib/auto/Cwd/Cwd.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/PathTools'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/DB_File/DB_File.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Parsing config.in...
Looks Good.
Generating a Unix-style Makefile
Writing Makefile for DB_File
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/DB_File'
Running Mkbootstrap for DB_File ()
chmod 644 "DB_File.bs"
ccache_cc -c  -I/usr/local/BerkeleyDB/include -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.840\" -DXS_VERSION=\"1.84\" -fPIC "-I../.."  -D_NOT_CORE  -DmDB_Prefix_t=size_t -DmDB_Hash_t=u_int32_t   version.c
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp" -noprototypes -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/DB_File/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/DB_File/typemap'  DB_File.xs > DB_File.xsc
mv DB_File.xsc DB_File.c
ccache_cc -c  -I/usr/local/BerkeleyDB/include -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.840\" -DXS_VERSION=\"1.84\" -fPIC "-I../.."  -D_NOT_CORE  -DmDB_Prefix_t=size_t -DmDB_Hash_t=u_int32_t   DB_File.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/DB_File/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- DB_File.bs ../../lib/auto/DB_File/DB_File.bs 644
rm -f ../../lib/auto/DB_File/DB_File.so
LD_RUN_PATH="/openwrt/staging_dir/target-x86_64_musl/usr/lib" ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  version.o DB_File.o  -o ../../lib/auto/DB_File/DB_File.so  \
   -ldb   \
  
chmod 755 ../../lib/auto/DB_File/DB_File.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/DB_File'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Data/Dumper/Dumper.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Data::Dumper
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Data-Dumper'
Running Mkbootstrap for Dumper ()
chmod 644 "Dumper.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Data-Dumper/../../lib/ExtUtils/typemap'  Dumper.xs > Dumper.xsc
mv Dumper.xsc Dumper.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.170\" -DXS_VERSION=\"2.170\" -fPIC "-I../.."   Dumper.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Data-Dumper/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Dumper.bs ../../lib/auto/Data/Dumper/Dumper.bs 644
rm -f ../../lib/auto/Data/Dumper/Dumper.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Dumper.o  -o ../../lib/auto/Data/Dumper/Dumper.so  \
      \
  
chmod 755 ../../lib/auto/Data/Dumper/Dumper.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Data-Dumper'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Devel/PPPort/PPPort.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Setting license tag...
Generating a Unix-style Makefile
Writing Makefile for Devel::PPPort
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Devel-PPPort'
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" PPPort_pm.PL PPPort.pm
including ppphdoc
including ppphbin
including version
including threads
including limits
including uv
including memory
including magic
including misc
including format
including mess
including variables
including mPUSH
including call
including newRV
including newCONSTSUB
including MY_CXT
including SvREFCNT
including newSV_type
including newSVpv
including SvPV
including Sv_set
including sv_xpvf
including shared_pv
including HvNAME
including gv
including warn
including pvs
including cop
including grok
including snprintf
including sprintf
including exception
including strlfuncs
including pv_tools
Running Mkbootstrap for PPPort ()
chmod 644 "PPPort.bs"
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Devel-PPPort/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- PPPort.bs ../../lib/auto/Devel/PPPort/PPPort.bs 644
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "-I../../lib" PPPort_xs.PL RealPPPort.xs
adding XS code from parts/inc/HvNAME
adding XS code from parts/inc/MY_CXT
adding XS code from parts/inc/SvPV
adding XS code from parts/inc/SvREFCNT
adding XS code from parts/inc/Sv_set
adding XS code from parts/inc/call
adding XS code from parts/inc/cop
adding XS code from parts/inc/exception
adding XS code from parts/inc/format
adding XS code from parts/inc/grok
adding XS code from parts/inc/gv
adding XS code from parts/inc/limits
adding XS code from parts/inc/mPUSH
adding XS code from parts/inc/magic
adding XS code from parts/inc/memory
adding XS code from parts/inc/mess
adding XS code from parts/inc/misc
adding XS code from parts/inc/newCONSTSUB
adding XS code from parts/inc/newRV
adding XS code from parts/inc/newSV_type
adding XS code from parts/inc/newSVpv
adding XS code from parts/inc/pv_tools
adding XS code from parts/inc/pvs
adding XS code from parts/inc/shared_pv
adding XS code from parts/inc/snprintf
adding XS code from parts/inc/sprintf
adding XS code from parts/inc/strlfuncs
adding XS code from parts/inc/sv_xpvf
adding XS code from parts/inc/threads
adding XS code from parts/inc/uv
adding XS code from parts/inc/variables
adding XS code from parts/inc/warn
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "-I../../lib" ppport_h.PL ppport.h
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp" -noprototypes -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Devel-PPPort/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Devel-PPPort/typemap'  RealPPPort.xs > RealPPPort.xsc
mv RealPPPort.xsc RealPPPort.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"3.40\" -DXS_VERSION=\"3.40\" -fPIC "-I../.."   module2.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"3.40\" -DXS_VERSION=\"3.40\" -fPIC "-I../.."   module3.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"3.40\" -DXS_VERSION=\"3.40\" -fPIC "-I../.."   RealPPPort.c
rm -f ../../lib/auto/Devel/PPPort/PPPort.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  RealPPPort.o module2.o module3.o  -o ../../lib/auto/Devel/PPPort/PPPort.so  \
      \
  
chmod 755 ../../lib/auto/Devel/PPPort/PPPort.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Devel-PPPort'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Devel/Peek/Peek.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Devel::Peek
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Devel-Peek'
Running Mkbootstrap for Peek ()
chmod 644 "Peek.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Devel-Peek/../../lib/ExtUtils/typemap'  Peek.xs > Peek.xsc
mv Peek.xsc Peek.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.27\" -DXS_VERSION=\"1.27\" -fPIC "-I../.."   Peek.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Devel-Peek/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Peek.bs ../../lib/auto/Devel/Peek/Peek.bs 644
rm -f ../../lib/auto/Devel/Peek/Peek.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Peek.o  -o ../../lib/auto/Devel/Peek/Peek.so  \
      \
  
chmod 755 ../../lib/auto/Devel/Peek/Peek.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Devel-Peek'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Digest/MD5/MD5.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Perl's config says that U32 access must be aligned.
Generating a Unix-style Makefile
Writing Makefile for Digest::MD5
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Digest-MD5'
Running Mkbootstrap for MD5 ()
chmod 644 "MD5.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Digest-MD5/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Digest-MD5/typemap'  MD5.xs > MD5.xsc
mv MD5.xsc MD5.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.55\" -DXS_VERSION=\"2.55\" -fPIC "-I../.."  -DU32_ALIGNMENT_REQUIRED MD5.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Digest-MD5/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- MD5.bs ../../lib/auto/Digest/MD5/MD5.bs 644
rm -f ../../lib/auto/Digest/MD5/MD5.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  MD5.o  -o ../../lib/auto/Digest/MD5/MD5.so  \
      \
  
chmod 755 ../../lib/auto/Digest/MD5/MD5.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Digest-MD5'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Digest/SHA/SHA.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Digest::SHA
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Digest-SHA'
Running Mkbootstrap for SHA ()
chmod 644 "SHA.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Digest-SHA/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Digest-SHA/typemap'  SHA.xs > SHA.xsc
mv SHA.xsc SHA.c
ccache_cc -c  -I. -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"6.01\" -DXS_VERSION=\"6.01\" -fPIC "-I../.."   SHA.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Digest-SHA/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- SHA.bs ../../lib/auto/Digest/SHA/SHA.bs 644
rm -f ../../lib/auto/Digest/SHA/SHA.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  SHA.o  -o ../../lib/auto/Digest/SHA/SHA.so  \
      \
  
chmod 755 ../../lib/auto/Digest/SHA/SHA.so
cp shasum blib/script/shasum
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Digest-SHA/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/shasum
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Digest-SHA'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Encode/Encode.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Writing MYMETA.yml and MYMETA.json
Writing MYMETA.yml and MYMETA.json
Writing MYMETA.yml and MYMETA.json
Writing MYMETA.yml and MYMETA.json
Writing MYMETA.yml and MYMETA.json
Writing MYMETA.yml and MYMETA.json
Writing MYMETA.yml and MYMETA.json
Writing MYMETA.yml and MYMETA.json
Generating a Unix-style Makefile
Writing Makefile for Encode
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode'
Running Mkbootstrap for Encode ()
chmod 644 "Encode.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/../../lib/ExtUtils/typemap'  Encode.xs > Encode.xsc
mv Encode.xsc Encode.c
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" bin/enc2xs -"Q" -"O" -o def_t.c -f def_t.fnm
Reading iso-8859-1 (iso-8859-1)
Reading ascii (ascii)
Reading cp1252 (cp1252)
Reading ascii-ctrl (ascii-ctrl)
Reading null (null)
ccache_cc -c  -I./Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.97\" -DXS_VERSION=\"2.97\" -fPIC "-I../.."   encengine.c
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/Byte'
Running Mkbootstrap for Byte ()
chmod 644 "Byte.bs"
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -"O" -o byte_t.c -f byte_t.fnm
Reading iso-8859-2 (iso-8859-2)
Reading iso-8859-3 (iso-8859-3)
Reading iso-8859-4 (iso-8859-4)
Reading iso-8859-5 (iso-8859-5)
Reading iso-8859-6 (iso-8859-6)
Reading iso-8859-7 (iso-8859-7)
Reading iso-8859-8 (iso-8859-8)
Reading iso-8859-9 (iso-8859-9)
Reading iso-8859-10 (iso-8859-10)
Reading iso-8859-11 (iso-8859-11)
Reading iso-8859-13 (iso-8859-13)
Reading iso-8859-14 (iso-8859-14)
Reading iso-8859-15 (iso-8859-15)
Reading iso-8859-16 (iso-8859-16)
Reading AdobeStandardEncoding (AdobeStandardEncoding)
Reading cp1006 (cp1006)
Reading cp1250 (cp1250)
Reading cp1251 (cp1251)
Reading cp1253 (cp1253)
Reading cp1254 (cp1254)
Reading cp1255 (cp1255)
Reading cp1256 (cp1256)
Reading cp1257 (cp1257)
Reading cp1258 (cp1258)
Reading cp424 (cp424)
Reading cp437 (cp437)
Reading cp737 (cp737)
Reading cp775 (cp775)
Reading cp850 (cp850)
Reading cp852 (cp852)
Reading cp855 (cp855)
Reading cp856 (cp856)
Reading cp857 (cp857)
Reading cp858 (cp858)
Reading cp860 (cp860)
Reading cp861 (cp861)
Reading cp862 (cp862)
Reading cp863 (cp863)
Reading cp864 (cp864)
Reading cp865 (cp865)
Reading cp866 (cp866)
Reading cp869 (cp869)
Reading cp874 (cp874)
Reading hp-roman8 (hp-roman8)
Reading koi8-f (koi8-f)
Reading koi8-r (koi8-r)
Reading koi8-u (koi8-u)
Reading MacArabic (MacArabic)
Reading MacCentralEurRoman (MacCentralEurRoman)
Reading MacCroatian (MacCroatian)
Reading MacCyrillic (MacCyrillic)
Reading MacFarsi (MacFarsi)
Reading MacGreek (MacGreek)
Reading MacHebrew (MacHebrew)
Reading MacIcelandic (MacIcelandic)
Reading MacRomanian (MacRomanian)
Reading MacRumanian (MacRumanian)
Reading MacRoman (MacRoman)
Reading MacSami (MacSami)
Reading MacThai (MacThai)
Reading MacTurkish (MacTurkish)
Reading MacUkrainian (MacUkrainian)
Reading nextstep (nextstep)
Reading viscii (viscii)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" "../../../lib/ExtUtils/xsubpp"  -nolinenumbers -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/Byte/../../../lib/ExtUtils/typemap'  Byte.xs > Byte.xsc
mv Byte.xsc Byte.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.04\" -DXS_VERSION=\"2.04\" -fPIC "-I../../.."   byte_t.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/Byte/../../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Byte.bs ../../../lib/auto/Encode/Byte/Byte.bs 644
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.04\" -DXS_VERSION=\"2.04\" -fPIC "-I../../.."   Byte.c
rm -f ../../../lib/auto/Encode/Byte/Byte.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Byte.o byte_t.o  -o ../../../lib/auto/Encode/Byte/Byte.so  \
      \
  
chmod 755 ../../../lib/auto/Encode/Byte/Byte.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/Byte'
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Encode.bs ../../lib/auto/Encode/Encode.bs 644
ccache_cc -c  -I./Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.97\" -DXS_VERSION=\"2.97\" -fPIC "-I../.."   Encode.c
ccache_cc -c  -I./Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.97\" -DXS_VERSION=\"2.97\" -fPIC "-I../.."   def_t.c
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/CN'
Running Mkbootstrap for CN ()
chmod 644 "CN.bs"
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o cp_00_t.c -f cp_00_t.fnm
Reading cp936 (cp936)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o eu_01_t.c -f eu_01_t.fnm
Reading euc-cn (euc-cn)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o gb_02_t.c -f gb_02_t.fnm
Reading gb12345-raw (gb12345-raw)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o gb_03_t.c -f gb_03_t.fnm
Reading gb2312-raw (gb2312-raw)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o ir_04_t.c -f ir_04_t.fnm
Reading iso-ir-165 (iso-ir-165)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o ma_05_t.c -f ma_05_t.fnm
Reading MacChineseSimp (MacChineseSimp)
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   cp_00_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   eu_01_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   gb_02_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   gb_03_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   ir_04_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   ma_05_t.c
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" "../../../lib/ExtUtils/xsubpp" -noprototypes -nolinenumbers -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/CN/../../../lib/ExtUtils/typemap'  CN.xs > CN.xsc
mv CN.xsc CN.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/CN/../../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- CN.bs ../../../lib/auto/Encode/CN/CN.bs 644
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   CN.c
rm -f ../../../lib/auto/Encode/CN/CN.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  CN.o cp_00_t.o eu_01_t.o gb_02_t.o gb_03_t.o ir_04_t.o ma_05_t.o  -o ../../../lib/auto/Encode/CN/CN.so  \
      \
  
chmod 755 ../../../lib/auto/Encode/CN/CN.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/CN'
rm -f ../../lib/auto/Encode/Encode.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Encode.o def_t.o encengine.o  -o ../../lib/auto/Encode/Encode.so  \
      \
  
chmod 755 ../../lib/auto/Encode/Encode.so
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/EBCDIC'
Running Mkbootstrap for EBCDIC ()
chmod 644 "EBCDIC.bs"
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -"O" -o ebcdic_t.c -f ebcdic_t.fnm
Reading cp37 (cp37)
Reading cp1026 (cp1026)
Reading cp1047 (cp1047)
Reading cp500 (cp500)
Reading cp875 (cp875)
Reading posix-bc (posix-bc)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" "../../../lib/ExtUtils/xsubpp"  -nolinenumbers -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/EBCDIC/../../../lib/ExtUtils/typemap'  EBCDIC.xs > EBCDIC.xsc
mv EBCDIC.xsc EBCDIC.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.02\" -DXS_VERSION=\"2.02\" -fPIC "-I../../.."   ebcdic_t.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/EBCDIC/../../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- EBCDIC.bs ../../../lib/auto/Encode/EBCDIC/EBCDIC.bs 644
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.02\" -DXS_VERSION=\"2.02\" -fPIC "-I../../.."   EBCDIC.c
rm -f ../../../lib/auto/Encode/EBCDIC/EBCDIC.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  EBCDIC.o ebcdic_t.o  -o ../../../lib/auto/Encode/EBCDIC/EBCDIC.so  \
      \
  
chmod 755 ../../../lib/auto/Encode/EBCDIC/EBCDIC.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/EBCDIC'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/JP'
Running Mkbootstrap for JP ()
chmod 644 "JP.bs"
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o cp_00_t.c -f cp_00_t.fnm
Reading cp932 (cp932)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o eu_01_t.c -f eu_01_t.fnm
Reading euc-jp (euc-jp)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o ji_02_t.c -f ji_02_t.fnm
Reading jis0201-raw (jis0201-raw)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o ji_03_t.c -f ji_03_t.fnm
Reading jis0208-raw (jis0208-raw)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o ji_04_t.c -f ji_04_t.fnm
Reading jis0212-raw (jis0212-raw)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o ma_05_t.c -f ma_05_t.fnm
Reading MacJapanese (MacJapanese)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o sh_06_t.c -f sh_06_t.fnm
Reading shiftjis (shiftjis)
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.04\" -DXS_VERSION=\"2.04\" -fPIC "-I../../.."   cp_00_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.04\" -DXS_VERSION=\"2.04\" -fPIC "-I../../.."   eu_01_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.04\" -DXS_VERSION=\"2.04\" -fPIC "-I../../.."   ji_02_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.04\" -DXS_VERSION=\"2.04\" -fPIC "-I../../.."   ji_03_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.04\" -DXS_VERSION=\"2.04\" -fPIC "-I../../.."   ji_04_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.04\" -DXS_VERSION=\"2.04\" -fPIC "-I../../.."   ma_05_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.04\" -DXS_VERSION=\"2.04\" -fPIC "-I../../.."   sh_06_t.c
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" "../../../lib/ExtUtils/xsubpp"  -nolinenumbers -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/JP/../../../lib/ExtUtils/typemap'  JP.xs > JP.xsc
mv JP.xsc JP.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/JP/../../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- JP.bs ../../../lib/auto/Encode/JP/JP.bs 644
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.04\" -DXS_VERSION=\"2.04\" -fPIC "-I../../.."   JP.c
rm -f ../../../lib/auto/Encode/JP/JP.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  JP.o cp_00_t.o eu_01_t.o ji_02_t.o ji_03_t.o ji_04_t.o ma_05_t.o sh_06_t.o  -o ../../../lib/auto/Encode/JP/JP.so  \
      \
  
chmod 755 ../../../lib/auto/Encode/JP/JP.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/JP'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/KR'
Running Mkbootstrap for KR ()
chmod 644 "KR.bs"
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o cp_00_t.c -f cp_00_t.fnm
Reading cp949 (cp949)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o eu_01_t.c -f eu_01_t.fnm
Reading euc-kr (euc-kr)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o jo_02_t.c -f jo_02_t.fnm
Reading johab (johab)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o ks_03_t.c -f ks_03_t.fnm
Reading ksc5601-raw (ksc5601-raw)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o ma_04_t.c -f ma_04_t.fnm
Reading MacKorean (MacKorean)
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   cp_00_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   eu_01_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   jo_02_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   ks_03_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   ma_04_t.c
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" "../../../lib/ExtUtils/xsubpp"  -nolinenumbers -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/KR/../../../lib/ExtUtils/typemap'  KR.xs > KR.xsc
mv KR.xsc KR.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/KR/../../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- KR.bs ../../../lib/auto/Encode/KR/KR.bs 644
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   KR.c
rm -f ../../../lib/auto/Encode/KR/KR.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  KR.o cp_00_t.o eu_01_t.o jo_02_t.o ks_03_t.o ma_04_t.o  -o ../../../lib/auto/Encode/KR/KR.so  \
      \
  
chmod 755 ../../../lib/auto/Encode/KR/KR.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/KR'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/Symbol'
Running Mkbootstrap for Symbol ()
chmod 644 "Symbol.bs"
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -"O" -o symbol_t.c -f symbol_t.fnm
Reading AdobeSymbol (AdobeSymbol)
Reading AdobeZdingbat (AdobeZdingbat)
Reading dingbats (dingbats)
Reading MacDingbats (MacDingbats)
Reading MacSymbol (MacSymbol)
Reading symbol (symbol)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" "../../../lib/ExtUtils/xsubpp"  -nolinenumbers -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/Symbol/../../../lib/ExtUtils/typemap'  Symbol.xs > Symbol.xsc
mv Symbol.xsc Symbol.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.02\" -DXS_VERSION=\"2.02\" -fPIC "-I../../.."   symbol_t.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/Symbol/../../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Symbol.bs ../../../lib/auto/Encode/Symbol/Symbol.bs 644
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.02\" -DXS_VERSION=\"2.02\" -fPIC "-I../../.."   Symbol.c
rm -f ../../../lib/auto/Encode/Symbol/Symbol.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Symbol.o symbol_t.o  -o ../../../lib/auto/Encode/Symbol/Symbol.so  \
      \
  
chmod 755 ../../../lib/auto/Encode/Symbol/Symbol.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/Symbol'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/TW'
Running Mkbootstrap for TW ()
chmod 644 "TW.bs"
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o bi_00_t.c -f bi_00_t.fnm
Reading big5-eten (big5-eten)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o bi_01_t.c -f bi_01_t.fnm
Reading big5-hkscs (big5-hkscs)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o cp_02_t.c -f cp_02_t.fnm
Reading cp950 (cp950)
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" ../bin/enc2xs -"Q" -o ma_03_t.c -f ma_03_t.fnm
Reading MacChineseTrad (MacChineseTrad)
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   bi_00_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   bi_01_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   cp_02_t.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   ma_03_t.c
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" "../../../lib/ExtUtils/xsubpp"  -nolinenumbers -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/TW/../../../lib/ExtUtils/typemap'  TW.xs > TW.xsc
mv TW.xsc TW.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/TW/../../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- TW.bs ../../../lib/auto/Encode/TW/TW.bs 644
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.03\" -DXS_VERSION=\"2.03\" -fPIC "-I../../.."   TW.c
rm -f ../../../lib/auto/Encode/TW/TW.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  TW.o bi_00_t.o bi_01_t.o cp_02_t.o ma_03_t.o  -o ../../../lib/auto/Encode/TW/TW.so  \
      \
  
chmod 755 ../../../lib/auto/Encode/TW/TW.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/TW'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/Unicode'
Running Mkbootstrap for Unicode ()
chmod 644 "Unicode.bs"
"../../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../../lib" "../../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/Unicode/../../../lib/ExtUtils/typemap'  Unicode.xs > Unicode.xsc
mv Unicode.xsc Unicode.c
ccache_cc -c -I./Encode  -I../Encode -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.17\" -DXS_VERSION=\"2.17\" -fPIC "-I../../.."   Unicode.c
Unicode.xs: In function 'enc_unpack':
Unicode.xs:70:4: warning: this statement may fall through [-Wimplicit-fallthrough=]
  v = (v << 8) | *s++;
  ~~^~~~~~~~~~~~~~~~~
Unicode.xs:71:5: note: here
     case 'n':
     ^~~~
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/Unicode/../../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Unicode.bs ../../../lib/auto/Encode/Unicode/Unicode.bs 644
rm -f ../../../lib/auto/Encode/Unicode/Unicode.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Unicode.o  -o ../../../lib/auto/Encode/Unicode/Unicode.so  \
      \
  
chmod 755 ../../../lib/auto/Encode/Unicode/Unicode.so
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/Unicode'
cp bin/enc2xs blib/script/enc2xs
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/enc2xs
cp bin/encguess blib/script/encguess
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/encguess
cp bin/piconv blib/script/piconv
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/piconv
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Encode'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Fcntl/Fcntl.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Fcntl
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Fcntl'
Running Mkbootstrap for Fcntl ()
chmod 644 "Fcntl.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp" -noprototypes -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Fcntl/../../lib/ExtUtils/typemap'  Fcntl.xs > Fcntl.xsc
mv Fcntl.xsc Fcntl.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.13\" -DXS_VERSION=\"1.13\" -fPIC "-I../.."   Fcntl.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Fcntl/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Fcntl.bs ../../lib/auto/Fcntl/Fcntl.bs 644
rm -f ../../lib/auto/Fcntl/Fcntl.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Fcntl.o  -o ../../lib/auto/Fcntl/Fcntl.so  \
      \
  
chmod 755 ../../lib/auto/Fcntl/Fcntl.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Fcntl'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/File/DosGlob/DosGlob.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for File::DosGlob
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/File-DosGlob'
Running Mkbootstrap for DosGlob ()
chmod 644 "DosGlob.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/File-DosGlob/../../lib/ExtUtils/typemap'  DosGlob.xs > DosGlob.xsc
mv DosGlob.xsc DosGlob.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.12\" -DXS_VERSION=\"1.12\" -fPIC "-I../.."   DosGlob.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/File-DosGlob/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- DosGlob.bs ../../lib/auto/File/DosGlob/DosGlob.bs 644
rm -f ../../lib/auto/File/DosGlob/DosGlob.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  DosGlob.o  -o ../../lib/auto/File/DosGlob/DosGlob.so  \
      \
  
chmod 755 ../../lib/auto/File/DosGlob/DosGlob.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/File-DosGlob'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/File/Glob/Glob.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for File::Glob
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/File-Glob'
Running Mkbootstrap for Glob ()
chmod 644 "Glob.bs"
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.31\" -DXS_VERSION=\"1.31\" -fPIC "-I../.."   bsd_glob.c
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/File-Glob/../../lib/ExtUtils/typemap'  Glob.xs > Glob.xsc
mv Glob.xsc Glob.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.31\" -DXS_VERSION=\"1.31\" -fPIC "-I../.."   Glob.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/File-Glob/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Glob.bs ../../lib/auto/File/Glob/Glob.bs 644
rm -f ../../lib/auto/File/Glob/Glob.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  bsd_glob.o Glob.o  -o ../../lib/auto/File/Glob/Glob.so  \
      \
  
chmod 755 ../../lib/auto/File/Glob/Glob.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/File-Glob'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Filter/Util/Call/Call.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Filter::Util::Call
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Filter-Util-Call'
Running Mkbootstrap for Call ()
chmod 644 "Call.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Filter-Util-Call/../../lib/ExtUtils/typemap'  Call.xs > Call.xsc
mv Call.xsc Call.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.58\" -DXS_VERSION=\"1.58\" -fPIC "-I../.."   Call.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Filter-Util-Call/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Call.bs ../../lib/auto/Filter/Util/Call/Call.bs 644
rm -f ../../lib/auto/Filter/Util/Call/Call.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Call.o  -o ../../lib/auto/Filter/Util/Call/Call.so  \
      \
  
chmod 755 ../../lib/auto/Filter/Util/Call/Call.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Filter-Util-Call'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/GDBM_File/GDBM_File.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for GDBM_File
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/GDBM_File'
Running Mkbootstrap for GDBM_File ()
chmod 644 "GDBM_File.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp" -noprototypes -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/GDBM_File/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/GDBM_File/typemap'  GDBM_File.xs > GDBM_File.xsc
mv GDBM_File.xsc GDBM_File.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.17\" -DXS_VERSION=\"1.17\" -fPIC "-I../.."   GDBM_File.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/GDBM_File/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- GDBM_File.bs ../../lib/auto/GDBM_File/GDBM_File.bs 644
rm -f ../../lib/auto/GDBM_File/GDBM_File.so
LD_RUN_PATH="/openwrt/staging_dir/target-x86_64_musl/usr/lib" ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  GDBM_File.o  -o ../../lib/auto/GDBM_File/GDBM_File.so  \
   -lgdbm   \
  
chmod 755 ../../lib/auto/GDBM_File/GDBM_File.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/GDBM_File'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Hash/Util/Util.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Hash::Util
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Hash-Util'
Running Mkbootstrap for Util ()
chmod 644 "Util.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Hash-Util/../../lib/ExtUtils/typemap'  Util.xs > Util.xsc
mv Util.xsc Util.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.22\" -DXS_VERSION=\"0.22\" -fPIC "-I../.."  -DPERL_EXT Util.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Hash-Util/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Util.bs ../../lib/auto/Hash/Util/Util.bs 644
rm -f ../../lib/auto/Hash/Util/Util.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Util.o  -o ../../lib/auto/Hash/Util/Util.so  \
      \
  
chmod 755 ../../lib/auto/Hash/Util/Util.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Hash-Util'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Hash/Util/FieldHash/FieldHash.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Hash::Util::FieldHash
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Hash-Util-FieldHash'
Running Mkbootstrap for FieldHash ()
chmod 644 "FieldHash.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Hash-Util-FieldHash/../../lib/ExtUtils/typemap'  FieldHash.xs > FieldHash.xsc
mv FieldHash.xsc FieldHash.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.20\" -DXS_VERSION=\"1.20\" -fPIC "-I../.."   FieldHash.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Hash-Util-FieldHash/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- FieldHash.bs ../../lib/auto/Hash/Util/FieldHash/FieldHash.bs 644
rm -f ../../lib/auto/Hash/Util/FieldHash/FieldHash.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  FieldHash.o  -o ../../lib/auto/Hash/Util/FieldHash/FieldHash.so  \
      \
  
chmod 755 ../../lib/auto/Hash/Util/FieldHash/FieldHash.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Hash-Util-FieldHash'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/I18N/Langinfo/Langinfo.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for I18N::Langinfo
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/I18N-Langinfo'
Running Mkbootstrap for Langinfo ()
chmod 644 "Langinfo.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/I18N-Langinfo/../../lib/ExtUtils/typemap'  Langinfo.xs > Langinfo.xsc
mv Langinfo.xsc Langinfo.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.17\" -DXS_VERSION=\"0.17\" -fPIC "-I../.."   Langinfo.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/I18N-Langinfo/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Langinfo.bs ../../lib/auto/I18N/Langinfo/Langinfo.bs 644
rm -f ../../lib/auto/I18N/Langinfo/Langinfo.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Langinfo.o  -o ../../lib/auto/I18N/Langinfo/Langinfo.so  \
      \
  
chmod 755 ../../lib/auto/I18N/Langinfo/Langinfo.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/I18N-Langinfo'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/IO/IO.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for IO
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/IO'
Running Mkbootstrap for IO ()
chmod 644 "IO.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/IO/../../lib/ExtUtils/typemap'  IO.xs > IO.xsc
mv IO.xsc IO.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.39\" -DXS_VERSION=\"1.39\" -fPIC "-I../.."   poll.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.39\" -DXS_VERSION=\"1.39\" -fPIC "-I../.."   IO.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/IO/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- IO.bs ../../lib/auto/IO/IO.bs 644
rm -f ../../lib/auto/IO/IO.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  IO.o poll.o  -o ../../lib/auto/IO/IO.so  \
      \
  
chmod 755 ../../lib/auto/IO/IO.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/IO'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/IPC/SysV/SysV.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Setting license tag...
Generating a Unix-style Makefile
Writing Makefile for IPC::SysV
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/IPC-SysV'
Running Mkbootstrap for SysV ()
chmod 644 "SysV.bs"
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/IPC-SysV'
"../../../../../../staging_dir/hostpkg/usr/bin/perl" -I../../lib -I../../lib regen.pl
Writing const-xs.inc
Writing const-c.inc
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/IPC-SysV'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/IPC-SysV'
"../../../../../../staging_dir/hostpkg/usr/bin/perl" -I../../lib -I../../lib regen.pl
Writing const-xs.inc
Writing const-c.inc
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/IPC-SysV'
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/IPC-SysV/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/IPC-SysV/typemap'  SysV.xs > SysV.xsc
mv SysV.xsc SysV.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/IPC-SysV/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- SysV.bs ../../lib/auto/IPC/SysV/SysV.bs 644
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.07\" -DXS_VERSION=\"2.07\" -fPIC "-I../.."   SysV.c
rm -f ../../lib/auto/IPC/SysV/SysV.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  SysV.o  -o ../../lib/auto/IPC/SysV/SysV.so  \
      \
  
chmod 755 ../../lib/auto/IPC/SysV/SysV.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/IPC-SysV'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/List/Util/Util.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for List::Util
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Scalar-List-Utils'
Running Mkbootstrap for Util ()
chmod 644 "Util.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Scalar-List-Utils/../../lib/ExtUtils/typemap'  ListUtil.xs > ListUtil.xsc
mv ListUtil.xsc ListUtil.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.50\" -DXS_VERSION=\"1.50\" -fPIC "-I../.."  -DPERL_EXT ListUtil.c
ListUtil.xs: In function 'XS_List__Util_sum':
ListUtil.xs:349:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
             accum = ACC_NV;
             ~~~~~~^~~~~~~~
ListUtil.xs:350:9: note: here
         case ACC_NV:
         ^~~~
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Scalar-List-Utils/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Util.bs ../../lib/auto/List/Util/Util.bs 644
rm -f ../../lib/auto/List/Util/Util.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  ListUtil.o  -o ../../lib/auto/List/Util/Util.so  \
      \
  
chmod 755 ../../lib/auto/List/Util/Util.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Scalar-List-Utils'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/MIME/Base64/Base64.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for MIME::Base64
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/MIME-Base64'
Running Mkbootstrap for Base64 ()
chmod 644 "Base64.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/MIME-Base64/../../lib/ExtUtils/typemap'  Base64.xs > Base64.xsc
mv Base64.xsc Base64.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"3.15\" -DXS_VERSION=\"3.15\" -fPIC "-I../.."   Base64.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/MIME-Base64/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Base64.bs ../../lib/auto/MIME/Base64/Base64.bs 644
rm -f ../../lib/auto/MIME/Base64/Base64.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Base64.o  -o ../../lib/auto/MIME/Base64/Base64.so  \
      \
  
chmod 755 ../../lib/auto/MIME/Base64/Base64.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/MIME-Base64'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Math/BigInt/FastCalc/FastCalc.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Math::BigInt::FastCalc
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Math-BigInt-FastCalc'
Running Mkbootstrap for FastCalc ()
chmod 644 "FastCalc.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Math-BigInt-FastCalc/../../lib/ExtUtils/typemap'  FastCalc.xs > FastCalc.xsc
mv FastCalc.xsc FastCalc.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.5006\" -DXS_VERSION=\"0.5006\" -fPIC "-I../.."   FastCalc.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Math-BigInt-FastCalc/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- FastCalc.bs ../../lib/auto/Math/BigInt/FastCalc/FastCalc.bs 644
rm -f ../../lib/auto/Math/BigInt/FastCalc/FastCalc.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  FastCalc.o  -o ../../lib/auto/Math/BigInt/FastCalc/FastCalc.so  \
      \
  
chmod 755 ../../lib/auto/Math/BigInt/FastCalc/FastCalc.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Math-BigInt-FastCalc'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Opcode/Opcode.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Opcode
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Opcode'
Running Mkbootstrap for Opcode ()
chmod 644 "Opcode.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Opcode/../../lib/ExtUtils/typemap'  Opcode.xs > Opcode.xsc
mv Opcode.xsc Opcode.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.43\" -DXS_VERSION=\"1.43\" -fPIC "-I../.."   Opcode.c
In file included from ../../perl.h:5310,
                 from Opcode.xs:3:
Opcode.xs: In function 'opmask_addlocal':
Opcode.xs:240:17: warning: cast between incompatible function types from 'void (*)(PerlInterpreter *, const char *, ...)' {aka 'void (*)(struct interpreter *, const char *, ...)'} to 'void (*)(void *)' [-Wcast-function-type]
  SAVEDESTRUCTOR((void(*)(void*))Perl_warn,"PL_op_mask restored");
                 ^
../../embed.h:658:57: note: in definition of macro 'save_destructor'
 #define save_destructor(a,b) Perl_save_destructor(aTHX_ a,b)
                                                         ^
Opcode.xs:240:2: note: in expansion of macro 'SAVEDESTRUCTOR'
  SAVEDESTRUCTOR((void(*)(void*))Perl_warn,"PL_op_mask restored");
  ^~~~~~~~~~~~~~
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Opcode/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Opcode.bs ../../lib/auto/Opcode/Opcode.bs 644
rm -f ../../lib/auto/Opcode/Opcode.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Opcode.o  -o ../../lib/auto/Opcode/Opcode.so  \
      \
  
chmod 755 ../../lib/auto/Opcode/Opcode.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Opcode'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/POSIX/POSIX.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Warning (mostly harmless): No library found for -lm
Warning (mostly harmless): No library found for -lposix
Warning (mostly harmless): No library found for -lcposix
Generating a Unix-style Makefile
Writing Makefile for POSIX
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/POSIX'
Running Mkbootstrap for POSIX ()
chmod 644 "POSIX.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp" -noprototypes -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/POSIX/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/POSIX/typemap'  POSIX.xs > POSIX.xsc
mv POSIX.xsc POSIX.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -DSTRUCT_TM_HASZONE -DHINT_SC_EXIST -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.84\" -DXS_VERSION=\"1.84\" -fPIC "-I../.."   POSIX.c
In file included from POSIX.xs:19:
POSIX.xs: In function 'S_setpayload':
../../perl.h:6996:26: warning: left shift count is negative [-Wshift-count-negative]
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
../../perl.h:6996:26: note: in definition of macro 'NV_NAN_QS_BIT'
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
../../perl.h:7021:6: note: in expansion of macro 'NV_NAN_QS_QUIET'
     (NV_NAN_QS_QUIET ? \
      ^~~~~~~~~~~~~~~
POSIX.xs:1268:5: note: in expansion of macro 'NV_NAN_SET_SIGNALING'
     NV_NAN_SET_SIGNALING(nvp);
     ^~~~~~~~~~~~~~~~~~~~
../../perl.h:6996:26: warning: left shift count is negative [-Wshift-count-negative]
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
../../perl.h:6996:26: note: in definition of macro 'NV_NAN_QS_BIT'
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
../../perl.h:7021:6: note: in expansion of macro 'NV_NAN_QS_QUIET'
     (NV_NAN_QS_QUIET ? \
      ^~~~~~~~~~~~~~~
POSIX.xs:1268:5: note: in expansion of macro 'NV_NAN_SET_SIGNALING'
     NV_NAN_SET_SIGNALING(nvp);
     ^~~~~~~~~~~~~~~~~~~~
../../perl.h:6996:26: warning: left shift count is negative [-Wshift-count-negative]
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
../../perl.h:6996:26: note: in definition of macro 'NV_NAN_QS_BIT'
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
POSIX.xs:1268:5: note: in expansion of macro 'NV_NAN_SET_SIGNALING'
     NV_NAN_SET_SIGNALING(nvp);
     ^~~~~~~~~~~~~~~~~~~~
../../perl.h:6996:26: warning: left shift count is negative [-Wshift-count-negative]
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
../../perl.h:6996:26: note: in definition of macro 'NV_NAN_QS_BIT'
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
POSIX.xs:1268:5: note: in expansion of macro 'NV_NAN_SET_SIGNALING'
     NV_NAN_SET_SIGNALING(nvp);
     ^~~~~~~~~~~~~~~~~~~~
POSIX.xs: In function 'XS_POSIX_issignaling':
../../perl.h:6996:26: warning: left shift count is negative [-Wshift-count-negative]
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
../../perl.h:6996:26: note: in definition of macro 'NV_NAN_QS_BIT'
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
../../perl.h:7015:6: note: in expansion of macro 'NV_NAN_QS_TEST'
     (NV_NAN_QS_TEST(nvp) == (NV_NAN_QS_QUIET ? 0 : NV_NAN_QS_BIT))
      ^~~~~~~~~~~~~~
POSIX.xs:2675:29: note: in expansion of macro 'NV_NAN_IS_SIGNALING'
  RETVAL = Perl_isnan(nv) && NV_NAN_IS_SIGNALING(&nv);
                             ^~~~~~~~~~~~~~~~~~~
../../perl.h:6996:26: warning: left shift count is negative [-Wshift-count-negative]
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
../../perl.h:6996:26: note: in definition of macro 'NV_NAN_QS_BIT'
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
../../perl.h:7015:30: note: in expansion of macro 'NV_NAN_QS_QUIET'
     (NV_NAN_QS_TEST(nvp) == (NV_NAN_QS_QUIET ? 0 : NV_NAN_QS_BIT))
                              ^~~~~~~~~~~~~~~
POSIX.xs:2675:29: note: in expansion of macro 'NV_NAN_IS_SIGNALING'
  RETVAL = Perl_isnan(nv) && NV_NAN_IS_SIGNALING(&nv);
                             ^~~~~~~~~~~~~~~~~~~
../../perl.h:6996:26: warning: left shift count is negative [-Wshift-count-negative]
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
../../perl.h:6996:26: note: in definition of macro 'NV_NAN_QS_BIT'
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
../../perl.h:7015:30: note: in expansion of macro 'NV_NAN_QS_QUIET'
     (NV_NAN_QS_TEST(nvp) == (NV_NAN_QS_QUIET ? 0 : NV_NAN_QS_BIT))
                              ^~~~~~~~~~~~~~~
POSIX.xs:2675:29: note: in expansion of macro 'NV_NAN_IS_SIGNALING'
  RETVAL = Perl_isnan(nv) && NV_NAN_IS_SIGNALING(&nv);
                             ^~~~~~~~~~~~~~~~~~~
../../perl.h:6996:26: warning: left shift count is negative [-Wshift-count-negative]
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
../../perl.h:6996:26: note: in definition of macro 'NV_NAN_QS_BIT'
 #define NV_NAN_QS_BIT (1 << (NV_NAN_QS_BIT_SHIFT))
                          ^~
POSIX.xs:2675:29: note: in expansion of macro 'NV_NAN_IS_SIGNALING'
  RETVAL = Perl_isnan(nv) && NV_NAN_IS_SIGNALING(&nv);
                             ^~~~~~~~~~~~~~~~~~~
In file included from ../../perl.h:5310,
                 from POSIX.xs:19:
POSIX.xs: In function 'XS_POSIX_strftime':
POSIX.xs:3661:63: warning: pointer targets in passing argument 3 of 'Perl_isSCRIPT_RUN' differ in signedness [-Wpointer-sign]
                         && isSCRIPT_RUN((const U8 *) buf, buf + len,
                                                           ~~~~^~~~~
../../embed.h:1168:55: note: in definition of macro 'isSCRIPT_RUN'
 #define isSCRIPT_RUN(a,b,c) Perl_isSCRIPT_RUN(aTHX_ a,b,c)
                                                       ^
In file included from ../../perl.h:5271,
                 from POSIX.xs:19:
../../proto.h:4566:20: note: expected 'const U8 *' {aka 'const unsigned char *'} but argument is of type 'char *'
 PERL_CALLCONV bool Perl_isSCRIPT_RUN(pTHX_ const U8 *s, const U8 *send, const bool utf8_target)
                    ^~~~~~~~~~~~~~~~~
At top level:
POSIX.xs:1016:12: warning: 'my_fegetround' defined but not used [-Wunused-function]
 static int my_fegetround()
            ^~~~~~~~~~~~~
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/POSIX/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- POSIX.bs ../../lib/auto/POSIX/POSIX.bs 644
rm -f ../../lib/auto/POSIX/POSIX.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  POSIX.o  -o ../../lib/auto/POSIX/POSIX.so  \
      \
  
chmod 755 ../../lib/auto/POSIX/POSIX.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/POSIX'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/PerlIO/encoding/encoding.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for PerlIO::encoding
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-encoding'
Running Mkbootstrap for encoding ()
chmod 644 "encoding.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-encoding/../../lib/ExtUtils/typemap'  encoding.xs > encoding.xsc
mv encoding.xsc encoding.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.26\" -DXS_VERSION=\"0.26\" -fPIC "-I../.."   encoding.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-encoding/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- encoding.bs ../../lib/auto/PerlIO/encoding/encoding.bs 644
rm -f ../../lib/auto/PerlIO/encoding/encoding.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  encoding.o  -o ../../lib/auto/PerlIO/encoding/encoding.so  \
      \
  
chmod 755 ../../lib/auto/PerlIO/encoding/encoding.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-encoding'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/PerlIO/mmap/mmap.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for PerlIO::mmap
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-mmap'
Running Mkbootstrap for mmap ()
chmod 644 "mmap.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-mmap/../../lib/ExtUtils/typemap'  mmap.xs > mmap.xsc
mv mmap.xsc mmap.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.016\" -DXS_VERSION=\"0.016\" -fPIC "-I../.."   mmap.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-mmap/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- mmap.bs ../../lib/auto/PerlIO/mmap/mmap.bs 644
rm -f ../../lib/auto/PerlIO/mmap/mmap.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  mmap.o  -o ../../lib/auto/PerlIO/mmap/mmap.so  \
      \
  
chmod 755 ../../lib/auto/PerlIO/mmap/mmap.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-mmap'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/PerlIO/scalar/scalar.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for PerlIO::scalar
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-scalar'
Running Mkbootstrap for scalar ()
chmod 644 "scalar.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-scalar/../../lib/ExtUtils/typemap'  scalar.xs > scalar.xsc
mv scalar.xsc scalar.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.29\" -DXS_VERSION=\"0.29\" -fPIC "-I../.."   scalar.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-scalar/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- scalar.bs ../../lib/auto/PerlIO/scalar/scalar.bs 644
rm -f ../../lib/auto/PerlIO/scalar/scalar.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  scalar.o  -o ../../lib/auto/PerlIO/scalar/scalar.so  \
      \
  
chmod 755 ../../lib/auto/PerlIO/scalar/scalar.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-scalar'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/PerlIO/via/via.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for PerlIO::via
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-via'
Running Mkbootstrap for via ()
chmod 644 "via.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-via/../../lib/ExtUtils/typemap'  via.xs > via.xsc
mv via.xsc via.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.17\" -DXS_VERSION=\"0.17\" -fPIC "-I../.."   via.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-via/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- via.bs ../../lib/auto/PerlIO/via/via.bs 644
rm -f ../../lib/auto/PerlIO/via/via.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  via.o  -o ../../lib/auto/PerlIO/via/via.so  \
      \
  
chmod 755 ../../lib/auto/PerlIO/via/via.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/PerlIO-via'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/SDBM_File/SDBM_File.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for SDBM_File
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/SDBM_File'
Running Mkbootstrap for SDBM_File ()
chmod 644 "SDBM_File.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/SDBM_File/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/SDBM_File/typemap'  SDBM_File.xs > SDBM_File.xsc
mv SDBM_File.xsc SDBM_File.c
ccache_cc -c  -I../.. -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.14\" -DXS_VERSION=\"1.14\" -fPIC "-I../.."  -DSDBM -DDUFF hash.c
ccache_cc -c  -I../.. -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.14\" -DXS_VERSION=\"1.14\" -fPIC "-I../.."  -DSDBM -DDUFF pair.c
ccache_cc -c  -I../.. -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.14\" -DXS_VERSION=\"1.14\" -fPIC "-I../.."  -DSDBM -DDUFF sdbm.c
ccache_cc -c  -I../.. -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.14\" -DXS_VERSION=\"1.14\" -fPIC "-I../.."  -DSDBM -DDUFF SDBM_File.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/SDBM_File/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- SDBM_File.bs ../../lib/auto/SDBM_File/SDBM_File.bs 644
rm -f ../../lib/auto/SDBM_File/SDBM_File.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  SDBM_File.o hash.o pair.o sdbm.o  -o ../../lib/auto/SDBM_File/SDBM_File.so  \
      \
  
chmod 755 ../../lib/auto/SDBM_File/SDBM_File.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/SDBM_File'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Socket/Socket.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Socket
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Socket'
Running Mkbootstrap for Socket ()
chmod 644 "Socket.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp" -noprototypes -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Socket/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Socket/typemap'  Socket.xs > Socket.xsc
mv Socket.xsc Socket.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.027\" -DXS_VERSION=\"2.027\" -fPIC "-I../.."   Socket.c
Socket.xs: In function 'XS_Socket_pack_sockaddr_in6':
Socket.xs:1063:10: warning: cast to pointer from integer of different size [-Wint-to-pointer-cast]
  ST(0) = (SV*)not_here("pack_sockaddr_in6");
          ^
Socket.c:1305:16: warning: variable 'flowinfo' set but not used [-Wunused-but-set-variable]
  unsigned long flowinfo;
                ^~~~~~~~
Socket.c:1304:16: warning: variable 'scope_id' set but not used [-Wunused-but-set-variable]
  unsigned long scope_id;
                ^~~~~~~~
Socket.xs: In function 'XS_Socket_unpack_sockaddr_in6':
Socket.xs:1106:10: warning: cast to pointer from integer of different size [-Wint-to-pointer-cast]
  ST(0) = (SV*)not_here("pack_sockaddr_in6");
          ^
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Socket/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Socket.bs ../../lib/auto/Socket/Socket.bs 644
rm -f ../../lib/auto/Socket/Socket.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Socket.o  -o ../../lib/auto/Socket/Socket.so  \
      \
  
chmod 755 ../../lib/auto/Socket/Socket.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Socket'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Storable/Storable.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Storable
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Storable'
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" Storable.pm.PL
Running Mkbootstrap for Storable ()
chmod 644 "Storable.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Storable/../../lib/ExtUtils/typemap'  Storable.xs > Storable.xsc
mv Storable.xsc Storable.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Storable/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Storable.bs ../../lib/auto/Storable/Storable.bs 644
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"3.08\" -DXS_VERSION=\"3.08\" -fPIC "-I../.."   Storable.c
rm -f ../../lib/auto/Storable/Storable.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Storable.o  -o ../../lib/auto/Storable/Storable.so  \
      \
  
chmod 755 ../../lib/auto/Storable/Storable.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Storable'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Sys/Hostname/Hostname.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Sys::Hostname
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Sys-Hostname'
Running Mkbootstrap for Hostname ()
chmod 644 "Hostname.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Sys-Hostname/../../lib/ExtUtils/typemap'  Hostname.xs > Hostname.xsc
mv Hostname.xsc Hostname.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.22\" -DXS_VERSION=\"1.22\" -fPIC "-I../.."   Hostname.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Sys-Hostname/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Hostname.bs ../../lib/auto/Sys/Hostname/Hostname.bs 644
rm -f ../../lib/auto/Sys/Hostname/Hostname.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Hostname.o  -o ../../lib/auto/Sys/Hostname/Hostname.so  \
      \
  
chmod 755 ../../lib/auto/Sys/Hostname/Hostname.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Sys-Hostname'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Sys/Syslog/Syslog.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Sys::Syslog
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Sys-Syslog'
Running Mkbootstrap for Syslog ()
chmod 644 "Syslog.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp" -noprototypes -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Sys-Syslog/../../lib/ExtUtils/typemap'  Syslog.xs > Syslog.xsc
mv Syslog.xsc Syslog.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.35\" -DXS_VERSION=\"0.35\" -fPIC "-I../.."   Syslog.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Sys-Syslog/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Syslog.bs ../../lib/auto/Sys/Syslog/Syslog.bs 644
rm -f ../../lib/auto/Sys/Syslog/Syslog.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Syslog.o  -o ../../lib/auto/Sys/Syslog/Syslog.so  \
      \
  
chmod 755 ../../lib/auto/Sys/Syslog/Syslog.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Sys-Syslog'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Tie/Hash/NamedCapture/NamedCapture.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Tie::Hash::NamedCapture
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Tie-Hash-NamedCapture'
Running Mkbootstrap for NamedCapture ()
chmod 644 "NamedCapture.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Tie-Hash-NamedCapture/../../lib/ExtUtils/typemap'  NamedCapture.xs > NamedCapture.xsc
mv NamedCapture.xsc NamedCapture.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.10\" -DXS_VERSION=\"0.10\" -fPIC "-I../.."   NamedCapture.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Tie-Hash-NamedCapture/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- NamedCapture.bs ../../lib/auto/Tie/Hash/NamedCapture/NamedCapture.bs 644
rm -f ../../lib/auto/Tie/Hash/NamedCapture/NamedCapture.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  NamedCapture.o  -o ../../lib/auto/Tie/Hash/NamedCapture/NamedCapture.so  \
      \
  
chmod 755 ../../lib/auto/Tie/Hash/NamedCapture/NamedCapture.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/Tie-Hash-NamedCapture'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Time/HiRes/HiRes.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Configuring Time::HiRes...
Using hints hints/linux.pl...
Extra libraries: -lrt...
Have syscall()... looking for syscall.h... found <syscall.h>.
Looking for gettimeofday()... found.
Looking for setitimer()... found.
Looking for getitimer()... found.
You have interval timers (both setitimer and getitimer).
Looking for ualarm()... found.
Looking for usleep()... found.
Looking for nanosleep()... believing $Config{d_nanosleep}... found.
You can mix subsecond sleeps with signals, if you want to.
(It's still not portable, though.)
Looking for clockid_t... found.
Looking for clock_gettime()... found.
Looking for clock_getres()... found.
Looking for clock_nanosleep()... found.
Looking for clock()... found.
Looking for working futimens()... found.
Looking for working utimensat()... found.
You seem to have subsecond timestamp setting.
Looking for stat() subsecond timestamps...
Trying struct stat st_atimespec.tv_nsec...NOT found.
Trying struct stat st_atimensec...NOT found.
Trying struct stat st_atime_n...NOT found.
Trying struct stat st_atim.tv_nsec...found.
Trying struct stat st_uatime...NOT found.
You seem to have subsecond timestamp reading.
(Your struct stat has them, but the filesystems must help.)
Warning (mostly harmless): No library found for -lrt
Generating a Unix-style Makefile
Writing Makefile for Time::HiRes
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Time-HiRes'
Running Mkbootstrap for HiRes ()
chmod 644 "HiRes.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Time-HiRes/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Time-HiRes/typemap'  HiRes.xs > HiRes.xsc
mv HiRes.xsc HiRes.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.9759\" -DXS_VERSION=\"1.9759\" -fPIC "-I../.."  -DTIME_HIRES_NANOSLEEP -DTIME_HIRES_CLOCKID_T -DHAS_FUTIMENS -DHAS_UTIMENSAT -DTIME_HIRES_UTIME -DTIME_HIRES_STAT_XTIM -DTIME_HIRES_STAT=4 -DATLEASTFIVEOHOHFIVE HiRes.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Time-HiRes/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- HiRes.bs ../../lib/auto/Time/HiRes/HiRes.bs 644
rm -f ../../lib/auto/Time/HiRes/HiRes.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  HiRes.o  -o ../../lib/auto/Time/HiRes/HiRes.so  \
      \
  
chmod 755 ../../lib/auto/Time/HiRes/HiRes.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Time-HiRes'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Time/Piece/Piece.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for Time::Piece
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Time-Piece'
Running Mkbootstrap for Piece ()
chmod 644 "Piece.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Time-Piece/../../lib/ExtUtils/typemap'  Piece.xs > Piece.xsc
mv Piece.xsc Piece.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.3204\" -DXS_VERSION=\"1.3204\" -fPIC "-I../.."   Piece.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Time-Piece/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Piece.bs ../../lib/auto/Time/Piece/Piece.bs 644
rm -f ../../lib/auto/Time/Piece/Piece.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Piece.o  -o ../../lib/auto/Time/Piece/Piece.so  \
      \
  
chmod 755 ../../lib/auto/Time/Piece/Piece.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Time-Piece'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/Unicode/Collate/Collate.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Making header files for XS...
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Unicode-Collate'
Running Mkbootstrap for Collate ()
chmod 644 "Collate.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Unicode-Collate/../../lib/ExtUtils/typemap'  Collate.xs > Collate.xsc
mv Collate.xsc Collate.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.25\" -DXS_VERSION=\"1.25\" -fPIC "-I../.."   Collate.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Unicode-Collate/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Collate.bs ../../lib/auto/Unicode/Collate/Collate.bs 644
rm -f ../../lib/auto/Unicode/Collate/Collate.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  Collate.o  -o ../../lib/auto/Unicode/Collate/Collate.so  \
      \
  
chmod 755 ../../lib/auto/Unicode/Collate/Collate.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/cpan/Unicode-Collate'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/XS/APItest/APItest.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for XS::APItest
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/XS-APItest'
Running Mkbootstrap for APItest ()
Writing APItest.bs
chmod 644 "APItest.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/XS-APItest/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/XS-APItest/typemap'  APItest.xs > APItest.xsc
mv APItest.xsc APItest.c
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/XS-APItest/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/XS-APItest/typemap'  XSUB-undef-XS_VERSION.xs > XSUB-undef-XS_VERSION.xsc
mv XSUB-undef-XS_VERSION.xsc XSUB-undef-XS_VERSION.c
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/XS-APItest/../../lib/ExtUtils/typemap' -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/XS-APItest/typemap'  XSUB-redefined-macros.xs > XSUB-redefined-macros.xsc
mv XSUB-redefined-macros.xsc XSUB-redefined-macros.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wno-deprecated-declarations -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.98\" -DXS_VERSION=\"0.98\" -fPIC "-I../.."   core.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wno-deprecated-declarations -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.98\" -DXS_VERSION=\"0.98\" -fPIC "-I../.."   exception.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wno-deprecated-declarations -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.98\" -DXS_VERSION=\"0.98\" -fPIC "-I../.."   notcore.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wno-deprecated-declarations -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.98\" -DXS_VERSION=\"0.98\" -fPIC "-I../.."   APItest.c
In file included from ../../perl.h:2465,
                 from APItest.xs:10:
APItest.xs: In function 'XS_XS__APItest__Magic_test_toLOWER_LC':
../../handy.h:1655:39: warning: operand of ?: changes signedness from 'int' to 'UV' {aka 'long unsigned int'} due to unsignedness of other operand [-Wsign-compare]
 #  define toLOWER_LC(c) (isascii(c) ? tolower(c) : (c))
                                       ^~~~~~~~~~
APItest.xs:6373:18: note: in expansion of macro 'toLOWER_LC'
         RETVAL = toLOWER_LC(ord);
                  ^~~~~~~~~~
APItest.xs: In function 'XS_XS__APItest__Magic_test_toFOLD_LC':
../../handy.h:1657:38: warning: operand of ?: changes signedness from 'int' to 'UV' {aka 'long unsigned int'} due to unsignedness of other operand [-Wsign-compare]
 #  define toFOLD_LC(c) (isascii(c) ? tolower(c) : (c))
                                      ^~~~~~~~~~
APItest.xs:6463:18: note: in expansion of macro 'toFOLD_LC'
         RETVAL = toFOLD_LC(ord);
                  ^~~~~~~~~
APItest.xs: In function 'XS_XS__APItest__Magic_test_toUPPER_LC':
../../handy.h:1656:39: warning: operand of ?: changes signedness from 'int' to 'UV' {aka 'long unsigned int'} due to unsignedness of other operand [-Wsign-compare]
 #  define toUPPER_LC(c) (isascii(c) ? toupper(c) : (c))
                                       ^~~~~~~~~~
APItest.xs:6553:18: note: in expansion of macro 'toUPPER_LC'
         RETVAL = toUPPER_LC(ord);
                  ^~~~~~~~~~
In file included from APItest.xs:10:
APItest.c: In function 'XS_XS__APItest__Magic_test_Gconvert':
../../config.h:928:39: warning: '%.*g' directive writing between 1 and 106 bytes into a region of size 100 [-Wformat-overflow=]
 #define Gconvert(x,n,t,b) sprintf((b),"%.*g",(n),(x))
                                       ^~~~~~
../../perl.h:392:67: note: in definition of macro 'PERL_UNUSED_RESULT'
 #    define PERL_UNUSED_RESULT(v) STMT_START { __typeof__(v) z = (v); (void)sizeof(z); } STMT_END
                                                                   ^
APItest.xs:6725:28: note: in expansion of macro 'Gconvert'
         PERL_UNUSED_RESULT(Gconvert(SvNV(number), len,
                            ^~~~~~~~
../../config.h:928:39: note: assuming directive output of 105 bytes
 #define Gconvert(x,n,t,b) sprintf((b),"%.*g",(n),(x))
                                       ^~~~~~
../../perl.h:392:67: note: in definition of macro 'PERL_UNUSED_RESULT'
 #    define PERL_UNUSED_RESULT(v) STMT_START { __typeof__(v) z = (v); (void)sizeof(z); } STMT_END
                                                                   ^
APItest.xs:6725:28: note: in expansion of macro 'Gconvert'
         PERL_UNUSED_RESULT(Gconvert(SvNV(number), len,
                            ^~~~~~~~
../../config.h:928:27: note: 'sprintf' output between 2 and 107 bytes into a destination of size 100
 #define Gconvert(x,n,t,b) sprintf((b),"%.*g",(n),(x))
../../perl.h:392:67: note: in definition of macro 'PERL_UNUSED_RESULT'
 #    define PERL_UNUSED_RESULT(v) STMT_START { __typeof__(v) z = (v); (void)sizeof(z); } STMT_END
                                                                   ^
APItest.xs:6725:28: note: in expansion of macro 'Gconvert'
         PERL_UNUSED_RESULT(Gconvert(SvNV(number), len,
                            ^~~~~~~~
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wno-deprecated-declarations -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.98\" -DXS_VERSION=\"0.98\" -fPIC "-I../.."   XSUB-undef-XS_VERSION.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wno-deprecated-declarations -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.98\" -DXS_VERSION=\"0.98\" -fPIC "-I../.."   XSUB-redefined-macros.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/XS-APItest/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- APItest.bs ../../lib/auto/XS/APItest/APItest.bs 644
rm -f ../../lib/auto/XS/APItest/APItest.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  APItest.o XSUB-undef-XS_VERSION.o XSUB-redefined-macros.o core.o exception.o notcore.o  -o ../../lib/auto/XS/APItest/APItest.so  \
      \
  
chmod 755 ../../lib/auto/XS/APItest/APItest.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/XS-APItest'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/XS/Typemap/Typemap.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for XS::Typemap
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/XS-Typemap'
Running Mkbootstrap for Typemap ()
chmod 644 "Typemap.bs"
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.16\" -DXS_VERSION=\"0.16\" -fPIC "-I../.."   stdio.c
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/XS-Typemap/../../lib/ExtUtils/typemap'  Typemap.xs > Typemap.xsc
mv Typemap.xsc Typemap.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.16\" -DXS_VERSION=\"0.16\" -fPIC "-I../.."   Typemap.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/XS-Typemap/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- Typemap.bs ../../lib/auto/XS/Typemap/Typemap.bs 644
rm -f ../../lib/auto/XS/Typemap/Typemap.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  stdio.o  Typemap.o  -o ../../lib/auto/XS/Typemap/Typemap.so  \
      \
  
chmod 755 ../../lib/auto/XS/Typemap/Typemap.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/XS-Typemap'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/arybase/arybase.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for arybase
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/arybase'
Running Mkbootstrap for arybase ()
chmod 644 "arybase.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/arybase/../../lib/ExtUtils/typemap'  arybase.xs > arybase.xsc
mv arybase.xsc arybase.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.15\" -DXS_VERSION=\"0.15\" -fPIC "-I../.."   arybase.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/arybase/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- arybase.bs ../../lib/auto/arybase/arybase.bs 644
rm -f ../../lib/auto/arybase/arybase.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  arybase.o  -o ../../lib/auto/arybase/arybase.so  \
      \
  
chmod 755 ../../lib/auto/arybase/arybase.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/arybase'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/attributes/attributes.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for attributes
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/attributes'
/bin/sh: 1: /openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/attributes/../../../../../../staging_dir/hostpkg/usr/bin/perl: Text file busy
make[5]: *** [Makefile:397: ../../lib/auto/attributes/.exists] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/attributes'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/attributes'
Running Mkbootstrap for attributes ()
chmod 644 "attributes.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/attributes/../../lib/ExtUtils/typemap'  attributes.xs > attributes.xsc
mv attributes.xsc attributes.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.33\" -DXS_VERSION=\"0.33\" -fPIC "-I../.."   attributes.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/attributes/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- attributes.bs ../../lib/auto/attributes/attributes.bs 644
rm -f ../../lib/auto/attributes/attributes.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  attributes.o  -o ../../lib/auto/attributes/attributes.so  \
      \
  
chmod 755 ../../lib/auto/attributes/attributes.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/attributes'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/mro/mro.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for mro
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/mro'
Running Mkbootstrap for mro ()
chmod 644 "mro.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/mro/../../lib/ExtUtils/typemap'  mro.xs > mro.xsc
mv mro.xsc mro.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.22\" -DXS_VERSION=\"1.22\" -fPIC "-I../.."   mro.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/mro/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- mro.bs ../../lib/auto/mro/mro.bs 644
rm -f ../../lib/auto/mro/mro.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  mro.o  -o ../../lib/auto/mro/mro.so  \
      \
  
chmod 755 ../../lib/auto/mro/mro.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/mro'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/re/re.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Generating a Unix-style Makefile
Writing Makefile for re
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/re'
Running Mkbootstrap for re ()
chmod 644 "re.bs"
rm -f re_exec.c
cp ../../regexec.c re_exec.c
rm -f invlist_inline.h
cp ../../invlist_inline.h invlist_inline.h
rm -f re_comp.c
cp ../../regcomp.c re_comp.c
rm -f dquote.c
cp ../../dquote.c dquote.c
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp" -noprototypes -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/re/../../lib/ExtUtils/typemap'  re.xs > re.xsc
mv re.xsc re.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.36\" -DXS_VERSION=\"0.36\" -fPIC "-I../.."  -DPERL_EXT_RE_BUILD -DPERL_EXT_RE_DEBUG -DPERL_EXT re_exec.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.36\" -DXS_VERSION=\"0.36\" -fPIC "-I../.."  -DPERL_EXT_RE_BUILD -DPERL_EXT_RE_DEBUG -DPERL_EXT re_comp.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"0.36\" -DXS_VERSION=\"0.36\" -fPIC "-I../.."  -DPERL_EXT_RE_BUILD -DPERL_EXT_RE_DEBUG -DPERL_EXT re.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/re/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- re.bs ../../lib/auto/re/re.bs 644
rm -f ../../lib/auto/re/re.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  re_exec.o re_comp.o re.o  -o ../../lib/auto/re/re.so  \
      \
  
chmod 755 ../../lib/auto/re/re.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/ext/re'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/threads/threads.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Warning (mostly harmless): No library found for -lpthread
Generating a Unix-style Makefile
Writing Makefile for threads
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/threads'
Running Mkbootstrap for threads ()
chmod 644 "threads.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/threads/../../lib/ExtUtils/typemap'  threads.xs > threads.xsc
mv threads.xsc threads.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"2.22\" -DXS_VERSION=\"2.22\" -fPIC "-I../.."   threads.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/threads/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- threads.bs ../../lib/auto/threads/threads.bs 644
rm -f ../../lib/auto/threads/threads.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  threads.o  -o ../../lib/auto/threads/threads.so  \
      \
  
chmod 755 ../../lib/auto/threads/threads.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/threads'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. make_ext.pl lib/auto/threads/shared/shared.so  MAKE="make" LIBPERL_A=libperl.so LINKTYPE=dynamic
Warning (mostly harmless): No library found for -lpthread
Generating a Unix-style Makefile
Writing Makefile for threads::shared
Writing MYMETA.yml and MYMETA.json
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/threads-shared'
Running Mkbootstrap for shared ()
chmod 644 "shared.bs"
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" "../../lib/ExtUtils/xsubpp"  -typemap '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/threads-shared/../../lib/ExtUtils/typemap'  shared.xs > shared.xsc
mv shared.xsc shared.c
ccache_cc -c   -D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing -pipe -fstack-protector-strong -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/include -Wall -Werror=declaration-after-statement -Werror=pointer-arith -Wextra -Wc++-compat -Wwrite-strings -O2   -DVERSION=\"1.58\" -DXS_VERSION=\"1.58\" -fPIC "-I../.."   shared.c
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/threads-shared/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command::MM -e 'cp_nonempty' -- shared.bs ../../lib/auto/threads/shared/shared.bs 644
rm -f ../../lib/auto/threads/shared/shared.so
ccache_cc  -shared -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-x86_64_gcc-8.4.0_musl/lib -znow -zrelro  shared.o  -o ../../lib/auto/threads/shared/shared.so  \
      \
  
chmod 755 ../../lib/auto/threads/shared/shared.so
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/threads-shared'
 
	Making utilities
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/utils'
../miniperl -I../lib corelist.PL
Extracting corelist (with variable substitutions)
../miniperl -I../lib cpan.PL
Extracting cpan (with variable substitutions)
../miniperl -I../lib h2ph.PL
Extracting h2ph (with variable substitutions)
../miniperl -I../lib h2xs.PL
Extracting h2xs (with variable substitutions)
../miniperl -I../lib instmodsh.PL
Extracting instmodsh (with variable substitutions)
../miniperl -I../lib json_pp.PL
Extracting json_pp (with variable substitutions)
../miniperl -I../lib perlbug.PL
Extracting perlbug (with variable substitutions)
../miniperl -I../lib perldoc.PL
Extracting "perldoc" (with variable substitutions)
../miniperl -I../lib perlivp.PL
Extracting perlivp (with variable substitutions)
../miniperl -I../lib pl2pm.PL
Extracting pl2pm (with variable substitutions)
../miniperl -I../lib prove.PL
Extracting prove (with variable substitutions)
../miniperl -I../lib ptar.PL
Extracting ptar (with variable substitutions)
../miniperl -I../lib ptardiff.PL
Extracting ptardiff (with variable substitutions)
../miniperl -I../lib ptargrep.PL
Extracting ptargrep (with variable substitutions)
../miniperl -I../lib shasum.PL
Extracting shasum (with variable substitutions)
../miniperl -I../lib splain.PL
Extracting splain (with variable substitutions)
../miniperl -I../lib libnetcfg.PL
Extracting libnetcfg (with variable substitutions)
../miniperl -I../lib piconv.PL
Extracting piconv (with variable substitutions)
../miniperl -I../lib enc2xs.PL
Extracting enc2xs (with variable substitutions)
../miniperl -I../lib encguess.PL
Extracting encguess (with variable substitutions)
../miniperl -I../lib xsubpp.PL
Extracting xsubpp (with variable substitutions)
../miniperl -I../lib pod2html.PL
Extracting pod2html (with variable substitutions)
../miniperl -I../lib zipdetails.PL
Extracting zipdetails (with variable substitutions)
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/utils'
cd dist/Storable ; LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 make lib/Storable/Limit.pm
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Storable'
/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Storable/../../../../../../staging_dir/hostpkg/usr/bin/perl "-I../../lib" -MExtUtils::Command -e 'mkpath' -- ../../lib
"../../../../../../staging_dir/hostpkg/usr/bin/perl" "-I../../lib" stacksize --core
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/dist/Storable'
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1  ./miniperl -Ilib -I. -f pod/buildtoc -q
test -d lib/Storable || mkdir lib/Storable
cp dist/Storable/lib/Storable/Limit.pm lib/Storable/Limit.pm
 
	Everything is up to date. Type 'make test' to run test suite.
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1'
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1'
/bin/ln -s /openwrt/staging_dir/hostpkg/usr/bin/generate_uudmap generate_uudmap
LD_LIBRARY_PATH=/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1 ./miniperl -Ilib -I. autodoc.pl
/bin/sh: 1: ./miniperl: Text file busy
make[4]: *** [makefile:408: pod/perlintern.pod] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1'
make[3]: *** [Makefile:152: /openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/.built] Error 2
```
