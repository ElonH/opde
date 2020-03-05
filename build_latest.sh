#!/bin/bash
SCRIPT_ABS_PATH="$(cd $(dirname "$0"); pwd)"
source "${SCRIPT_ABS_PATH}/scripts/common-vars.sh"

# directory name corresponds to openwrt source
SOURCE_NAME=latest

# feeds locations
FEEDS_CONF="
src-link packages ${SCRIPT_ABS_PATH}/feeds/openwrt/packages
src-link luci ${SCRIPT_ABS_PATH}/feeds/openwrt/luci
src-link routing ${SCRIPT_ABS_PATH}/feeds/openwrt/routing
src-link telephony ${SCRIPT_ABS_PATH}/feeds/openwrt/telephony
"

# basic configuration whatever build SDK or build packages
BASE_PACK_CONF="
$(TARGET_X86_64)

$(IMG_SETTING)
$(ENABLE_LOG)
CONFIG_CCACHE=y

CONFIG_PACKAGE_kmod-rtl8821cu=n
"

# this packages will not be added to conf when building SDK
USER_PACK_CONF="
$(DEFAULT_EXTRA_PACKAGE m)

"
# $(OFFICIAL_LUCI_APP m)
# CONFIG_PACKAGE_luci-app-rclone=y
# $(CTCGFW_PACKAGES y)

source "${SCRIPT_ABS_PATH}/scripts/main-build.sh"
