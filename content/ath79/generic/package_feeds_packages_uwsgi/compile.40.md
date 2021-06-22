---
title: "compile.40"
date: 2021-06-22 10:49:10.767442
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
make package/feeds/packages/uwsgi/compile -j$(nproc) || make package/feeds/packages/uwsgi/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-dont-hardcode-zlib.patch using plaintext: 
patching file uwsgiconfig.py

Applying ./patches/002-dont-override-toolchain-optimization.patch using plaintext: 
patching file uwsgiconfig.py

Applying ./patches/003-hard-code-Linux-as-compilation-os.patch using plaintext: 
patching file uwsgiconfig.py

Applying ./patches/010-uclibc-ng.patch using plaintext: 
patching file core/uwsgi.c

Applying ./patches/020-uwsgiconfig-system-python3.patch using plaintext: 
patching file Makefile

Applying ./patches/030-plugins-cgi_adds_dontresolve_option.patch using plaintext: 
patching file plugins/cgi/cgi_plugin.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/pypi/uWSGI-2.0.19.1'
/openwrt/staging_dir/hostpkg/bin/python3 uwsgiconfig.py --build openwrt
using profile: buildconf/openwrt.ini
detected include path: ['/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/sys-include', '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include', '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/include', '/openwrt/staging_dir/target-mips_24kc_musl/usr/include']
detected CPU cores: 2
configured CFLAGS: -I. -Wall -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/uWSGI-2.0.19.1=uWSGI-2.0.19.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -DUWSGI_HAS_IFADDRS -DUWSGI_LOCK_USE_MUTEX -DUWSGI_EVENT_USE_EPOLL -DUWSGI_EVENT_TIMER_USE_TIMERFD -DUWSGI_EVENT_FILEMONITOR_USE_INOTIFY -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include -DUWSGI_PCRE -DUWSGI_ROUTING -DUWSGI_CAP -DUWSGI_UUID -DUWSGI_VERSION="\"2.0.19.1\"" -DUWSGI_VERSION_BASE="2" -DUWSGI_VERSION_MAJOR="0" -DUWSGI_VERSION_MINOR="19" -DUWSGI_VERSION_REVISION="1" -DUWSGI_VERSION_CUSTOM="\"\"" -DUWSGI_PLUGIN_DIR="\"/usr/lib/uwsgi\""
*** uWSGI compiling server core ***
[thread 1][ccache_cc] core/utils.o
[thread 0][ccache_cc] core/protocol.o
[thread 0][ccache_cc] core/socket.o
[thread 0][ccache_cc] core/logging.o
[thread 1][ccache_cc] core/master.o
[thread 1][ccache_cc] core/master_utils.o
[thread 0][ccache_cc] core/emperor.o
[thread 1][ccache_cc] core/notify.o
[thread 1][ccache_cc] core/mule.o
[thread 1][ccache_cc] core/subscription.o
[thread 0][ccache_cc] core/stats.o
[thread 0][ccache_cc] core/sendfile.o
[thread 1][ccache_cc] core/async.o
[thread 0][ccache_cc] core/master_checks.o
[thread 1][ccache_cc] core/fifo.o
[thread 1][ccache_cc] core/offload.o
[thread 0][ccache_cc] core/io.o
[thread 1][ccache_cc] core/static.o
[thread 1][ccache_cc] core/websockets.o
[thread 0][ccache_cc] core/spooler.o
[thread 1][ccache_cc] core/snmp.o
[thread 1][ccache_cc] core/exceptions.o
[thread 0][ccache_cc] core/config.o
[thread 1][ccache_cc] core/setup_utils.o
[thread 0][ccache_cc] core/clock.o
[thread 0][ccache_cc] core/init.o
[thread 1][ccache_cc] core/buffer.o
[thread 0][ccache_cc] core/reader.o
[thread 1][ccache_cc] core/writer.o
[thread 0][ccache_cc] core/alarm.o
[thread 1][ccache_cc] core/cron.o
[thread 0][ccache_cc] core/hooks.o
[thread 1][ccache_cc] core/plugins.o
[thread 1][ccache_cc] core/lock.o
[thread 0][ccache_cc] core/cache.o
[thread 1][ccache_cc] core/daemons.o
[thread 1][ccache_cc] core/errors.o
[thread 1][ccache_cc] core/hash.o
[thread 0][ccache_cc] core/master_events.o
[thread 1][ccache_cc] core/chunked.o
[thread 0][ccache_cc] core/queue.o
[thread 1][ccache_cc] core/event.o
[thread 0][ccache_cc] core/signal.o
[thread 1][ccache_cc] core/strings.o
[thread 0][ccache_cc] core/progress.o
[thread 1][ccache_cc] core/timebomb.o
[thread 0][ccache_cc] core/ini.o
[thread 1][ccache_cc] core/fsmon.o
[thread 1][ccache_cc] core/mount.o
[thread 0][ccache_cc] core/metrics.o
[thread 1][ccache_cc] core/plugins_builder.o
[thread 1][ccache_cc] core/sharedarea.o
[thread 0][ccache_cc] core/rpc.o
[thread 1][ccache_cc] core/gateway.o
[thread 0][ccache_cc] core/loop.o
[thread 1][ccache_cc] core/cookie.o
[thread 0][ccache_cc] core/querystring.o
[thread 1][ccache_cc] core/rb_timers.o
[thread 0][ccache_cc] core/transformations.o
[thread 1][ccache_cc] core/uwsgi.o
[thread 0][ccache_cc] proto/base.o
[thread 0][ccache_cc] proto/uwsgi.o
[thread 0][ccache_cc] proto/http.o
[thread 0][ccache_cc] proto/fastcgi.o
[thread 1][ccache_cc] proto/scgi.o
[thread 1][ccache_cc] proto/puwsgi.o
[thread 0][ccache_cc] lib/linux_ns.o
[thread 1][ccache_cc] core/regexp.o
[thread 0][ccache_cc] core/routing.o
[thread 1][ccache_cc] core/dot_h.o
[thread 1][ccache_cc] core/config_py.o
*** uWSGI linking ***
ccache_cc -o uwsgi -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro core/utils.o core/protocol.o core/socket.o core/logging.o core/master.o core/master_utils.o core/emperor.o core/notify.o core/mule.o core/subscription.o core/stats.o core/sendfile.o core/async.o core/master_checks.o core/fifo.o core/offload.o core/io.o core/static.o core/websockets.o core/spooler.o core/snmp.o core/exceptions.o core/config.o core/setup_utils.o core/clock.o core/init.o core/buffer.o core/reader.o core/writer.o core/alarm.o core/cron.o core/hooks.o core/plugins.o core/lock.o core/cache.o core/daemons.o core/errors.o core/hash.o core/master_events.o core/chunked.o core/queue.o core/event.o core/signal.o core/strings.o core/progress.o core/timebomb.o core/ini.o core/fsmon.o core/mount.o core/metrics.o core/plugins_builder.o core/sharedarea.o core/rpc.o core/gateway.o core/loop.o core/cookie.o core/querystring.o core/rb_timers.o core/transformations.o core/uwsgi.o proto/base.o proto/uwsgi.o proto/http.o proto/fastcgi.o proto/scgi.o proto/puwsgi.o lib/linux_ns.o core/regexp.o core/routing.o core/dot_h.o core/config_py.o -lpthread -lm -rdynamic -ldl -L/openwrt/staging_dir/target-mips_24kc_musl/usr/lib -lpcre -lcap -luuid
################# uWSGI configuration #################

kernel = Linux
execinfo = False
ifaddrs = True
locking = pthread_mutex
event = epoll
timer = timerfd
filemonitor = inotify
pcre = True
routing = True
capabilities = True
yaml = False
json = False
ssl = False
xml = False
debug = False
plugin_dir = /usr/lib/uwsgi
zlib = False
ucontext = False
malloc = libc

############## end of uWSGI configuration #############
total build time: 16 seconds
*** uWSGI is ready, launch it with ./uwsgi ***
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/pypi/uWSGI-2.0.19.1'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/pypi/uWSGI-2.0.19.1'
/openwrt/staging_dir/hostpkg/bin/python3 uwsgiconfig.py --plugin plugins/logfile openwrt
using profile: buildconf/openwrt.ini
detected include path: ['/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/sys-include', '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include', '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/include', '/openwrt/staging_dir/target-mips_24kc_musl/usr/include']
*** uWSGI building and linking plugin plugins/logfile ***
[ccache_cc] ./logfile_plugin.so
build time: 0 seconds
*** logfile plugin built and available in ./logfile_plugin.so ***
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/pypi/uWSGI-2.0.19.1'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/pypi/uWSGI-2.0.19.1'
/openwrt/staging_dir/hostpkg/bin/python3 uwsgiconfig.py --plugin plugins/syslog openwrt
using profile: buildconf/openwrt.ini
detected include path: ['/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/sys-include', '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include', '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/include', '/openwrt/staging_dir/target-mips_24kc_musl/usr/include']
*** uWSGI building and linking plugin plugins/syslog ***
[ccache_cc] ./syslog_plugin.so
build time: 0 seconds
*** syslog plugin built and available in ./syslog_plugin.so ***
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/pypi/uWSGI-2.0.19.1'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/pypi/uWSGI-2.0.19.1'
/openwrt/staging_dir/hostpkg/bin/python3 uwsgiconfig.py --plugin plugins/cgi openwrt
using profile: buildconf/openwrt.ini
detected include path: ['/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/sys-include', '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include', '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/include', '/openwrt/staging_dir/target-mips_24kc_musl/usr/include']
*** uWSGI building and linking plugin plugins/cgi ***
[ccache_cc] ./cgi_plugin.so
build time: 0 seconds
*** cgi plugin built and available in ./cgi_plugin.so ***
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/pypi/uWSGI-2.0.19.1'
In file included from plugins/python/python_plugin.c:1:
plugins/python/uwsgi_python.h:2:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
In file included from plugins/python/pyutils.c:1:
plugins/python/uwsgi_python.h:2:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
In file included from plugins/python/pyloader.c:1:
plugins/python/uwsgi_python.h:2:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
In file included from plugins/python/wsgi_handlers.c:1:
plugins/python/uwsgi_python.h:2:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
In file included from plugins/python/wsgi_headers.c:1:
plugins/python/uwsgi_python.h:2:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
In file included from plugins/python/wsgi_subhandler.c:1:
plugins/python/uwsgi_python.h:2:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
In file included from plugins/python/web3_subhandler.c:1:
plugins/python/uwsgi_python.h:2:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
In file included from plugins/python/pump_subhandler.c:1:
plugins/python/uwsgi_python.h:2:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
In file included from plugins/python/gil.c:1:
plugins/python/uwsgi_python.h:2:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
In file included from plugins/python/uwsgi_pymodule.c:1:
plugins/python/uwsgi_python.h:2:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
In file included from plugins/python/profiler.c:1:
plugins/python/uwsgi_python.h:2:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
In file included from plugins/python/symimporter.c:1:
plugins/python/uwsgi_python.h:2:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
In file included from plugins/python/tracebacker.c:1:
plugins/python/uwsgi_python.h:2:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
In file included from plugins/python/raw.c:1:
plugins/python/uwsgi_python.h:2:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
using profile: buildconf/openwrt.ini
detected include path: ['/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/sys-include', '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/include', '/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/include', '/openwrt/staging_dir/target-mips_24kc_musl/usr/include']
*** uWSGI building and linking plugin plugins/python ***
[ccache_cc] ./python_plugin.so
*** unable to build python plugin ***
make[3]: *** [Makefile:173: /openwrt/build_dir/target-mips_24kc_musl/pypi/uWSGI-2.0.19.1/.built] Error 1
```
