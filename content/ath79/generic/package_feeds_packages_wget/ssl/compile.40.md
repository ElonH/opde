---
title: "compile.40"
date: 2021-06-22 10:51:50.619505
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
make package/feeds/packages/wget/compile -j$(nproc) || make package/feeds/packages/wget/compile V=s
```

#### Compile.txt

``` bash
configure: loading site script /openwrt/include/site/mips
configure: configuring for GNU Wget 1.21.1
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a race-free mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports the include directive... yes (GNU style)
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether the compiler supports GNU C... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to enable C11 features... none needed
checking whether ccache_cc understands -c and -o together... yes
checking whether the compiler is clang... no
checking for compiler option needed when checking for declarations... none
checking dependency style of ccache_cc... gcc3
checking for stdio.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for strings.h... yes
checking for sys/stat.h... yes
checking for sys/types.h... yes
checking for unistd.h... yes
checking for wchar.h... yes
checking for minix/config.h... no
checking for sys/socket.h... yes
checking for arpa/inet.h... yes
checking for features.h... yes
checking for sys/param.h... yes
checking for dirent.h... yes
checking for fnmatch.h... yes
checking for stdio_ext.h... yes
checking for netdb.h... yes
checking for netinet/in.h... yes
checking for getopt.h... yes
checking for sys/cdefs.h... yes
checking for termios.h... yes
checking for sys/time.h... yes
checking for threads.h... yes
checking for iconv.h... yes
checking for limits.h... yes
checking for crtdefs.h... no
checking for wctype.h... yes
checking for langinfo.h... yes
checking for xlocale.h... no
checking for sys/mman.h... yes
checking for sys/select.h... yes
checking for malloc.h... yes
checking for spawn.h... yes
checking for sys/file.h... yes
checking for sys/ioctl.h... yes
checking for sys/random.h... yes
checking for sys/uio.h... yes
checking for sys/wait.h... yes
checking for utime.h... yes
checking whether it is safe to define __EXTENSIONS__... yes
checking whether _XOPEN_SOURCE should be defined... no
checking for mips-openwrt-linux-gcc... (cached) ccache_cc
checking whether the compiler supports GNU C... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to enable C11 features... (cached) none needed
checking whether ccache_cc understands -c and -o together... (cached) yes
checking whether the compiler is clang... (cached) no
checking for compiler option needed when checking for declarations... (cached) none
checking dependency style of ccache_cc... (cached) gcc3
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking whether make supports nested variables... (cached) yes
checking for library containing dlopen... none required
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for Minix Amsterdam compiler... no
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking for _LARGEFILE_SOURCE value needed for large files... no
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for a Python interpreter with version >= 3.0... python
checking for python... /openwrt/staging_dir/host/bin/python
checking for python version... 3.8
checking for python platform... linux
checking for python script directory... ${prefix}/lib/python3.8/site-packages
checking for python extension module directory... ${exec_prefix}/lib/python3.8/site-packages
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking whether NLS is requested... no
checking for msgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for gmsgfmt... /openwrt/staging_dir/hostpkg/bin/msgfmt
checking for xgettext... /openwrt/staging_dir/hostpkg/bin/xgettext
checking for msgmerge... /openwrt/staging_dir/hostpkg/bin/msgmerge
checking for ld... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for shared library run path origin... done
checking 32-bit host C ABI... yes
checking for ELF binary format... yes
checking for the common suffixes of directories in the library search path... lib,lib32,lib
checking for CFPreferencesCopyAppValue... no
checking for CFLocaleCopyCurrent... no
checking whether to use NLS... no
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking for flex... flex
checking for lex output file root... lex.yy
checking for lex library... none needed
checking for library containing yywrap... no
checking whether yytext is a pointer... yes
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking for working volatile... yes
checking for egrep... (cached) /openwrt/staging_dir/host/bin/grep -E
checking for special C compiler options needed for large files... (cached) no
checking for _FILE_OFFSET_BITS value needed for large files... (cached) no
checking size of off_t... (cached) 8
checking for stdbool.h that conforms to C99... yes
checking for _Bool... yes
checking for unistd.h... (cached) yes
checking for sys/time.h... (cached) yes
checking for termios.h... (cached) yes
checking for sys/ioctl.h... (cached) yes
checking for sys/select.h... (cached) yes
checking for utime.h... (cached) yes
checking for sys/utime.h... no
checking for stdint.h... (cached) yes
checking for inttypes.h... (cached) yes
checking for pwd.h... yes
checking for wchar.h... (cached) yes
checking for dlfcn.h... yes
checking how ccache_cc reports undeclared, standard C functions... error
checking whether h_errno is declared... yes
checking size of long... (cached) 4
checking for size_t... yes
checking for pid_t... yes
checking for uint32_t... yes
checking for uintptr_t... yes
checking for intptr_t... yes
checking for int64_t... yes
checking for sig_atomic_t... yes
checking for iconv... yes
checking for working iconv... guessing yes
checking whether iconv is compatible with its POSIX signature... yes
checking whether the preprocessor supports include_next... yes
checking whether source code line length is unlimited... yes
checking for C/C++ restrict keyword... __restrict__
checking whether <sys/socket.h> is self-contained... yes
checking for shutdown... yes
checking whether <sys/socket.h> defines the SHUT_* macros... yes
checking for struct sockaddr_storage... yes
checking for sa_family_t... yes
checking for struct sockaddr_storage.ss_family... yes
checking for working alloca.h... yes
checking for alloca... yes
checking whether <wchar.h> uses 'inline' correctly... yes
checking for btowc... yes
checking for canonicalize_file_name... no
checking for faccessat... yes
checking for realpath... yes
checking for _set_invalid_parameter_handler... no
checking for fchdir... yes
checking for fcntl... yes
checking for symlink... yes
checking for fdopendir... yes
checking for mempcpy... yes
checking for flock... yes
checking for fnmatch... yes
checking for mbsrtowcs... yes
checking for fpurge... yes
checking for __fpurge... yes
checking for __freading... yes
checking for fstatat... yes
checking for futimens... yes
checking for getdelim... yes
checking for getdtablesize... yes
checking for getpass... yes
checking for __fsetlocking... yes
checking for getprogname... no
checking for getexecname... no
checking for getrandom... yes
checking for gettimeofday... (cached) yes
checking for isblank... yes
checking for iswcntrl... yes
checking for iswblank... yes
checking for link... yes
checking for lstat... (cached) yes
checking for mbsinit... yes
checking for mbrtowc... yes
checking for mprotect... yes
checking for mkostemp... yes
checking for mkstemp... yes
checking for nl_langinfo... yes
checking for openat... yes
checking for pipe... yes
checking for pipe2... yes
checking for posix_spawn_file_actions_addchdir_np... yes
checking for posix_spawn_file_actions_addchdir... no
checking for readlink... yes
checking for iswctype... yes
checking for secure_getenv... yes
checking for getuid... yes
checking for geteuid... yes
checking for getgid... yes
checking for getegid... yes
checking for sigaction... yes
checking for sigaltstack... yes
checking for siginterrupt... yes
checking for snprintf... yes
checking for strerror_r... yes
checking for __xpg_strerror_r... yes
checking for catgets... yes
checking for strndup... yes
checking for strptime... yes
checking for localtime_r... yes
checking for timegm... yes
checking for futimes... yes
checking for futimesat... yes
checking for utimensat... yes
checking for lutimes... yes
checking for vasnprintf... no
checking for wcrtomb... yes
checking for wcwidth... yes
checking for wmempcpy... no
checking for getpagesize... yes
checking for nl_langinfo and CODESET... yes
checking for a traditional french locale... none
checking whether lstat correctly handles trailing slash... guessing yes
checking whether // is distinct from /... unknown, assuming no
checking whether realpath works... guessing yes
checking whether linux/if_alg.h has struct sockaddr_alg.... yes
checking whether byte ordering is bigendian... (cached) yes
checking if environ is properly declared... yes
checking for complete errno.h... yes
checking whether strerror_r is declared... yes
checking whether strerror_r returns char *... no
checking for sig_atomic_t... (cached) yes
checking whether fchdir is declared... yes
checking for working fcntl.h... cross-compiling
checking for mode_t... yes
checking for eaccess... yes
checking for mbstate_t... yes
checking whether stdin defaults to large file offsets... yes
checking whether fseeko is declared... yes
checking for fseeko... yes
checking whether fflush works on input streams... cross
checking whether stat file-mode macros are broken... no
checking for nlink_t... yes
checking whether ftello is declared... yes
checking for ftello... yes
checking whether ftello works... guessing yes
checking for library containing gethostbyname... none required
checking for gethostbyname... yes
checking for library containing getservbyname... none required
checking for getservbyname... yes
checking for library containing inet_ntop... none required
checking whether inet_ntop is declared... yes
checking for IPv4 sockets... yes
checking for IPv6 sockets... yes
checking whether getcwd (NULL, 0) allocates memory for result... guessing yes
checking for getcwd with POSIX signature... yes
checking whether getcwd is declared... yes
checking whether getdelim is declared... yes
checking whether getdtablesize is declared... yes
checking for uid_t in sys/types.h... yes
checking type of array argument to getgroups... gid_t
checking whether getline is declared... yes
checking for getopt.h... (cached) yes
checking for getopt_long_only... yes
checking whether getopt is POSIX compatible... guessing yes
checking for working GNU getopt function... guessing no
checking whether fflush_unlocked is declared... yes
checking whether flockfile is declared... yes
checking whether fputs_unlocked is declared... yes
checking whether funlockfile is declared... yes
checking whether putc_unlocked is declared... yes
checking for struct timeval... yes
checking for wide-enough struct timeval.tv_sec member... yes
checking for pthread.h... yes
checking for pthread_kill in -lpthread... yes
checking whether POSIX threads API is available... yes
checking whether setlocale (LC_ALL, NULL) is multithread-safe... yes
checking whether setlocale (category, NULL) is multithread-safe... yes
checking whether limits.h has LLONG_MAX, WORD_BIT, ULLONG_WIDTH etc.... no
checking for wint_t... yes
checking whether wint_t is large enough... yes
checking whether the compiler produces multi-arch binaries... no
checking whether stdint.h conforms to C99... guessing yes
checking whether stdint.h works without ISO C predefines... yes
checking whether stdint.h has UINTMAX_WIDTH etc.... no
checking whether iswcntrl works... guessing yes
checking for towlower... yes
checking for wctype_t... yes
checking for wctrans_t... yes
checking for a traditional japanese locale... none
checking for a french Unicode locale... none
checking for a transitional chinese locale... none
checking whether included libunistring is requested... yes
checking for wchar_t... yes
checking for good max_align_t... yes
checking whether NULL can be used in arbitrary expressions... yes
checking whether locale.h defines locale_t... yes
checking whether imported symbols can be declared weak... guessing yes
checking for multithread API to use... posix
checking whether malloc, realloc, calloc are POSIX compliant... yes
checking for GNU libc compatible malloc... (cached) yes
checking for mmap... yes
checking for MAP_ANONYMOUS... yes
checking whether memchr works... guessing no
checking whether memrchr is declared... yes
checking whether <limits.h> defines MIN and MAX... no
checking whether <sys/param.h> defines MIN and MAX... yes
checking whether time_t is signed... yes
checking whether alarm is declared... yes
checking for working mktime... guessing no
checking whether <sys/select.h> is self-contained... yes
checking for library containing setsockopt... none needed
checking whether select supports a 0 argument... guessing yes
checking whether select detects invalid fds... guessing yes
checking for O_CLOEXEC... yes
checking for promoted mode_t type... mode_t
checking for library containing posix_spawn... none required
checking for posix_spawn... yes
checking whether posix_spawn works... guessing yes
checking whether posix_spawn rejects scripts without shebang... guessing yes
checking whether posix_spawnp rejects scripts without shebang... guessing yes
checking whether posix_spawnattr_setschedpolicy is supported... yes
checking whether posix_spawnattr_setschedparam is supported... yes
checking for sigset_t... yes
checking for SIGPIPE... yes
checking whether C symbols are prefixed with underscore at the linker level... no
checking whether snprintf returns a byte count as in C99... guessing yes
checking whether snprintf is declared... yes
checking whether fcloseall is declared... no
checking whether ecvt is declared... yes
checking whether fcvt is declared... yes
checking whether gcvt is declared... yes
checking whether strdup is declared... yes
checking whether strerror(0) succeeds... guessing yes
checking for strerror_r with POSIX signature... yes
checking whether strerror_r works... guessing yes
checking whether strndup is declared... yes
checking whether strnlen is declared... yes
checking for struct tm.tm_gmtoff... yes
checking whether strtok_r is declared... yes
checking for struct timespec in <time.h>... yes
checking for TIME_UTC in <time.h>... yes
checking whether execvpe is declared... yes
checking whether clearerr_unlocked is declared... yes
checking whether feof_unlocked is declared... yes
checking whether ferror_unlocked is declared... yes
checking whether fgets_unlocked is declared... yes
checking whether fputc_unlocked is declared... yes
checking whether fread_unlocked is declared... yes
checking whether fwrite_unlocked is declared... yes
checking whether getc_unlocked is declared... yes
checking whether getchar_unlocked is declared... yes
checking whether putchar_unlocked is declared... yes
checking whether the utimes function works... guessing no
checking for inttypes.h... yes
checking for stdint.h... yes
checking for intmax_t... yes
checking where to find the exponent in a 'double'... (cached) word 0 bit 20
checking whether snprintf truncates the result as in C99... guessing yes
checking for snprintf... (cached) yes
checking for strnlen... yes
checking for wcslen... yes
checking for wcsnlen... yes
checking for mbrtowc... (cached) yes
checking for wcrtomb... (cached) yes
checking whether _snprintf is declared... no
checking whether vsnprintf is declared... yes
checking for alloca as a compiler built-in... yes
checking whether btowc(0) is correct... guessing yes
checking whether btowc(EOF) is correct... guessing yes
checking for __builtin_expect... yes
checking for byteswap.h... yes
checking whether this system supports file names of any length... no
checking for library containing clock_gettime... none required
checking for clock_gettime... yes
checking for clock_settime... yes
checking for closedir... yes
checking for d_ino member in directory struct... guessing yes
checking for dirfd... yes
checking whether dirfd is declared... yes
checking whether dirfd is a macro... no
checking whether // is distinct from /... (cached) unknown, assuming no
checking whether dup works... guessing yes
checking whether dup2 works... guessing yes
checking for error_at_line... no
checking whether fcntl handles F_DUPFD correctly... guessing yes
checking whether fcntl understands F_DUPFD_CLOEXEC... guessing no
checking whether fdopendir is declared... yes
checking whether fdopendir works... guessing yes
checking whether fflush works on input streams... (cached) cross
checking for flexible array member... yes
checking whether conversion from 'int' to 'long double' works... guessing yes
checking for working GNU fnmatch... guessing no
checking whether fopen recognizes a trailing slash... guessing yes
checking whether fopen supports the mode character 'x'... guessing yes
checking whether fopen supports the mode character 'e'... guessing yes
checking whether fpurge is declared... no
checking whether fpurge works... guessing no
checking whether free is known to preserve errno... no
checking for fseeko... (cached) yes
checking whether fflush works on input streams... (cached) cross
checking for _fseeki64... no
checking whether fstatat (..., 0) works... guessing yes
checking for ftello... (cached) yes
checking whether ftello works... (cached) guessing yes
checking whether futimens works... guessing no
checking for library containing getaddrinfo... none required
checking for getaddrinfo... yes
checking whether gai_strerror is declared... yes
checking whether gai_strerrorA is declared... no
checking for gai_strerror with POSIX signature... yes
checking for struct sockaddr.sa_len... no
checking whether getaddrinfo is declared... yes
checking whether freeaddrinfo is declared... yes
checking whether getnameinfo is declared... yes
checking for struct addrinfo... yes
checking whether getcwd handles long file names properly... guessing no, but it is partly working
checking for getpagesize... yes
checking whether getcwd succeeds when 4k < cwd_length < 16k... guessing no
checking for working getdelim function... guessing no
checking for flockfile... yes
checking for funlockfile... yes
checking whether getc_unlocked is declared... (cached) yes
checking whether getdtablesize works... guessing yes
checking for getgroups... yes
checking for working getgroups... guessing yes
checking whether getgroups handles negative values... guessing yes
checking for getline... yes
checking for working getline function... guessing no
checking for getpass without length limitations... no
checking whether __fsetlocking is declared... yes
checking for tcgetattr... yes
checking for tcsetattr... yes
checking whether program_invocation_name is declared... yes
checking whether program_invocation_short_name is declared... yes
checking whether __argv is declared... no
checking whether getrandom is compatible with its GNU+BSD signature... yes
checking for gettimeofday with POSIX signature... yes
checking for group_member... no
checking for library containing gethostbyname... (cached) none required
checking for gethostbyname... (cached) yes
checking for library containing inet_ntop... (cached) none required
checking whether inet_ntop is declared... (cached) yes
checking whether the compiler generally respects inline... yes
checking whether INT32_MAX < INTMAX_MAX... yes
checking whether INT64_MAX == LONG_MAX... no
checking whether UINT32_MAX < UINTMAX_MAX... yes
checking whether UINT64_MAX == ULONG_MAX... no
checking for ioctl... yes
checking for ioctl with POSIX signature... yes
checking whether iswblank is declared... yes
checking whether iswdigit is ISO C compliant... guessing yes
checking whether iswxdigit is ISO C compliant... guessing yes
checking whether langinfo.h defines CODESET... yes
checking whether langinfo.h defines T_FMT_AMPM... yes
checking whether langinfo.h defines ALTMON_1... no
checking whether langinfo.h defines ERA... yes
checking whether langinfo.h defines YESEXPR... yes
checking whether the compiler supports the __inline keyword... yes
checking whether to use the included libunistring... yes
checking whether link obeys POSIX... guessing yes
checking whether locale.h conforms to POSIX:2001... yes
checking whether struct lconv is properly defined... yes
checking for pthread_rwlock_t... yes
checking whether pthread_rwlock_rdlock prefers a writer to a reader... guessing no
checking whether lseek detects pipes... yes
checking whether mbrtowc handles incomplete characters... guessing yes
checking whether mbrtowc works as well as mbtowc... guessing yes
checking whether mbrtowc handles a NULL pwc argument... guessing yes
checking whether mbrtowc handles a NULL string argument... guessing yes
checking whether mbrtowc has a correct return value... guessing yes
checking whether mbrtowc returns 0 when parsing a NUL character... guessing yes
checking whether mbrtowc stores incomplete characters... guessing no
checking whether mbrtowc works on empty input... guessing no
checking whether the C locale is free of encoding errors... guessing no
checking whether mbrtowc handles incomplete characters... (cached) guessing yes
checking whether mbrtowc works as well as mbtowc... (cached) guessing yes
checking whether mbrtowc handles incomplete characters... (cached) guessing yes
checking whether mbrtowc works as well as mbtowc... (cached) guessing yes
checking whether mbsrtowcs works... guessing yes
checking for mbtowc... yes
checking for bp-sym.h... no
checking for mempcpy... (cached) yes
checking for memrchr... yes
checking whether mkdir handles trailing slash... guessing yes
checking whether mkdir handles trailing dot... guessing yes
checking for working mkstemp... guessing yes
checking for __mktime_internal... no
checking for library containing nanosleep... none required
checking for working nanosleep... guessing no (mishandles large arguments)
checking whether <netinet/in.h> is self-contained... yes
checking whether YESEXPR works... guessing yes
checking whether open recognizes a trailing slash... guessing yes
checking for opendir... yes
checking whether posix_spawn_file_actions_addclose works... guessing yes
checking whether posix_spawn_file_actions_adddup2 works... guessing yes
checking whether posix_spawn_file_actions_addopen works... guessing yes
checking for raise... yes
checking for sigprocmask... yes
checking for rawmemchr... no
checking for readdir... yes
checking whether readlink signature is correct... yes
checking whether readlink handles trailing slash correctly... guessing yes
checking whether readlink truncates results correctly... guessing yes
checking for working re_compile_pattern... guessing no
checking for libintl.h... yes
checking whether isblank is declared... yes
checking for rewinddir... yes
checking for sched.h... yes
checking for struct sched_param... yes
checking whether select supports a 0 argument... (cached) guessing yes
checking whether select detects invalid fds... (cached) guessing yes
checking for library containing getservbyname... (cached) none required
checking for getservbyname... (cached) yes
checking whether setlocale (LC_ALL, NULL) is multithread-safe... (cached) yes
checking whether setlocale (category, NULL) is multithread-safe... (cached) yes
checking for struct sigaction.sa_sigaction... yes
checking for volatile sig_atomic_t... yes
checking for sighandler_t... yes
checking for sigprocmask... (cached) yes
checking for stdint.h... (cached) yes
checking for SIZE_MAX... yes
checking for snprintf... (cached) yes
checking whether snprintf respects a size of 1... guessing yes
checking whether printf supports POSIX/XSI format strings with positions... guessing yes
checking for socklen_t... yes
checking for posix_spawnattr_t... yes
checking for posix_spawn_file_actions_t... yes
checking for ssize_t... yes
checking whether stat handles trailing slashes on files... guessing yes
checking for struct stat.st_atim.tv_nsec... yes
checking whether struct stat.st_atim is of type struct timespec... yes
checking for struct stat.st_birthtimespec.tv_nsec... no
checking for struct stat.st_birthtimensec... no
checking for struct stat.st_birthtim.tv_nsec... no
checking for working stdalign.h... yes
checking for good max_align_t... (cached) yes
checking whether NULL can be used in arbitrary expressions... (cached) yes
checking which flavor of printf attribute matches inttypes macros... system
checking for stpcpy... yes
checking for strcasecmp... yes
checking for strncasecmp... yes
checking whether strncasecmp is declared... yes
checking for strchrnul... yes
checking whether strchrnul works... guessing yes
checking for working strerror function... guessing yes
checking for working strndup... guessing yes
checking for working strnlen... yes
checking for strpbrk... yes
checking for strtok_r... yes
checking whether strtok_r works... guessing no
checking for strtol... yes
checking for strtoll... yes
checking whether symlink handles trailing slash correctly... guessing yes
checking whether <sys/ioctl.h> declares ioctl... yes
checking for nlink_t... (cached) yes
checking for sys/single_threaded.h... no
checking whether localtime_r is declared... yes
checking whether localtime_r is compatible with its POSIX signature... yes
checking whether unlink honors trailing slashes... guessing yes
checking whether unlink of a parent directory fails as it should... guessing yes
checking for utime... yes
checking whether utime handles trailing slashes on files... guessing yes
checking for ptrdiff_t... yes
checking for vasprintf... yes
checking for vsnprintf... (cached) yes
checking whether snprintf respects a size of 1... (cached) guessing yes
checking whether printf supports POSIX/XSI format strings with positions... (cached) guessing yes
checking for waitid... yes
checking whether wcsdup is declared... yes
checking whether mbrtowc handles incomplete characters... (cached) guessing yes
checking whether mbrtowc works as well as mbtowc... (cached) guessing yes
checking whether wcrtomb works in the C locale... guessing yes
checking whether wcrtomb return value is correct... guessing yes
checking whether iswcntrl works... (cached) guessing yes
checking for towlower... (cached) yes
checking for wctype_t... (cached) yes
checking for wctrans_t... (cached) yes
checking whether wcwidth is declared... yes
checking whether wcwidth works reasonably in UTF-8 locales... guessing yes
checking for wmemchr... yes
checking for stdint.h... (cached) yes
./configure: line 51078: AX_CODE_COVERAGE: command not found
checking for working mmap... yes
checking for _LARGEFILE_SOURCE value needed for large files... (cached) no
checking for strptime... (cached) yes
checking for timegm... (cached) yes
checking for vsnprintf... (cached) yes
checking for vasprintf... (cached) yes
checking for drand48... yes
checking for pathconf... yes
checking for strtoll... (cached) yes
checking for usleep... yes
checking for ftello... yes
checking for sigblock... no
checking for sigsetjmp... yes
checking for memrchr... (cached) yes
checking for wcwidth... (cached) yes
checking for mbtowc... (cached) yes
checking for sleep... yes
checking for symlink... (cached) yes
checking for utime... (cached) yes
checking for strlcpy... yes
checking for random... yes
checking for fmemopen... yes
checking pkg-config is at least version 0.9.0... yes
checking for ZLIB... yes
checking for dlopen in -ldl... yes
checking for libssl... (cached) yes
checking how to link with libssl... -lssl -lcrypto
configure: compiling in support for SSL via OpenSSL
checking for RAND_egd... no
checking for INET6 protocol support... yes
checking for struct sockaddr_in6... yes
checking for struct sockaddr_storage... (cached) yes
checking for struct sockaddr_in6.sin6_scope_id... yes
configure: Enabling support for IPv6.
checking for makeinfo... ${SHELL} /openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1/build-aux/missing makeinfo
checking for perl5... no
checking for perl... /openwrt/staging_dir/host/bin/perl
checking for pod2man... /usr/bin/pod2man
configure: disabling IRIs at user request
checking for uuid.h... no
checking for PCRE... yes
checking for pcre.h... yes
checking for gpgme-config... no
checking for METALINK... no
checking for fsetxattr... no
configure: Disabling Extended Attribute support: your system does not support fsetxattr
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating src/Makefile
config.status: creating doc/Makefile
config.status: creating util/Makefile
config.status: creating po/Makefile.in
config.status: creating gnulib_po/Makefile.in
config.status: creating tests/Makefile
config.status: creating fuzz/Makefile
config.status: creating lib/Makefile
config.status: creating testenv/Makefile
config.status: creating tests/certs/interca.conf
config.status: creating tests/certs/rootca.conf
config.status: creating src/config.h
config.status: executing depfiles commands
config.status: executing po-directories commands
config.status: creating po/POTFILES
config.status: creating po/Makefile
config.status: creating gnulib_po/POTFILES
config.status: creating gnulib_po/Makefile
configure: Summary of build options:

  Version:           1.21.1
  Host OS:           linux-gnu
  Install prefix:    /usr
  Compiler:          ccache_cc
  CFlags:            -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DNDEBUG -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1=wget-1.21.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include   
  LDFlags:           -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro 
  Libs:              -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lpcre  -lssl -lcrypto -ldl -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lz  
  SSL:               openssl
  Zlib:              yes
  PSL:               no
  PCRE:              yes, via libpcre
  Digest:            yes
  NTLM:              yes
  OPIE:              yes
  POSIX xattr:       no
  Debugging:         yes
  Assertions:        no
  Valgrind:          Valgrind testing not enabled
  Metalink:          no
  Resolver:          libc, --bind-dns-address and --dns-servers not available
  GPGME:             no
  IRI:               no
  Fuzzing build:     no, 

make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1'
make  all-recursive
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1'
Making all in lib
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1/lib'
  GEN      alloca.h
  GEN      arpa/inet.h
  GEN      ctype.h
  GEN      dirent.h
  GEN      fcntl.h
  GEN      fnmatch.h
  GEN      getopt.h
  GEN      getopt-cdefs.h
  GEN      inttypes.h
  GEN      langinfo.h
  GEN      limits.h
  GEN      locale.h
  GEN      netdb.h
  GEN      sched.h
  GEN      signal.h
  GEN      spawn.h
  GEN      stdint.h
  GEN      stdio.h
  GEN      stdlib.h
  GEN      string.h
  GEN      strings.h
  GEN      sys/file.h
  GEN      sys/ioctl.h
  GEN      sys/random.h
  GEN      sys/select.h
  GEN      sys/socket.h
  GEN      sys/stat.h
  GEN      sys/time.h
  GEN      sys/types.h
  GEN      sys/uio.h
  GEN      sys/wait.h
  GEN      time.h
  GEN      unicase.h
  GEN      unicase/special-casing.h
  GEN      unictype.h
  GEN      uninorm.h
  GEN      unistd.h
  GEN      unistr.h
  GEN      unitypes.h
  GEN      uniwidth.h
  GEN      utime.h
  GEN      wchar.h
  GEN      wctype.h
make  all-am
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1/lib'
  CC       openat-proc.o
  CC       base32.o
  CC       basename-lgpl.o
  CC       binary-io.o
  CC       bitrotate.o
  CC       c-ctype.o
  CC       c-strcasecmp.o
  CC       c-strncasecmp.o
  CC       c-strcasestr.o
  CC       canonicalize.o
  CC       cloexec.o
  CC       concat-filename.o
  CC       af_alg.o
  CC       md2.o
  CC       md4.o
  CC       md5.o
  CC       sha1.o
  CC       sha256.o
  CC       sha512.o
  CC       dirname.o
  CC       basename.o
  CC       dirname-lgpl.o
  CC       stripslash.o
  CC       exitfail.o
  CC       fatal-signal.o
  CC       fd-hook.o
  CC       fd-safer-flag.o
  CC       dup-safer-flag.o
  CC       file-set.o
  CC       filenamecat-lgpl.o
  CC       findprog-in.o
  CC       freading.o
  CC       getprogname.o
  CC       gettime.o
  CC       hard-locale.o
  CC       hash.o
  CC       hash-pjw.o
  CC       hash-triple-simple.o
  CC       localcharset.o
  CC       malloca.o
  CC       mbchar.o
  CC       mbiter.o
  CC       openat-die.o
  CC       pipe2.o
  CC       pipe2-safer.o
  CC       quotearg.o
  CC       save-cwd.o
  CC       malloc/scratch_buffer_dupfree.o
  CC       malloc/scratch_buffer_grow.o
  CC       malloc/scratch_buffer_grow_preserve.o
  CC       malloc/scratch_buffer_set_array_size.o
  CC       setlocale_null.o
  CC       sig-handler.o
  CC       sockets.o
  CC       spawn-pipe.o
  CC       stat-time.o
  CC       strnlen1.o
  CC       sys_socket.o
  CC       tempname.o
  CC       glthread/threadlib.o
  CC       timespec.o
  CC       tmpdir.o
  CC       u64.o
  CC       unistd.o
  CC       dup-safer.o
  CC       fd-safer.o
  CC       pipe-safer.o
  CC       utimens.o
  CC       wait-process.o
  CC       wctype-h.o
  CC       xmalloc.o
  CC       xalloc-die.o
  CC       xmemdup0.o
  CC       xsize.o
  CC       xstrndup.o
  CC       asnprintf.o
  CC       chdir-long.o
  CC       error.o
  CC       fcntl.o
  CC       fflush.o
  CC       fnmatch.o
  CC       fpurge.o
  CC       free.o
  CC       fseek.o
  CC       fseeko.o
  CC       futimens.o
  CC       getcwd.o
  CC       getcwd-lgpl.o
  CC       getdelim.o
  CC       getline.o
  CC       getopt.o
  CC       getopt1.o
  CC       getpass.o
  CC       group-member.o
  CC       mbrtowc.o
  CC       memchr.o
  CC       mktime.o
  CC       nanosleep.o
  CC       nl_langinfo.o
  CC       printf-args.o
  CC       printf-parse.o
  CC       rawmemchr.o
  CC       regex.o
  CC       spawn_faction_addchdir.o
  CC       timegm.o
  CC       vasnprintf.o
  CC       wmempcpy.o
  CC       malloc/dynarray_at_failure.o
  CC       malloc/dynarray_emplace_enlarge.o
  CC       malloc/dynarray_finalize.o
  CC       malloc/dynarray_resize.o
  CC       malloc/dynarray_resize_clear.o
  CC       glthread/lock.o
  CC       unicase/cased.o
  CC       unicase/empty-prefix-context.o
  CC       unicase/empty-suffix-context.o
  CC       unicase/ignorable.o
  CC       unicase/special-casing.o
  CC       unicase/tolower.o
  CC       unicase/u8-casemap.o
  CC       unicase/u8-tolower.o
  CC       unictype/combiningclass.o
  CC       unictype/pr_soft_dotted.o
  CC       uninorm/decompose-internal.o
  CC       uninorm/u8-normalize.o
  CC       unistr/u8-cpy.o
  CC       unistr/u8-mbtouc-unsafe.o
  CC       unistr/u8-mbtouc-unsafe-aux.o
  CC       unistr/u8-strlen.o
  CC       unistr/u8-uctomb.o
  CC       unistr/u8-uctomb-aux.o
  CC       uniwidth/width.o
  AR       libgnu.a
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1/lib'
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1/lib'
Making all in src
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1/src'
make  all-am
make[7]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1/src'
  CC       connect.o
  CC       convert.o
  CC       cookies.o
  CC       ftp.o
  CC       css_.o
  CC       css-url.o
  CC       ftp-basic.o
  CC       ftp-ls.o
  CC       hash.o
  CC       host.o
  CC       hsts.o
  CC       html-parse.o
  CC       html-url.o
  CC       http.o
  CC       init.o
  CC       log.o
  CC       main.o
  CC       netrc.o
  CC       progress.o
  CC       ptimer.o
  CC       recur.o
  CC       res.o
  CC       retr.o
  CC       spider.o
  CC       url.o
  CC       warc.o
  CC       utils.o
  CC       exits.o
  CC       build_info.o
echo '/* version.c */' > version.c
echo '/* Autogenerated by Makefile - DO NOT EDIT */' >> version.c
echo '' >> version.c
echo '#include "version.h"' >> version.c
echo 'const char *version_string = "1.21.1";' >> version.c
echo 'const char *compilation_string = "'ccache_cc -DHAVE_CONFIG_H -DSYSTEM_WGETRC=\"/etc/wgetrc\" -DLOCALEDIR=\"/usr/share/locale\" -I.  -I../lib -I../lib  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include     -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DNDEBUG -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1=wget-1.21.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro '";' \
    | sed -e 's/[\\"]/\\&/g' -e 's/\\"/"/' -e 's/\\";$/";/' >> version.c
echo 'const char *link_string = "'ccache_cc    -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include  -DNDEBUG -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1=wget-1.21.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro  \
 -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro  -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lpcre  -lssl -lcrypto -ldl -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lz    ftp-opie.o openssl.o http-ntlm.o ../lib/libgnu.a              '";' \
    | sed -e 's/[\\"]/\\&/g' -e 's/\\"/"/' -e 's/\\";$/";/' >> version.c
  CC       ftp-opie.o
  CC       openssl.o
openssl.c:40:10: fatal error: openssl/ssl.h: No such file or directory
 #include <openssl/ssl.h>
          ^~~~~~~~~~~~~~~
compilation terminated.
make[7]: *** [Makefile:1948: openssl.o] Error 1
make[7]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1/src'
make[6]: *** [Makefile:1760: all] Error 2
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1/src'
make[5]: *** [Makefile:1707: all-recursive] Error 1
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1'
make[4]: *** [Makefile:1659: all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1'
make[3]: *** [Makefile:115: /openwrt/build_dir/target-mips_24kc_musl/wget-ssl/wget-1.21.1/.built] Error 2
```
