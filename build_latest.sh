#!/bin/bash
SCRIPT_ABS_PATH="$(cd $(dirname "$0"); pwd)"
source "${SCRIPT_ABS_PATH}/scripts/common-vars.sh"

# directory name corresponds to openwrt source
SOURCE_NAME=latest

# feeds locations
function feeds_conf {
FEEDS_CONF="
src-link packages ${SCRIPT_ABS_PATH}/feeds/latest/packages
src-link luci ${SCRIPT_ABS_PATH}/feeds/latest/luci
src-link routing ${SCRIPT_ABS_PATH}/feeds/openwrt/routing
src-link telephony ${SCRIPT_ABS_PATH}/feeds/openwrt/telephony
"
}

# basic configuration whatever build SDK or build packages
function base_pack_conf {
BASE_PACK_CONF="
$(TARGET_X86_64)

$(IMG_SETTING)
$(ENABLE_LOG)
CONFIG_CCACHE=y

CONFIG_PACKAGE_kmod-rtl8821cu=n
"
}

# this packages will not be added to conf when building SDK
function user_pack_conf {
USER_PACK_CONF="
CONFIG_PACKAGE_ootoc=y
CONFIG_TESTING_KERNEL=y
"
}

source "${SCRIPT_ABS_PATH}/scripts/main-build.sh"
