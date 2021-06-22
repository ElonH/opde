---
title: "compile.40"
date: 2021-06-22 10:45:15.526012
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
make package/feeds/packages/libreswan/compile -j$(nproc) || make package/feeds/packages/libreswan/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-nanosleep.patch using plaintext: 
patching file programs/pluto/send.c

Applying ./patches/020-limits.patch using plaintext: 
patching file programs/pluto/connections.c
patching file programs/pluto/rcv_whack.c

Applying ./patches/030-fix_musl_build.patch using plaintext: 
patching file include/fd.h

Applying ./patches/040-disable_man.patch using plaintext: 
patching file mk/targets.mk
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4'
/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/mk/config.mk:636: Warning: Overriding USE_AUTHPAM with deprecated variable USE_XAUTHPAM
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib'
/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/mk/config.mk:636: Warning: Overriding USE_AUTHPAM with deprecated variable USE_XAUTHPAM
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan'
../../mk/config.mk:636: Warning: Overriding USE_AUTHPAM with deprecated variable USE_XAUTHPAM
mkdir -p ../../OBJ.linux./lib/libswan
set -e ; \
for f in x509dn.o asn1.o oid.o constants.o id.o initaddr.o lex.o lswconf.o lswfips.o sameaddr.o secrets.o subnettypeof.o ttodata.o ttosa.o ttosubnet.o ttoul.o secitem_chunk.o base64_pubkey.o lswnss.o alg_byname.o ttoaddress.o alloc.o alloc_printf.o diag.o passert.o pexpect.o nss_cert_load.o certs.o reqid.o keyid.o addr_lookup.o kernel_netlink_reply.o kernel_netlink_query.o netlink_attrib.o log_ip.o fd.o kernel_alg.o kernel_sadb.o role.o addrtypeof.o datatot.o ultot.o proposals.o v1_proposals.o v2_proposals.o esp_info.o ah_info.o ike_info.o ckaid.o chunk.o shunk.o hunk.o ip_bytes.o ip_address.o ip_cidr.o ip_encap.o ip_endpoint.o ip_info.o ip_port.o ip_port_range.o ip_protocol.o ip_protoport.o ip_range.o ip_said.o ip_selector.o ip_sockaddr.o ip_subnet.o lmod.o lset.o deltatime.o realtime.o monotime.o refcnt.o debug.o impair.o keywords.o DBG_dump.o DBG_log.o log_error.o fatal.o libreswan_bad_case.o lswglob.o jambuf.o jam_bytes.o log_message.o log_va_list.o log_nss_error.o jam_nss_error.o jam_nss_ckm.o jam_nss_ckf.o jam_nss_cka.o jam_nss_secitem.o test_buffer.o ike_alg.o ike_alg_test.o ike_alg_dh_nss_ecp_ops.o ike_alg_dh_nss_modp_ops.o ike_alg_hash_nss_ops.o ike_alg_prf_mac_hmac_ops.o ike_alg_prf_mac_nss_ops.o ike_alg_prf_mac_xcbc_ops.o ike_alg_prf_ikev1_mac_ops.o ike_alg_prf_ikev2_mac_ops.o ike_alg_prf_ikev1_nss_ops.o ike_alg_prf_ikev2_nss_ops.o ike_alg_encrypt_chacha20_poly1305.o ike_alg_encrypt_nss_aead_ops.o ike_alg_encrypt_nss_cbc_ops.o ike_alg_encrypt_nss_ctr_ops.o ike_alg_encrypt_nss_gcm_ops.o ike_alg_desc.o ike_alg_3des.o ike_alg_aes.o ike_alg_camellia.o ike_alg_dh.o ike_alg_md5.o ike_alg_none.o ike_alg_sha1.o ike_alg_sha2.o ike_alg_encrypt_cbc_test_vectors.o ike_alg_encrypt_ctr_test_vectors.o ike_alg_encrypt_gcm_test_vectors.o ike_alg_prf_test_vectors.o crypt_mac.o crypt_hash.o crypt_prf.o crypt_symkey.o ikev1_prf.o ikev2_prf.o unbound.o /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/OBJ.linux./lib/libswan/version.o ; do \
	case $f in \
		*.c ) echo "-include \$(builddir)/$(basename $f .c).d # $f" ;; \
		*.o ) echo "-include \$(builddir)/$(basename $f .o).d # $f" ;; \
		* ) echo "# $f ignored by Makefile.dep" ;; \
	esac ; \
done > ../../OBJ.linux./lib/libswan/Makefile.depend.mk.tmp
mv ../../OBJ.linux./lib/libswan/Makefile.depend.mk.tmp ../../OBJ.linux./lib/libswan/Makefile.depend.mk
../../mk/config.mk:636: Warning: Overriding USE_AUTHPAM with deprecated variable USE_XAUTHPAM
../../mk/config.mk:636: Warning: Overriding USE_AUTHPAM with deprecated variable USE_XAUTHPAM
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"x509dn.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/x509dn.d \
	-MP -MMD -MT x509dn.o \
	-o ../../OBJ.linux./lib/libswan/x509dn.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/x509dn.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plarena.h:15,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/cert.h:13,
                 from ../../include/x509.h:28,
                 from x509dn.c:29:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/cert.h:14,
                 from ../../include/x509.h:28,
                 from x509dn.c:29:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"asn1.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/asn1.d \
	-MP -MMD -MT asn1.o \
	-o ../../OBJ.linux./lib/libswan/asn1.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/asn1.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from asn1.c:23:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from asn1.c:24:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"oid.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/oid.d \
	-MP -MMD -MT oid.o \
	-o ../../OBJ.linux./lib/libswan/oid.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/oid.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"constants.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/constants.d \
	-MP -MMD -MT constants.o \
	-o ../../OBJ.linux./lib/libswan/constants.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/constants.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from constants.c:29:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from constants.c:36:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"id.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/id.d \
	-MP -MMD -MT id.o \
	-o ../../OBJ.linux./lib/libswan/id.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/id.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from id.c:35:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from id.c:38:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"initaddr.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/initaddr.d \
	-MP -MMD -MT initaddr.o \
	-o ../../OBJ.linux./lib/libswan/initaddr.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/initaddr.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_address.h:24,
                 from ../../include/ip_info.h:8,
                 from initaddr.c:20:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from initaddr.c:23:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"lex.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/lex.d \
	-MP -MMD -MT lex.o \
	-o ../../OBJ.linux./lib/libswan/lex.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/lex.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from lex.c:16:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from lex.c:24:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"lswconf.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/lswconf.d \
	-MP -MMD -MT lswconf.o \
	-o ../../OBJ.linux./lib/libswan/lswconf.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/lswconf.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from lswconf.c:24:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from lswconf.c:25:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"lswfips.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/lswfips.d \
	-MP -MMD -MT lswfips.o \
	-o ../../OBJ.linux./lib/libswan/lswfips.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/lswfips.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from lswfips.c:20:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/seccomon.h:17,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/nss.h:34,
                 from lswfips.c:24:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"sameaddr.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/sameaddr.d \
	-MP -MMD -MT sameaddr.o \
	-o ../../OBJ.linux./lib/libswan/sameaddr.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/sameaddr.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_address.h:24,
                 from sameaddr.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"secrets.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/secrets.d \
	-MP -MMD -MT secrets.o \
	-o ../../OBJ.linux./lib/libswan/secrets.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/secrets.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plarena.h:15,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:6,
                 from secrets.c:40:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from secrets.c:40:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"subnettypeof.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/subnettypeof.d \
	-MP -MMD -MT subnettypeof.o \
	-o ../../OBJ.linux./lib/libswan/subnettypeof.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/subnettypeof.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_address.h:24,
                 from ../../include/ip_subnet.h:29,
                 from subnettypeof.c:17:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ttodata.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ttodata.d \
	-MP -MMD -MT ttodata.o \
	-o ../../OBJ.linux./lib/libswan/ttodata.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ttodata.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ttosa.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ttosa.d \
	-MP -MMD -MT ttosa.o \
	-o ../../OBJ.linux./lib/libswan/ttosa.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ttosa.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_endpoint.h:22,
                 from ../../include/ip_said.h:22,
                 from ttosa.c:19:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ttosubnet.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ttosubnet.d \
	-MP -MMD -MT ttosubnet.o \
	-o ../../OBJ.linux./lib/libswan/ttosubnet.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ttosubnet.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_address.h:24,
                 from ../../include/ip_subnet.h:29,
                 from ttosubnet.c:20:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from ttosubnet.c:23:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ttoul.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ttoul.d \
	-MP -MMD -MT ttoul.o \
	-o ../../OBJ.linux./lib/libswan/ttoul.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ttoul.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"secitem_chunk.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/secitem_chunk.d \
	-MP -MMD -MT secitem_chunk.o \
	-o ../../OBJ.linux./lib/libswan/secitem_chunk.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/secitem_chunk.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from secitem_chunk.c:17:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/secrets.h:25,
                 from secitem_chunk.c:19:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"base64_pubkey.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/base64_pubkey.d \
	-MP -MMD -MT base64_pubkey.o \
	-o ../../OBJ.linux./lib/libswan/base64_pubkey.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/base64_pubkey.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from base64_pubkey.c:24:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from base64_pubkey.c:25:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"lswnss.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/lswnss.d \
	-MP -MMD -MT lswnss.o \
	-o ../../OBJ.linux./lib/libswan/lswnss.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/lswnss.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/pratom.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/nspr.h:9,
                 from lswnss.c:17:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prinit.h:12,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/nspr.h:18,
                 from lswnss.c:17:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"alg_byname.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/alg_byname.d \
	-MP -MMD -MT alg_byname.o \
	-o ../../OBJ.linux./lib/libswan/alg_byname.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/alg_byname.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from alg_byname.c:19:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from alg_byname.c:19:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ttoaddress.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ttoaddress.d \
	-MP -MMD -MT ttoaddress.o \
	-o ../../OBJ.linux./lib/libswan/ttoaddress.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ttoaddress.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_address.h:24,
                 from ttoaddress.c:22:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from ttoaddress.c:25:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"alloc.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/alloc.d \
	-MP -MMD -MT alloc.o \
	-o ../../OBJ.linux./lib/libswan/alloc.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/alloc.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from alloc.c:22:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from alloc.c:29:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"alloc_printf.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/alloc_printf.d \
	-MP -MMD -MT alloc_printf.o \
	-o ../../OBJ.linux./lib/libswan/alloc_printf.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/alloc_printf.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from alloc_printf.c:16:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from alloc_printf.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"diag.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/diag.d \
	-MP -MMD -MT diag.o \
	-o ../../OBJ.linux./lib/libswan/diag.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/diag.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from diag.c:16:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from diag.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"passert.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/passert.d \
	-MP -MMD -MT passert.o \
	-o ../../OBJ.linux./lib/libswan/passert.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/passert.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from passert.c:18:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from passert.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"pexpect.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/pexpect.d \
	-MP -MMD -MT pexpect.o \
	-o ../../OBJ.linux./lib/libswan/pexpect.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/pexpect.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from pexpect.c:17:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from pexpect.c:20:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"nss_cert_load.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/nss_cert_load.d \
	-MP -MMD -MT nss_cert_load.o \
	-o ../../OBJ.linux./lib/libswan/nss_cert_load.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/nss_cert_load.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prerror.h:9,
                 from ../../include/lswnss.h:20,
                 from nss_cert_load.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/lswnss.h:21,
                 from nss_cert_load.c:18:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"certs.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/certs.d \
	-MP -MMD -MT certs.o \
	-o ../../OBJ.linux./lib/libswan/certs.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/certs.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/cert.h:14,
                 from ../../include/certs.h:41,
                 from certs.c:24:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"reqid.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/reqid.d \
	-MP -MMD -MT reqid.o \
	-o ../../OBJ.linux./lib/libswan/reqid.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/reqid.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"keyid.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/keyid.d \
	-MP -MMD -MT keyid.o \
	-o ../../OBJ.linux./lib/libswan/keyid.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/keyid.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"addr_lookup.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/addr_lookup.d \
	-MP -MMD -MT addr_lookup.o \
	-o ../../OBJ.linux./lib/libswan/addr_lookup.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/addr_lookup.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from addr_lookup.c:19:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from addr_lookup.c:29:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"kernel_netlink_reply.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/kernel_netlink_reply.d \
	-MP -MMD -MT kernel_netlink_reply.o \
	-o ../../OBJ.linux./lib/libswan/kernel_netlink_reply.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/kernel_netlink_reply.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from kernel_netlink_reply.c:17:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from kernel_netlink_reply.c:23:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"kernel_netlink_query.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/kernel_netlink_query.d \
	-MP -MMD -MT kernel_netlink_query.o \
	-o ../../OBJ.linux./lib/libswan/kernel_netlink_query.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/kernel_netlink_query.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from kernel_netlink_query.c:25:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from kernel_netlink_query.c:25:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"netlink_attrib.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/netlink_attrib.d \
	-MP -MMD -MT netlink_attrib.o \
	-o ../../OBJ.linux./lib/libswan/netlink_attrib.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/netlink_attrib.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from netlink_attrib.c:23:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from netlink_attrib.c:23:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"log_ip.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/log_ip.d \
	-MP -MMD -MT log_ip.o \
	-o ../../OBJ.linux./lib/libswan/log_ip.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/log_ip.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_address.h:24,
                 from log_ip.c:16:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"fd.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/fd.d \
	-MP -MMD -MT fd.o \
	-o ../../OBJ.linux./lib/libswan/fd.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/fd.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from fd.c:24:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from ../../include/refcnt.h:22,
                 from fd.c:25:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"kernel_alg.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/kernel_alg.d \
	-MP -MMD -MT kernel_alg.o \
	-o ../../OBJ.linux./lib/libswan/kernel_alg.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/kernel_alg.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from kernel_alg.c:23:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from kernel_alg.c:25:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"kernel_sadb.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/kernel_sadb.d \
	-MP -MMD -MT kernel_sadb.o \
	-o ../../OBJ.linux./lib/libswan/kernel_sadb.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/kernel_sadb.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from kernel_sadb.c:22:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from kernel_sadb.c:22:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"role.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/role.d \
	-MP -MMD -MT role.o \
	-o ../../OBJ.linux./lib/libswan/role.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/role.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from role.c:17:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"addrtypeof.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/addrtypeof.d \
	-MP -MMD -MT addrtypeof.o \
	-o ../../OBJ.linux./lib/libswan/addrtypeof.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/addrtypeof.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_address.h:24,
                 from addrtypeof.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"datatot.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/datatot.d \
	-MP -MMD -MT datatot.o \
	-o ../../OBJ.linux./lib/libswan/datatot.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/datatot.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ultot.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ultot.d \
	-MP -MMD -MT ultot.o \
	-o ../../OBJ.linux./lib/libswan/ultot.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ultot.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"proposals.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/proposals.d \
	-MP -MMD -MT proposals.o \
	-o ../../OBJ.linux./lib/libswan/proposals.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/proposals.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from proposals.c:19:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from proposals.c:23:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"v1_proposals.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/v1_proposals.d \
	-MP -MMD -MT v1_proposals.o \
	-o ../../OBJ.linux./lib/libswan/v1_proposals.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/v1_proposals.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from v1_proposals.c:17:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from v1_proposals.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"v2_proposals.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/v2_proposals.d \
	-MP -MMD -MT v2_proposals.o \
	-o ../../OBJ.linux./lib/libswan/v2_proposals.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/v2_proposals.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from v2_proposals.c:17:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from v2_proposals.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"esp_info.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/esp_info.d \
	-MP -MMD -MT esp_info.o \
	-o ../../OBJ.linux./lib/libswan/esp_info.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/esp_info.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from esp_info.c:19:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from esp_info.c:23:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ah_info.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ah_info.d \
	-MP -MMD -MT ah_info.o \
	-o ../../OBJ.linux./lib/libswan/ah_info.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ah_info.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ah_info.c:19:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ah_info.c:23:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_info.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_info.d \
	-MP -MMD -MT ike_info.o \
	-o ../../OBJ.linux./lib/libswan/ike_info.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_info.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from ike_info.c:22:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from ike_info.c:22:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ckaid.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ckaid.d \
	-MP -MMD -MT ckaid.o \
	-o ../../OBJ.linux./lib/libswan/ckaid.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ckaid.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plarena.h:15,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:15,
                 from ../../include/ckaid.h:23,
                 from ckaid.c:26:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../include/ckaid.h:23,
                 from ckaid.c:26:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"chunk.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/chunk.d \
	-MP -MMD -MT chunk.o \
	-o ../../OBJ.linux./lib/libswan/chunk.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/chunk.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from chunk.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from chunk.c:20:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"shunk.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/shunk.d \
	-MP -MMD -MT shunk.o \
	-o ../../OBJ.linux./lib/libswan/shunk.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/shunk.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from shunk.c:22:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from shunk.c:22:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"hunk.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/hunk.d \
	-MP -MMD -MT hunk.o \
	-o ../../OBJ.linux./lib/libswan/hunk.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/hunk.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from hunk.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_bytes.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_bytes.d \
	-MP -MMD -MT ip_bytes.o \
	-o ../../OBJ.linux./lib/libswan/ip_bytes.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_bytes.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from ip_bytes.c:18:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from ip_bytes.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_address.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_address.d \
	-MP -MMD -MT ip_address.o \
	-o ../../OBJ.linux./lib/libswan/ip_address.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_address.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_address.h:24,
                 from ip_address.c:20:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from ip_address.c:21:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_cidr.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_cidr.d \
	-MP -MMD -MT ip_cidr.o \
	-o ../../OBJ.linux./lib/libswan/ip_cidr.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_cidr.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_address.h:24,
                 from ../../include/ip_cidr.h:26,
                 from ip_cidr.c:19:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_encap.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_encap.d \
	-MP -MMD -MT ip_encap.o \
	-o ../../OBJ.linux./lib/libswan/ip_encap.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_encap.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_endpoint.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_endpoint.d \
	-MP -MMD -MT ip_endpoint.o \
	-o ../../OBJ.linux./lib/libswan/ip_endpoint.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_endpoint.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_endpoint.h:22,
                 from ip_endpoint.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from ip_endpoint.c:22:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_info.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_info.d \
	-MP -MMD -MT ip_info.o \
	-o ../../OBJ.linux./lib/libswan/ip_info.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_info.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_address.h:24,
                 from ../../include/ip_info.h:8,
                 from ip_info.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from ip_info.c:23:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_port.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_port.d \
	-MP -MMD -MT ip_port.o \
	-o ../../OBJ.linux./lib/libswan/ip_port.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_port.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ip_port.c:22:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_port_range.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_port_range.d \
	-MP -MMD -MT ip_port_range.o \
	-o ../../OBJ.linux./lib/libswan/ip_port_range.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_port_range.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ip_port_range.c:19:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_protocol.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_protocol.d \
	-MP -MMD -MT ip_protocol.o \
	-o ../../OBJ.linux./lib/libswan/ip_protocol.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_protocol.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ip_protocol.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_protoport.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_protoport.d \
	-MP -MMD -MT ip_protoport.o \
	-o ../../OBJ.linux./lib/libswan/ip_protoport.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_protoport.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ip_protoport.c:22:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_range.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_range.d \
	-MP -MMD -MT ip_range.o \
	-o ../../OBJ.linux./lib/libswan/ip_range.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_range.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_address.h:24,
                 from ../../include/ip_range.h:23,
                 from ip_range.c:28:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from ip_range.c:31:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_said.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_said.d \
	-MP -MMD -MT ip_said.o \
	-o ../../OBJ.linux./lib/libswan/ip_said.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_said.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_endpoint.h:22,
                 from ../../include/ip_said.h:22,
                 from ip_said.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from ip_said.c:21:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_selector.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_selector.d \
	-MP -MMD -MT ip_selector.o \
	-o ../../OBJ.linux./lib/libswan/ip_selector.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_selector.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from ip_selector.c:17:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from ip_selector.c:17:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_sockaddr.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_sockaddr.d \
	-MP -MMD -MT ip_sockaddr.o \
	-o ../../OBJ.linux./lib/libswan/ip_sockaddr.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_sockaddr.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_endpoint.h:22,
                 from ../../include/ip_sockaddr.h:26,
                 from ip_sockaddr.c:17:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from ip_sockaddr.c:20:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ip_subnet.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ip_subnet.d \
	-MP -MMD -MT ip_subnet.o \
	-o ../../OBJ.linux./lib/libswan/ip_subnet.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ip_subnet.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ../../include/chunk.h:29,
                 from ../../include/ip_address.h:24,
                 from ../../include/ip_subnet.h:29,
                 from ip_subnet.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from ip_subnet.c:23:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"lmod.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/lmod.d \
	-MP -MMD -MT lmod.o \
	-o ../../OBJ.linux./lib/libswan/lmod.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/lmod.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from lmod.c:17:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from lmod.c:20:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"lset.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/lset.d \
	-MP -MMD -MT lset.o \
	-o ../../OBJ.linux./lib/libswan/lset.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/lset.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from lset.c:22:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from lset.c:22:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"deltatime.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/deltatime.d \
	-MP -MMD -MT deltatime.o \
	-o ../../OBJ.linux./lib/libswan/deltatime.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/deltatime.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from deltatime.c:22:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from deltatime.c:22:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"realtime.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/realtime.d \
	-MP -MMD -MT realtime.o \
	-o ../../OBJ.linux./lib/libswan/realtime.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/realtime.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from realtime.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from realtime.c:22:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"monotime.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/monotime.d \
	-MP -MMD -MT monotime.o \
	-o ../../OBJ.linux./lib/libswan/monotime.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/monotime.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from monotime.c:22:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from monotime.c:23:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"refcnt.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/refcnt.d \
	-MP -MMD -MT refcnt.o \
	-o ../../OBJ.linux./lib/libswan/refcnt.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/refcnt.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from ../../include/refcnt.h:22,
                 from refcnt.c:16:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from ../../include/refcnt.h:22,
                 from refcnt.c:16:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"debug.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/debug.d \
	-MP -MMD -MT debug.o \
	-o ../../OBJ.linux./lib/libswan/debug.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/debug.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from debug.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"impair.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/impair.d \
	-MP -MMD -MT impair.o \
	-o ../../OBJ.linux./lib/libswan/impair.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/impair.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from impair.c:20:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from impair.c:25:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"keywords.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/keywords.d \
	-MP -MMD -MT keywords.o \
	-o ../../OBJ.linux./lib/libswan/keywords.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/keywords.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from keywords.c:17:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from keywords.c:17:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"DBG_dump.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/DBG_dump.d \
	-MP -MMD -MT DBG_dump.o \
	-o ../../OBJ.linux./lib/libswan/DBG_dump.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/DBG_dump.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from DBG_dump.c:27:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from DBG_dump.c:27:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"DBG_log.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/DBG_log.d \
	-MP -MMD -MT DBG_log.o \
	-o ../../OBJ.linux./lib/libswan/DBG_log.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/DBG_log.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from DBG_log.c:18:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from DBG_log.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"log_error.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/log_error.d \
	-MP -MMD -MT log_error.o \
	-o ../../OBJ.linux./lib/libswan/log_error.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/log_error.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from log_error.c:17:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from log_error.c:20:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"fatal.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/fatal.d \
	-MP -MMD -MT fatal.o \
	-o ../../OBJ.linux./lib/libswan/fatal.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/fatal.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from fatal.c:17:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from fatal.c:20:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"libreswan_bad_case.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/libreswan_bad_case.d \
	-MP -MMD -MT libreswan_bad_case.o \
	-o ../../OBJ.linux./lib/libswan/libreswan_bad_case.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/libreswan_bad_case.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from libreswan_bad_case.c:17:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from libreswan_bad_case.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"lswglob.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/lswglob.d \
	-MP -MMD -MT lswglob.o \
	-o ../../OBJ.linux./lib/libswan/lswglob.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/lswglob.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from lswglob.c:23:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from lswglob.c:23:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"jambuf.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/jambuf.d \
	-MP -MMD -MT jambuf.o \
	-o ../../OBJ.linux./lib/libswan/jambuf.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/jambuf.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from jambuf.c:17:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from jambuf.c:22:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"jam_bytes.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/jam_bytes.d \
	-MP -MMD -MT jam_bytes.o \
	-o ../../OBJ.linux./lib/libswan/jam_bytes.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/jam_bytes.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"log_message.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/log_message.d \
	-MP -MMD -MT log_message.o \
	-o ../../OBJ.linux./lib/libswan/log_message.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/log_message.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from log_message.c:18:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from log_message.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"log_va_list.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/log_va_list.d \
	-MP -MMD -MT log_va_list.o \
	-o ../../OBJ.linux./lib/libswan/log_va_list.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/log_va_list.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from log_va_list.c:19:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from log_va_list.c:19:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"log_nss_error.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/log_nss_error.d \
	-MP -MMD -MT log_nss_error.o \
	-o ../../OBJ.linux./lib/libswan/log_nss_error.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/log_nss_error.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from log_nss_error.c:16:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prerror.h:9,
                 from log_nss_error.c:19:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"jam_nss_error.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/jam_nss_error.d \
	-MP -MMD -MT jam_nss_error.o \
	-o ../../OBJ.linux./lib/libswan/jam_nss_error.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/jam_nss_error.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from jam_nss_error.c:17:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prerror.h:9,
                 from jam_nss_error.c:20:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"jam_nss_ckm.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/jam_nss_ckm.d \
	-MP -MMD -MT jam_nss_ckm.o \
	-o ../../OBJ.linux./lib/libswan/jam_nss_ckm.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/jam_nss_ckm.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from jam_nss_ckm.c:21:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from jam_nss_ckm.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"jam_nss_ckf.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/jam_nss_ckf.d \
	-MP -MMD -MT jam_nss_ckf.o \
	-o ../../OBJ.linux./lib/libswan/jam_nss_ckf.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/jam_nss_ckf.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from jam_nss_ckf.c:21:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from jam_nss_ckf.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"jam_nss_cka.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/jam_nss_cka.d \
	-MP -MMD -MT jam_nss_cka.o \
	-o ../../OBJ.linux./lib/libswan/jam_nss_cka.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/jam_nss_cka.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from jam_nss_cka.c:21:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from jam_nss_cka.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"jam_nss_secitem.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/jam_nss_secitem.d \
	-MP -MMD -MT jam_nss_secitem.o \
	-o ../../OBJ.linux./lib/libswan/jam_nss_secitem.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/jam_nss_secitem.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from jam_nss_secitem.c:21:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from jam_nss_secitem.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"test_buffer.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/test_buffer.d \
	-MP -MMD -MT test_buffer.o \
	-o ../../OBJ.linux./lib/libswan/test_buffer.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/test_buffer.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from test_buffer.c:17:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from test_buffer.c:19:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg.d \
	-MP -MMD -MT ike_alg.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ike_alg.c:25:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ike_alg.c:32:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_test.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_test.d \
	-MP -MMD -MT ike_alg_test.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_test.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_test.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/lswlog.h:24,
                 from ike_alg_test.c:16:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from ike_alg_test.c:16:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_dh_nss_ecp_ops.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_dh_nss_ecp_ops.d \
	-MP -MMD -MT ike_alg_dh_nss_ecp_ops.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_dh_nss_ecp_ops.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_dh_nss_ecp_ops.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/pratom.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/nspr.h:9,
                 from ike_alg_dh_nss_ecp_ops.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prinit.h:12,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/nspr.h:18,
                 from ike_alg_dh_nss_ecp_ops.c:18:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_dh_nss_modp_ops.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_dh_nss_modp_ops.d \
	-MP -MMD -MT ike_alg_dh_nss_modp_ops.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_dh_nss_modp_ops.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_dh_nss_modp_ops.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/pratom.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/nspr.h:9,
                 from ike_alg_dh_nss_modp_ops.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prinit.h:12,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/nspr.h:18,
                 from ike_alg_dh_nss_modp_ops.c:18:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_hash_nss_ops.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_hash_nss_ops.d \
	-MP -MMD -MT ike_alg_hash_nss_ops.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_hash_nss_ops.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_hash_nss_ops.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ike_alg_hash_nss_ops.c:17:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from ike_alg_hash_nss_ops.c:18:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_prf_mac_hmac_ops.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_prf_mac_hmac_ops.d \
	-MP -MMD -MT ike_alg_prf_mac_hmac_ops.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_prf_mac_hmac_ops.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_prf_mac_hmac_ops.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from ike_alg_prf_mac_hmac_ops.c:17:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from ike_alg_prf_mac_hmac_ops.c:18:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_prf_mac_nss_ops.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_prf_mac_nss_ops.d \
	-MP -MMD -MT ike_alg_prf_mac_nss_ops.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_prf_mac_nss_ops.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_prf_mac_nss_ops.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ike_alg_prf_mac_nss_ops.c:15:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prmem.h:14,
                 from ike_alg_prf_mac_nss_ops.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_prf_mac_xcbc_ops.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_prf_mac_xcbc_ops.d \
	-MP -MMD -MT ike_alg_prf_mac_xcbc_ops.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_prf_mac_xcbc_ops.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_prf_mac_xcbc_ops.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ike_alg_prf_mac_xcbc_ops.c:16:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prmem.h:14,
                 from ike_alg_prf_mac_xcbc_ops.c:19:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_prf_ikev1_mac_ops.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_prf_ikev1_mac_ops.d \
	-MP -MMD -MT ike_alg_prf_ikev1_mac_ops.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_prf_ikev1_mac_ops.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_prf_ikev1_mac_ops.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plarena.h:15,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:6,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_prf_ikev1_mac_ops.c:20:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_prf_ikev1_mac_ops.c:20:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_prf_ikev2_mac_ops.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_prf_ikev2_mac_ops.d \
	-MP -MMD -MT ike_alg_prf_ikev2_mac_ops.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_prf_ikev2_mac_ops.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_prf_ikev2_mac_ops.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plarena.h:15,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:6,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_prf_ikev2_mac_ops.c:24:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_prf_ikev2_mac_ops.c:24:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_prf_ikev1_nss_ops.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_prf_ikev1_nss_ops.d \
	-MP -MMD -MT ike_alg_prf_ikev1_nss_ops.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_prf_ikev1_nss_ops.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_prf_ikev1_nss_ops.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plarena.h:15,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:6,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_prf_ikev1_nss_ops.c:22:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_prf_ikev1_nss_ops.c:22:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_prf_ikev2_nss_ops.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_prf_ikev2_nss_ops.d \
	-MP -MMD -MT ike_alg_prf_ikev2_nss_ops.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_prf_ikev2_nss_ops.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_prf_ikev2_nss_ops.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plarena.h:15,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:6,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_prf_ikev2_nss_ops.c:24:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_prf_ikev2_nss_ops.c:24:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_encrypt_chacha20_poly1305.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_encrypt_chacha20_poly1305.d \
	-MP -MMD -MT ike_alg_encrypt_chacha20_poly1305.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_encrypt_chacha20_poly1305.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_encrypt_chacha20_poly1305.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pkcs11t.h:25,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pkcs11.h:178,
                 from ike_alg_encrypt_chacha20_poly1305.c:16:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_encrypt_chacha20_poly1305.c:18:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_encrypt_nss_aead_ops.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_encrypt_nss_aead_ops.d \
	-MP -MMD -MT ike_alg_encrypt_nss_aead_ops.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_encrypt_nss_aead_ops.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_encrypt_nss_aead_ops.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ike_alg_encrypt_nss_aead_ops.c:16:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from ike_alg_encrypt_nss_aead_ops.c:19:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_encrypt_nss_cbc_ops.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_encrypt_nss_cbc_ops.d \
	-MP -MMD -MT ike_alg_encrypt_nss_cbc_ops.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_encrypt_nss_cbc_ops.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_encrypt_nss_cbc_ops.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ike_alg_encrypt_nss_cbc_ops.c:19:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from ike_alg_encrypt_nss_cbc_ops.c:23:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_encrypt_nss_ctr_ops.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_encrypt_nss_ctr_ops.d \
	-MP -MMD -MT ike_alg_encrypt_nss_ctr_ops.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_encrypt_nss_ctr_ops.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_encrypt_nss_ctr_ops.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ike_alg_encrypt_nss_ctr_ops.c:21:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plarena.h:15,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:6,
                 from ike_alg_encrypt_nss_ctr_ops.c:26:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_encrypt_nss_gcm_ops.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_encrypt_nss_gcm_ops.d \
	-MP -MMD -MT ike_alg_encrypt_nss_gcm_ops.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_encrypt_nss_gcm_ops.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_encrypt_nss_gcm_ops.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ike_alg_encrypt_nss_gcm_ops.c:16:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ../../include/lswlog.h:31,
                 from ike_alg_encrypt_nss_gcm_ops.c:25:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_desc.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_desc.d \
	-MP -MMD -MT ike_alg_desc.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_desc.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_desc.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ike_alg_desc.c:19:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from ike_alg_desc.c:20:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_3des.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_3des.d \
	-MP -MMD -MT ike_alg_3des.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_3des.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_3des.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ike_alg_3des.c:17:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_3des.c:19:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_aes.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_aes.d \
	-MP -MMD -MT ike_alg_aes.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_aes.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_aes.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/seccomon.h:17,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/blapit.h:11,
                 from ike_alg_aes.c:22:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_aes.c:26:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_camellia.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_camellia.d \
	-MP -MMD -MT ike_alg_camellia.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_camellia.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_camellia.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plarena.h:15,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:6,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_camellia.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_camellia.c:18:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_dh.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_dh.d \
	-MP -MMD -MT ike_alg_dh.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_dh.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_dh.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ike_alg_dh.c:17:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ike_alg_dh.c:22:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_md5.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_md5.d \
	-MP -MMD -MT ike_alg_md5.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_md5.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_md5.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ike_alg_md5.c:23:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_md5.c:25:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_none.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_none.d \
	-MP -MMD -MT ike_alg_none.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_none.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_none.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plarena.h:15,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:6,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_none.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_none.c:18:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_sha1.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_sha1.d \
	-MP -MMD -MT ike_alg_sha1.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_sha1.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_sha1.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ike_alg_sha1.c:24:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_sha1.c:26:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_sha2.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_sha2.d \
	-MP -MMD -MT ike_alg_sha2.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_sha2.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_sha2.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pkcs11t.h:25,
                 from ike_alg_sha2.c:21:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/ike_alg.h:20,
                 from ike_alg_sha2.c:25:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_encrypt_cbc_test_vectors.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_encrypt_cbc_test_vectors.d \
	-MP -MMD -MT ike_alg_encrypt_cbc_test_vectors.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_encrypt_cbc_test_vectors.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_encrypt_cbc_test_vectors.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ike_alg_encrypt_cbc_test_vectors.c:15:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ike_alg_encrypt_cbc_test_vectors.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_encrypt_ctr_test_vectors.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_encrypt_ctr_test_vectors.d \
	-MP -MMD -MT ike_alg_encrypt_ctr_test_vectors.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_encrypt_ctr_test_vectors.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_encrypt_ctr_test_vectors.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ike_alg_encrypt_ctr_test_vectors.c:15:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ike_alg_encrypt_ctr_test_vectors.c:17:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_encrypt_gcm_test_vectors.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_encrypt_gcm_test_vectors.d \
	-MP -MMD -MT ike_alg_encrypt_gcm_test_vectors.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_encrypt_gcm_test_vectors.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_encrypt_gcm_test_vectors.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ike_alg_encrypt_gcm_test_vectors.c:15:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ike_alg_encrypt_gcm_test_vectors.c:17:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ike_alg_prf_test_vectors.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ike_alg_prf_test_vectors.d \
	-MP -MMD -MT ike_alg_prf_test_vectors.o \
	-o ../../OBJ.linux./lib/libswan/ike_alg_prf_test_vectors.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ike_alg_prf_test_vectors.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ike_alg_prf_test_vectors.c:15:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
In file included from ../../include/constants.h:114,
                 from ike_alg_prf_test_vectors.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h: At top level:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"crypt_mac.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/crypt_mac.d \
	-MP -MMD -MT crypt_mac.o \
	-o ../../OBJ.linux./lib/libswan/crypt_mac.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/crypt_mac.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"crypt_hash.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/crypt_hash.d \
	-MP -MMD -MT crypt_hash.o \
	-o ../../OBJ.linux./lib/libswan/crypt_hash.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/crypt_hash.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from crypt_hash.c:20:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from crypt_hash.c:21:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"crypt_prf.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/crypt_prf.d \
	-MP -MMD -MT crypt_prf.o \
	-o ../../OBJ.linux./lib/libswan/crypt_prf.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/crypt_prf.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from crypt_prf.c:30:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from crypt_prf.c:31:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"crypt_symkey.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/crypt_symkey.d \
	-MP -MMD -MT crypt_symkey.o \
	-o ../../OBJ.linux./lib/libswan/crypt_symkey.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/crypt_symkey.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../include/constants.h:114,
                 from ../../include/lswalloc.h:27,
                 from crypt_symkey.c:18:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../include/lswlog.h:24,
                 from crypt_symkey.c:19:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ikev1_prf.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ikev1_prf.d \
	-MP -MMD -MT ikev1_prf.o \
	-o ../../OBJ.linux./lib/libswan/ikev1_prf.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ikev1_prf.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prerror.h:9,
                 from ../../include/lswnss.h:20,
                 from ../../include/ikev1_prf.h:23,
                 from ikev1_prf.c:20:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/lswnss.h:21,
                 from ../../include/ikev1_prf.h:23,
                 from ikev1_prf.c:20:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"ikev2_prf.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/ikev2_prf.d \
	-MP -MMD -MT ikev2_prf.o \
	-o ../../OBJ.linux./lib/libswan/ikev2_prf.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/ikev2_prf.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prtypes.h:26,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plarena.h:15,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:6,
                 from ../../include/ike_alg.h:20,
                 from ikev2_prf.c:25:
../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/prcpucfg.h:514:18: warning: "_ABI64" is not defined, evaluates to 0 [-Wundef]
 #if _MIPS_SIM == _ABI64
                  ^~~~~~
In file included from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nspr/plhash.h:11,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secitem.h:16,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/secoidt.h:14,
                 from ../../../../../staging_dir/target-mips_24kc_musl/usr/include/nss/pk11pub.h:8,
                 from ../../include/ike_alg.h:20,
                 from ikev2_prf.c:25:
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'snprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:101:2: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
  return __orig_snprintf(__s, __n, __f, __builtin_va_arg_pack());
  ^~~~~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h: In function 'sprintf':
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:110:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_snprintf(__s, __b, __f, __builtin_va_arg_pack());
   ^~~
../../../../../staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify/stdio.h:114:3: warning: format not a string literal, argument types not checked [-Wformat-nonliteral]
   __r = __orig_sprintf(__s, __f, __builtin_va_arg_pack());
   ^~~
ccache_cc -DTimeZoneOffset=timezone -Dlinux -D_GNU_SOURCE -pthread -std=gnu99 -g  -Wall -Wextra -Wformat -Wformat-nonliteral -Wformat-security -Wundef -Wmissing-declarations -Wredundant-decls -Wnested-externs -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2 -fstack-protector-all -fno-strict-aliasing -fPIE -DPIE -DNSS_IPSEC_PROFILE -DXFRM_LIFETIME_DEFAULT=30 -DUSE_IKEv1 -DXFRM_SUPPORT -DUSE_XFRM_INTERFACE -DUSE_DNSSEC -DDEFAULT_DNSSEC_ROOTKEY_FILE=\"/usr/share/dns/root.key\" -DUSE_3DES -DUSE_AES -DUSE_CAMELLIA -DUSE_CHACHA -DUSE_DH31 -DUSE_MD5 -DUSE_SHA1 -DUSE_SHA2 -DUSE_PRF_AES_XCBC -DUSE_NSS_KDF -DDEFAULT_RUNDIR=\"/var/run/pluto\" -DIPSEC_CONF=\"/etc/ipsec.conf\" -DIPSEC_CONFDDIR=\"/etc/ipsec.d\" -DIPSEC_NSSDIR=\"/etc/ipsec.d\" -DIPSEC_CONFDIR=\"/etc\" -DIPSEC_EXECDIR=\"/usr/libexec/ipsec\" -DIPSEC_SBINDIR=\"/usr/sbin\" -DIPSEC_VARDIR=\"/var\" -DPOLICYGROUPSDIR=\"/etc/ipsec.d/policies\" -DIPSEC_SECRETS_FILE=\"/etc/ipsec.secrets\" -DFORCE_PR_ASSERT -DUSE_FORK=1 -DUSE_VFORK=0 -DUSE_DAEMON=0 -DUSE_PTHREAD_SETSCHEDPRIO=1 -DGCC_LINT -DHAVE_LIBCAP_NG \
	-I. -I../../OBJ.linux./lib/libswan -I../../include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nss -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/nspr  \
	-DHERE_BASENAME=\"unbound.c\" -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4=libreswan-4.4 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto  -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include  \
	-MF ../../OBJ.linux./lib/libswan/unbound.d \
	-MP -MMD -MT unbound.o \
	-o ../../OBJ.linux./lib/libswan/unbound.o \
	-c /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/unbound.c
<command-line>: warning: "_FORTIFY_SOURCE" redefined
<command-line>: note: this is the location of the previous definition
/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan/unbound.c:32:10: fatal error: event2/event.h: No such file or directory
 #include <event2/event.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
make[7]: *** [../../mk/rules.mk:57: unbound.o] Error 1
make[6]: *** [../../mk/targets.mk:82: all] Error 2
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib/libswan'
make[5]: *** [../mk/targets.mk:82: recursive-all] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/lib'
make[4]: *** [/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/mk/targets.mk:82: recursive-all] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4'
make[3]: *** [Makefile:121: /openwrt/build_dir/target-mips_24kc_musl/libreswan-4.4/.built] Error 2
```
