#!/bin/bash

sed -i "s/^[ ]*option check_signature/# option check_signaturesign/" /etc/opkg.conf

if [[ "jsdelivr" == $1 ]]; then
	echo "
src/gz luci https://cdn.jsdelivr.net/gh/ElonH/BuildOpenWRT@snapshot/latest-Packages/packages/x86_64/luci
src/gz routing https://cdn.jsdelivr.net/gh/ElonH/BuildOpenWRT@snapshot/latest-Packages/packages/x86_64/routing
src/gz base https://cdn.jsdelivr.net/gh/ElonH/BuildOpenWRT@snapshot/latest-Packages/packages/x86_64/base
src/gz packages https://cdn.jsdelivr.net/gh/ElonH/BuildOpenWRT@snapshot/latest-Packages/packages/x86_64/packages
src/gz telephony https://cdn.jsdelivr.net/gh/ElonH/BuildOpenWRT@snapshot/latest-Packages/packages/x86_64/telephony
src/gz targets https://cdn.jsdelivr.net/gh/ElonH/BuildOpenWRT@snapshot/latest-Packages/targets/x86/64/packages
	" > /etc/opkg/distfeeds.conf
elif [[ "githack" == $1 ]]; then
	echo "
src/gz luci https://rawcdn.githack.com/ElonH/BuildOpenWRT/snapshot/latest-Packages/packages/x86_64/luci
src/gz routing https://rawcdn.githack.com/ElonH/BuildOpenWRT/snapshot/latest-Packages/packages/x86_64/routing
src/gz base https://rawcdn.githack.com/ElonH/BuildOpenWRT/snapshot/latest-Packages/packages/x86_64/base
src/gz packages https://rawcdn.githack.com/ElonH/BuildOpenWRT/snapshot/latest-Packages/packages/x86_64/packages
src/gz telephony https://rawcdn.githack.com/ElonH/BuildOpenWRT/snapshot/latest-Packages/packages/x86_64/telephony
src/gz targets https://rawcdn.githack.com/ElonH/BuildOpenWRT/snapshot/latest-Packages/targets/x86/64/packages
	" > /etc/opkg/distfeeds.conf
else
#elif [[ "github" == $1 ]]; then
	echo "
src/gz luci https://raw.githubusercontent.com/ElonH/BuildOpenWRT/snapshot/latest-Packages/packages/x86_64/luci
src/gz routing https://raw.githubusercontent.com/ElonH/BuildOpenWRT/snapshot/latest-Packages/packages/x86_64/routing
src/gz base https://raw.githubusercontent.com/ElonH/BuildOpenWRT/snapshot/latest-Packages/packages/x86_64/base
src/gz packages https://raw.githubusercontent.com/ElonH/BuildOpenWRT/snapshot/latest-Packages/packages/x86_64/packages
src/gz telephony https://raw.githubusercontent.com/ElonH/BuildOpenWRT/snapshot/latest-Packages/packages/x86_64/telephony
src/gz targets https://raw.githubusercontent.com/ElonH/BuildOpenWRT/snapshot/latest-Packages/targets/x86/64/packages
	" > /etc/opkg/distfeeds.conf
fi

exit 0
