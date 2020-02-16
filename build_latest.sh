#!/bin/bash
SCRIPT_ABS_PATH="$(cd $(dirname "$0"); pwd)"

cd $SCRIPT_ABS_PATH/ctcgfw-latest

cat>feeds.conf<<EOF
src-link packages ${SCRIPT_ABS_PATH}/feeds/openwrt/packages
src-link luci ${SCRIPT_ABS_PATH}/feeds/openwrt/luci
src-link routing ${SCRIPT_ABS_PATH}/feeds/openwrt/routing
src-link telephony ${SCRIPT_ABS_PATH}/feeds/openwrt/telephony
EOF

# just enable/disable feeds update and install
source $SCRIPT_ABS_PATH/scripts/feeds.sh

cat>.config<<'EOF'
CONFIG_TARGET_ath79=n
CONFIG_TARGET_x86=y
CONFIG_TARGET_x86_64=y
CONFIG_TARGET_ROOTFS_EXT4FS=y
CONFIG_TARGET_ROOTFS_SQUASHFS=y
CONFIG_VMDK_IMAGES=y
CONFIG_TARGET_IMAGES_GZIP=y
CONFIG_TARGET_IMAGES_PAD=n
CONFIG_TARGET_KERNEL_PARTSIZE=32
CONFIG_TARGET_ROOTFS_PARTSIZE=1024

CONFIG_DEVEL=y
# CONFIG_CCACHE=y
CONFIG_BUILD_LOG=y
CONFIG_IB=y
CONFIG_SDK=y

CONFIG_PACKAGE_luci-app-rclone=y
# official luci application
CONFIG_PACKAGE_luci-app-adblock=m
CONFIG_PACKAGE_luci-app-advanced-reboot=m
CONFIG_PACKAGE_luci-app-ahcp=m
CONFIG_PACKAGE_luci-app-aria2=m
CONFIG_PACKAGE_luci-app-attendedsysupgrade=m
CONFIG_PACKAGE_luci-app-banip=m
CONFIG_PACKAGE_luci-app-bcp38=m
CONFIG_PACKAGE_luci-app-bmx7=m
CONFIG_PACKAGE_luci-app-clamav=m
CONFIG_PACKAGE_luci-app-commands=m
CONFIG_PACKAGE_luci-app-coovachilli=m
CONFIG_PACKAGE_luci-app-cshark=m
CONFIG_PACKAGE_luci-app-dcwapd=m
CONFIG_PACKAGE_luci-app-ddns=m
CONFIG_PACKAGE_luci-app-diag-core=m
CONFIG_PACKAGE_luci-app-dnscrypt-proxy=m
CONFIG_PACKAGE_luci-app-dump1090=m
CONFIG_PACKAGE_luci-app-dynapoint=m
CONFIG_PACKAGE_luci-app-firewall=m
CONFIG_PACKAGE_luci-app-frpc=m
CONFIG_PACKAGE_luci-app-frps=m
CONFIG_PACKAGE_luci-app-fwknopd=m
CONFIG_PACKAGE_luci-app-hd-idle=m
CONFIG_PACKAGE_luci-app-https-dns-proxy=m
CONFIG_PACKAGE_luci-app-ksmbd=m
CONFIG_PACKAGE_luci-app-ltqtapi=m
CONFIG_PACKAGE_luci-app-lxc=m
CONFIG_PACKAGE_luci-app-minidlna=m
CONFIG_PACKAGE_luci-app-mjpg-streamer=m
CONFIG_PACKAGE_luci-app-mosquitto=m
CONFIG_PACKAGE_luci-app-mwan3=m
CONFIG_PACKAGE_luci-app-nextdns=m
CONFIG_PACKAGE_luci-app-nft-qos=m
CONFIG_PACKAGE_luci-app-nlbwmon=m
CONFIG_PACKAGE_luci-app-noddos=m
CONFIG_PACKAGE_luci-app-ntpc=m
CONFIG_PACKAGE_luci-app-nut=m
CONFIG_PACKAGE_luci-app-ocserv=m
# CONFIG_PACKAGE_luci-app-olsr=m
# CONFIG_PACKAGE_luci-app-olsr-services=m
# CONFIG_PACKAGE_luci-app-olsr-viz=m
CONFIG_PACKAGE_luci-app-omcproxy=m
CONFIG_PACKAGE_luci-app-openvpn=m
CONFIG_PACKAGE_luci-app-opkg=m
CONFIG_PACKAGE_luci-app-p910nd=m
CONFIG_PACKAGE_luci-app-pagekitec=m
CONFIG_PACKAGE_luci-app-polipo=m
CONFIG_PACKAGE_luci-app-privoxy=m
CONFIG_PACKAGE_luci-app-qos=m
CONFIG_PACKAGE_luci-app-radicale=m
CONFIG_PACKAGE_luci-app-radicale2=m
CONFIG_PACKAGE_luci-app-rosy-file-server=m
CONFIG_PACKAGE_luci-app-rp-pppoe-server=m
CONFIG_PACKAGE_luci-app-samba=m
CONFIG_PACKAGE_luci-app-samba=m
CONFIG_PACKAGE_luci-app-ser2net=m
CONFIG_PACKAGE_luci-app-shadowsocks-libev=m
CONFIG_PACKAGE_luci-app-shairplay=m
CONFIG_PACKAGE_luci-app-siitwizard=m
CONFIG_PACKAGE_luci-app-simple-adblock=m
CONFIG_PACKAGE_luci-app-snmp=m
CONFIG_PACKAGE_luci-app-splash=m
CONFIG_PACKAGE_luci-app-squid=m
CONFIG_PACKAGE_luci-app-statistics=m
CONFIG_PACKAGE_luci-app-tinyproxy=m
CONFIG_PACKAGE_luci-app-transmission=m
CONFIG_PACKAGE_luci-app-travelmate=m
CONFIG_PACKAGE_luci-app-ttyd=m
CONFIG_PACKAGE_luci-app-udpxy=m
CONFIG_PACKAGE_luci-app-uhttpd=m
CONFIG_PACKAGE_luci-app-unbound=m
CONFIG_PACKAGE_luci-app-upnp=m
CONFIG_PACKAGE_luci-app-vnstat=m
CONFIG_PACKAGE_luci-app-vnstat2=m
CONFIG_PACKAGE_luci-app-vpnbypass=m
CONFIG_PACKAGE_luci-app-vpn-policy-routing=m
CONFIG_PACKAGE_luci-app-watchcat=m
CONFIG_PACKAGE_luci-app-wifischedule=m
CONFIG_PACKAGE_luci-app-wireguard=m
CONFIG_PACKAGE_luci-app-wol=m
CONFIG_PACKAGE_luci-app-yggdrasil=m
EOF

make defconfig

