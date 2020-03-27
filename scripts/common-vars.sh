#!/bin/bash

function TARGET_X86_64 {
    echo "
CONFIG_TARGET_ath79=n
CONFIG_TARGET_x86=y
CONFIG_TARGET_x86_64=y
"
}

function ENABLE_LOG {
    echo "
CONFIG_DEVEL=y
CONFIG_BUILD_LOG=y
"
}

function IMG_SETTING {
    echo "
CONFIG_TARGET_ROOTFS_EXT4FS=y
CONFIG_TARGET_ROOTFS_SQUASHFS=n
CONFIG_VMDK_IMAGES=n
CONFIG_TARGET_IMAGES_GZIP=y
CONFIG_TARGET_ROOTFS_TARGZ=n
CONFIG_TARGET_KERNEL_PARTSIZE=32
CONFIG_TARGET_ROOTFS_PARTSIZE=512
"
}

function GEN_SDK_IB {
    echo "
CONFIG_IB=$1
CONFIG_SDK=$1
"
}

function SAVE_SPACE {
    echo "CONFIG_BUILDBOT=$1"
}

function CTCGFW_PACKAGES {
    obtain_packages_conf "$SOURCE_ORIGIN_PATH/package/ctcgfw" "$1"
    echo "CONFIG_PACKAGE_cups-bjnp=n
CONFIG_PACKAGE_cups=n
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_Trojan=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_Kcptun=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_Shadowsocks_Server=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_Shadowsocks_Socks=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_dnscrypt_proxy=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_dnsforwarder=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_ChinaDNS=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_haproxy=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_privoxy=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_simple-obfs=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_simple-obfs-server=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_ipt2socks=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_GoQuiet-client=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_GoQuiet-server=y
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_v2ray-plugin=y
"
}
function LEAN_PACKAGES {
    obtain_packages_conf "$SOURCE_ORIGIN_PATH/package/lean" "$1"
}
function LIENOL_ZXLHHYCCC_NTLF9T_PACKAGES {
    obtain_packages_conf "$SOURCE_ORIGIN_PATH/package/ntlf9t" "$1"
    obtain_packages_conf "$SOURCE_ORIGIN_PATH/package/lienol" "$1"
    obtain_packages_conf "$SOURCE_ORIGIN_PATH/package/zxlhhyccc" "$1"
}

function OFFICIAL_LUCI_APP {
    obtain_packages_conf "$SOURCE_BASE_PATH/package/feeds/luci" "$1"
}
function OFFICIAL_PACKAGES_LANG {
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/lang" "$1"
}
function OFFICIAL_PACKAGES_LIB_1 {
    # 0-50%
    ALL_PACKAGE_LIBS=$(obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/libs" "$1")
    PACKAGES_CNT=$(echo "$ALL_PACKAGE_LIBS" | wc -l)
    echo "$ALL_PACKAGE_LIBS" | head -$(("$PACKAGES_CNT"/2))
}
function OFFICIAL_PACKAGES_LIB_2 {
    # 50%-75%
    ALL_PACKAGE_LIBS=$(obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/libs" "$1")
    PACKAGES_CNT=$(echo "$ALL_PACKAGE_LIBS" | wc -l)
    ALL_PACKAGE_LIBS=$(echo "$ALL_PACKAGE_LIBS" | tail -$(("$PACKAGES_CNT"-"$PACKAGES_CNT"/2)))
    PACKAGES_CNT=$(echo "$ALL_PACKAGE_LIBS" | wc -l)
    echo "$ALL_PACKAGE_LIBS" | head -$(("$PACKAGES_CNT"/2))
}
function OFFICIAL_PACKAGES_LIB_3 {
    # 75%-100%
    ALL_PACKAGE_LIBS=$(obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/libs" "$1")
    PACKAGES_CNT=$(echo "$ALL_PACKAGE_LIBS" | wc -l)
    ALL_PACKAGE_LIBS=$(echo "$ALL_PACKAGE_LIBS" | tail -$(("$PACKAGES_CNT"-"$PACKAGES_CNT"/2)))
    PACKAGES_CNT=$(echo "$ALL_PACKAGE_LIBS" | wc -l)
    echo "$ALL_PACKAGE_LIBS" | tail -$(("$PACKAGES_CNT"-"$PACKAGES_CNT"/2))
}
function OFFICIAL_PACKAGES_NET_1 {
    # 0-50%
    ALL_PACKAGE_LIBS=$(obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/net" "$1")
    PACKAGES_CNT=$(echo "$ALL_PACKAGE_LIBS" | wc -l)
    echo "$ALL_PACKAGE_LIBS" | head -$(("$PACKAGES_CNT"/2))
}
function OFFICIAL_PACKAGES_NET_2 {
    # 50-100%
    ALL_PACKAGE_LIBS=$(obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/net" "$1")
    PACKAGES_CNT=$(echo "$ALL_PACKAGE_LIBS" | wc -l)
    echo "$ALL_PACKAGE_LIBS" | tail -$(("$PACKAGES_CNT"-"$PACKAGES_CNT"/2))
}
function OFFICIAL_PACKAGES_UTILS {
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/utils" "$1"
}
function OFFICIAL_PACKAGES_OTHER {
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/admin" "$1"
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/devel" "$1"
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/ipv6" "$1"
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/mail" "$1"
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/sound" "$1"
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/multimedia" "$1"
    echo "
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSerif-Italic=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSerifCondensed-Italic=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSerifCondensed-BoldItalic=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSerifCondensed-Bold=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSerifCondensed=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSerif-BoldItalic=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSerif-Bold=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSerif=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSans-Oblique=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSansMono-Oblique=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSansMono-BoldOblique=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSansMono-Bold=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSansMono=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSans-ExtraLight=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSansCondensed-Oblique=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSansCondensed-BoldOblique=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSansCondensed-Bold=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSansCondensed=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSans-BoldOblique=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSans-Bold=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuSans=$1
CONFIG_PACKAGE_dejavu-fonts-ttf-DejaVuMathTeXGyre=$1
"
}


function _scans_packages() {
    shopt -s globstar
    for i in "$1"/**/Makefile; do
        [[ $(cat "$i" | grep "rules.mk") == 'include $(TOPDIR)/rules.mk' ]] || continue # opkg Makefile must be contain 'rules.mk'
        DIR_NAME=$(dirname "$i")
        DIR_NAME="${DIR_NAME##*/}" # is directory name, is NOT path
        # echo "$i"
        grep '$(eval $(call BuildPackage,.*))' < "$i" | while IFS= read -r j ; do
            # echo "$j"
            PKG_NAME="${j#*,}"
            PKG_NAME="${PKG_NAME%%))}" # $(eval $(call BuildPackage,[PKG_NAME]))
            PKG_NAME="${PKG_NAME%%,*}" # [PKG_NAME],+zlib,+some_package...
            # echo "$PKG_NAME"
            if [[ "$PKG_NAME" == *'$(PKG_NAME)'* ]]; then
                REAL_NAME=$(cat "$i" | grep "PKG_NAME:=" | sed  's/^PKG_NAME:=//') # PKG_NAME:=[REAL_NAME]
                # echo "$REAL_NAME"
                PKG_NAME=${PKG_NAME//'$(PKG_NAME)'/$REAL_NAME}
            fi
            echo "$PKG_NAME"
            # break
        done
        if [[ $(cat "$i" | grep "luci.mk" | sed 's/^.*luci.mk/luci.mk/') == "luci.mk" ]];then
            echo "$DIR_NAME"
        fi
        # break;
    done
}

# $1: dir path
# $2: 'n','y','m'
function obtain_packages_conf() {
    if ! [ -d "$1" ]; then
        echo -e "#Dir '$1' not exist"
        return
    fi
    CONTENTS=$(_scans_packages "$1" | sort | sed "s/^/CONFIG_PACKAGE_/" | sed "s/$/=$2/")
    echo $'\n'"$CONTENTS"
}
