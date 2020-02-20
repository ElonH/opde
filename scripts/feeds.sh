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

show_help () {
    echo -e "
    -i          interactive mode
    --help      show this message
    ----------
    --feeds     update and install feeds[default is disable]
    "
}

if ( argsContains "--help" );then
    show_help
    exit 1
fi

if ( argsContains "--feeds" );then
    SKIP_FEEDS="n"
else
    SKIP_FEEDS="y"
fi

if ( argsContains "-i" );then
    read -e -p "Skip feeds update and install: [Y/n]" SKIP_FEEDS
    SKIP_FEEDS="${SKIP_FEEDS:-y}"
fi

case $SKIP_FEEDS in
    "y"|"Y")
    ;;
    "n"|"N")
        ./scripts/feeds update -a && ./scripts/feeds install -a
    ;;
    *)
        echo -e "Skip Feeds unknow"
        exit 1
    ;;
esac
