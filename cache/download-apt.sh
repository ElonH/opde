#!/bin/bash
SCRIPT_ABS_PATH="$(cd $(dirname "$0"); pwd)"

echoerr() { echo "$@" 1>&2; }
exiterr() { echoerr "$@" ; exit 1; }

# $1: download dir
# $2: apt names list

DOWNLOAD_APT_DIR="$SCRIPT_ABS_PATH/apt"
# DOWNLOAD_APT_DIR="$1"

mkdir -p "$DOWNLOAD_APT_DIR" 2>/dev/null
cd "$DOWNLOAD_APT_DIR" || exit 0

INSTALL_PACKS=(
	build-essential asciidoc binutils bzip2 gawk gettext git libncurses5-dev patch unzip zlib1g-dev lib32gcc1 libc6-dev-i386 subversion flex git
	gcc-8 gcc-8-multilib g++-8-multilib p7zip p7zip-full msmtp libssl-dev texinfo libreadline-dev libglib2.0-dev xmlto qemu-utils upx-ucl libelf-dev
	autoconf automake libtool autopoint ccache curl wget python python3 python-pip python3-pip python-ply python3-ply haveged lrzsz device-tree-compiler
	cmake libcurl4-openssl-dev libncursesw5-dev xsltproc genisoimage python3-pycurl zlib1g-dev perl-base node-uglify default-jdk
	antlr3 gperf ecj fastjar)
# INSTALL_PACKS=($2)

ALL_PACKAGES=$(apt-rdepends ${INSTALL_PACKS[*]} | grep -v "^ " | sort)
#  | grep -v "^c-compiler$" | grep -v "^libc-dev$" | grep -v "^debconf-2.0$" | grep -v "^libz-dev$" | grep -v "perlapi-5.26.1$" | grep -v "^uglifyjs$" | grep -v "^vim$" | grep -v "^vim-runtime$")

mapfile -t ALL_PACKAGES <<< "$ALL_PACKAGES"

for item in ${ALL_PACKAGES[*]} ; do
	echo "downloading: $item"
	apt-get download "$item"
	echo ""
	# break
done
