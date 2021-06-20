---
title: "compile.37"
date: 2021-06-20 22:33:34.393506
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
make package/feeds/packages/python-cryptodome/compile -j$(nproc) || make package/feeds/packages/python-cryptodome/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-fix-libgmp-loading.patch using plaintext: 
patching file lib/Crypto/Math/_IntegerGMP.py

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
creating build/lib.-3.9/Crypto
copying lib/Crypto/__init__.py -> build/lib.-3.9/Crypto
creating build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/ChaCha20.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/PKCS1_OAEP.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/DES.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_gcm.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/ARC2.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/AES.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_ccm.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/ARC4.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_cbc.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/ChaCha20_Poly1305.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_ecb.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/__init__.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_siv.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_cfb.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/Blowfish.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/PKCS1_v1_5.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_ocb.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_ofb.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/Salsa20.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_openpgp.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_ctr.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/CAST.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_eax.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/DES3.py -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_EKSBlowfish.py -> build/lib.-3.9/Crypto/Cipher
creating build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/Poly1305.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/RIPEMD160.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/keccak.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/HMAC.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/MD2.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHAKE128.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA384.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA3_384.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA256.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/__init__.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA3_224.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA3_256.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA1.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHAKE256.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA224.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/BLAKE2s.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/CMAC.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA512.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA3_512.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/MD5.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/MD4.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/RIPEMD.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA.py -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/BLAKE2b.py -> build/lib.-3.9/Crypto/Hash
creating build/lib.-3.9/Crypto/IO
copying lib/Crypto/IO/_PBES.py -> build/lib.-3.9/Crypto/IO
copying lib/Crypto/IO/PEM.py -> build/lib.-3.9/Crypto/IO
copying lib/Crypto/IO/__init__.py -> build/lib.-3.9/Crypto/IO
copying lib/Crypto/IO/PKCS8.py -> build/lib.-3.9/Crypto/IO
creating build/lib.-3.9/Crypto/PublicKey
copying lib/Crypto/PublicKey/_openssh.py -> build/lib.-3.9/Crypto/PublicKey
copying lib/Crypto/PublicKey/ECC.py -> build/lib.-3.9/Crypto/PublicKey
copying lib/Crypto/PublicKey/__init__.py -> build/lib.-3.9/Crypto/PublicKey
copying lib/Crypto/PublicKey/ElGamal.py -> build/lib.-3.9/Crypto/PublicKey
copying lib/Crypto/PublicKey/RSA.py -> build/lib.-3.9/Crypto/PublicKey
copying lib/Crypto/PublicKey/DSA.py -> build/lib.-3.9/Crypto/PublicKey
creating build/lib.-3.9/Crypto/Protocol
copying lib/Crypto/Protocol/KDF.py -> build/lib.-3.9/Crypto/Protocol
copying lib/Crypto/Protocol/__init__.py -> build/lib.-3.9/Crypto/Protocol
copying lib/Crypto/Protocol/SecretSharing.py -> build/lib.-3.9/Crypto/Protocol
creating build/lib.-3.9/Crypto/Random
copying lib/Crypto/Random/__init__.py -> build/lib.-3.9/Crypto/Random
copying lib/Crypto/Random/random.py -> build/lib.-3.9/Crypto/Random
creating build/lib.-3.9/Crypto/Signature
copying lib/Crypto/Signature/PKCS1_PSS.py -> build/lib.-3.9/Crypto/Signature
copying lib/Crypto/Signature/pkcs1_15.py -> build/lib.-3.9/Crypto/Signature
copying lib/Crypto/Signature/__init__.py -> build/lib.-3.9/Crypto/Signature
copying lib/Crypto/Signature/PKCS1_v1_5.py -> build/lib.-3.9/Crypto/Signature
copying lib/Crypto/Signature/pss.py -> build/lib.-3.9/Crypto/Signature
copying lib/Crypto/Signature/DSS.py -> build/lib.-3.9/Crypto/Signature
creating build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/py3compat.py -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/_raw_api.py -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/RFC1751.py -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/__init__.py -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/Counter.py -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/_file_system.py -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/asn1.py -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/strxor.py -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/number.py -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/Padding.py -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/_cpu_features.py -> build/lib.-3.9/Crypto/Util
creating build/lib.-3.9/Crypto/Math
copying lib/Crypto/Math/_IntegerBase.py -> build/lib.-3.9/Crypto/Math
copying lib/Crypto/Math/_IntegerCustom.py -> build/lib.-3.9/Crypto/Math
copying lib/Crypto/Math/Numbers.py -> build/lib.-3.9/Crypto/Math
copying lib/Crypto/Math/Primality.py -> build/lib.-3.9/Crypto/Math
copying lib/Crypto/Math/__init__.py -> build/lib.-3.9/Crypto/Math
copying lib/Crypto/Math/_IntegerGMP.py -> build/lib.-3.9/Crypto/Math
copying lib/Crypto/Math/_IntegerNative.py -> build/lib.-3.9/Crypto/Math
copying lib/Crypto/py.typed -> build/lib.-3.9/Crypto
copying lib/Crypto/__init__.pyi -> build/lib.-3.9/Crypto
copying lib/Crypto/Cipher/PKCS1_v1_5.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_ccm.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/Blowfish.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_cbc.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/ChaCha20.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_ofb.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/Salsa20.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/DES3.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_EKSBlowfish.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_ecb.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_openpgp.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_cfb.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_eax.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/CAST.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/AES.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_gcm.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/ARC4.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/PKCS1_OAEP.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_siv.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/ARC2.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/__init__.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_ctr.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/ChaCha20_Poly1305.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/_mode_ocb.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Cipher/DES.pyi -> build/lib.-3.9/Crypto/Cipher
copying lib/Crypto/Hash/RIPEMD.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA1.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA384.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/BLAKE2b.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA3_512.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA3_384.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA512.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/MD2.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA224.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/Poly1305.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA3_224.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/keccak.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHAKE256.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/BLAKE2s.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/HMAC.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHAKE128.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/MD5.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA3_256.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/SHA256.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/MD4.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/__init__.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/CMAC.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/Hash/RIPEMD160.pyi -> build/lib.-3.9/Crypto/Hash
copying lib/Crypto/IO/PKCS8.pyi -> build/lib.-3.9/Crypto/IO
copying lib/Crypto/IO/PEM.pyi -> build/lib.-3.9/Crypto/IO
copying lib/Crypto/IO/_PBES.pyi -> build/lib.-3.9/Crypto/IO
copying lib/Crypto/PublicKey/ElGamal.pyi -> build/lib.-3.9/Crypto/PublicKey
copying lib/Crypto/PublicKey/RSA.pyi -> build/lib.-3.9/Crypto/PublicKey
copying lib/Crypto/PublicKey/ECC.pyi -> build/lib.-3.9/Crypto/PublicKey
copying lib/Crypto/PublicKey/_openssh.pyi -> build/lib.-3.9/Crypto/PublicKey
copying lib/Crypto/PublicKey/__init__.pyi -> build/lib.-3.9/Crypto/PublicKey
copying lib/Crypto/PublicKey/DSA.pyi -> build/lib.-3.9/Crypto/PublicKey
copying lib/Crypto/Protocol/SecretSharing.pyi -> build/lib.-3.9/Crypto/Protocol
copying lib/Crypto/Protocol/__init__.pyi -> build/lib.-3.9/Crypto/Protocol
copying lib/Crypto/Protocol/KDF.pyi -> build/lib.-3.9/Crypto/Protocol
copying lib/Crypto/Random/random.pyi -> build/lib.-3.9/Crypto/Random
copying lib/Crypto/Random/__init__.pyi -> build/lib.-3.9/Crypto/Random
copying lib/Crypto/Signature/PKCS1_v1_5.pyi -> build/lib.-3.9/Crypto/Signature
copying lib/Crypto/Signature/PKCS1_PSS.pyi -> build/lib.-3.9/Crypto/Signature
copying lib/Crypto/Signature/DSS.pyi -> build/lib.-3.9/Crypto/Signature
copying lib/Crypto/Signature/pkcs1_15.pyi -> build/lib.-3.9/Crypto/Signature
copying lib/Crypto/Signature/pss.pyi -> build/lib.-3.9/Crypto/Signature
copying lib/Crypto/Util/py3compat.pyi -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/RFC1751.pyi -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/strxor.pyi -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/Counter.pyi -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/number.pyi -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/Padding.pyi -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/_cpu_features.pyi -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/_file_system.pyi -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/_raw_api.pyi -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Util/asn1.pyi -> build/lib.-3.9/Crypto/Util
copying lib/Crypto/Math/_IntegerCustom.pyi -> build/lib.-3.9/Crypto/Math
copying lib/Crypto/Math/_IntegerBase.pyi -> build/lib.-3.9/Crypto/Math
copying lib/Crypto/Math/Numbers.pyi -> build/lib.-3.9/Crypto/Math
copying lib/Crypto/Math/_IntegerGMP.pyi -> build/lib.-3.9/Crypto/Math
copying lib/Crypto/Math/_IntegerNative.pyi -> build/lib.-3.9/Crypto/Math
copying lib/Crypto/Math/Primality.pyi -> build/lib.-3.9/Crypto/Math
warning: PCTBuildPy: byte-compiling is disabled, skipping.

running build_ext
building 'Crypto.Hash._MD2' extension
creating build/temp.-3.9
creating build/temp.-3.9/src
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/pycryptodome-3.9.7=pycryptodome-3.9.7 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -DHAVE_STDINT_H -DPYCRYPTO_LITTLE_ENDIAN -DSYS_BITS=64 -DLTC_NO_ASM -DHAVE_POSIX_MEMALIGN -Isrc/ -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c src/MD2.c -o build/temp.-3.9/src/MD2.o
ccache_cc -shared -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -lpython3.9 -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/pycryptodome-3.9.7=pycryptodome-3.9.7 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 build/temp.-3.9/src/MD2.o -o build/lib.-3.9/Crypto/Hash/_MD2.cpython-39.so
/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lpython3.9
collect2: error: ld returned 1 exit status
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:48: /openwrt/build_dir/target-mips_24kc_musl/pypi/pycryptodome-3.9.7/.built] Error 1
```
