---
title: "compile.37"
date: 2021-06-20 22:37:23.038138
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
make package/feeds/packages/python-curl/compile -j$(nproc) || make package/feeds/packages/python-curl/compile V=s
```

#### Compile.txt

``` bash
Traceback (most recent call last):
  File "/openwrt/build_dir/target-mips_24kc_musl/pypi/pycurl-7.43.0.6/setup.py", line 236, in configure_unix
    p = subprocess.Popen((self.curl_config(), '--version'),
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/subprocess.py", line 951, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/subprocess.py", line 1821, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'curl-config'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/openwrt/build_dir/target-mips_24kc_musl/pypi/pycurl-7.43.0.6/setup.py", line 988, in <module>
    ext = get_extension(sys.argv, split_extension_source=split_extension_source)
  File "/openwrt/build_dir/target-mips_24kc_musl/pypi/pycurl-7.43.0.6/setup.py", line 649, in get_extension
    ext_config = ExtensionConfiguration(argv)
  File "/openwrt/build_dir/target-mips_24kc_musl/pypi/pycurl-7.43.0.6/setup.py", line 101, in __init__
    self.configure()
  File "/openwrt/build_dir/target-mips_24kc_musl/pypi/pycurl-7.43.0.6/setup.py", line 241, in configure_unix
    raise ConfigurationError(msg)
__main__.ConfigurationError: Could not run curl-config: [Errno 2] No such file or directory: 'curl-config'
make[3]: *** [Makefile:59: /openwrt/build_dir/target-mips_24kc_musl/pypi/pycurl-7.43.0.6/.built] Error 1
```
