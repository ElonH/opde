---
title: "compile.40"
date: 2021-06-22 10:50:44.053542
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
make package/feeds/packages/python-cryptodomex/compile -j$(nproc) || make package/feeds/packages/python-cryptodomex/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-fix-libgmp-loading.patch using plaintext: 
patching file lib/Cryptodome/Math/_IntegerGMP.py

Applying ./patches/002-omit-tests.patch using plaintext: 
patching file setup.py
Testing support for clang
Target does not support clang
Testing support for gcc
Target does support gcc
Testing support for stdint.h header
Target does support stdint.h header
Testing support for 128-bit integer
Target does not support 128-bit integer
Testing support for cpuid.h header
Target does not support cpuid.h header
Testing support for intrin.h header
Target does not support intrin.h header
Testing support for posix_memalign
Target does support posix_memalign
Testing support for SSE2(intrin.h)
Target does not support SSE2(intrin.h)
Testing support for SSE2(x86intrin.h)
Target does not support SSE2(x86intrin.h)
Testing support for SSE2(emmintrin.h)
Target does not support SSE2(emmintrin.h)
Warning: compiler does not support AESNI instructions
Warning: compiler does not support CLMUL instructions
running install
running build
running build_py
creating build/lib.-3.9
creating build/lib.-3.9/Cryptodome
copying lib/Cryptodome/__init__.py -> build/lib.-3.9/Cryptodome
creating build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/ChaCha20.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/PKCS1_OAEP.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/DES.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_gcm.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/ARC2.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/AES.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_ccm.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/ARC4.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_cbc.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/ChaCha20_Poly1305.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_ecb.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/__init__.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_siv.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_cfb.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/Blowfish.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/PKCS1_v1_5.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_ocb.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_ofb.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/Salsa20.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_openpgp.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_ctr.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/CAST.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_eax.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/DES3.py -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_EKSBlowfish.py -> build/lib.-3.9/Cryptodome/Cipher
creating build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/Poly1305.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/RIPEMD160.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/keccak.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/HMAC.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/MD2.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHAKE128.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA384.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA3_384.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA256.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/__init__.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA3_224.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA3_256.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA1.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHAKE256.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA224.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/BLAKE2s.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/CMAC.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA512.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA3_512.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/MD5.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/MD4.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/RIPEMD.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA.py -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/BLAKE2b.py -> build/lib.-3.9/Cryptodome/Hash
creating build/lib.-3.9/Cryptodome/IO
copying lib/Cryptodome/IO/_PBES.py -> build/lib.-3.9/Cryptodome/IO
copying lib/Cryptodome/IO/PEM.py -> build/lib.-3.9/Cryptodome/IO
copying lib/Cryptodome/IO/__init__.py -> build/lib.-3.9/Cryptodome/IO
copying lib/Cryptodome/IO/PKCS8.py -> build/lib.-3.9/Cryptodome/IO
creating build/lib.-3.9/Cryptodome/PublicKey
copying lib/Cryptodome/PublicKey/_openssh.py -> build/lib.-3.9/Cryptodome/PublicKey
copying lib/Cryptodome/PublicKey/ECC.py -> build/lib.-3.9/Cryptodome/PublicKey
copying lib/Cryptodome/PublicKey/__init__.py -> build/lib.-3.9/Cryptodome/PublicKey
copying lib/Cryptodome/PublicKey/ElGamal.py -> build/lib.-3.9/Cryptodome/PublicKey
copying lib/Cryptodome/PublicKey/RSA.py -> build/lib.-3.9/Cryptodome/PublicKey
copying lib/Cryptodome/PublicKey/DSA.py -> build/lib.-3.9/Cryptodome/PublicKey
creating build/lib.-3.9/Cryptodome/Protocol
copying lib/Cryptodome/Protocol/KDF.py -> build/lib.-3.9/Cryptodome/Protocol
copying lib/Cryptodome/Protocol/__init__.py -> build/lib.-3.9/Cryptodome/Protocol
copying lib/Cryptodome/Protocol/SecretSharing.py -> build/lib.-3.9/Cryptodome/Protocol
creating build/lib.-3.9/Cryptodome/Random
copying lib/Cryptodome/Random/__init__.py -> build/lib.-3.9/Cryptodome/Random
copying lib/Cryptodome/Random/random.py -> build/lib.-3.9/Cryptodome/Random
creating build/lib.-3.9/Cryptodome/Signature
copying lib/Cryptodome/Signature/PKCS1_PSS.py -> build/lib.-3.9/Cryptodome/Signature
copying lib/Cryptodome/Signature/pkcs1_15.py -> build/lib.-3.9/Cryptodome/Signature
copying lib/Cryptodome/Signature/__init__.py -> build/lib.-3.9/Cryptodome/Signature
copying lib/Cryptodome/Signature/PKCS1_v1_5.py -> build/lib.-3.9/Cryptodome/Signature
copying lib/Cryptodome/Signature/pss.py -> build/lib.-3.9/Cryptodome/Signature
copying lib/Cryptodome/Signature/DSS.py -> build/lib.-3.9/Cryptodome/Signature
creating build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/py3compat.py -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/_raw_api.py -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/RFC1751.py -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/__init__.py -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/Counter.py -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/_file_system.py -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/asn1.py -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/strxor.py -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/number.py -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/Padding.py -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/_cpu_features.py -> build/lib.-3.9/Cryptodome/Util
creating build/lib.-3.9/Cryptodome/Math
copying lib/Cryptodome/Math/_IntegerBase.py -> build/lib.-3.9/Cryptodome/Math
copying lib/Cryptodome/Math/_IntegerCustom.py -> build/lib.-3.9/Cryptodome/Math
copying lib/Cryptodome/Math/Numbers.py -> build/lib.-3.9/Cryptodome/Math
copying lib/Cryptodome/Math/Primality.py -> build/lib.-3.9/Cryptodome/Math
copying lib/Cryptodome/Math/__init__.py -> build/lib.-3.9/Cryptodome/Math
copying lib/Cryptodome/Math/_IntegerGMP.py -> build/lib.-3.9/Cryptodome/Math
copying lib/Cryptodome/Math/_IntegerNative.py -> build/lib.-3.9/Cryptodome/Math
copying lib/Cryptodome/py.typed -> build/lib.-3.9/Cryptodome
copying lib/Cryptodome/__init__.pyi -> build/lib.-3.9/Cryptodome
copying lib/Cryptodome/Cipher/PKCS1_v1_5.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_ccm.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/Blowfish.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_cbc.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/ChaCha20.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_ofb.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/Salsa20.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/DES3.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_EKSBlowfish.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_ecb.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_openpgp.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_cfb.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_eax.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/CAST.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/AES.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_gcm.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/ARC4.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/PKCS1_OAEP.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_siv.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/ARC2.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/__init__.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_ctr.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/ChaCha20_Poly1305.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/_mode_ocb.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Cipher/DES.pyi -> build/lib.-3.9/Cryptodome/Cipher
copying lib/Cryptodome/Hash/RIPEMD.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA1.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA384.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/BLAKE2b.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA3_512.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA3_384.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA512.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/MD2.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA224.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/Poly1305.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA3_224.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/keccak.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHAKE256.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/BLAKE2s.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/HMAC.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHAKE128.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/MD5.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA3_256.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/SHA256.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/MD4.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/__init__.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/CMAC.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/Hash/RIPEMD160.pyi -> build/lib.-3.9/Cryptodome/Hash
copying lib/Cryptodome/IO/PKCS8.pyi -> build/lib.-3.9/Cryptodome/IO
copying lib/Cryptodome/IO/PEM.pyi -> build/lib.-3.9/Cryptodome/IO
copying lib/Cryptodome/IO/_PBES.pyi -> build/lib.-3.9/Cryptodome/IO
copying lib/Cryptodome/PublicKey/ElGamal.pyi -> build/lib.-3.9/Cryptodome/PublicKey
copying lib/Cryptodome/PublicKey/RSA.pyi -> build/lib.-3.9/Cryptodome/PublicKey
copying lib/Cryptodome/PublicKey/ECC.pyi -> build/lib.-3.9/Cryptodome/PublicKey
copying lib/Cryptodome/PublicKey/_openssh.pyi -> build/lib.-3.9/Cryptodome/PublicKey
copying lib/Cryptodome/PublicKey/__init__.pyi -> build/lib.-3.9/Cryptodome/PublicKey
copying lib/Cryptodome/PublicKey/DSA.pyi -> build/lib.-3.9/Cryptodome/PublicKey
copying lib/Cryptodome/Protocol/SecretSharing.pyi -> build/lib.-3.9/Cryptodome/Protocol
copying lib/Cryptodome/Protocol/__init__.pyi -> build/lib.-3.9/Cryptodome/Protocol
copying lib/Cryptodome/Protocol/KDF.pyi -> build/lib.-3.9/Cryptodome/Protocol
copying lib/Cryptodome/Random/random.pyi -> build/lib.-3.9/Cryptodome/Random
copying lib/Cryptodome/Random/__init__.pyi -> build/lib.-3.9/Cryptodome/Random
copying lib/Cryptodome/Signature/PKCS1_v1_5.pyi -> build/lib.-3.9/Cryptodome/Signature
copying lib/Cryptodome/Signature/PKCS1_PSS.pyi -> build/lib.-3.9/Cryptodome/Signature
copying lib/Cryptodome/Signature/DSS.pyi -> build/lib.-3.9/Cryptodome/Signature
copying lib/Cryptodome/Signature/pkcs1_15.pyi -> build/lib.-3.9/Cryptodome/Signature
copying lib/Cryptodome/Signature/pss.pyi -> build/lib.-3.9/Cryptodome/Signature
copying lib/Cryptodome/Util/py3compat.pyi -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/RFC1751.pyi -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/strxor.pyi -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/Counter.pyi -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/number.pyi -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/Padding.pyi -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/_cpu_features.pyi -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/_file_system.pyi -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/_raw_api.pyi -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Util/asn1.pyi -> build/lib.-3.9/Cryptodome/Util
copying lib/Cryptodome/Math/_IntegerCustom.pyi -> build/lib.-3.9/Cryptodome/Math
copying lib/Cryptodome/Math/_IntegerBase.pyi -> build/lib.-3.9/Cryptodome/Math
copying lib/Cryptodome/Math/Numbers.pyi -> build/lib.-3.9/Cryptodome/Math
copying lib/Cryptodome/Math/_IntegerGMP.pyi -> build/lib.-3.9/Cryptodome/Math
copying lib/Cryptodome/Math/_IntegerNative.pyi -> build/lib.-3.9/Cryptodome/Math
copying lib/Cryptodome/Math/Primality.pyi -> build/lib.-3.9/Cryptodome/Math
warning: PCTBuildPy: byte-compiling is disabled, skipping.

running build_ext
building 'Cryptodome.Hash._MD2' extension
creating build/temp.-3.9
creating build/temp.-3.9/src
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/pycryptodomex-3.10.1=pycryptodomex-3.10.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -DHAVE_STDINT_H -DPYCRYPTO_LITTLE_ENDIAN -DSYS_BITS=64 -DLTC_NO_ASM -DHAVE_POSIX_MEMALIGN -Isrc/ -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c src/MD2.c -o build/temp.-3.9/src/MD2.o
ccache_cc -shared -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -lpython3.9 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/pycryptodomex-3.10.1=pycryptodomex-3.10.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 build/temp.-3.9/src/MD2.o -o build/lib.-3.9/Cryptodome/Hash/_MD2.abi3.so
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lpython3.9
collect2: error: ld returned 1 exit status
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:46: /openwrt/build_dir/target-mips_24kc_musl/pypi/pycryptodomex-3.10.1/.built] Error 1
```
