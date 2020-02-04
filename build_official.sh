#!/bin/bash
SCRIPT_ABS_PATH="$(cd $(dirname "$0"); pwd)"
FEED_CONF=""
for FEED_SOURCE in $SCRIPT_ABS_PATH/feeds/openwrt/*/
do
	FEED_ABS_PATH=${FEED_SOURCE%*/}
	FEED_NAME=${FEED_ABS_PATH##*/}
	FEED_CONF+=$"src-link $FEED_NAME $FEED_ABS_PATH
"
done

cd $SCRIPT_ABS_PATH/openwrt

cat>feeds.conf<<EOF
${FEED_CONF}
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

EOF

make defconfig

