#!/bin/bash

GLOBAL_ARGS="$@"

argsContains () {
    for item in $GLOBAL_ARGS
    do
        if [ "$item" == "$1" ] ; then
            return 0
        fi
    done
    return 1
}

if ( argsContains "--help" );then
    echo -e "Args:
    --only-deploy-feeds     only create feeds.conf[default is disable]
    ----------"
fi

if ( argsContains "--only-deploy-feeds" );then
    exit 0
fi
