#!/bin/bash

if ( argsContains "--help" );then
    echo -e "Args:
    --sdk     add base feeds (useful for SDK)[default is disable]"
fi


if ( argsContains "--sdk" );then
    FEEDS_CONF+="
src-link base $SOURCE_BASE_PATH
"
fi
