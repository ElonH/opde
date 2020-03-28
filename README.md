# OPDE
OpenWrt Development Environment

## Intro
- using git submodule to update feeds and packages
- automate compile and release firmware on action

## Consumer Usage:

### Basic
1. download compiled firmware from [release](https://github.com/ElonH/BuildOpenWRT/releases) and burn it into the router(required 512M+32M space).
2. ssh the router
3. run command to active `ootoc`

    `ootoc` as an agent, providing OpenWrt packages in the remote tar file.
    ``` bash
    bash <(wget -qO- https://cdn.jsdelivr.net/gh/ElonH/BuildOpenWRT@master/feeds/scripts/activate-ootoc.sh) [source] [version tag]
    ```
    > Note:  
    > [source]-Firmware-[version tag].tar is your downloaded firmware.  
    > source: 'latest' or 'ctcgfw'.  
    > version tag: the tag in release (eg: snapshot, v20.03.1 etc.)

4. watch log file `tail -f /var/log/ootoc` and wait ootoc deployment done.

    For example: [latest-snapshot](https://github.com/ElonH/BuildOpenWRT/releases/tag/snapshot)
    ```
    [ootoc] [14:17:57.080] [8913] [debug] auxilary file downloaded: 451063+1048
    [ootoc] [14:17:57.080] [8913] [debug] auxilary file downloaded: 452111+5406
    [ootoc] [14:17:57.080] [8913] [info] fetching range success: https://github.com/ElonH/BuildOpenWRT/releases/download/snapshot/latest-Packages-snapshot.yml
    [ootoc] [14:17:57.080] [8913] [info] auxilary file download completed
    [ootoc] [14:17:57.080] [8913] [info] auxilary file size: 457517
    [ootoc] [14:17:57.791] [8913] [info] subscription: save content to '/etc/opkg/distfeeds.conf'
    src/gz 1 http://127.0.0.1:21730/latest-Packages/targets/x86/64/packages
    src/gz 2 http://127.0.0.1:21730/latest-Packages/packages/x86_64/telephony
    src/gz 3 http://127.0.0.1:21730/latest-Packages/packages/x86_64/base
    src/gz 4 http://127.0.0.1:21730/latest-Packages/packages/x86_64/luci
    src/gz 5 http://127.0.0.1:21730/latest-Packages/packages/x86_64/packages
    src/gz 6 http://127.0.0.1:21730/latest-Packages/packages/x86_64/routing

    [ootoc] [14:17:57.791] [8913] [debug] Deploying server.
    [ootoc] [14:17:57.791] [8913] [info] Deploy done.                                                             <=======here
    ```
    Proxy

    `ootoc` can use proxy to fetch data.
    ``` bash
    uci set ootoc.proxy.enabled='1'
    uci set ootoc.proxy.proxy_addr='socks5://[proxy ip]:[port]'
    uci commit
    uci show ootoc # show ootoc configuration
    /etc/init.d/ootoc restart
    ```

5. run `opkg update`
6. run `opkg install [favourite package]` or use luci to install favourite packages **(4000+)**.
    ![luci-app-opkg](asset/luci-app-opkg.png)
    > Tips: if installing packages take a long time and still no result, check whether is network problem via log file `tail -f /var/log/ootoc`

### Advance Usage
#### SDK compile

- without building the whole openwrt.
- build newer version packages
- build private packages.
- ...

Note: shouldn't use SDK to build kernel packages.

TODO: a document that how to setup SDK environment

#### TODO: ImageBuilder


## Configure OpenWrt Compile

### init

```bash
git clone https://github.com/ElonH/BuildOpenWRT.git --recursive
cd BuildOpenWRT

./build-official.sh --feeds
# or ./build-lede.sh --feeds
# or ./build-ctcgfw.sh --feeds
# or ./build-latest.sh --feeds
```

### sync

``` bash
git pull
git submodule update
```
