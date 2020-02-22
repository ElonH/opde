#!/bin/bash

if ( argsContains "--help" );then
    echo -e "
    --build-sdk     disable extra default package (useful for build SDK)[default is disable]"
fi

if ( argsContains "--build-sdk" );then
    CONFIG_CONTS+="
$(GEN_SDK_IB y)
$(DEFAULT_EXTRA_PACKAGE n)
"
fi
