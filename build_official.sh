#!/bin/bash
SCRIPT_ABS_PATH="$(cd $(dirname "$0"); pwd)"
source $SCRIPT_ABS_PATH/scripts/common-func.sh

SOURCE_NAME=latest
SOURCE_BASE_PATH=$SCRIPT_ABS_PATH/$SOURCE_NAME
cd $SOURCE_BASE_PATH

FEEDS_CONF="
src-link packages ${SCRIPT_ABS_PATH}/feeds/openwrt/packages
src-link luci ${SCRIPT_ABS_PATH}/feeds/openwrt/luci
src-link routing ${SCRIPT_ABS_PATH}/feeds/openwrt/routing
src-link telephony ${SCRIPT_ABS_PATH}/feeds/openwrt/telephony
src-link rclone ${SCRIPT_ABS_PATH}/feeds/openwrt/rclone
"

# add base feeds (only for SDK)
source $SCRIPT_ABS_PATH/scripts/base-feeds.sh
source $SCRIPT_ABS_PATH/scripts/change-to-sdk.sh

echo "${FEEDS_CONF}">feeds.conf

# just enable/disable feeds update and install
source $SCRIPT_ABS_PATH/scripts/feeds.sh

source ${SCRIPT_ABS_PATH}/scripts/common-vars.sh
CONFIG_CONTS="
$(TARGET_X86_64)

$(IMG_SETTING)
$(ENABLE_LOG)
# CONFIG_CCACHE=y

"
source $SCRIPT_ABS_PATH/scripts/default-extra-config.sh
source $SCRIPT_ABS_PATH/scripts/sdk-config.sh
ADDON_CONFIG_CONTS="
CONFIG_PACKAGE_runc=y

CONFIG_PACKAGE_luci=y
CONFIG_LUCI_LANG_zh_Hans=y
CONFIG_PACKAGE_luci-theme-material=y
CONFIG_PACKAGE_luci-theme-openwrt=y

CONFIG_PACKAGE_luci-app-rclone=y
CONFIG_PACKAGE_luci-app-adblock=y
CONFIG_PACKAGE_luci-app-aria2=y
"
source $SCRIPT_ABS_PATH/scripts/addon-packages.sh
source $SCRIPT_ABS_PATH/scripts/help-exit.sh
echo "${CONFIG_CONTS}"
echo "${CONFIG_CONTS}">.config
make defconfig

