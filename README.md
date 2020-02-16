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
