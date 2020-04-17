#!/bin/bash
# $1: repo, eg: 'ElonH/opde'
# $2: source, 'latest' or 'ctcgfw'
# $3: version tag, the tag in release (eg: v20.03.1 etc.)
uci set ootoc.global.enabled='1'
OOTOC_URL="https://github.com/$1/releases/download"
uci set ootoc.server.tar_url="$OOTOC_URL/$3/$2-Packages-$3.tar"
uci set ootoc.server.aux_url="$OOTOC_URL/$3/$2-Packages-$3.yml"
uci commit
/etc/init.d/ootoc enable
/etc/init.d/ootoc restart
uci show ootoc
# tail -f /var/log/ootoc
exit 0
