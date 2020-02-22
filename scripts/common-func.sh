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
