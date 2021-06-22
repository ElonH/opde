---
title: "compile.40"
date: 2021-06-22 10:50:44.054931
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
make package/feeds/packages/python-cryptography/compile -j$(nproc) || make package/feeds/packages/python-cryptography/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0001-Add-new-ASN1_STRING_get0_data-API.patch using plaintext: 
patching file src/_cffi_src/openssl/asn1.py

Applying ./patches/0002-Add-compatibility-for-X509_STORE_set_get_issuer.patch using plaintext: 
patching file src/_cffi_src/openssl/x509_vfy.py
patching file src/cryptography/hazmat/bindings/openssl/_conditional.py

Applying ./patches/0003-Add-compatibility-for-deprecated-TLS-methods.patch using plaintext: 
patching file src/_cffi_src/openssl/ssl.py
patching file src/cryptography/hazmat/bindings/openssl/_conditional.py

Applying ./patches/0004-disable-rust.patch using plaintext: 
patching file setup.py

Applying ./patches/0006-Add-X509_STORE_CTX_trusted_stack-compatibility-macro.patch using plaintext: 
patching file src/_cffi_src/openssl/x509_vfy.py

Applying ./patches/0007-Add-defines-for-totally-deprecated-functions.patch using plaintext: 
patching file src/_cffi_src/openssl/conf.py
patching file src/_cffi_src/openssl/crypto.py
patching file src/_cffi_src/openssl/ecdh.py
patching file src/_cffi_src/openssl/ssl.py
Requirement already satisfied: cffi==1.14.5 in /openwrt/staging_dir/hostpkg/lib/python3.9/site-packages (from -r ../host-pip-requirements/cffi.txt (line 1)) (1.14.5)
Requirement already satisfied: pycparser==2.20 in /openwrt/staging_dir/hostpkg/lib/python3.9/site-packages (from -r ../host-pip-requirements/cffi.txt (line 2)) (2.20)
WARNING: The wheel package is not available.
ERROR: Exception:
Traceback (most recent call last):
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/cli/base_command.py", line 180, in _main
    status = self.run(options, args)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/cli/req_command.py", line 204, in wrapper
    return func(self, options, args)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/commands/wheel.py", line 142, in run
    requirement_set = resolver.resolve(
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/resolver.py", line 127, in resolve
    result = self._result = resolver.resolve(
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py", line 473, in resolve
    state = resolution.resolve(requirements, max_rounds=max_rounds)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py", line 341, in resolve
    name, crit = self._merge_into_criterion(r, parent=None)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py", line 172, in _merge_into_criterion
    if not criterion.candidates:
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_vendor/resolvelib/structs.py", line 139, in __bool__
    return bool(self._sequence)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py", line 143, in __bool__
    return any(self)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py", line 129, in <genexpr>
    return (c for c in iterator if id(c) not in self._incompatible_ids)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py", line 30, in _iter_built
    for version, func in infos:
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/factory.py", line 258, in iter_index_candidate_infos
    result = self._finder.find_best_candidate(
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/index/package_finder.py", line 879, in find_best_candidate
    candidates = self.find_all_candidates(project_name)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/index/package_finder.py", line 824, in find_all_candidates
    page_candidates = list(page_candidates_it)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/index/sources.py", line 134, in page_candidates
    yield from self._candidates_from_page(self._link)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/index/package_finder.py", line 790, in process_project_url
    package_links = self.evaluate_links(
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/index/package_finder.py", line 772, in evaluate_links
    candidate = self.get_install_candidate(link_evaluator, link)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/index/package_finder.py", line 753, in get_install_candidate
    is_candidate, result = link_evaluator.evaluate_link(link)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/index/package_finder.py", line 185, in evaluate_link
    supported_tags = self._target_python.get_tags()
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/models/target_python.py", line 106, in get_tags
    tags = get_supported(
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_internal/utils/compatibility_tags.py", line 151, in get_supported
    supported.extend(
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_vendor/packaging/tags.py", line 276, in cpython_tags
    platforms = list(platforms or _platform_tags())
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pip/_vendor/packaging/tags.py", line 790, in _linux_platforms
    _, arch = linux.split("_", 1)
ValueError: not enough values to unpack (expected 2, got 1)

    =============================DEBUG ASSISTANCE=============================
    If you are seeing a compilation error please try the following steps to
    successfully install cryptography:
    1) Upgrade to the latest pip and try again. This will fix errors for most
       users. See: https://pip.pypa.io/en/stable/installing/#upgrading-pip
    2) Read https://cryptography.io/en/latest/installation.html for specific
       instructions for your platform.
    3) Check our frequently asked questions for more information:
       https://cryptography.io/en/latest/faq.html
    4) Ensure you have a recent Rust toolchain installed:
       https://cryptography.io/en/latest/installation.html#rust
    5) If you are experiencing issues with Rust for *this release only* you may
       set the environment variable `CRYPTOGRAPHY_DONT_BUILD_RUST=1`.
    =============================DEBUG ASSISTANCE=============================
    
Traceback (most recent call last):
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/setuptools/installer.py", line 75, in fetch_build_egg
    subprocess.check_call(cmd)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/subprocess.py", line 373, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['/openwrt/staging_dir/hostpkg/bin/python3.9', '-m', 'pip', '--disable-pip-version-check', 'wheel', '--no-deps', '-w', '/openwrt/tmp/tmpfarof1us', '--quiet', 'setuptools-rust>=0.11.4']' returned non-zero exit status 2.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/openwrt/build_dir/target-mips_24kc_musl/pypi/cryptography-3.4.7/setup.py", line 71, in <module>
    setup(
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/setuptools/__init__.py", line 152, in setup
    _install_setup_requires(attrs)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/setuptools/__init__.py", line 147, in _install_setup_requires
    dist.fetch_build_eggs(dist.setup_requires)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/setuptools/dist.py", line 721, in fetch_build_eggs
    resolved_dists = pkg_resources.working_set.resolve(
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pkg_resources/__init__.py", line 766, in resolve
    dist = best[req.key] = env.best_match(
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pkg_resources/__init__.py", line 1051, in best_match
    return self.obtain(req, installer)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/pkg_resources/__init__.py", line 1063, in obtain
    return installer(requirement)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/setuptools/dist.py", line 780, in fetch_build_egg
    return fetch_build_egg(self, req)
  File "/openwrt/staging_dir/hostpkg/lib/python3.9/site-packages/setuptools/installer.py", line 77, in fetch_build_egg
    raise DistutilsError(str(e)) from e
distutils.errors.DistutilsError: Command '['/openwrt/staging_dir/hostpkg/bin/python3.9', '-m', 'pip', '--disable-pip-version-check', 'wheel', '--no-deps', '-w', '/openwrt/tmp/tmpfarof1us', '--quiet', 'setuptools-rust>=0.11.4']' returned non-zero exit status 2.
make[3]: *** [Makefile:57: /openwrt/build_dir/target-mips_24kc_musl/pypi/cryptography-3.4.7/.built] Error 1
```
