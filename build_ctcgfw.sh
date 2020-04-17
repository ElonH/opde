#!/bin/bash
SCRIPT_ABS_PATH="$(cd $(dirname "$0"); pwd)"
source "${SCRIPT_ABS_PATH}/scripts/common-vars.sh"

# directory name corresponds to openwrt source
SOURCE_NAME=ctcgfw

# feeds locations
function feeds_conf {
FEEDS_CONF="
src-link packages ${SCRIPT_ABS_PATH}/feeds/ctcgfw/packages
src-link luci ${SCRIPT_ABS_PATH}/feeds/ctcgfw/luci
src-link routing ${SCRIPT_ABS_PATH}/feeds/ctcgfw/routing
src-link telephony ${SCRIPT_ABS_PATH}/feeds/openwrt/telephony
"
}

# basic configuration whatever build SDK, build packages or develepment
function base_pack_conf {
BASE_PACK_CONF="
$(TARGET_bcm27xx_bcm2709)

$(GENERAL_SETTING)

CONFIG_PACKAGE_kmod-batman-adv=n
CONFIG_PACKAGE_kmod-mt_wifi=n
CONFIG_PACKAGE_kmod-rtl8821cu=n

CONFIG_PACKAGE_luci-app-ddns=n
CONFIG_PACKAGE_luci-app-sqm=n
CONFIG_PACKAGE_luci-app-upnp=n
CONFIG_PACKAGE_luci-app-adbyby-plus=n
CONFIG_PACKAGE_luci-app-autoreboot=n
CONFIG_PACKAGE_luci-app-filetransfer=n
CONFIG_PACKAGE_luci-app-vsftpd=n
CONFIG_PACKAGE_luci-app-ssr-plus=n
CONFIG_PACKAGE_luci-app-unblockmusic=n
CONFIG_PACKAGE_luci-app-arpbind=n
CONFIG_PACKAGE_luci-app-vlmcsd=n
CONFIG_PACKAGE_luci-app-wol=n
CONFIG_PACKAGE_luci-app-ramfree=n
CONFIG_PACKAGE_luci-app-sfe=n
CONFIG_PACKAGE_luci-app-nlbwmon=n
CONFIG_PACKAGE_luci-app-accesscontrol=n
CONFIG_PACKAGE_luci-app-cpufreq=n
CONFIG_PACKAGE_ddns-scripts_aliyun=n
CONFIG_PACKAGE_ddns-scripts_dnspod=n
CONFIG_PACKAGE_luci-app-airplay2=n
CONFIG_PACKAGE_luci-app-xlnetacc=n
CONFIG_PACKAGE_luci-app-zerotier=n
CONFIG_PACKAGE_autosamba=n
CONFIG_PACKAGE_luci-app-music-remote-center=n
CONFIG_PACKAGE_kmod-tcp-bbr=m
CONFIG_PACKAGE_luci-app-flowoffload=n
CONFIG_PACKAGE_luci-app-amule=n
CONFIG_PACKAGE_luci-app-qbittorrent=n
CONFIG_PACKAGE_luci-app-openvpn-server=n

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

