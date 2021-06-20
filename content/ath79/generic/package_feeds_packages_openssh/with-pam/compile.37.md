---
title: "compile.37"
date: 2021-06-20 22:39:07.390646
hidden: false
draft: false
weight: -37
---

build number: `37`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/openssh/compile -j$(nproc) || make package/feeds/packages/openssh/compile V=s
```

#### Compile.txt

``` bash
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
checking for mips-openwrt-linux-cc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking if ccache_cc supports C99-style variadic macros... yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
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
checking whether byte ordering is bigendian... (cached) yes
checking for gawk... gawk
checking how to run the C preprocessor... ccache_cc -E
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking for egrep... (cached) /openwrt/staging_dir/host/bin/grep -E
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking for cat... /usr/bin/cat
checking for kill... /usr/bin/kill
checking for sed... /openwrt/staging_dir/host/bin/sed
checking for bash... /openwrt/staging_dir/host/bin/bash
checking for ksh... (cached) /openwrt/staging_dir/host/bin/bash
checking for sh... (cached) /openwrt/staging_dir/host/bin/bash
checking for sh... /usr/bin/sh
checking for groff... no
checking for nroff... no
checking for mandoc... no
configure: WARNING: no manpage formatter found
checking for groupadd... /usr/sbin/groupadd
checking for useradd... /usr/sbin/useradd
checking for pkgmk... no
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for passwd... /usr/bin/passwd
checking for inline... inline
checking whether LLONG_MAX is declared... yes
checking whether LONG_LONG_MAX is declared... no
checking whether SYSTR_POLICY_KILL is declared... no
checking whether RLIMIT_NPROC is declared... yes
checking whether PR_SET_NO_NEW_PRIVS is declared... yes
checking whether OpenSSL will be used for cryptography... yes
checking if ccache_cc supports -Werror... yes
checking if ccache_cc supports compile flag -pipe... yes
checking if ccache_cc supports compile flag -Wunknown-warning-option... no
checking if ccache_cc supports compile flag -Wno-error=format-truncation... yes
checking if ccache_cc supports compile flag -Qunused-arguments... no
checking if ccache_cc supports compile flag -Wall... yes
checking if ccache_cc supports compile flag -Wextra... yes
checking if ccache_cc supports compile flag -Wpointer-arith... yes
checking if ccache_cc supports compile flag -Wuninitialized... yes
checking if ccache_cc supports compile flag -Wsign-compare... yes
checking if ccache_cc supports compile flag -Wformat-security... yes
checking if ccache_cc supports compile flag -Wsizeof-pointer-memaccess... yes
checking if ccache_cc supports compile flag -Wpointer-sign... yes
checking if ccache_cc supports compile flag -Wunused-parameter... yes
checking if ccache_cc supports compile flag -Wunused-result... yes
checking if ccache_cc supports compile flag -Wimplicit-fallthrough... yes
checking if ccache_cc supports compile flag -fno-strict-aliasing... yes
checking if ccache_cc supports compile flag -mretpoline... no
checking if ccache_cc supports link flag -Wl,-z,retpolineplt... no
checking if ccache_cc supports compile flag -D_FORTIFY_SOURCE=2... no
checking if ccache_cc supports link flag -Wl,-z,relro... yes
checking if ccache_cc supports link flag -Wl,-z,now... yes
checking if ccache_cc supports link flag -Wl,-z,noexecstack... yes
checking if ccache_cc supports compile flag -ftrapv and linking succeeds... yes
checking gcc version... 8.4.0
checking if ccache_cc accepts -fno-builtin-memset... yes
checking if ccache_cc supports -fstack-protector-strong... yes
checking if -fstack-protector-strong works... configure: WARNING: cross compiling: cannot test
checking if compiler allows __attribute__ on return types... yes
checking if compiler allows __attribute__ prototype args... yes
checking if compiler supports variable length arrays... yes
checking blf.h usability... no
checking blf.h presence... no
checking for blf.h... no
checking bstring.h usability... no
checking bstring.h presence... no
checking for bstring.h... no
checking crypt.h usability... yes
checking crypt.h presence... yes
checking for crypt.h... yes
checking crypto/sha2.h usability... no
checking crypto/sha2.h presence... no
checking for crypto/sha2.h... no
checking dirent.h usability... yes
checking dirent.h presence... yes
checking for dirent.h... yes
checking endian.h usability... yes
checking endian.h presence... yes
checking for endian.h... yes
checking elf.h usability... yes
checking elf.h presence... yes
checking for elf.h... yes
checking err.h usability... yes
checking err.h presence... yes
checking for err.h... yes
checking features.h usability... yes
checking features.h presence... yes
checking for features.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking floatingpoint.h usability... no
checking floatingpoint.h presence... no
checking for floatingpoint.h... no
checking fnmatch.h usability... yes
checking fnmatch.h presence... yes
checking for fnmatch.h... yes
checking getopt.h usability... yes
checking getopt.h presence... yes
checking for getopt.h... yes
checking glob.h usability... yes
checking glob.h presence... yes
checking for glob.h... yes
checking ia.h usability... no
checking ia.h presence... no
checking for ia.h... no
checking iaf.h usability... no
checking iaf.h presence... no
checking for iaf.h... no
checking ifaddrs.h usability... yes
checking ifaddrs.h presence... yes
checking for ifaddrs.h... yes
checking for inttypes.h... (cached) yes
checking langinfo.h usability... yes
checking langinfo.h presence... yes
checking for langinfo.h... yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking locale.h usability... yes
checking locale.h presence... yes
checking for locale.h... yes
checking login.h usability... no
checking login.h presence... no
checking for login.h... no
checking maillock.h usability... no
checking maillock.h presence... no
checking for maillock.h... no
checking ndir.h usability... no
checking ndir.h presence... no
checking for ndir.h... no
checking net/if_tun.h usability... no
checking net/if_tun.h presence... no
checking for net/if_tun.h... no
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking netgroup.h usability... no
checking netgroup.h presence... no
checking for netgroup.h... no
checking pam/pam_appl.h usability... no
checking pam/pam_appl.h presence... no
checking for pam/pam_appl.h... no
checking paths.h usability... yes
checking paths.h presence... yes
checking for paths.h... yes
checking poll.h usability... yes
checking poll.h presence... yes
checking for poll.h... yes
checking pty.h usability... yes
checking pty.h presence... yes
checking for pty.h... yes
checking readpassphrase.h usability... no
checking readpassphrase.h presence... no
checking for readpassphrase.h... no
checking rpc/types.h usability... no
checking rpc/types.h presence... no
checking for rpc/types.h... no
checking security/pam_appl.h usability... yes
checking security/pam_appl.h presence... yes
checking for security/pam_appl.h... yes
checking sha2.h usability... no
checking sha2.h presence... no
checking for sha2.h... no
checking shadow.h usability... yes
checking shadow.h presence... yes
checking for shadow.h... yes
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking for stdint.h... (cached) yes
checking for string.h... (cached) yes
checking for strings.h... (cached) yes
checking sys/bitypes.h usability... no
checking sys/bitypes.h presence... no
checking for sys/bitypes.h... no
checking sys/byteorder.h usability... no
checking sys/byteorder.h presence... no
checking for sys/byteorder.h... no
checking sys/bsdtty.h usability... no
checking sys/bsdtty.h presence... no
checking for sys/bsdtty.h... no
checking sys/cdefs.h usability... yes
checking sys/cdefs.h presence... yes
checking for sys/cdefs.h... yes
checking sys/dir.h usability... yes
checking sys/dir.h presence... yes
checking for sys/dir.h... yes
checking sys/file.h usability... yes
checking sys/file.h presence... yes
checking for sys/file.h... yes
checking sys/mman.h usability... yes
checking sys/mman.h presence... yes
checking for sys/mman.h... yes
checking sys/label.h usability... no
checking sys/label.h presence... no
checking for sys/label.h... no
checking sys/ndir.h usability... no
checking sys/ndir.h presence... no
checking for sys/ndir.h... no
checking sys/poll.h usability... yes
checking sys/poll.h presence... yes
checking for sys/poll.h... yes
checking sys/prctl.h usability... yes
checking sys/prctl.h presence... yes
checking for sys/prctl.h... yes
checking sys/pstat.h usability... no
checking sys/pstat.h presence... no
checking for sys/pstat.h... no
checking sys/ptrace.h usability... yes
checking sys/ptrace.h presence... yes
checking for sys/ptrace.h... yes
checking sys/random.h usability... yes
checking sys/random.h presence... yes
checking for sys/random.h... yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking for sys/stat.h... (cached) yes
checking sys/stream.h usability... no
checking sys/stream.h presence... no
checking for sys/stream.h... no
checking sys/stropts.h usability... yes
checking sys/stropts.h presence... yes
checking for sys/stropts.h... yes
checking sys/strtio.h usability... no
checking sys/strtio.h presence... no
checking for sys/strtio.h... no
checking sys/statvfs.h usability... yes
checking sys/statvfs.h presence... yes
checking for sys/statvfs.h... yes
checking sys/sysmacros.h usability... yes
checking sys/sysmacros.h presence... yes
checking for sys/sysmacros.h... yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking sys/timers.h usability... no
checking sys/timers.h presence... no
checking for sys/timers.h... no
checking sys/vfs.h usability... yes
checking sys/vfs.h presence... yes
checking for sys/vfs.h... yes
checking time.h usability... yes
checking time.h presence... yes
checking for time.h... yes
checking tmpdir.h usability... no
checking tmpdir.h presence... no
checking for tmpdir.h... no
checking ttyent.h usability... no
checking ttyent.h presence... no
checking for ttyent.h... no
checking ucred.h usability... no
checking ucred.h presence... no
checking for ucred.h... no
checking for unistd.h... (cached) yes
checking usersec.h usability... no
checking usersec.h presence... no
checking for usersec.h... no
checking util.h usability... no
checking util.h presence... no
checking for util.h... no
checking utime.h usability... yes
checking utime.h presence... yes
checking for utime.h... yes
checking utmp.h usability... yes
checking utmp.h presence... yes
checking for utmp.h... yes
checking utmpx.h usability... yes
checking utmpx.h presence... yes
checking for utmpx.h... yes
checking vis.h usability... no
checking vis.h presence... no
checking for vis.h... no
checking wchar.h usability... yes
checking wchar.h presence... yes
checking for wchar.h... yes
checking for sys/audit.h... no
checking for sys/capsicum.h... no
checking for net/route.h... yes
checking for sys/sysctl.h... no
checking for lastlog.h... yes
checking for sys/ptms.h... no
checking for login_cap.h... no
checking for sys/mount.h... yes
checking for sys/un.h... yes
checking linux/if_tun.h usability... yes
checking linux/if_tun.h presence... yes
checking for linux/if_tun.h... yes
checking for linux/if.h... yes
checking for linux/seccomp.h... yes
checking for linux/filter.h... yes
checking for linux/audit.h... yes
checking for seccomp architecture... "AUDIT_ARCH_MIPS"
checking compiler and flags for sanity... configure: WARNING: cross compiling: not checking compiler sanity
checking for setsockopt... yes
checking for dirname... yes
checking libgen.h usability... yes
checking libgen.h presence... yes
checking for libgen.h... yes
checking for getspnam... yes
checking for library containing basename... none required
checking for zlib... yes
checking zlib.h usability... yes
checking zlib.h presence... yes
checking for zlib.h... yes
checking for deflate in -lz... yes
checking for possibly buggy zlib... configure: WARNING: cross compiling: not checking zlib version
checking for strcasecmp... yes
checking for utimes... (cached) yes
checking bsd/libutil.h usability... yes
checking bsd/libutil.h presence... yes
checking for bsd/libutil.h... yes
checking libutil.h usability... no
checking libutil.h presence... no
checking for libutil.h... no
checking for library containing fmt_scaled... no
checking for library containing scan_scaled... no
checking for library containing login... no
checking for library containing logout... no
checking for library containing logwtmp... no
checking for library containing openpty... none required
checking for library containing updwtmp... none required
checking for fmt_scaled... no
checking for scan_scaled... no
checking for login... no
checking for logout... no
checking for openpty... yes
checking for updwtmp... yes
checking for logwtmp... no
checking for library containing inet_ntop... none required
checking for library containing gethostbyname... none required
checking for library containing SHA256Update... no
checking for strftime... (cached) yes
checking for stdlib.h... (cached) yes
checking for GNU libc compatible malloc... (cached) yes
checking for stdlib.h... (cached) yes
checking for GNU libc compatible realloc... (cached) yes
checking if calloc(0, N) returns non-null... configure: WARNING: cross compiling: assuming same as malloc
yes
checking for GLOB_ALTDIRFUNC support... no
checking for gl_matchc field in glob_t... no
checking for gl_statv and GLOB_KEEPSTAT extensions for glob... no
checking whether GLOB_NOMATCH is declared... yes
checking whether VIS_ALL is declared... no
checking whether struct dirent allocates space for d_name... configure: WARNING: cross compiling: assuming BROKEN_ONE_BYTE_DIRENT_D_NAME
checking for /proc/pid/fd directory... yes
checking for gcc >= 4.x... yes
checking if ccache_cc supports compile flag -fPIE... yes
checking if ccache_cc supports link flag -pie... yes
checking whether both -fPIE and -pie are supported... yes
checking whether -fPIC is accepted... yes
checking for Blowfish_initstate... no
checking for Blowfish_expandstate... no
checking for Blowfish_expand0state... no
checking for Blowfish_stream2word... no
checking for SHA256Update... no
checking for SHA384Update... no
checking for SHA512Update... no
checking for asprintf... yes
checking for b64_ntop... no
checking for __b64_ntop... no
checking for b64_pton... no
checking for __b64_pton... no
checking for bcopy... (cached) yes
checking for bcrypt_pbkdf... no
checking for bindresvport_sa... no
checking for blf_enc... no
checking for bzero... (cached) yes
checking for cap_rights_limit... no
checking for clock... yes
checking for closefrom... no
checking for dirfd... yes
checking for endgrent... yes
checking for err... yes
checking for errx... yes
checking for explicit_bzero... yes
checking for explicit_memset... no
checking for fchmod... (cached) yes
checking for fchmodat... yes
checking for fchown... yes
checking for fchownat... yes
checking for flock... yes
checking for fnmatch... yes
checking for freeaddrinfo... yes
checking for freezero... no
checking for fstatfs... yes
checking for fstatvfs... yes
checking for futimes... yes
checking for getaddrinfo... (cached) yes
checking for getcwd... (cached) yes
checking for getgrouplist... yes
checking for getline... yes
checking for getnameinfo... yes
checking for getopt... yes
checking for getpagesize... yes
checking for getpeereid... no
checking for getpeerucred... no
checking for getpgid... yes
checking for _getpty... no
checking for getrlimit... yes
checking for getrandom... yes
checking for getsid... yes
checking for getttyent... no
checking for glob... yes
checking for group_from_gid... no
checking for inet_aton... yes
checking for inet_ntoa... yes
checking for inet_ntop... yes
checking for innetgr... no
checking for llabs... yes
checking for localtime_r... yes
checking for login_getcapbool... no
checking for login_getpwclass... no
checking for md5_crypt... no
checking for memmem... yes
checking for memmove... yes
checking for memset_s... no
checking for mkdtemp... yes
checking for ngetaddrinfo... no
checking for nsleep... no
checking for ogetaddrinfo... no
checking for openlog_r... no
checking for pledge... no
checking for poll... yes
checking for prctl... yes
checking for pstat... no
checking for raise... yes
checking for readpassphrase... no
checking for reallocarray... no
checking for realpath... yes
checking for recvmsg... yes
checking for recallocarray... no
checking for rresvport_af... no
checking for sendmsg... yes
checking for setdtablesize... no
checking for setegid... yes
checking for setenv... yes
checking for seteuid... yes
checking for setgroupent... no
checking for setgroups... yes
checking for setlinebuf... yes
checking for setlogin... no
checking for setpassent... no
checking for setpcred... no
checking for setproctitle... no
checking for setregid... yes
checking for setreuid... yes
checking for setrlimit... yes
checking for setsid... yes
checking for setvbuf... yes
checking for sigaction... yes
checking for sigvec... no
checking for snprintf... yes
checking for socketpair... yes
checking for statfs... yes
checking for statvfs... yes
checking for strcasestr... yes
checking for strdup... yes
checking for strerror... (cached) yes
checking for strlcat... yes
checking for strlcpy... yes
checking for strmode... no
checking for strndup... yes
checking for strnlen... yes
checking for strnvis... no
checking for strptime... yes
checking for strsignal... yes
checking for strtonum... no
checking for strtoll... yes
checking for strtoul... yes
checking for strtoull... yes
checking for swap32... no
checking for sysconf... yes
checking for tcgetpgrp... yes
checking for timingsafe_bcmp... no
checking for truncate... yes
checking for unsetenv... yes
checking for updwtmpx... yes
checking for utimensat... yes
checking for user_from_uid... no
checking for usleep... yes
checking for vasprintf... yes
checking for vsnprintf... (cached) yes
checking for waitpid... yes
checking for warn... yes
checking whether bzero is declared... yes
checking whether memmem is declared... no
checking for mblen... yes
checking for mbtowc... yes
checking for nl_langinfo... yes
checking for wcwidth... yes
checking for utf8 locale support... configure: WARNING: cross compiling: assuming yes
checking for library containing dlopen... none required
checking for dlopen... yes
checking whether RTLD_NOW is declared... yes
checking for gai_strerror... yes
checking for library containing nanosleep... none required
checking for library containing clock_gettime... none required
checking whether localtime_r is declared... yes
checking whether strsep is declared... yes
checking for strsep... yes
checking whether tcsendbreak is declared... yes
checking whether h_errno is declared... yes
checking whether SHUT_RD is declared... yes
checking whether getpeereid is declared... no
checking whether O_NONBLOCK is declared... yes
checking whether readv is declared... yes
checking whether writev is declared... yes
checking whether MAXSYMLINKS is declared... yes
checking whether offsetof is declared... yes
checking whether howmany is declared... yes
checking whether NFDBITS is declared... yes
checking for fd_mask... yes
checking for setresuid... (cached) no
checking for setresgid... yes
checking if setresgid seems to work... configure: WARNING: cross compiling: not checking setresuid
checking for working fflush(NULL)... configure: WARNING: cross compiling: assuming working
checking for gettimeofday... (cached) yes
checking for time... yes
checking for endutent... yes
checking for getutent... yes
checking for getutid... yes
checking for getutline... yes
checking for pututline... yes
checking for setutent... yes
checking for utmpname... yes
checking for endutxent... yes
checking for getutxent... yes
checking for getutxid... yes
checking for getutxline... yes
checking for getutxuser... no
checking for pututxline... yes
checking for setutxdb... no
checking for setutxent... yes
checking for utmpxname... yes
checking for getlastlogxbyname... no
checking for daemon... yes
checking for getpagesize... (cached) yes
checking whether snprintf correctly terminates long strings... configure: WARNING: cross compiling: Assuming working snprintf()
checking whether snprintf understands %zu... configure: WARNING: cross compiling: Assuming working snprintf()
checking whether vsnprintf returns correct values on overflow... configure: WARNING: cross compiling: Assuming working vsnprintf()
checking whether snprintf can declare const char *fmt... yes
checking whether system supports SO_PEERCRED getsockopt... yes
checking if openpty correctly handles controlling tty... cross-compiling, assuming yes
checking whether AI_NUMERICSERV is declared... yes
checking if SA_RESTARTed signals interrupt select()... configure: WARNING: cross compiling: assuming yes
checking for getpgrp... yes
checking if getpgrp accepts zero args... yes
configure: error: *** working libcrypto not found, check config.log
make[3]: *** [Makefile:267: /openwrt/build_dir/target-mips_24kc_musl/openssh-with-pam/openssh-8.6p1/.configured_a708d0c3539a2f3a09217c5527a5f9e6] Error 1
```
