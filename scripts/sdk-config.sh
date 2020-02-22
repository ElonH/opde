#!/bin/bash

if ( argsContains "--help" );then
    echo -e "
    --sdk     sdk configure head (useful for SDK)[default is disable]"
fi

if ( argsContains "--sdk" );then
    CONFIG_CONTS="
CONFIG_ALL_NONSHARED=n
CONFIG_ALL_KMODS=n
CONFIG_ALL=n
CONFIG_BUILD_LOG=y
CONFIG_CCACHE=y
"
fi
