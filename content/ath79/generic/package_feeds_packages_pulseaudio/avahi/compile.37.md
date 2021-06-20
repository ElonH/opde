---
title: "compile.37"
date: 2021-06-20 22:32:33.805812
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
make package/feeds/packages/pulseaudio/compile -j$(nproc) || make package/feeds/packages/pulseaudio/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-no_default_64mb_alloc.patch using plaintext: 
patching file src/pulsecore/memblock.c

Applying ./patches/010-iconv.patch using plaintext: 
patching file meson.build

Applying ./patches/020-doxygen.patch using plaintext: 
patching file meson.build
The Meson build system
Version: 0.57.2
Source dir: /openwrt/build_dir/target-mips_24kc_musl/pulseaudio-avahi/pulseaudio-14.2
Build dir: /openwrt/build_dir/target-mips_24kc_musl/pulseaudio-avahi/pulseaudio-14.2/openwrt-build
Build type: cross build
Program git-version-gen found: YES (/openwrt/build_dir/target-mips_24kc_musl/pulseaudio-avahi/pulseaudio-14.2/git-version-gen)
WARNING: Unknown options: "build.libdir, build.prefix, build.sbindir"
The value of new options can be set with:
meson setup <builddir> --reconfigure -Dnew_option=new_value ...
Project name: pulseaudio
Project version: 14.2
C compiler for the host machine: ccache_cc (gcc 8.4.0 "mips-openwrt-linux-musl-gcc (OpenWrt GCC 8.4.0 r0-91deb05) 8.4.0")
C linker for the host machine: ccache_cc ld.bfd 2.34
C++ compiler for the host machine: ccache_cxx (gcc 8.4.0 "mips-openwrt-linux-musl-g++ (OpenWrt GCC 8.4.0 r0-91deb05) 8.4.0")
C++ linker for the host machine: ccache_cxx ld.bfd 2.34
C compiler for the build machine: ccache gcc (gcc 9.3.0 "gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C linker for the build machine: gcc ld.bfd 2.34
C++ compiler for the build machine: ccache g++ (gcc 9.3.0 "g++ (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0")
C++ linker for the build machine: g++ ld.bfd 2.34
Build machine cpu family: x86_64
Build machine cpu: x86_64
Host machine cpu family: mips
Host machine cpu: generic
Target machine cpu family: mips
Target machine cpu: generic
Found pkg-config: /openwrt/staging_dir/host/bin/pkg-config (1.7.3)
Found CMake: NO
Run-time dependency bash-completion found: NO (tried pkgconfig and cmake)
Checking for type "_Bool" : YES 
Checking for size of "void *" : 4
Has header "arpa/inet.h" : YES 
Has header "byteswap.h" : YES 
Has header "cpuid.h" : NO 
Has header "dlfcn.h" : YES 
Has header "execinfo.h" : NO 
Has header "grp.h" : YES 
Has header "langinfo.h" : YES 
Has header "linux/sockios.h" : YES 
Has header "locale.h" : YES 
Has header "netdb.h" : YES 
Has header "netinet/in.h" : YES 
Has header "netinet/in_systm.h" : YES 
Has header "netinet/ip.h" : YES 
Has header "netinet/tcp.h" : YES 
Has header "pcreposix.h" : YES 
Has header "poll.h" : YES 
Has header "pwd.h" : YES 
Has header "regex.h" : YES 
Has header "sched.h" : YES 
Has header "stdint.h" : YES 
Has header "sys/atomic.h" : NO 
Has header "sys/capability.h" : YES 
Has header "sys/conf.h" : NO 
Has header "sys/dl.h" : NO 
Has header "sys/eventfd.h" : YES 
Has header "sys/filio.h" : NO 
Has header "sys/ioctl.h" : YES 
Has header "sys/mman.h" : YES 
Has header "sys/prctl.h" : YES 
Has header "sys/resource.h" : YES 
Has header "sys/select.h" : YES 
Has header "sys/socket.h" : YES 
Has header "sys/syscall.h" : YES 
Has header "sys/uio.h" : YES 
Has header "sys/un.h" : YES 
Has header "sys/wait.h" : YES 
Has header "syslog.h" : YES 
Has header "valgrind/memcheck.h" : NO 
Has header "xlocale.h" : NO 
Has header "pthread.h" : YES 
Header <pthread.h> has symbol "PTHREAD_PRIO_INHERIT" : YES 
Checking for function "accept4" : YES 
Checking for function "clock_gettime" : YES 
Checking for function "ctime_r" : YES 
Checking for function "fchmod" : YES 
Checking for function "fchown" : YES 
Checking for function "fork" : YES 
Checking for function "fstat" : YES 
Checking for function "getaddrinfo" : YES 
Checking for function "getgrgid_r" : YES 
Checking for function "getgrnam_r" : YES 
Checking for function "getpwnam_r" : YES 
Checking for function "getpwuid_r" : YES 
Checking for function "gettimeofday" : YES 
Checking for function "getuid" : YES 
Checking for function "lrintf" : YES 
Checking for function "lstat" : YES 
Checking for function "memfd_create" : YES 
Checking for function "mkfifo" : YES 
Checking for function "mlock" : YES 
Checking for function "nanosleep" : YES 
Checking for function "open64" : YES 
Checking for function "paccept" : NO 
Checking for function "pipe" : YES 
Checking for function "pipe2" : YES 
Checking for function "posix_fadvise" : YES 
Checking for function "posix_madvise" : YES 
Checking for function "posix_memalign" : YES 
Checking for function "ppoll" : YES 
Checking for function "readlink" : YES 
Checking for function "setegid" : YES 
Checking for function "seteuid" : YES 
Checking for function "setpgid" : YES 
Checking for function "setregid" : YES 
Checking for function "setresgid" : YES 
Checking for function "setresuid" : YES 
Checking for function "setreuid" : YES 
Checking for function "setsid" : YES 
Checking for function "sig2str" : NO 
Checking for function "sigaction" : YES 
Checking for function "strerror_r" : YES 
Checking for function "strtod_l" : YES 
Checking for function "strtof" : YES 
Checking for function "symlink" : YES 
Checking for function "sysconf" : YES 
Checking for function "uname" : YES 
Header <sys/syscall.h> has symbol "SYS_memfd_create" : YES 
Checking for function "dgettext" : YES 
Header <signal.h> has symbol "SIGXCPU" : YES 
Header <netinet/in.h> has symbol "INADDR_NONE" : YES 
Header <unistd.h> has symbol "environ" : YES 
Header <sys/soundcard.h> has symbol "SOUND_PCM_READ_RATE" : YES 
Header <sys/soundcard.h> has symbol "SOUND_PCM_READ_CHANNELS" : YES 
Header <sys/soundcard.h> has symbol "SOUND_PCM_READ_BITS" : YES 
Library m found: YES
Run-time dependency threads found: YES
Checking for function "pthread_getname_np" with dependency threads: NO 
Checking for function "pthread_setaffinity_np" with dependency threads: YES 
Checking for function "pthread_setname_np" with dependency threads: YES 
Library cap found: YES
Library rt found: YES
Library dl found: YES
Library iconv found: YES
Library ltdl found: YES
Run-time dependency alsa found: YES 1.2.5
Dependency libasyncns skipped: feature asyncns disabled
Run-time dependency dbus-1 found: YES 1.13.18
Dependency gio-2.0 skipped: feature gsettings disabled
Dependency glib-2.0 skipped: feature glib disabled
Dependency gtk+-3.0 skipped: feature gtk disabled
Dependency orc-0.4 skipped: feature orc disabled
Program orcc skipped: feature orc disabled
Dependency samplerate skipped: feature samplerate disabled
Run-time dependency sndfile found: YES 1.0.29
Dependency soxr skipped: feature soxr disabled
Dependency libsystemd skipped: feature systemd disabled
Dependency systemd skipped: feature systemd disabled
Dependency x11-xcb skipped: feature x11 disabled
Has header "sys/soundcard.h" : YES 
Run-time dependency avahi-client found: YES 0.8
Run-time dependency sbc found: YES 1.5
Dependency fftw3f skipped: feature fftw disabled
Dependency jack skipped: feature jack disabled
Dependency lirc skipped: feature lirc disabled
Run-time dependency openssl found: NO (tried pkgconfig)

../../../../build_dir/target-mips_24kc_musl/pulseaudio-avahi/pulseaudio-14.2/meson.build:659:0: ERROR: Dependency "openssl" not found, tried pkgconfig

A full log can be found at /openwrt/build_dir/target-mips_24kc_musl/pulseaudio-avahi/pulseaudio-14.2/openwrt-build/meson-logs/meson-log.txt
make[3]: *** [Makefile:304: /openwrt/build_dir/target-mips_24kc_musl/pulseaudio-avahi/pulseaudio-14.2/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
