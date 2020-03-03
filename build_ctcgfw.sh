#!/bin/bash
SCRIPT_ABS_PATH="$(cd $(dirname "$0"); pwd)"
source "${SCRIPT_ABS_PATH}/scripts/common-vars.sh"

# directory name corresponds to openwrt source
SOURCE_NAME=ctcgfw

# feeds locations
FEEDS_CONF="
src-link packages ${SCRIPT_ABS_PATH}/feeds/ctcgfw/packages
src-link luci ${SCRIPT_ABS_PATH}/feeds/ctcgfw/luci
src-link routing ${SCRIPT_ABS_PATH}/feeds/openwrt/routing
src-link telephony ${SCRIPT_ABS_PATH}/feeds/openwrt/telephony
"

# basic configuration whatever build SDK or build packages
BASE_PACK_CONF="
$(TARGET_X86_64)

$(IMG_SETTING)
$(ENABLE_LOG)
CONFIG_CCACHE=y

"

# this packages will not be added to conf when building SDK
USER_PACK_CONF="

"

source "${SCRIPT_ABS_PATH}/scripts/main-build.sh"

