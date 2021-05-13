---
title: "compile.14"
date: 2021-05-13 00:29:47.002191
hidden: false
draft: false
weight: -14
---

build number: `14`

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
Can't exec "../../miniperl": Text file busy at make_ext.pl line 513.
Unsuccessful Makefile.PL(ext/File-Glob): code=-1 at make_ext.pl line 518.
make[4]: *** [Makefile:579: lib/auto/File/Glob/Glob.so] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1'
make[3]: *** [Makefile:150: /openwrt/build_dir/target-x86_64_musl/perl/perl-5.28.1/.built] Error 2
```
