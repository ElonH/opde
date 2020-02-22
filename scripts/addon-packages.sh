#!/bin/bash

if ( argsContains "--help" );then
    echo -e "
    --build-sdk     do not add addon packages (useful for build SDK)[default is disable]"
fi


if ( argsContains "--build-sdk" );then
    CONFIG_CONTS+=""
else
    CONFIG_CONTS+=${ADDON_CONFIG_CONTS}
fi
