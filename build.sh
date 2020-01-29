#!/bin/bash

cd ctcgfw

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
CONFIG_TARGET_ROOTFS_EXT4FS=y
CONFIG_TARGET_ROOTFS_SQUASHFS=n
CONFIG_VMDK_IMAGES=n
CONFIG_TARGET_IMAGES_GZIP=y
CONFIG_TARGET_IMAGES_PAD=n
CONFIG_TARGET_KERNEL_PARTSIZE=32
CONFIG_TARGET_ROOTFS_PARTSIZE=1024

CONFIG_DEVEL=y
CONFIG_BUILD_LOG=y

CONFIG_PACKAGE_luci-theme-material=y

CONFIG_PACKAGE_luci-app-aria2=y
CONFIG_PACKAGE_luci-app-adguardhome=y
CONFIG_PACKAGE_luci-app-clash=y

CONFIG_PACKAGE_luci-app-cifs=y
CONFIG_PACKAGE_luci-app-cifsd=y

CONFIG_PACKAGE_luci-app-diskman=y
CONFIG_PACKAGE_luci-app-filebrowser=y
CONFIG_PACKAGE_luci-app-kodexplorer=y
CONFIG_PACKAGE_luci-app-rclone=y
CONFIG_PACKAGE_luci-app-transmission=y
CONFIG_PACKAGE_luci-app-ttyd=y
CONFIG_PACKAGE_luci-app-serverchan=y

CONFIG_PACKAGE_luci-app-ssr-plus=n
CONFIG_PACKAGE_luci-app-vssr=y
EOF

make defconfig

