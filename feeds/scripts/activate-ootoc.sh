#!/bin/bash
# $1: source, 'latest' or 'ctcgfw'
# $2: version tag, the tag in release (eg: v20.03.1 etc.)
uci set ootoc.global.enabled='1'
OOTOC_URL="https://github.com/ElonH/BuildOpenWRT/releases/download"
uci set ootoc.server.tar_url="$OOTOC_URL/$2/$1-Packages-$2.tar"
uci set ootoc.server.aux_url="$OOTOC_URL/$2/$1-Packages-$2.yml"
uci commit
/etc/init.d/ootoc enable
/etc/init.d/ootoc restart
uci show ootoc
# tail -f /var/log/ootoc
exit 0
