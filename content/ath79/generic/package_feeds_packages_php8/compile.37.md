---
title: "compile.37"
date: 2021-06-20 22:33:34.413739
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
make package/feeds/packages/php8/compile -j$(nproc) || make package/feeds/packages/php8/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0007-Add-support-for-use-of-the-system-timezone-database.patch using plaintext: 
patching file ext/date/config0.m4
patching file ext/date/lib/parse_tz.c

Applying ./patches/0022-Use-system-timezone.patch using plaintext: 
patching file ext/date/php_date.c

Applying ./patches/0025-php-5.4.9-fixheader.patch using plaintext: 
patching file configure.ac

Applying ./patches/0030-Remove-W3C-validation-icon-to-not-expose-the-reader-.patch using plaintext: 
patching file sapi/fpm/status.html.in

Applying ./patches/0041-Add-patch-to-remove-build-timestamps-from-generated-.patch using plaintext: 
patching file ext/standard/info.c
patching file sapi/apache2handler/config.m4
patching file sapi/cgi/cgi_main.c
patching file sapi/cli/php_cli.c
patching file sapi/fpm/fpm/fpm_main.c
patching file sapi/phpdbg/phpdbg.c

Applying ./patches/0050-remove-build-timestamps.patch using plaintext: 
patching file sapi/litespeed/lsapi_main.c

Applying ./patches/1001-ext-opcache-fix-detection-of-shm-mmap.patch using plaintext: 
patching file ext/opcache/config.m4

Applying ./patches/1004-disable-phar-command.patch using plaintext: 
patching file ext/phar/config.m4
patching file configure.ac

Applying ./patches/1010-Fix-opcache-jit-minilua-compiling.patch using plaintext: 
patching file ext/opcache/jit/Makefile.frag
buildconf: Checking installation
buildconf: autoconf version 2.69 (ok)
buildconf: Forcing buildconf. The configure files will be regenerated.
buildconf: Cleaning cache and configure files
buildconf: Rebuilding configure
buildconf: Rebuilding main/php_config.h.in
buildconf: Run ./configure to proceed with customizing the PHP build.
configure: loading site script /openwrt/include/site/mips
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking target system type... mips-openwrt-linux-gnu
shtool:echo:Warning: unable to determine terminal sequence for bold mode
shtool:echo:Warning: unable to determine terminal sequence for bold mode
checking pkg-config is at least version 0.9.0... yes
checking for mips-openwrt-linux-cc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking how to run the C preprocessor... ccache_cc -E
checking for icc... no
checking for suncc... no
checking for ccache_cc option to accept ISO C99... none needed
checking how to run the C preprocessor... ccache_cc -E
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
checking minix/config.h usability... no
checking minix/config.h presence... no
checking for minix/config.h... no
checking whether it is safe to define __EXTENSIONS__... yes
checking whether ln -s works... yes
checking for system library directory... lib
checking whether to enable runpaths... no
checking if compiler supports -R... yes
checking for gawk... gawk
checking for bison... bison
checking for bison version... 3.7.4 (ok)
checking for re2c... no
checking whether to enable computed goto gcc extension with re2c... no
checking whether C compiler accepts -fvisibility=hidden... yes
checking whether to force non-PIC code in shared modules... no
checking whether /dev/urandom exists... yes
checking for global register variables support... no
checking whether __cpuid_count is available... no
checking for pthreads_cflags... -pthread
checking for pthreads_lib... pthread

Configuring SAPI modules
checking for Apache 2 handler module support via DSO through APXS... no
checking for setproctitle... no
checking sys/pstat.h usability... no
checking sys/pstat.h presence... no
checking for sys/pstat.h... no
checking for PS_STRINGS... no
checking for CLI build... yes
checking for embedded SAPI library support... no
checking for FPM build... yes
checking for clearenv... yes
checking for setproctitle... (cached) no
checking for setproctitle_fast... no
checking for library containing socket... none required
checking for library containing inet_addr... none required
checking for prctl... yes
checking for clock_gettime... yes
checking for ptrace... yes
checking whether ptrace works... skipped (cross-compiling)
checking for proc mem file... skipped (cross-compiling)
checking if gcc supports __sync_bool_compare_and_swap... yes
checking for TCP_INFO... yes
checking for sysconf... yes
checking for times... yes
checking for kqueue... no
checking for port framework... no
checking for /dev/poll... no
checking for epoll... yes
checking for select... yes
checking for clang fuzzer SAPI... no
checking for LiteSpeed support... no
checking for phpdbg support... no
checking for phpdbg web SAPI support... no
checking for phpdbg debug build... no
checking for phpdbg readline support... no
checking for CGI build... yes
checking for sun_len in sys/un.h... no
checking whether cross-process locking is required by accept()... no
checking for chosen SAPI module... none
checking for executable SAPI binaries...  cli fpm cgi

Running system checks
checking for sendmail... /usr/sbin/sendmail
checking whether system uses EBCDIC... no
checking whether byte ordering is bigendian... (cached) yes
checking whether writing to stdout works... no
checking for socket... yes
checking for socketpair... yes
checking for htonl... yes
checking for gethostname... yes
checking for gethostbyaddr... yes
checking for dlopen... yes
checking for dlsym... yes
checking for sin in -lm... yes
checking for inet_aton... yes
checking for stdint.h... (cached) yes
checking for dirent.h... yes
checking for sys/param.h... yes
checking for sys/types.h... (cached) yes
checking for sys/time.h... yes
checking for netinet/in.h... yes
checking for alloca.h... yes
checking for arpa/inet.h... yes
checking for arpa/nameser.h... yes
checking for crypt.h... yes
checking for dns.h... no
checking for fcntl.h... yes
checking for grp.h... yes
checking for ieeefp.h... no
checking for langinfo.h... yes
checking for malloc.h... yes
checking for poll.h... yes
checking for pty.h... yes
checking for pwd.h... yes
checking for resolv.h... yes
checking for strings.h... (cached) yes
checking for syslog.h... yes
checking for sysexits.h... yes
checking for sys/ioctl.h... yes
checking for sys/file.h... yes
checking for sys/mman.h... yes
checking for sys/mount.h... yes
checking for sys/poll.h... yes
checking for sys/resource.h... yes
checking for sys/select.h... yes
checking for sys/socket.h... yes
checking for sys/stat.h... (cached) yes
checking for sys/statfs.h... yes
checking for sys/statvfs.h... yes
checking for sys/vfs.h... yes
checking for sys/sysexits.h... no
checking for sys/uio.h... yes
checking for sys/wait.h... yes
checking for sys/loadavg.h... no
checking for unistd.h... (cached) yes
checking for unix.h... no
checking for utime.h... yes
checking for sys/utsname.h... yes
checking for sys/ipc.h... yes
checking for dlfcn.h... yes
checking for tmmintrin.h... no
checking for nmmintrin.h... no
checking for wmmintrin.h... no
checking for immintrin.h... no
checking for fopencookie... yes
checking for broken getcwd... no
checking for broken gcc optimize-strlen... no
checking whether struct tm is in sys/time.h or time.h... time.h
checking for struct tm.tm_zone... yes
checking for missing declarations of reentrant functions... done
checking for fclose declaration... ok
checking for struct flock... yes
checking for socklen_t... yes
checking size of intmax_t... 0
checking size of ssize_t... 8
checking size of ptrdiff_t... 8
checking size of short... (cached) 2
checking size of int... (cached) 4
checking size of long... (cached) 4
checking size of long long... (cached) 8
checking size of size_t... (cached) 4
checking size of off_t... (cached) 8
checking for int8_t... yes
checking for int16_t... yes
checking for int32_t... yes
checking for int64_t... yes
checking for uint8_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for uint64_t... yes
checking for __builtin_expect... yes
checking for __builtin_clz... yes
checking for __builtin_clzl... yes
checking for __builtin_clzll... yes
checking for __builtin_ctzl... yes
checking for __builtin_ctzll... yes
checking for __builtin_smull_overflow... yes
checking for __builtin_smulll_overflow... yes
checking for __builtin_saddl_overflow... yes
checking for __builtin_saddll_overflow... yes
checking for __builtin_ssubl_overflow... yes
checking for __builtin_ssubll_overflow... yes
checking for __builtin_cpu_init... no
checking for __builtin_cpu_supports... no
checking whether the compiler supports __alignof__... yes
checking for struct tm.tm_gmtoff... yes
checking for struct stat.st_blksize... yes
checking for struct stat.st_rdev... yes
checking for struct stat.st_blocks... yes
checking for size_t... yes
checking for uid_t in sys/types.h... yes
checking for struct sockaddr_storage... yes
checking for field sa_len in struct sockaddr... no
checking for __attribute__((ifunc))... no
checking for __attribute__((target))... no
checking for IPv6 support... yes
checking for alphasort... yes
checking for asctime_r... yes
checking for chroot... yes
checking for ctime_r... yes
checking for explicit_memset... no
checking for flock... yes
checking for ftok... yes
checking for funopen... no
checking for gai_strerror... yes
checking for getcwd... (cached) yes
checking for getloadavg... yes
checking for getlogin... yes
checking for getprotobyname... yes
checking for getprotobynumber... yes
checking for getservbyname... yes
checking for getservbyport... yes
checking for getrusage... yes
checking for gettimeofday... (cached) yes
checking for gmtime_r... yes
checking for getpwnam_r... yes
checking for getgrnam_r... yes
checking for getpwuid_r... (cached) yes
checking for getwd... no
checking for glob... yes
checking for inet_ntoa... yes
checking for inet_ntop... yes
checking for inet_pton... yes
checking for localtime_r... yes
checking for lchown... yes
checking for memmove... yes
checking for mkstemp... yes
checking for mmap... yes
checking for nice... yes
checking for nl_langinfo... yes
checking for poll... yes
checking for putenv... yes
checking for scandir... yes
checking for setitimer... yes
checking for setenv... yes
checking for shutdown... yes
checking for sigprocmask... yes
checking for statfs... yes
checking for statvfs... yes
checking for std_syslog... no
checking for strcasecmp... yes
checking for strnlen... yes
checking for strptime... yes
checking for strtok_r... yes
checking for symlink... yes
checking for tzset... yes
checking for unsetenv... yes
checking for usleep... yes
checking for utime... yes
checking for vasprintf... yes
checking for asprintf... yes
checking for nanosleep... yes
checking for memmem... yes
checking how many arguments gethostbyname_r() takes... six
checking for nanosleep in -lrt... yes
checking for setsockopt in -lnetwork... no
checking for __setsockopt in -lnetwork... no
checking for getaddrinfo... (cached) yes
checking for strlcat... yes
checking for strlcpy... yes
checking for explicit_bzero... yes
checking for getopt... yes
checking for working alloca.h... yes
checking for alloca... yes
checking for type of reentrant time-related functions... (cached) POSIX
checking for in_addr_t... yes
checking for aarch64 CRC32 API... no
checking for asm goto... no
checking whether to enable valgrind support... no
checking for openpty... yes

General settings
checking whether to include gcov symbols... no
checking whether to include debugging symbols... no
checking whether to enable debug assertions in release mode... no
checking whether to dlopen extensions with RTLD_NOW instead of RTLD_LAZY... no
checking layout of installed files... PHP
checking path to configuration file... /etc
checking where to scan for configuration files... /etc/php8
checking whether to enable PHP's own SIGCHLD handler... no
checking whether to explicitly link against libgcc... no
checking whether to enable short tags by default... no
checking whether to enable dmalloc... no
checking whether to enable IPv6 support... yes
checking whether to enable DTrace support... no
checking how big to make fd sets... using system default

Configuring extensions
checking io.h usability... no
checking io.h presence... no
checking for io.h... no
checking for strtoll... yes
checking for atoll... yes
checking for use of system timezone data... yes
checking whether to build with LIBXML support... yes
checking for libxml-2.0 >= 2.9.0... yes
checking for OpenSSL support... yes, shared
checking for Kerberos support... no
checking whether to use system default cipher list instead of hardcoded value... no
checking for RAND_egd... no
checking for openssl >= 1.0.1... no
configure: error: Package requirements (openssl >= 1.0.1) were not met:

Package 'openssl', required by 'virtual:world', not found

Consider adjusting the PKG_CONFIG_PATH environment variable if you
installed software in a non-standard prefix.

Alternatively, you may set the environment variables OPENSSL_CFLAGS
and OPENSSL_LIBS to avoid the need to call pkg-config.
See the pkg-config man page for more details.
make[3]: *** [Makefile:593: /openwrt/build_dir/target-mips_24kc_musl/php-8.0.7/.configured_459023fc4b73ed5f58e1d363e0e985a9] Error 1
```
