## Usage:

1. download compiled firmware from [release](https://github.com/ElonH/BuildOpenWRT/releases) and burn it into the router(required 512M+32M space).
2. ssh the router
3. run command to active ootoc
    ``` bash
    bash <(wget -qO- https://cdn.jsdelivr.net/gh/ElonH/BuildOpenWRT@master/feeds/scripts/update-by-ootoc.sh) xxx
    ```
    > Note: `xxx` given in release note

    `ootoc` as an agent, providing OpenWrt packages in the remote tar file.
4. watch log file `tail -f /var/log/ootoc` and wait ootoc deployment done.

    For example: [snapshot](https://github.com/ElonH/BuildOpenWRT/releases/tag/snapshot)
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
    <details>
    <summary>Proxy</summary>
    <code>ootoc</code> can use proxy to fetch data.
    
    <pre>
    uci show ootoc # show ootoc configuration
    uci set ootoc.proxy.enabled='1'
    uci set ootoc.proxy.proxy_addr='socks5://[proxy ip]:[port]'
    uci commit
    /etc/init.d/ootoc restart
    </pre>
    </details>

5. run `opkg update`
6. run `opkg install [favourite package]`

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
