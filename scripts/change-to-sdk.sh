#!/bin/bash

if ( argsContains "--help" );then
    echo -e "
    --sdk     change to sdk directory (useful for SDK)[default is disable]"
fi

if ( argsContains "--sdk" );then
    SDK_PATH="${SOURCE_BASE_PATH}_sdk"
    [[ ! -d $SDK_PATH ]] && echo "no such directory ${SDK_PATH}" && exit 1
    cd $SDK_PATH
fi
