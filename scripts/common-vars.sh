#!/bin/bash

function TARGET_X86_64 {
    echo "
CONFIG_TARGET_ath79=n
CONFIG_TARGET_x86=y
CONFIG_TARGET_x86_64=y

CONFIG_TARGET_ROOTFS_CPIOGZ=n
CONFIG_TARGET_ROOTFS_TARGZ=n
CONFIG_TARGET_ROOTFS_EXT4FS=y
CONFIG_TARGET_ROOTFS_SQUASHFS=y
CONFIG_ISO_IMAGES=y
CONFIG_VDI_IMAGES=y
CONFIG_VMDK_IMAGES=y
CONFIG_TARGET_IMAGES_GZIP=y
CONFIG_TARGET_KERNEL_PARTSIZE=32
CONFIG_TARGET_ROOTFS_PARTSIZE=512
"
}

function TARGET_RAMIPS_MT7621 {
echo "
CONFIG_TARGET_ramips=y
CONFIG_TARGET_ramips_mt7621=y
CONFIG_TARGET_MULTI_PROFILE=y
CONFIG_TARGET_ALL_PROFILES=y
CONFIG_TARGET_PER_DEVICE_ROOTFS=n
CONFIG_TARGET_DEVICE_ramips_mt7621_DEVICE_buffalo_wsr-2533dhpl=n
CONFIG_KERNEL_CC_OPTIMIZE_FOR_PERFORMANCE=n
CONFIG_KERNEL_CC_OPTIMIZE_FOR_SIZE=y
"
}

function TARGET_ipq40xx_generic {
echo "
CONFIG_TARGET_ipq40xx=y
CONFIG_TARGET_ipq40xx_generic=y
CONFIG_TARGET_MULTI_PROFILE=y
CONFIG_TARGET_ALL_PROFILES=y
CONFIG_TARGET_PER_DEVICE_ROOTFS=n
"
}

function TARGET_bcm27xx_bcm2709 {
echo "
CONFIG_TARGET_bcm27xx=y
CONFIG_TARGET_bcm27xx_bcm2709=y
CONFIG_TARGET_bcm27xx_bcm2709_DEVICE_rpi-2=y
"
}
function GENERAL_SETTING {
    echo "
CONFIG_DEVEL=y
CONFIG_BUILD_LOG=y
CONFIG_CCACHE=y
CONFIG_TOOLCHAINOPTS=y
CONFIG_GDB=n
"
}

function GEN_SDK_IB {
    echo "
CONFIG_ALL_KMODS=y
CONFIG_IB=$1
CONFIG_SDK=$1
"
}

function SAVE_SPACE {
    echo "CONFIG_BUILDBOT=$1"
}

function CTCGFW_PACKAGES {
    echo "# ${FUNCNAME[0]}"
    obtain_packages_conf "$SOURCE_ORIGIN_PATH/package/ctcgfw" "$1"
    echo "CONFIG_PACKAGE_cups-bjnp=n
CONFIG_PACKAGE_cups=n
CONFIG_PACKAGE_luci-app-ssr-plus-Jo_INCLUDE_Kcptun=y
CONFIG_PACKAGE_luci-app-diskman_INCLUDE_btrfs_progs=y
CONFIG_PACKAGE_luci-app-diskman_INCLUDE_lsblk=y
CONFIG_PACKAGE_luci-app-diskman_INCLUDE_mdadm=y
CONFIG_PACKAGE_luci-app-diskman_INCLUDE_kmod_md_raid456=y
CONFIG_PACKAGE_luci-app-diskman_INCLUDE_kmod_md_linear=y
CONFIG_PACKAGE_luci-app-vssr_INCLUDE_microsocks=y
CONFIG_PACKAGE_luci-app-vssr_INCLUDE_dns2socks=y
CONFIG_PACKAGE_luci-app-vssr_INCLUDE_haproxy=y
CONFIG_PACKAGE_luci-app-vssr_INCLUDE_GoQuiet-client=y
CONFIG_PACKAGE_luci-app-vssr_INCLUDE_GoQuiet-server=y
"
}
function LEAN_PACKAGES {
    echo "# ${FUNCNAME[0]}"
    obtain_packages_conf "$SOURCE_ORIGIN_PATH/package/lean" "$1"
    echo "CONFIG_PACKAGE_kcptun-client=$1
CONFIG_PACKAGE_kcptun-server=$1
PACKAGE_luci-app-ssr-plus_INCLUDE_Kcptun=y
"
}
function LIENOL_ZXLHHYCCC_NTLF9T_PACKAGES {
    echo "# ${FUNCNAME[0]}"
    obtain_packages_conf "$SOURCE_ORIGIN_PATH/package/ntlf9t" "$1"
    obtain_packages_conf "$SOURCE_ORIGIN_PATH/package/lienol" "$1"
    obtain_packages_conf "$SOURCE_ORIGIN_PATH/package/zxlhhyccc" "$1"
    echo "CONFIG_PACKAGE_luci-app-passwall_INCLUDE_Shadowsocks=y
CONFIG_PACKAGE_luci-app-passwall_INCLUDE_Shadowsocks_socks=y
CONFIG_PACKAGE_luci-app-passwall_INCLUDE_ShadowsocksR_socks=y
CONFIG_PACKAGE_luci-app-passwall_INCLUDE_Trojan=y
CONFIG_PACKAGE_luci-app-passwall_INCLUDE_Brook=y
CONFIG_PACKAGE_luci-app-passwall_INCLUDE_kcptun=y
CONFIG_PACKAGE_luci-app-passwall_INCLUDE_v2ray-plugin=y
CONFIG_PACKAGE_luci-app-passwall_INCLUDE_simple-obfs=y
"
}
function FIRMWARE_PACKAGES {
    echo "# ${FUNCNAME[0]}"
    obtain_packages_conf "$SOURCE_BASE_PATH/package/firmware" "$1"
}

function OFFICIAL_LUCI_APP {
    echo "# ${FUNCNAME[0]}"
    obtain_packages_conf "$SOURCE_BASE_PATH/package/feeds/luci" "$1"
}
function PHP7_CONF {
    PHP7_MODULES=(
        bcmath calendar ctype curl dom exif fileinfo filter ftp gettext gd gmp
        iconv imap intl json ldap mbstring mysqli mysqlnd opcache openssl pcntl pdo pdo-mysql pdo-pgsql pdo-sqlite pgsql phar
        session shmop simplexml snmp soap sockets sqlite3 sysvmsg sysvsem sysvshm tokenizer xml xmlreader xmlwriter zip
    )
    for PHP7_MOD_NAME in ${PHP7_MODULES[*]}; do
        echo "CONFIG_PACKAGE_php7-mod-$PHP7_MOD_NAME=$1"
    done
    echo "CONFIG_PHP7_FULLICUDATA=y"
}
function OFFICIAL_PACKAGES_LANG {
    echo "# ${FUNCNAME[0]}"
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/lang" "$1"
    obtain_packages_conf_from_file "$SOURCE_BASE_PATH/feeds/packages/lang/perl/perlbase.mk" "$1"
    PHP7_CONF "$1"
    echo "
CONFIG_PACKAGE_php7-pecl-dio=$1
CONFIG_PACKAGE_php7-pecl-libevent=$1
"
}
function OFFICIAL_PACKAGES_LIB_1 {
    # 0-50%
    echo "# ${FUNCNAME[0]}"
    ALL_PACKAGE_LIBS=$(obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/libs" "$1")
    PACKAGES_CNT=$(echo "$ALL_PACKAGE_LIBS" | wc -l)
    echo "$ALL_PACKAGE_LIBS" | head -$(("$PACKAGES_CNT"/2))
    echo "
# no maintainer
CONFIG_PACKAGE_classpath=n

"
}
function OFFICIAL_PACKAGES_LIB_2 {
    echo "# ${FUNCNAME[0]}"
    # 50%-75%
    ALL_PACKAGE_LIBS=$(obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/libs" "$1")
    PACKAGES_CNT=$(echo "$ALL_PACKAGE_LIBS" | wc -l)
    ALL_PACKAGE_LIBS=$(echo "$ALL_PACKAGE_LIBS" | tail -$(("$PACKAGES_CNT"-"$PACKAGES_CNT"/2)))
    PACKAGES_CNT=$(echo "$ALL_PACKAGE_LIBS" | wc -l)
    echo "$ALL_PACKAGE_LIBS" | head -$(("$PACKAGES_CNT"/2))
}
function OFFICIAL_PACKAGES_LIB_3 {
    echo "# ${FUNCNAME[0]}"
    # 75%-100%
    ALL_PACKAGE_LIBS=$(obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/libs" "$1")
    PACKAGES_CNT=$(echo "$ALL_PACKAGE_LIBS" | wc -l)
    ALL_PACKAGE_LIBS=$(echo "$ALL_PACKAGE_LIBS" | tail -$(("$PACKAGES_CNT"-"$PACKAGES_CNT"/2)))
    PACKAGES_CNT=$(echo "$ALL_PACKAGE_LIBS" | wc -l)
    echo "$ALL_PACKAGE_LIBS" | tail -$(("$PACKAGES_CNT"-"$PACKAGES_CNT"/2))
    LIBEXTRACTOR_PLUGINS=(
        archive deb dvi flac gif gstreamer it jpeg man mime mpeg
        nsf nsfe odf ogg png ps riff s3m sid thumbnailffmpeg tiff wav xm zip
    )
    for PLUGIN_NAME in ${LIBEXTRACTOR_PLUGINS[*]}; do
        echo "CONFIG_PACKAGE_libextractor-plugin-$PLUGIN_NAME=$1"
    done
    echo "
# no maintainer
CONFIG_PACKAGE_rxtx=n

"
}
function OFFICIAL_PACKAGES_NET_1 {
    echo "# ${FUNCNAME[0]}"
    # 0-50%
    ALL_PACKAGE_LIBS=$(obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/net" "$1")
    PACKAGES_CNT=$(echo "$ALL_PACKAGE_LIBS" | wc -l)
    echo "$ALL_PACKAGE_LIBS" | head -$(("$PACKAGES_CNT"/2))
}
function OFFICIAL_PACKAGES_NET_2 {
    echo "# ${FUNCNAME[0]}"
    # 50-100%
    ALL_PACKAGE_LIBS=$(obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/net" "$1")
    PACKAGES_CNT=$(echo "$ALL_PACKAGE_LIBS" | wc -l)
    echo "$ALL_PACKAGE_LIBS" | tail -$(("$PACKAGES_CNT"-"$PACKAGES_CNT"/2))
}
function OFFICIAL_PACKAGES_UTILS {
    echo "# ${FUNCNAME[0]}"
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/utils" "$1"
    PHP7_CONF "$1"
}
function OFFICIAL_PACKAGES_OTHER {
    echo "# ${FUNCNAME[0]}"
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/admin" "$1"
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/devel" "$1"
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/ipv6" "$1"
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/mail" "$1"
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/sound" "$1"
    obtain_packages_conf "$SOURCE_BASE_PATH/feeds/packages/multimedia" "$1"
    DEJAVU_FONTS=(
        DejaVuSerif-Italic DejaVuSerifCondensed-Italic DejaVuSerifCondensed-BoldItalic DejaVuSerifCondensed-Bold DejaVuSerifCondensed
        DejaVuSerif-BoldItalic DejaVuSerif-Bold DejaVuSerif DejaVuSans-Oblique DejaVuSansMono-Oblique DejaVuSansMono-BoldOblique
        DejaVuSansMono-Bold DejaVuSansMono DejaVuSans-ExtraLight DejaVuSansCondensed-Oblique DejaVuSansCondensed-BoldOblique
        DejaVuSansCondensed-Bold DejaVuSansCondensed DejaVuSans-BoldOblique DejaVuSans-Bold DejaVuSans DejaVuMathTeXGyre
    )
    for FONT_NAME in ${DEJAVU_FONTS[*]}; do
        echo "CONFIG_PACKAGE_dejavu-fonts-ttf-$FONT_NAME=$1"
    done
    PHP7_CONF "$1"
}


function _scans_packages_from_file(){
    grep '$(eval $(call BuildPackage,.*))' < "$1" | while IFS= read -r j ; do
        # echo "$j"
        PKG_NAME="${j#*,}"
        PKG_NAME="${PKG_NAME%%))}" # $(eval $(call BuildPackage,[PKG_NAME]))
        PKG_NAME="${PKG_NAME%%,*}" # [PKG_NAME],+zlib,+some_package...
        # echo "$PKG_NAME"
        if [[ "$PKG_NAME" == *'$(PKG_NAME)'* ]]; then
            REAL_NAME=$(cat "$1" | grep "PKG_NAME:=" | sed  's/^PKG_NAME:=//') # PKG_NAME:=[REAL_NAME]
            # echo "$REAL_NAME"
            PKG_NAME=${PKG_NAME//'$(PKG_NAME)'/$REAL_NAME}
        fi
        echo "$PKG_NAME"
        # break
    done
}

function _scans_packages() {
    shopt -s globstar
    for i in "$1"/**/Makefile; do
        [[ $(cat "$i" | grep "rules.mk") == 'include $(TOPDIR)/rules.mk' ]] || continue # opkg Makefile must be contain 'rules.mk'
        DIR_NAME=$(dirname "$i")
        DIR_NAME="${DIR_NAME##*/}" # is directory name, is NOT path
        # echo "$i"
        _scans_packages_from_file "$i"
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

# $1: file path
# $2: 'n','y','m'
function obtain_packages_conf_from_file() {
    if ! [ -f "$1" ]; then
        echo -e "#File '$1' not exist"
        return
    fi
    CONTENTS=$(_scans_packages_from_file "$1" | sort | sed "s/^/CONFIG_PACKAGE_/" | sed "s/$/=$2/")
    echo $'\n'"$CONTENTS"
}
