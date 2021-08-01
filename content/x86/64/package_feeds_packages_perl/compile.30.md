---
title: "compile.30"
date: 2021-06-09 21:56:39.868784
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
/bin/sh: 1: ./miniperl: Text file busy
make[4]: *** [Makefile:579: lib/auto/B/B.so] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1'
make[3]: *** [Makefile:150: /openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/.built] Error 2
```