#!/bin/bash

function TARGET_X86_64 {
    echo "
CONFIG_TARGET_ath79=n
CONFIG_TARGET_x86=y
CONFIG_TARGET_x86_64=y
"
}

function ENABLE_LOG {
    echo "
CONFIG_DEVEL=y
CONFIG_BUILD_LOG=y
"
}

function IMG_SETTING {
    echo "
CONFIG_TARGET_ROOTFS_EXT4FS=n
CONFIG_TARGET_ROOTFS_SQUASHFS=y
CONFIG_VMDK_IMAGES=n
CONFIG_TARGET_IMAGES_GZIP=y
CONFIG_TARGET_ROOTFS_TARGZ=n
CONFIG_TARGET_KERNEL_PARTSIZE=32
CONFIG_TARGET_ROOTFS_PARTSIZE=512
"
}

function GEN_SDK_IB {
    echo "
CONFIG_IB=$1
CONFIG_SDK=$1
"
}

function SAVE_SPACE {
    echo "CONFIG_BUILDBOT=$1"
}

function CTCGFW_PACKAGES {
    obtain_packages_conf "$SOURCE_ORIGIN_PATH/package/ctcgfw" "$1"
    echo "CONFIG_PACKAGE_cups-bjnp=n
CONFIG_PACKAGE_cups=n
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_Trojan=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_Kcptun=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_Shadowsocks_Server=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_Shadowsocks_Socks=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_dnscrypt_proxy=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_dnsforwarder=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_ChinaDNS=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_haproxy=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_privoxy=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_simple-obfs=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_simple-obfs-server=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_ipt2socks=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_GoQuiet-client=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_GoQuiet-server=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_v2ray-plugin=y
"
}
function LEAN_PACKAGES {
    obtain_packages_conf "$SOURCE_ORIGIN_PATH/package/lean" "$1"
}
function NTLF9T_PACKAGES {
    obtain_packages_conf "$SOURCE_ORIGIN_PATH/package/ntlf9t" "$1"
}
function DEFAULT_EXTRA_PACKAGE {
    echo "
# CONFIG_PACKAGE_base-files=$1
# CONFIG_PACKAGE_libc=$1
# CONFIG_PACKAGE_libgcc=$1
CONFIG_PACKAGE_busybox=$1
CONFIG_PACKAGE_dropbear=$1
# CONFIG_PACKAGE_mtd=$1
CONFIG_PACKAGE_uci=$1
# CONFIG_PACKAGE_opkg=$1
# CONFIG_PACKAGE_netifd=$1
# CONFIG_PACKAGE_fstools=$1
# CONFIG_PACKAGE_uclient-fetch=$1
CONFIG_PACKAGE_logd=$1
CONFIG_PACKAGE_urandom-seed=$1
CONFIG_PACKAGE_urngd=$1
# CONFIG_PACKAGE_kmod-nf-nathelper=$1
# CONFIG_PACKAGE_kmod-nf-nathelper-extra=$1
# CONFIG_PACKAGE_kmod-ipt-raw=$1
CONFIG_PACKAGE_wget=$1
CONFIG_PACKAGE_libustream-openssl=$1
CONFIG_PACKAGE_ca-certificates=$1
CONFIG_PACKAGE_luci-proto-relay=$1
CONFIG_PACKAGE_default-settings=$1
# CONFIG_PACKAGE_luci=$1
# CONFIG_PACKAGE_luci-base=$1
CONFIG_PACKAGE_luci-compat=$1
CONFIG_PACKAGE_luci-lib-ipkg=$1
CONFIG_PACKAGE_luci-app-flowoffload=$1
CONFIG_PACKAGE_dnsmasq-full=$1
# CONFIG_PACKAGE_iptables=$1
# CONFIG_PACKAGE_ip6tables=$1
CONFIG_PACKAGE_ppp=$1
CONFIG_PACKAGE_ppp-mod-pppoe=$1
# CONFIG_PACKAGE_firewall=$1
CONFIG_PACKAGE_odhcpd-ipv6only=$1
CONFIG_PACKAGE_odhcp6c=$1
# CONFIG_PACKAGE_kmod-ipt-offload=$1
# CONFIG_PACKAGE_kmod-tcp-bbr=$1
CONFIG_PACKAGE_block-mount=$1
CONFIG_PACKAGE_fdisk=$1
CONFIG_PACKAGE_lsblk=$1
CONFIG_PACKAGE_mdadm=$1
CONFIG_PACKAGE_partx-utils=$1
CONFIG_PACKAGE_mkf2fs=$1
CONFIG_PACKAGE_fdisk=$1
CONFIG_PACKAGE_e2fsprogs=$1
CONFIG_PACKAGE_wpad=$1
CONFIG_PACKAGE_ath10k-firmware-qca988x=$1
CONFIG_PACKAGE_ath10k-firmware-qca9888=$1
CONFIG_PACKAGE_ath10k-firmware-qca9984=$1
CONFIG_PACKAGE_brcmfmac-firmware-43602a1-pcie=$1
CONFIG_PACKAGE_alsa-utils=$1
CONFIG_PACKAGE_htop=$1
CONFIG_PACKAGE_lm-sensors=$1
CONFIG_PACKAGE_autocore=$1
CONFIG_PACKAGE_luci-proto-bonding=$1
CONFIG_PACKAGE_ca-certificates=$1
"
}

function OFFICIAL_LUCI_APP {
    echo "
# official luci application
CONFIG_PACKAGE_luci-app-adblock=$1
CONFIG_PACKAGE_luci-app-advanced-reboot=$1
CONFIG_PACKAGE_luci-app-ahcp=$1
CONFIG_PACKAGE_luci-app-aria2=$1
CONFIG_PACKAGE_luci-app-attendedsysupgrade=$1
CONFIG_PACKAGE_luci-app-banip=$1
CONFIG_PACKAGE_luci-app-bcp38=$1
CONFIG_PACKAGE_luci-app-bmx7=$1
CONFIG_PACKAGE_luci-app-clamav=$1
CONFIG_PACKAGE_luci-app-commands=$1
CONFIG_PACKAGE_luci-app-coovachilli=$1
CONFIG_PACKAGE_luci-app-cshark=$1
CONFIG_PACKAGE_luci-app-dcwapd=$1
CONFIG_PACKAGE_luci-app-ddns=$1
CONFIG_PACKAGE_luci-app-diag-core=$1
CONFIG_PACKAGE_luci-app-dnscrypt-proxy=$1
CONFIG_PACKAGE_luci-app-dump1090=$1
CONFIG_PACKAGE_luci-app-dynapoint=$1
CONFIG_PACKAGE_luci-app-firewall=$1
CONFIG_PACKAGE_luci-app-frpc=$1
CONFIG_PACKAGE_luci-app-frps=$1
CONFIG_PACKAGE_luci-app-fwknopd=$1
CONFIG_PACKAGE_luci-app-hd-idle=$1
CONFIG_PACKAGE_luci-app-https-dns-proxy=$1
CONFIG_PACKAGE_luci-app-ksmbd=$1
CONFIG_PACKAGE_luci-app-ltqtapi=$1
CONFIG_PACKAGE_luci-app-lxc=$1
CONFIG_PACKAGE_luci-app-minidlna=$1
CONFIG_PACKAGE_luci-app-mjpg-streamer=$1
CONFIG_PACKAGE_luci-app-mosquitto=$1
CONFIG_PACKAGE_luci-app-mwan3=$1
CONFIG_PACKAGE_luci-app-nextdns=$1
CONFIG_PACKAGE_luci-app-nft-qos=$1
CONFIG_PACKAGE_luci-app-nlbwmon=$1
CONFIG_PACKAGE_luci-app-noddos=$1
CONFIG_PACKAGE_luci-app-ntpc=$1
CONFIG_PACKAGE_luci-app-nut=$1
CONFIG_PACKAGE_luci-app-ocserv=$1
# TODO: fix olsrd package
CONFIG_PACKAGE_luci-app-olsr=n
CONFIG_PACKAGE_luci-app-olsr-services=n
CONFIG_PACKAGE_luci-app-olsr-viz=n
CONFIG_PACKAGE_luci-app-omcproxy=$1
CONFIG_PACKAGE_luci-app-openvpn=$1
CONFIG_PACKAGE_luci-app-opkg=$1
CONFIG_PACKAGE_luci-app-p910nd=$1
CONFIG_PACKAGE_luci-app-pagekitec=$1
CONFIG_PACKAGE_luci-app-polipo=$1
CONFIG_PACKAGE_luci-app-privoxy=$1
CONFIG_PACKAGE_luci-app-qos=$1
CONFIG_PACKAGE_luci-app-radicale=$1
CONFIG_PACKAGE_luci-app-radicale2=$1
CONFIG_PACKAGE_luci-app-rosy-file-server=$1
CONFIG_PACKAGE_luci-app-rp-pppoe-server=$1
CONFIG_PACKAGE_luci-app-samba=$1
CONFIG_PACKAGE_luci-app-samba=$1
CONFIG_PACKAGE_luci-app-ser2net=$1
CONFIG_PACKAGE_luci-app-shadowsocks-libev=$1
CONFIG_PACKAGE_luci-app-shairplay=$1
CONFIG_PACKAGE_luci-app-siitwizard=$1
CONFIG_PACKAGE_luci-app-simple-adblock=$1
CONFIG_PACKAGE_luci-app-snmp=$1
CONFIG_PACKAGE_luci-app-splash=$1
CONFIG_PACKAGE_luci-app-squid=$1
CONFIG_PACKAGE_luci-app-statistics=$1
CONFIG_PACKAGE_luci-app-tinyproxy=$1
CONFIG_PACKAGE_luci-app-transmission=$1
CONFIG_PACKAGE_luci-app-travelmate=$1
CONFIG_PACKAGE_luci-app-ttyd=$1
CONFIG_PACKAGE_luci-app-udpxy=$1
CONFIG_PACKAGE_luci-app-uhttpd=$1
CONFIG_PACKAGE_luci-app-unbound=$1
CONFIG_PACKAGE_luci-app-upnp=$1
CONFIG_PACKAGE_luci-app-vnstat=$1
CONFIG_PACKAGE_luci-app-vnstat2=$1
CONFIG_PACKAGE_luci-app-vpnbypass=$1
CONFIG_PACKAGE_luci-app-vpn-policy-routing=$1
CONFIG_PACKAGE_luci-app-watchcat=$1
CONFIG_PACKAGE_luci-app-wifischedule=$1
CONFIG_PACKAGE_luci-app-wireguard=$1
CONFIG_PACKAGE_luci-app-wol=$1
CONFIG_PACKAGE_luci-app-yggdrasil=$1
"
}

function _scans_packages() {
    shopt -s globstar
    for i in "$1"/**/Makefile; do
        [[ $(cat "$i" | grep "rules.mk") == 'include $(TOPDIR)/rules.mk' ]] || continue # opkg Makefile must be contain 'rules.mk'
        DIR_NAME=$(dirname "$i")
        DIR_NAME="${DIR_NAME##*/}" # is directory name, is NOT path
        # echo "$i"
        grep '$(eval $(call BuildPackage,.*))' < "$i" | while IFS= read -r j ; do
            # echo "$j"
            PKG_NAME="${j#*,}"
            PKG_NAME="${PKG_NAME%%))}" # $(eval $(call BuildPackage,[PKG_NAME]))
            PKG_NAME="${PKG_NAME%%,*}" # [PKG_NAME],+zlib,+some_package...
            # echo "$PKG_NAME"
            if [[ "$PKG_NAME" == *'$(PKG_NAME)'* ]]; then
                REAL_NAME=$(cat "$i" | grep "PKG_NAME:=" | sed  's/^PKG_NAME:=//') # PKG_NAME:=[REAL_NAME]
                # echo "$REAL_NAME"
                PKG_NAME=${PKG_NAME//'$(PKG_NAME)'/$REAL_NAME}
            fi
            echo "$PKG_NAME"
            # break
        done
        if [[ $(cat "$i" | grep "luci.mk" | sed 's/^.*luci.mk/luci.mk/') == "luci.mk" ]];then
            echo "$DIR_NAME"
        fi
        # break;
    done
}

# $1: dir path
# $2: 'n','y','m'
function obtain_packages_conf() {
    if ! [ -d "$1" ]; then
        echo -e "#Dir '$1' not exist"
        return
    fi
    CONTENTS=$(_scans_packages "$1" | sed "s/^/CONFIG_PACKAGE_/" | sed "s/$/=$2/")
    echo $'\n'"$CONTENTS"
}
