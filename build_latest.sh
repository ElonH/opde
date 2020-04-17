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
src-link routing ${SCRIPT_ABS_PATH}/feeds/ctcgfw/routing
src-link telephony ${SCRIPT_ABS_PATH}/feeds/openwrt/telephony
"
}

# basic configuration whatever build SDK, build packages or develepment
function base_pack_conf {
BASE_PACK_CONF="
$(TARGET_bcm27xx_bcm2709)

$(GENERAL_SETTING)

CONFIG_PACKAGE_kmod-rtl8821cu=n
CONFIG_PACKAGE_kmod-dahdi=n
"
}

# this configuration will be added only when building SDK
function build_sdk_pack_conf {
# cancel default packages
BUILD_SDK_PACK_CONF="
CONFIG_PACKAGE_ootoc=y
"
}

# this configuration will be added only when build packages using SDK
function sdk_pack_conf {
# cancel default packages
SDK_PACK_CONF="
CONFIG_PACKAGE_ootoc=n
"
}

# this configuration will be add in develepment envirment
function user_pack_conf {
USER_PACK_CONF="

"
}

source "${SCRIPT_ABS_PATH}/scripts/main-build.sh"
