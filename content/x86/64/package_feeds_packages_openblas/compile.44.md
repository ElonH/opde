---
title: "compile.44"
date: 2021-08-01 09:47:06.122922
hidden: false
draft: false
weight: -44
---

build number: `44`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/openblas/compile -j$(nproc) || make package/feeds/packages/openblas/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/OpenBLAS-0.3.15'
/openwrt/staging_dir/host/bin/ccache: invalid option -- 'D'
Usage:
    ccache [options]
    ccache compiler [compiler options]
    compiler [compiler options]          (via symbolic link)

Common options:
    -c, --cleanup              delete old files and recalculate size counters
                               (normally not needed as this is done
                               automatically)
    -C, --clear                clear the cache completely (except configuration)
        --config-path PATH     operate on configuration file PATH instead of the
                               default
    -d, --directory PATH       operate on cache directory PATH instead of the
                               default
        --evict-older-than AGE remove files older than AGE (unsigned integer
                               with a d (days) or s (seconds) suffix)
    -F, --max-files NUM        set maximum number of files in cache to NUM (use
                               0 for no limit)
    -M, --max-size SIZE        set maximum size of cache to SIZE (use 0 for no
                               limit); available suffixes: k, M, G, T (decimal)
                               and Ki, Mi, Gi, Ti (binary); default suffix: G
    -X, --recompress LEVEL     recompress the cache to level LEVEL (integer or
                               "uncompressed") using the Zstandard algorithm;
                               see "Cache compression" in the manual for details
    -o, --set-config KEY=VAL   set configuration item KEY to value VAL
    -x, --show-compression     show compression statistics
    -p, --show-config          show current configuration options in
                               human-readable format
    -s, --show-stats           show summary of configuration and statistics
                               counters in human-readable format
    -z, --zero-stats           zero statistics counters

    -h, --help                 print this help text
    -V, --version              print version and copyright information

Options for scripting or debugging:
        --checksum-file PATH   print the checksum (64 bit XXH3) of the file at
                               PATH
        --dump-manifest PATH   dump manifest file at PATH in text format
        --dump-result PATH     dump result file at PATH in text format
        --extract-result PATH  extract data stored in result file at PATH to the
                               current working directory
    -k, --get-config KEY       print the value of configuration key KEY
        --hash-file PATH       print the hash (160 bit BLAKE3) of the file at
                               PATH
        --print-stats          print statistics counter IDs and corresponding
                               values in machine-parsable format

See also the manual on <https://ccache.dev/documentation.html>.
make[4]: *** [Makefile.prebuild:70: getarch] Error 1
Makefile.system:255: Makefile.conf: No such file or directory
make[4]: *** No rule to make target 'Makefile.conf'.  Stop.
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/OpenBLAS-0.3.15'
make[3]: *** [Makefile:109: /openwrt/build_dir/target-x86_64_musl/OpenBLAS-0.3.15/.built] Error 2
```
