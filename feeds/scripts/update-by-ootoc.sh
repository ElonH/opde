#!/bin/bash

uci set ootoc.global.enabled='1'
uci set ootoc.server.tar_url="https://github.com/ElonH/BuildOpenWRT/releases/download/$1/latest-Packages-$1.tar"
uci set ootoc.server.aux_url="https://github.com/ElonH/BuildOpenWRT/releases/download/$1/latest-Packages-$1.yml"
uci commit
/etc/init.d/ootoc enable
/etc/init.d/ootoc restart
# tail -f /var/log/ootoc
exit 0
