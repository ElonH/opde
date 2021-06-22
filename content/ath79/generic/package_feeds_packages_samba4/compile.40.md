---
title: "compile.40"
date: 2021-06-22 10:51:50.608163
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
make package/feeds/packages/samba4/compile -j$(nproc) || make package/feeds/packages/samba4/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-samba-4.4.0-pam.patch using plaintext: 
patching file source3/wscript

Applying ./patches/002-dnsserver-4.7.0.patch using plaintext: 
patching file source4/dns_server/wscript_build

Applying ./patches/003-getpwent_r.patch using plaintext: 
patching file source4/torture/local/nss_tests.c

Applying ./patches/004-missing-headers.patch using plaintext: 
patching file lib/param/loadparm.h
patching file source3/lib/system_smbd.c
patching file source4/torture/local/nss_tests.c

Applying ./patches/005-musl_uintptr.patch using plaintext: 
patching file third_party/cmocka/cmocka.h

Applying ./patches/006-netdb-defines.patch using plaintext: 
patching file nsswitch/wins.c

Applying ./patches/007-libldb-fix-musl-libc-unkown-type-error.patch using plaintext: 
patching file lib/tevent/tevent.h

Applying ./patches/008-samba-4.11-add_missing___compar_fn_t.patch using plaintext: 
patching file source4/dsdb/samdb/ldb_modules/count_attrs.c

Applying ./patches/009-samba-4-11-fix-host-tools-checks.patch.patch using plaintext: 
patching file wscript_configure_embedded_heimdal
patching file wscript_configure_system_heimdal

Applying ./patches/010-samba-4-12-fix-musl_missing__nss_buflen_passwd.patch using plaintext: 
patching file lib/util/util_paths.c

Applying ./patches/020-source3-msgsock-nvram-fix.patch using plaintext: 
patching file source3/lib/messages.c

Applying ./patches/021-source4-msgsock-nvram-fix.patch using plaintext: 
patching file source4/lib/messaging/messaging.c

Applying ./patches/101-do-not-check-xsltproc-manpages.patch using plaintext: 
patching file lib/ldb/wscript
patching file lib/talloc/wscript
patching file lib/tdb/wscript

Applying ./patches/102-samba-4.11-unbundle-libbsd.patch using plaintext: 
patching file lib/replace/wscript

Applying ./patches/103-samba-4.12-unbundle-libunwind.patch using plaintext: 
patching file lib/util/wscript_configure

Applying ./patches/104-samba-4.12-unbundle-icu.patch using plaintext: 
patching file lib/util/charset/wscript_configure
Setting top to                           : /openwrt/build_dir/target-mips_24kc_musl/samba-4.13.9 
Setting out to                           : /openwrt/build_dir/target-mips_24kc_musl/samba-4.13.9/bin 
Checking for 'gcc' (C compiler)          : ccache_cc 
Checking for program 'git'               : /openwrt/staging_dir/host/bin/git 
Checking for c flags '-MMD'              : yes 
Checking for program 'gdb'               : not found 
Checking for header sys/utsname.h        : yes 
Checking uname sysname type              : Linux 
Checking uname machine type              : mips 
Checking uname release type              : 5.4.124 
Checking uname version type              : ImmortalWrt Linux-5.4.124 2021-06-22 
Checking for header stdio.h              : yes 
Checking simple C program                : ok 
Checking compiler accepts ['-Werror']    : yes 
Checking linker accepts ['-Wl,-rpath,.'] : yes 
Checking for rpath library support       : yes 
Checking for -Wl,--version-script support : yes 
Checking compiler accepts ['-fvisibility=hidden'] : yes 
Checking for HAVE_VISIBILITY_ATTR                 : ok 
Checking for library constructor support          : ok 
Checking for library destructor support           : ok 
Checking for __attribute__                        : ok 
Checking compiler accepts ['-fPIC']               : yes 
Checking for inline                               : inline 
Checking for program 'pkg-config'                 : /openwrt/staging_dir/host/bin/pkg-config 
Checking for pkg-config version >= '0.0.0'        : yes 
Checking compiler accepts ['-D__STDC_WANT_LIB_EXT1__=1'] : yes 
Checking compiler accepts ['']                           : yes 
Checking for header sys/types.h                          : yes 
Checking for header sys/stat.h                           : yes 
Checking for header stdlib.h                             : yes 
Checking for header stddef.h                             : yes 
Checking for header memory.h                             : yes 
Checking for header string.h                             : yes 
Checking for header strings.h                            : yes 
Checking for header inttypes.h                           : yes 
Checking for header stdint.h                             : yes 
Checking for header unistd.h                             : yes 
Checking for header minix/config.h                       : no 
Checking for header ctype.h                              : yes 
Checking for header standards.h                          : no 
Checking for header stdbool.h                            : yes 
Checking for header stdarg.h                             : yes 
Checking for header vararg.h                             : no 
Checking for header limits.h                             : yes 
Checking for header assert.h                             : yes 
Checking getconf LFS_CFLAGS                              : not found 
Checking for large file support without additional flags : ok 
Checking for header sys/time.h                           : yes 
Checking for header time.h                               : yes 
Checking for header endian.h                             : yes 
Checking for header sys/endian.h                         : no 
Checking for HAVE_LITTLE_ENDIAN                          : not found 
Checking for HAVE_BIG_ENDIAN                             : ok 
Checking for header signal.h                             : yes 
Checking if signal handlers return int                   : not found 
Checking for variable __FUNCTION__                       : ok 
Checking for va_copy                                     : ok 
Checking for HAVE__VA_ARGS__MACRO                        : ok 
Checking for header linux/types.h                        : yes 
Checking for header crypt.h                              : yes 
Checking for header locale.h                             : yes 
Checking for header acl/libacl.h                         : yes 
Checking for header compat.h                             : no 
Checking for header attr/xattr.h                         : no 
Checking for header dustat.h                             : no 
Checking for header fcntl.h                              : yes 
Checking for header fnmatch.h                            : yes 
Checking for header glob.h                               : yes 
Checking for header history.h                            : no 
Checking for header krb5.h                               : no 
Checking for header langinfo.h                           : yes 
Checking for header ndir.h                               : no 
Checking for header pwd.h                                : yes 
Checking for header shadow.h                             : yes 
Checking for header sys/acl.h                            : yes 
Checking for header sys/attributes.h                     : no 
Checking for header attr/attributes.h                    : yes 
Checking for header sys/capability.h                     : yes 
Checking for header sys/dir.h                            : yes 
Checking for header sys/epoll.h                          : yes 
Checking for header port.h                               : no 
Checking for header sys/fcntl.h                          : yes 
Checking for header sys/filio.h                          : no 
Checking for header sys/filsys.h                         : no 
Checking for header sys/fs/s5param.h                     : no 
Checking for header sys/id.h                             : no 
Checking for header sys/ioctl.h                          : yes 
Checking for header sys/ipc.h                            : yes 
Checking for header sys/mman.h                           : yes 
Checking for header sys/mode.h                           : no 
Checking for header sys/ndir.h                           : no 
Checking for header sys/priv.h                           : no 
Checking for header sys/resource.h                       : yes 
Checking for header sys/security.h                       : no 
Checking for header sys/shm.h                            : yes 
Checking for header sys/statfs.h                         : yes 
Checking for header sys/statvfs.h                        : yes 
Checking for header sys/termio.h                         : no 
Checking for header sys/vfs.h                            : yes 
Checking for header sys/xattr.h                          : yes 
Checking for header termio.h                             : no 
Checking for header termios.h                            : yes 
Checking for header sys/file.h                           : yes 
Checking for header sys/ucontext.h                       : yes 
Checking for header sys/wait.h                           : yes 
Checking for declaration of malloc                       : ok 
Checking for header grp.h                                : yes 
Checking for header sys/select.h                         : yes 
Checking for header setjmp.h                             : yes 
Checking for header utime.h                              : yes 
Checking for header sys/syslog.h                         : yes 
Checking for header syslog.h                             : yes 
Checking for header sys/mount.h                          : yes 
Checking for header mntent.h                             : yes 
Checking for header stropts.h                            : yes 
Checking for header unix.h                               : no 
Checking for header sys/param.h                          : yes 
Checking for header sys/socket.h                         : yes 
Checking for header netinet/in.h                         : yes 
Checking for header netdb.h                              : yes 
Checking for header arpa/inet.h                          : yes 
Checking for header netinet/in_systm.h                   : yes 
Checking for header netinet/ip.h                         : yes 
Checking for header netinet/tcp.h                        : yes 
Checking for header netinet/in_ip.h                      : no 
Checking for header sys/sockio.h                         : no 
Checking for header sys/un.h                             : yes 
Checking for header sys/uio.h                            : yes 
Checking for header ifaddrs.h                            : yes 
Checking for header direct.h                             : no 
Checking for header dirent.h                             : yes 
Checking for header windows.h                            : no 
Checking for header winsock2.h                           : no 
Checking for header ws2tcpip.h                           : no 
Checking for header errno.h                              : yes 
Checking for header getopt.h                             : yes 
Checking for header iconv.h                              : yes 
Checking for header nss.h                                : no 
Checking for header sasl/sasl.h                          : yes 
Checking for inotify_init                                : ok 
Checking for header security/pam_appl.h                  : yes 
Checking for header zlib.h                               : yes 
Checking for header asm/unistd.h                         : yes 
Checking for header sys/unistd.h                         : no 
Checking for header alloca.h                             : yes 
Checking for header float.h                              : yes 
Checking for header rpc/rpc.h                            : no 
Checking for header rpc/nettype.h                        : no 
Checking for tirpc rpc headers in default system path    : not found 
Checking for libtirpc headers                            : yes 
Checking for header rpc/rpc.h                            : yes 
Checking for header rpc/nettype.h                        : yes 
Checking for header rpcsvc/yp_prot.h                     : no 
Checking for libnsl                                      : not found 
Checking for header rpcsvc/nis.h                         : no 
Checking for header rpcsvc/ypclnt.h                      : no 
Checking for header sys/sysctl.h                         : not found 
Checking for header sys/fileio.h                         : no 
Checking for header sys/filesys.h                        : no 
Checking for header sys/dustat.h                         : no 
Checking for header sys/sysmacros.h                      : yes 
Checking for header xfs/libxfs.h                         : no 
Checking for header netgroup.h                           : no 
Checking for header valgrind.h                           : no 
Checking for header valgrind/valgrind.h                  : no 
Checking for header valgrind/memcheck.h                  : no 
Checking for header valgrind/helgrind.h                  : no 
Checking for header nss_common.h                         : no 
Checking for header nsswitch.h                           : no 
Checking for header ns_api.h                             : no 
Checking for header sys/extattr.h                        : no 
Checking for header sys/ea.h                             : no 
Checking for header sys/proplist.h                       : no 
Checking for header sys/cdefs.h                          : yes 
Checking for header utmp.h                               : yes 
Checking for header utmpx.h                              : yes 
Checking for header lastlog.h                            : yes 
Checking for header syscall.h                            : yes 
Checking for header sys/syscall.h                        : yes 
Checking for header sys/atomic.h                         : no 
Checking for header stdatomic.h                          : yes 
Checking for header libgen.h                             : yes 
Checking compiler accepts -Wno-format-truncation         : yes 
Checking compiler accepts -Wno-unused-function           : yes 
Checking compiler accepts -Wno-strict-overflow           : yes 
Checking for header sys/prctl.h                          : yes 
Checking for prctl syscall                               : ok 
Checking for O_DIRECT flag to open(2)                    : ok 
Checking for long long                                   : ok 
Checking for intptr_t                                    : ok 
Checking for uintptr_t                                   : ok 
Checking for ptrdiff_t                                   : ok 
Checking for comparison_fn_t                             : not found 
Checking for _Bool                                       : ok 
Checking for bool                                        : ok 
Checking for int8_t                                      : ok 
Checking for uint8_t                                     : ok 
Checking for int16_t                                     : ok 
Checking for uint16_t                                    : ok 
Checking for int32_t                                     : ok 
Checking for uint32_t                                    : ok 
Checking for int64_t                                     : ok 
Checking for uint64_t                                    : ok 
Checking for size_t                                      : ok 
Checking for ssize_t                                     : ok 
Checking for ino_t                                       : ok 
Checking for loff_t                                      : not found 
Checking for offset_t                                    : not found 
Checking for volatile int                                : ok 
Checking for uint_t                                      : not found 
Checking for blksize_t                                   : ok 
Checking for blkcnt_t                                    : ok 
Checking if size of bool == 1                            : ok 
Checking if size of char == 1                            : ok 
Checking if size of int == 1                             : not found 
Checking if size of int == 2                             : not found 
Checking if size of int == 4                             : ok 
Checking if size of long long == 1                       : not found 
Checking if size of long long == 2                       : not found 
Checking if size of long long == 4                       : not found 
Checking if size of long long == 8                       : ok 
Checking if size of long == 1                            : not found 
Checking if size of long == 2                            : not found 
Checking if size of long == 4                            : ok 
Checking if size of short == 1                           : not found 
Checking if size of short == 2                           : ok 
Checking if size of size_t == 1                          : not found 
Checking if size of size_t == 2                          : not found 
Checking if size of size_t == 4                          : ok 
Checking if size of ssize_t == 1                         : not found 
Checking if size of ssize_t == 2                         : not found 
Checking if size of ssize_t == 4                         : ok 
Checking if size of int8_t == 1                          : ok 
Checking if size of uint8_t == 1                         : ok 
Checking if size of int16_t == 1                         : not found 
Checking if size of int16_t == 2                         : ok 
Checking if size of uint16_t == 1                        : not found 
Checking if size of uint16_t == 2                        : ok 
Checking if size of int32_t == 1                         : not found 
Checking if size of int32_t == 2                         : not found 
Checking if size of int32_t == 4                         : ok 
Checking if size of uint32_t == 1                        : not found 
Checking if size of uint32_t == 2                        : not found 
Checking if size of uint32_t == 4                        : ok 
Checking if size of int64_t == 1                         : not found 
Checking if size of int64_t == 2                         : not found 
Checking if size of int64_t == 4                         : not found 
Checking if size of int64_t == 8                         : ok 
Checking if size of uint64_t == 1                        : not found 
Checking if size of uint64_t == 2                        : not found 
Checking if size of uint64_t == 4                        : not found 
Checking if size of uint64_t == 8                        : ok 
Checking if size of void* == 1                           : not found 
Checking if size of void* == 2                           : not found 
Checking if size of void* == 4                           : ok 
Checking if size of off_t == 1                           : not found 
Checking if size of off_t == 2                           : not found 
Checking if size of off_t == 4                           : not found 
Checking if size of off_t == 8                           : ok 
Checking if size of dev_t == 1                           : not found 
Checking if size of dev_t == 2                           : not found 
Checking if size of dev_t == 4                           : not found 
Checking if size of dev_t == 8                           : ok 
Checking if size of ino_t == 1                           : not found 
Checking if size of ino_t == 2                           : not found 
Checking if size of ino_t == 4                           : not found 
Checking if size of ino_t == 8                           : ok 
Checking if size of time_t == 1                          : not found 
Checking if size of time_t == 2                          : not found 
Checking if size of time_t == 4                          : ok 
Checking for socklen_t                                   : ok 
Checking for struct ifaddrs                              : ok 
Checking for struct addrinfo                             : ok 
Checking for struct sockaddr                             : ok 
Checking for HAVE_STRUCT_SOCKADDR_IN6                    : ok 
Checking for struct sockaddr_storage                     : ok 
Checking for sa_family_t                                 : ok 
Checking for sig_atomic_t                                : ok 
Checking for sigsetmask                                  : not found 
Checking for siggetmask                                  : not found 
Checking for sigprocmask                                 : ok 
Checking for sigblock                                    : not found 
Checking for sigaction                                   : ok 
Checking for sigset                                      : ok 
Checking for inet_ntoa                                   : ok 
Checking for inet_aton                                   : ok 
Checking for inet_ntop                                   : ok 
Checking for inet_pton                                   : ok 
Checking for connect                                     : ok 
Checking for gethostbyname                               : ok 
Checking for getaddrinfo                                 : ok 
Checking for getnameinfo                                 : ok 
Checking for freeaddrinfo                                : ok 
Checking for gai_strerror                                : ok 
Checking for socketpair                                  : ok 
Checking for memset_s                                    : not found 
Checking for memset_explicit                             : not found 
Checking for volatile memory protection                  : ok 
Checking for variable IPV6_V6ONLY                        : ok 
Checking for header net/if.h                             : yes 
Checking for HAVE_IPV6                                   : ok 
Checking whether we have ucontext_t                      : ok 
Checking for __sync_fetch_and_add compiler builtin       : ok 
Checking for atomic_add_32 compiler builtin              : not found 
Checking for atomic_thread_fence(memory_order_seq_cst) in stdatomic.h : ok 
Checking for fallthrough attribute                                    : ok 
Checking for strdup                                                   : ok 
Checking for memmem                                                   : ok 
Checking for printf                                                   : ok 
Checking for memset                                                   : ok 
Checking for memcpy                                                   : ok 
Checking for memmove                                                  : ok 
Checking for strcpy                                                   : ok 
Checking for strncpy                                                  : ok 
Checking for bzero                                                    : ok 
Checking for shl_load                                                 : not found 
Checking for shl_unload                                               : not found 
Checking for shl_findsym                                              : not found 
Checking for pipe                                                     : ok 
Checking for strftime                                                 : ok 
Checking for srandom                                                  : ok 
Checking for random                                                   : ok 
Checking for srand                                                    : ok 
Checking for rand                                                     : ok 
Checking for usleep                                                   : ok 
Checking for setbuffer                                                : ok 
Checking for lstat                                                    : ok 
Checking for getpgrp                                                  : ok 
Checking for utime                                                    : ok 
Checking for utimes                                                   : ok 
Checking for setuid                                                   : ok 
Checking for seteuid                                                  : ok 
Checking for setreuid                                                 : ok 
Checking for setresuid                                                : ok 
Checking for setgid                                                   : ok 
Checking for setegid                                                  : ok 
Checking for setregid                                                 : ok 
Checking for setresgid                                                : ok 
Checking for chroot                                                   : ok 
Checking for strerror                                                 : ok 
Checking for vsyslog                                                  : ok 
Checking for setlinebuf                                               : ok 
Checking for mktime                                                   : ok 
Checking for ftruncate                                                : ok 
Checking for chsize                                                   : not found 
Checking for rename                                                   : ok 
Checking for waitpid                                                  : ok 
Checking for wait4                                                    : ok 
Checking for initgroups                                               : ok 
Checking for pread                                                    : ok 
Checking for pwrite                                                   : ok 
Checking for strndup                                                  : ok 
Checking for strcasestr                                               : ok 
Checking for strsep                                                   : ok 
Checking for strtok_r                                                 : ok 
Checking for mkdtemp                                                  : ok 
Checking for dup2                                                     : ok 
Checking for dprintf                                                  : ok 
Checking for vdprintf                                                 : ok 
Checking for isatty                                                   : ok 
Checking for chown                                                    : ok 
Checking for lchown                                                   : ok 
Checking for link                                                     : ok 
Checking for readlink                                                 : ok 
Checking for symlink                                                  : ok 
Checking for realpath                                                 : ok 
Checking for snprintf                                                 : ok 
Checking for vsnprintf                                                : ok 
Checking for asprintf                                                 : ok 
Checking for vasprintf                                                : ok 
Checking for setenv                                                   : ok 
Checking for unsetenv                                                 : ok 
Checking for strnlen                                                  : ok 
Checking for strtoull                                                 : ok 
Checking for __strtoull                                               : not found 
Checking for strtouq                                                  : not found 
Checking for strtoll                                                  : ok 
Checking for __strtoll                                                : not found 
Checking for strtoq                                                   : not found 
Checking for memalign                                                 : ok 
Checking for posix_memalign                                           : ok 
Checking for fmemopen                                                 : ok 
Checking for header malloc.h                                          : yes 
Checking for declaration of memalign                                  : ok 
Checking for posix_fallocate-capable libc                             : ok 
Checking for posix_fallocate                                          : ok 
Checking for prctl                                                    : ok 
Checking for dirname                                                  : ok 
Checking for basename                                                 : ok 
Checking for strlcpy                                                  : ok 
Checking for strlcat                                                  : ok 
Checking for getpeereid                                               : not found 
Checking for library setproctitle                                     : no 
Checking for setproctitle                                             : not found 
Checking for setproctitle_init                                        : not found 
Checking for closefrom                                                : not found 
Checking whether we can use SO_PEERCRED to get socket credentials     : ok 
Checking correct behavior of strtoll                                  : ok 
Checking for if_nametoindex                                           : ok 
Checking for strerror_r                                               : ok 
Checking for syslog                                                   : ok 
Checking for gai_strerror                                             : ok 
Checking for get_current_dir_name                                     : ok 
Checking for timegm                                                   : ok 
Checking for getifaddrs                                               : ok 
Checking for freeifaddrs                                              : ok 
Checking for mmap                                                     : ok 
Checking for setgroups                                                : ok 
Checking for syscall                                                  : ok 
Checking for setsid                                                   : ok 
Checking for getgrent_r                                               : not found 
Checking for getgrgid_r                                               : ok 
Checking for getgrnam_r                                               : ok 
Checking for getgrouplist                                             : ok 
Checking for getpagesize                                              : ok 
Checking for getpwent_r                                               : not found 
Checking for getpwnam_r                                               : ok 
Checking for getpwuid_r                                               : ok 
Checking for epoll_create                                             : ok 
Checking for port_create                                              : not found 
Checking for getprogname                                              : not found 
Checking for getxattr                                                 : ok 
Checking whether xattr interface takes additional options             : not found 
Checking for dlopen                                                   : ok 
Checking for dlsym                                                    : ok 
Checking for dlerror                                                  : ok 
Checking for dlclose                                                  : ok 
Checking for declaration of dlopen                                    : ok 
Checking C prototype for dlopen                                       : not found 
Checking for fdatasync                                                : ok 
Checking for declaration of fdatasync                                 : ok 
Checking for clock_gettime                                            : ok 
Checking whether the clock_gettime clock ID CLOCK_MONOTONIC is available : ok 
Checking whether the clock_gettime clock ID CLOCK_PROCESS_CPUTIME_ID is available : ok 
Checking whether the clock_gettime clock ID CLOCK_REALTIME is available           : ok 
Checking for struct timespec                                                      : ok 
Checking for header arpa/nameser.h                                                : yes 
Checking for header resolv.h                                                      : yes 
Checking for res_search                                                           : ok 
Checking for pthread_create                                                       : ok 
Checking for pthread_attr_init                                                    : ok 
Checking for pthread_mutexattr_setrobust                                          : ok 
Checking for declaration of PTHREAD_MUTEX_ROBUST                                  : ok 
Checking for pthread_mutex_consistent                                             : ok 
Checking for __thread local storage                                               : ok 
Checking for crypt                                                                : ok 
Checking for crypt_r                                                              : ok 
Checking for crypt_rn                                                             : not found 
Checking for library crypt                                                        : yes 
Checking for crypt_rn in crypt                                                    : not found 
Checking for header readline.h                                                    : no 
Checking for header readline/readline.h                                           : yes 
Checking for header readline/history.h                                            : yes 
Checking for variable rl_event_hook                                               : ok 
Checking for variable program_invocation_short_name                               : ok 
Checking for declaration of snprintf                                              : ok 
Checking for declaration of vsnprintf                                             : ok 
Checking for declaration of asprintf                                              : ok 
Checking for declaration of vasprintf                                             : ok 
Checking for declaration of errno                                                 : ok 
Checking for declaration of EWOULDBLOCK                                           : ok 
Checking for declaration of environ                                               : ok 
Checking for declaration of getgrent_r                                            : not found 
Checking for declaration of getgrent_r (as enum)                                  : not found 
Checking for declaration of getpwent_r                                            : not found 
Checking for declaration of getpwent_r (as enum)                                  : not found 
Checking for declaration of pread                                                 : ok 
Checking for declaration of pwrite                                                : ok 
Checking for declaration of setenv                                                : ok 
Checking for declaration of setresgid                                             : ok 
Checking for declaration of setresuid                                             : ok 
Checking for eventfd                                                              : ok 
Checking for header poll.h                                                        : yes 
Checking for poll                                                                 : ok 
Checking for strptime                                                             : ok 
Checking for declaration of strptime                                              : ok 
Checking for working strptime                                                     : not found 
Checking for declaration of gettimeofday                                          : ok 
Checking C prototype for gettimeofday                                             : not found 
Checking C prototype for gettimeofday                                             : ok 
Checking for C99 vsnprintf                                                        : ok 
Checking for HAVE_SHARED_MMAP                                                     : ok 
Checking for HAVE_MREMAP                                                          : ok 
Checking for HAVE_INCOHERENT_MMAP                                                 : not found 
Checking for HAVE_IMMEDIATE_STRUCTURES                                            : ok 
Checking for HAVE_MKDIR_MODE                                                      : ok 
Checking for member st_mtim.tv_nsec in struct stat                                : ok 
Checking for member st_rdev in struct stat                                        : ok 
Checking for member st_rdev in struct stat                                        : ok 
Checking for member ss_family in struct sockaddr_storage                          : ok 
Checking for member __ss_family in struct sockaddr_storage                        : not found 
Checking for member sa_len in struct sockaddr                                     : not found 
Checking for member sin_len in struct sockaddr_in                                 : not found 
Checking for member sin6_len in struct sockaddr_in6                               : not found 
Checking for HAVE_UNIXSOCKET                                                      : ok 
Checking for HAVE_SECURE_MKSTEMP                                                  : ok 
Checking for HAVE_IFACE_GETIFADDRS                                                : not found 
Checking for HAVE_IFACE_AIX                                                       : not found 
Checking for HAVE_IFACE_IFCONF                                                    : not found 
Checking for HAVE_IFACE_IFREQ                                                     : not found 
Checking for declaration of getpwent_r                                            : not found 
Checking for declaration of getpwent_r (as enum)                                  : not found 
Checking for declaration of getgrent_r                                            : not found 
Checking for declaration of getgrent_r (as enum)                                  : not found 
Checking for declaration of getpwent_r                                            : not found 
Checking for declaration of getpwent_r (as enum)                                  : not found 
Checking for declaration of getgrent_r                                            : not found 
Checking for declaration of getgrent_r (as enum)                                  : not found 
Checking for strerror_r                                                           : ok 
Checking for XSI (rather than GNU) prototype for strerror_r                       : ok 
Checking for HAVE_FUSE_FUSE_LOWLEVEL_H                                            : not found 
Checking for program 'i386-mingw32-gcc'                                           : not found 
Checking for program 'i386-mingw32msvc-gcc'                                       : not found 
Checking for program 'i386-w64-mingw32-gcc'                                       : not found 
Checking for program 'i586-mingw32-gcc'                                           : not found 
Checking for program 'i586-mingw32msvc-gcc'                                       : not found 
Checking for program 'i586-w64-mingw32-gcc'                                       : not found 
Checking for program 'i686-mingw32-gcc'                                           : not found 
Checking for program 'i686-mingw32msvc-gcc'                                       : not found 
Checking for program 'i686-w64-mingw32-gcc'                                       : not found 
Checking for program 'x86_64-mingw32-gcc'                                         : not found 
Checking for program 'x86_64-mingw32msvc-gcc'                                     : not found 
Checking for program 'x86_64-w64-mingw32-gcc'                                     : not found 
Checking for program 'amd64-mingw32-gcc'                                          : not found 
Checking for program 'amd64-mingw32msvc-gcc'                                      : not found 
Checking for program 'amd64-w64-mingw32-gcc'                                      : not found 
Checking for program 'perl'                                                       : /openwrt/staging_dir/hostpkg/usr/bin/perl 
Checking for program 'perl'                                                       : /openwrt/staging_dir/hostpkg/usr/bin/perl 
Checking for minimum perl version 5.0.0                                           : 5.28.1 
Checking for perl $Config{vendorprefix}:                                          : not found 
PERL_ARCH_INSTALL_DIR:                                                            : '${LIBDIR}/perl5' 
PERL_LIB_INSTALL_DIR:                                                             : '${DATADIR}/perl5' 
PERL_INC:                                                                         : ['/openwrt/staging_dir/hostpkg/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi', '/openwrt/staging_dir/hostpkg/usr/lib/perl5/site_perl/5.28.1', '/openwrt/staging_dir/hostpkg/usr/lib/perl5/5.28.1/x86_64-linux-thread-multi', '/openwrt/staging_dir/hostpkg/usr/lib/perl5/5.28.1'] 
Checking for program 'xsltproc'                                                   : false 
Checking for program 'python3'                                                    : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for program 'python'                                                     : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for program 'python3'                                                    : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for python version >= 2.6.0                                              : 3.9.5 
python headers                                                                    : Check disabled due to --disable-python 
Dynconfig[BINDIR]:                                                                : '/usr/bin' 
Dynconfig[SBINDIR]:                                                               : '/usr/sbin' 
Dynconfig[LIBDIR]:                                                                : '/usr/lib' 
Dynconfig[LIBEXECDIR]:                                                            : '/usr/lib' 
Dynconfig[DATADIR]:                                                               : '/usr/share' 
Dynconfig[SAMBA_DATADIR]:                                                         : '/usr/share/samba' 
Dynconfig[LOCALEDIR]:                                                             : '/usr/share/locale' 
Dynconfig[PYTHONDIR]:                                                             : '/usr/lib/python3.9/site-packages' 
Dynconfig[PYTHONARCHDIR]:                                                         : '/usr/lib/python3.9/site-packages' 
Dynconfig[PERL_LIB_INSTALL_DIR]:                                                  : '/usr/share/perl5' 
Dynconfig[PERL_ARCH_INSTALL_DIR]:                                                 : '/usr/lib/perl5' 
Dynconfig[INCLUDEDIR]:                                                            : '/usr/include/samba-4.0' 
Dynconfig[SCRIPTSBINDIR]:                                                         : '/usr/sbin' 
Dynconfig[SETUPDIR]:                                                              : '/usr/share/samba/setup' 
Dynconfig[PKGCONFIGDIR]:                                                          : '/usr/lib/pkgconfig' 
Dynconfig[CODEPAGEDIR]:                                                           : '/usr/share/samba/codepages' 
Dynconfig[PRIVATELIBDIR]:                                                         : '/usr/lib/samba' 
Dynconfig[MODULESDIR]:                                                            : '/usr/lib/samba' 
Dynconfig[PAMMODULESDIR]:                                                         : '/usr/lib/security' 
Dynconfig[CONFIGDIR]:                                                             : '/etc/samba' 
Dynconfig[PRIVATE_DIR]:                                                           : '/etc/samba' 
Dynconfig[BINDDNS_DIR]:                                                           : '/var/lib/samba/bind-dns' 
Dynconfig[LOCKDIR]:                                                               : '/var/lock' 
Dynconfig[PIDDIR]:                                                                : '/var/run' 
Dynconfig[STATEDIR]:                                                              : '/var/lib/samba' 
Dynconfig[CACHEDIR]:                                                              : '/var/cache/samba' 
Dynconfig[LOGFILEBASE]:                                                           : '/var/log' 
Dynconfig[SOCKET_DIR]:                                                            : '/var/run/samba' 
Dynconfig[PRIVILEGED_SOCKET_DIR]:                                                 : '/var/lib/samba' 
Dynconfig[WINBINDD_SOCKET_DIR]:                                                   : '/var/run/samba/winbindd' 
Dynconfig[NMBDSOCKETDIR]:                                                         : '/var/run/samba/nmbd' 
Dynconfig[NTP_SIGND_SOCKET_DIR]:                                                  : '/var/lib/samba/ntp_signd' 
Dynconfig[NCALRPCDIR]:                                                            : '/var/run/samba/ncalrpc' 
Dynconfig[CONFIGFILE]:                                                            : '/etc/samba/smb.conf' 
Dynconfig[LMHOSTSFILE]:                                                           : '/etc/samba/lmhosts' 
Dynconfig[SMB_PASSWD_FILE]:                                                       : '/etc/samba/smbpasswd' 
Checking for 'zlib'                                                               : yes 
Checking for library z                                                            : yes 
Checking for inflateInit2 in z                                                    : not found 
Checking for longjmp                                                              : ok 
Checking for siglongjmp                                                           : ok 
Checking for system popt                                                          : yes 
Checking for header popt.h                                                        : yes 
Checking for library popt                                                         : yes 
Checking for poptGetContext in popt                                               : ok 
Checking for program 'python3'                                                    : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for program 'python'                                                     : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for program 'python3'                                                    : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for python version >= 2.6.0                                              : 3.9.5 
python headers                                                                    : Check disabled due to --disable-python 
Checking linker accepts -Wl,-no-undefined                                         : yes 
Checking linker accepts ['-undefined', 'dynamic_lookup']                          : no 
Checking for header sys/auxv.h                                                    : yes 
Checking for getauxval                                                            : ok 
Checking linker accepts -Wl,-no-undefined                                         : yes 
Checking linker accepts ['-undefined', 'dynamic_lookup']                          : no 
Checking for program 'python3'                                                    : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for program 'python'                                                     : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for program 'python3'                                                    : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for python version >= 2.6.0                                              : 3.9.5 
python headers                                                                    : Check disabled due to --disable-python 
Checking for epoll_create                                                         : ok 
Checking value of NSIG                                                            : 128 
Checking value of _NSIG                                                           : 128 
Checking value of SIGRTMAX                                                        : 127 
Checking value of SIGRTMIN                                                        : 35 
Checking for program 'python3'                                                    : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for program 'python'                                                     : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for program 'python3'                                                    : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for python version >= 2.6.0                                              : 3.9.5 
python headers                                                                    : Check disabled due to --disable-python 
Checking linker accepts -Wl,-no-undefined                                         : yes 
Checking linker accepts ['-undefined', 'dynamic_lookup']                          : no 
Checking for program 'xsltproc'                                                   : false 
Checking for program 'python3'                                                    : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for program 'python'                                                     : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for program 'python3'                                                    : /openwrt/staging_dir/hostpkg/bin/python3 
Checking for python version >= 2.6.0                                              : 3.9.5 
python headers                                                                    : Check disabled due to --disable-python 
Checking for a 64-bit host to support lmdb                                        : not found 
--without-ldb-lmdb implied as this host is not 64-bit
Checking linker accepts -Wl,-no-undefined                                         : yes 
Checking linker accepts ['-undefined', 'dynamic_lookup']                          : no 
Checking linker accepts ['-Wl,--wrap=test']                                       : yes 
Checking for u_char                                                               : ok 
Checking for u_int32_t                                                            : ok 
Checking for header err.h                                                         : yes 
Checking for header sys/bswap.h                                                   : no 
Checking for header sys/stropts.h                                                 : yes 
Checking for header sys/timeb.h                                                   : yes 
Checking for header sys/times.h                                                   : yes 
Checking for header timezone.h                                                    : no 
Checking for header ttyname.h                                                     : no 
Checking for header netinet/in6.h                                                 : no 
Checking for header netinet6/in6.h                                                : no 
Checking for header curses.h                                                      : yes 
Checking for header term.h                                                        : yes 
Checking for header termcap.h                                                     : yes 
Checking for atexit                                                               : ok 
Checking for cgetent                                                              : not found 
Checking for getprogname                                                          : not found 
Checking for setprogname                                                          : not found 
Checking for gethostname                                                          : ok 
Checking for putenv                                                               : ok 
Checking for rcmd                                                                 : not found 
Checking for readv                                                                : ok 
Checking for sendmsg                                                              : ok 
Checking for setitimer                                                            : ok 
Checking for strlwr                                                               : not found 
Checking for strncasecmp                                                          : ok 
Checking for strptime                                                             : ok 
Checking for strsep                                                               : ok 
Checking for strsep_copy                                                          : not found 
Checking for strtok_r                                                             : ok 
Checking for strupr                                                               : not found 
Checking for swab                                                                 : ok 
Checking for umask                                                                : ok 
Checking for uname                                                                : ok 
Checking for unsetenv                                                             : ok 
Checking for closefrom                                                            : not found 
Checking for err                                                                  : ok 
Checking for warn                                                                 : ok 
Checking for errx                                                                 : ok 
Checking for warnx                                                                : ok 
Checking for flock                                                                : ok 
Checking for writev                                                               : ok 
Checking for hstrerror                                                            : ok 
Checking for socket                                                               : ok 
Checking for getipnodebyname                                                      : not found 
Checking for gethostent                                                           : ok 
Checking for gethostent_r                                                         : not found 
Checking for sethostent                                                           : ok 
Checking for endhostent                                                           : ok 
Checking for getipnodebyaddr                                                      : not found 
Checking for freehostent                                                          : not found 
Checking for gethostbyname_r                                                      : ok 
Checking for gethostbyaddr                                                        : ok 
Checking for library socket                                                       : no 
Checking for getipnodebyname in nsl                                               : not found 
Checking for gethostent_r in nsl                                                  : not found 
Checking for getipnodebyaddr in nsl                                               : not found 
Checking for freehostent in nsl                                                   : not found 
Checking for iruserok                                                             : not found 
Checking for bswap16                                                              : not found 
Checking for bswap32                                                              : not found 
Checking for header sys/termios.h                                                 : yes 
Checking for struct winsize                                                       : ok 
Checking for member ws_xpixel in struct winsize                                   : ok 
Checking for member ws_ypixel in struct winsize                                   : ok 
Checking for variable h_errno                                                     : ok 
Checking for declaration of h_errno                                               : ok 
Checking for res_nsearch                                                          : not found 
Checking for res_ndestroy                                                         : not found 
Checking for dns_search                                                           : not found 
Checking for dn_expand                                                            : ok 
Checking for library resolv                                                       : yes 
Checking for res_nsearch in resolv                                                : not found 
Checking for res_ndestroy in resolv                                               : not found 
Checking for dns_search in resolv                                                 : not found 
Checking for variable _res                                                        : ok 
Checking for declaration of _res                                                  : ok 
Checking for dirfd                                                                : ok 
Checking for declaration of dirfd                                                 : ok 
Checking for member dd_fd in DIR                                                  : not found 
Using in-tree heimdal kerberos defines
Checking for program 'compile_et'                                                 : /openwrt/staging_dir/hostpkg/bin/compile_et_samba 
Checking for program 'asn1_compile'                                               : /openwrt/staging_dir/hostpkg/bin/asn1_compile_samba 
Checking for GnuTLS >= 3.4.7                                                      : not found 
The configuration failed
(complete log in /openwrt/build_dir/target-mips_24kc_musl/samba-4.13.9/bin/config.log)
make[3]: *** [Makefile:461: /openwrt/build_dir/target-mips_24kc_musl/samba-4.13.9/.configured_e7513375d4aee0412e142789921ec856] Error 1
```
