#!/bin/bash

echoerr() { echo "$@" 1>&2; }
exiterr() { echoerr "$@" ; exit 1; }

# variable check if exist
function check_var_not_set() {
	if [[ -v $1 ]]; then
		# echo "[info]: $1 = ${!1}"
		return 0
	else
		echoerr "[ERROR]: Variable '$1' is not defined"
		exit 1
	fi
}

check_var_not_set SCRIPT_ABS_PATH
check_var_not_set SOURCE_NAME
check_var_not_set FEEDS_CONF
check_var_not_set BASE_PACK_CONF
check_var_not_set USER_PACK_CONF

# internal variable
SOURCE_BASE_PATH="$SCRIPT_ABS_PATH/$SOURCE_NAME"
GLOBAL_ARGS="$@"
PACK_CONF=""
BUILD_SDK_PACK_CONF=""

# args check
argsContains () {
	for item in $GLOBAL_ARGS
	do
		if [ "$item" == "$1" ] ; then
			return 0
		fi
	done
	return 1
}

if (argsContains "--sdk" ) && (argsContains "--build-sdk"); then
	exiterr "You can't select both --build-sdk and --sdk"
fi

# main program
if ( argsContains "--help" );then
	echo -e "Args:
	--sdk			add base feeds (useful for SDK)[default is disable]
					change to sdk directory (useful for SDK)[default is disable]
					sdk configure head (useful for SDK)[default is disable]
	--feeds			update and install feeds[default is disable]
	--build-sdk		disable extra default package (useful for build SDK)[default is disable]
					do not add addon packages (useful for build SDK)[default is disable]
	"
	exit 0
fi


if ( argsContains "--sdk" );then
    SOURCE_BASE_PATH="${SOURCE_BASE_PATH}_sdk"
fi
cd "$SOURCE_BASE_PATH" || exiterr "path '$SOURCE_BASE_PATH' not exist"

# add base feeds (only for SDK)
if ( argsContains "--sdk" );then
	FEEDS_CONF+="
src-link base $SOURCE_BASE_PATH
"
fi
echo "${FEEDS_CONF}">feeds.conf


if ( argsContains "--feeds" );then
    ./scripts/feeds update -a && ./scripts/feeds install -a
fi

if ( argsContains "--build-sdk" );then
    BUILD_SDK_PACK_CONF="
CONFIG_ALL_KMODS=y
$(GEN_SDK_IB y)
$(DEFAULT_EXTRA_PACKAGE n)
"
else
	BUILD_SDK_PACK_CONF="
$USER_PACK_CONF
"
fi


if ( argsContains "--sdk" );then
    SDK_PACK_CONF="
CONFIG_ALL_NONSHARED=n
CONFIG_ALL_KMODS=n
CONFIG_ALL=n
CONFIG_CCACHE=y
$USER_PACK_CONF
"
fi

PACK_CONF+="$BASE_PACK_CONF $BUILD_SDK_PACK_CONF $SDK_PACK_CONF"

echo "${PACK_CONF}"
echo "${PACK_CONF}">.config
make defconfig
