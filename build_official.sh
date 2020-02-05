#!/bin/bash
SCRIPT_ABS_PATH="$(cd $(dirname "$0"); pwd)"

cd $SCRIPT_ABS_PATH/openwrt

cat>feeds.conf<<EOF
src-link packages ${SCRIPT_ABS_PATH}/feeds/openwrt/packages
src-link luci ${SCRIPT_ABS_PATH}/feeds/openwrt/luci
src-link routing ${SCRIPT_ABS_PATH}/feeds/openwrt/routing
src-link telephony ${SCRIPT_ABS_PATH}/feeds/openwrt/telephony
src-link rclone ${SCRIPT_ABS_PATH}/feeds/openwrt/rclone
EOF

QUICK_DEFAULT="y"
read -e -p "quick config: [Y/n]" QUICK
QUICK="${QUICK:-$QUICK_DEFAULT}"
case $QUICK in
	"y")
		;;
	"n")
		./scripts/feeds update -a && ./scripts/feeds install -a
		;;
	*)
		echo -e "unknow"
		exit 1
		;;
esac

cat>.config<<'EOF'
CONFIG_TARGET_ath79=n
CONFIG_TARGET_x86=y
CONFIG_TARGET_x86_64=y
CONFIG_TARGET_ROOTFS_EXT4FS=y
CONFIG_TARGET_ROOTFS_SQUASHFS=n
CONFIG_VMDK_IMAGES=n
CONFIG_TARGET_IMAGES_GZIP=y
CONFIG_TARGET_IMAGES_PAD=n
CONFIG_TARGET_KERNEL_PARTSIZE=32
CONFIG_TARGET_ROOTFS_PARTSIZE=1024

CONFIG_DEVEL=y
# CONFIG_CCACHE=y
CONFIG_BUILD_LOG=y

CONFIG_PACKAGE_runc=y

CONFIG_PACKAGE_luci=y
CONFIG_LUCI_LANG_zh_Hans=y
CONFIG_PACKAGE_luci-theme-material=y
CONFIG_PACKAGE_luci-theme-openwrt=y

CONFIG_PACKAGE_luci-app-rclone=y
CONFIG_PACKAGE_luci-app-adblock=y
EOF

make defconfig

