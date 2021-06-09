---
title: "compile.30"
date: 2021-06-09 21:52:39.407952
hidden: false
draft: false
weight: -30
---

build number: `30`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/node-red/compile -j$(nproc) || make package/feeds/packages/node-red/compile V=s
```

#### Compile.txt

``` bash
npm info it worked if it ends with ok
npm info using npm@6.14.13
npm info using node@v14.17.0
npm info lifecycle node-red@1.3.5~preinstall: node-red@1.3.5
npm timing stage:loadCurrentTree Completed in 11ms
npm timing stage:loadIdealTree:cloneCurrentTree Completed in 1ms
npm timing stage:loadIdealTree:loadShrinkwrap Completed in 1ms
npm http fetch GET 200 https://registry.npmjs.org/basic-auth 221ms
npm http fetch GET 200 https://registry.npmjs.org/@node-red%2feditor-api 227ms
npm http fetch GET 200 https://registry.npmjs.org/node-red-admin 218ms
npm http fetch GET 200 https://registry.npmjs.org/express 224ms
npm http fetch GET 200 https://registry.npmjs.org/node-red-node-rbe 227ms
npm http fetch GET 200 https://registry.npmjs.org/fs-extra 254ms
npm http fetch GET 200 https://registry.npmjs.org/bcryptjs 262ms
npm http fetch GET 200 https://registry.npmjs.org/basic-auth/-/basic-auth-2.0.1.tgz 151ms
npm http fetch GET 200 https://registry.npmjs.org/fs-extra/-/fs-extra-8.1.0.tgz 124ms
npm http fetch GET 200 https://registry.npmjs.org/@node-red%2fruntime 394ms
npm http fetch GET 200 https://registry.npmjs.org/express/-/express-4.17.1.tgz 131ms
npm http fetch GET 200 https://registry.npmjs.org/node-red-node-rbe/-/node-red-node-rbe-0.5.0.tgz 135ms
npm http fetch GET 200 https://registry.npmjs.org/node-red-admin/-/node-red-admin-0.2.7.tgz 159ms
npm http fetch GET 200 https://registry.npmjs.org/bcryptjs/-/bcryptjs-2.4.3.tgz 132ms
npm http fetch GET 200 https://registry.npmjs.org/@node-red/runtime/-/runtime-1.3.5.tgz 90ms
npm http fetch GET 200 https://registry.npmjs.org/accepts 69ms
npm http fetch GET 200 https://registry.npmjs.org/semver 82ms
npm http fetch GET 200 https://registry.npmjs.org/array-flatten 79ms
npm http fetch GET 200 https://registry.npmjs.org/body-parser 76ms
npm http fetch GET 200 https://registry.npmjs.org/node-red-node-tail 100ms
npm http fetch GET 200 https://registry.npmjs.org/nopt 101ms
npm http fetch GET 200 https://registry.npmjs.org/node-red-node-tail/-/node-red-node-tail-0.3.1.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/semver/-/semver-6.3.0.tgz 60ms
npm http fetch GET 200 https://registry.npmjs.org/accepts/-/accepts-1.3.7.tgz 63ms
npm http fetch GET 200 https://registry.npmjs.org/array-flatten/-/array-flatten-1.1.1.tgz 62ms
npm http fetch GET 200 https://registry.npmjs.org/body-parser/-/body-parser-1.19.0.tgz 67ms
npm http fetch GET 200 https://registry.npmjs.org/content-disposition 60ms
npm http fetch GET 200 https://registry.npmjs.org/nopt/-/nopt-5.0.0.tgz 75ms
npm http fetch GET 200 https://registry.npmjs.org/content-disposition/-/content-disposition-0.5.3.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/cookie-signature 37ms
npm http fetch GET 200 https://registry.npmjs.org/debug 37ms
npm http fetch GET 200 https://registry.npmjs.org/content-type 57ms
npm http fetch GET 200 https://registry.npmjs.org/depd 52ms
npm http fetch GET 200 https://registry.npmjs.org/cookie 61ms
npm http fetch GET 200 https://registry.npmjs.org/escape-html 35ms
npm http fetch GET 200 https://registry.npmjs.org/encodeurl 54ms
npm http fetch GET 200 https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.0.6.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/debug/-/debug-2.6.9.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/@node-red/editor-api/-/editor-api-1.3.5.tgz 449ms
npm http fetch GET 200 https://registry.npmjs.org/content-type/-/content-type-1.0.4.tgz 68ms
npm http fetch GET 200 https://registry.npmjs.org/depd/-/depd-1.1.2.tgz 68ms
npm http fetch GET 200 https://registry.npmjs.org/encodeurl/-/encodeurl-1.0.2.tgz 73ms
npm http fetch GET 200 https://registry.npmjs.org/cookie/-/cookie-0.4.0.tgz 76ms
npm http fetch GET 200 https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz 78ms
npm http fetch GET 200 https://registry.npmjs.org/finalhandler 33ms
npm http fetch GET 200 https://registry.npmjs.org/fresh 76ms
npm http fetch GET 200 https://registry.npmjs.org/parseurl 62ms
npm http fetch GET 200 https://registry.npmjs.org/etag 88ms
npm http fetch GET 200 https://registry.npmjs.org/on-finished 64ms
npm http fetch GET 200 https://registry.npmjs.org/finalhandler/-/finalhandler-1.1.2.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/methods 82ms
npm http fetch GET 200 https://registry.npmjs.org/path-to-regexp 77ms
npm http fetch GET 200 https://registry.npmjs.org/merge-descriptors 94ms
npm http fetch GET 200 https://registry.npmjs.org/fresh/-/fresh-0.5.2.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/parseurl/-/parseurl-1.3.3.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/methods/-/methods-1.1.2.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/on-finished/-/on-finished-2.3.0.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/etag/-/etag-1.8.1.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-0.1.7.tgz 66ms
npm http fetch GET 200 https://registry.npmjs.org/qs 48ms
npm http fetch GET 200 https://registry.npmjs.org/proxy-addr 64ms
npm http fetch GET 200 https://registry.npmjs.org/merge-descriptors/-/merge-descriptors-1.0.1.tgz 70ms
npm http fetch GET 200 https://registry.npmjs.org/@node-red%2futil 908ms
npm http fetch GET 200 https://registry.npmjs.org/serve-static 43ms
npm http fetch GET 200 https://registry.npmjs.org/range-parser 72ms
npm http fetch GET 200 https://registry.npmjs.org/proxy-addr/-/proxy-addr-2.0.7.tgz 68ms
npm http fetch GET 200 https://registry.npmjs.org/send 79ms
npm http fetch GET 200 https://registry.npmjs.org/safe-buffer 93ms
npm http fetch GET 200 https://registry.npmjs.org/statuses 67ms
npm http fetch GET 200 https://registry.npmjs.org/setprototypeof 69ms
npm http fetch GET 200 https://registry.npmjs.org/qs/-/qs-6.7.0.tgz 94ms
npm http fetch GET 200 https://registry.npmjs.org/serve-static/-/serve-static-1.14.1.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/send/-/send-0.17.1.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/range-parser/-/range-parser-1.2.1.tgz 46ms
npm http fetch GET 200 https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.1.1.tgz 73ms
npm http fetch GET 200 https://registry.npmjs.org/type-is 70ms
npm http fetch GET 200 https://registry.npmjs.org/vary 56ms
npm http fetch GET 200 https://registry.npmjs.org/utils-merge 66ms
npm http fetch GET 200 https://registry.npmjs.org/statuses/-/statuses-1.5.0.tgz 84ms
npm http fetch GET 200 https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz 91ms
npm http fetch GET 200 https://registry.npmjs.org/graceful-fs 53ms
npm http fetch GET 200 https://registry.npmjs.org/bcryptjs/-/bcryptjs-2.4.3.tgz 10ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/jsonfile 61ms
npm http fetch GET 200 https://registry.npmjs.org/type-is/-/type-is-1.6.18.tgz 64ms
npm http fetch GET 200 https://registry.npmjs.org/vary/-/vary-1.1.2.tgz 65ms
npm http fetch GET 200 https://registry.npmjs.org/utils-merge/-/utils-merge-1.0.1.tgz 65ms
npm http fetch GET 200 https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.6.tgz 60ms
npm http fetch GET 200 https://registry.npmjs.org/universalify 54ms
npm http fetch GET 200 https://registry.npmjs.org/axios 72ms
npm http fetch GET 200 https://registry.npmjs.org/jsonfile/-/jsonfile-4.0.0.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/cli-table 41ms
npm http fetch GET 200 https://registry.npmjs.org/universalify/-/universalify-0.1.2.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/minimist 37ms
npm http fetch GET 200 https://registry.npmjs.org/async-mutex 35ms
npm http fetch GET 200 https://registry.npmjs.org/read 78ms
npm http fetch GET 200 https://registry.npmjs.org/axios/-/axios-0.21.1.tgz 64ms
npm http fetch GET 200 https://registry.npmjs.org/cli-table/-/cli-table-0.3.6.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/clone 55ms
npm http fetch GET 200 https://registry.npmjs.org/minimist/-/minimist-1.2.5.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/async-mutex/-/async-mutex-0.3.1.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/json-stringify-safe 49ms
npm http fetch GET 200 https://registry.npmjs.org/clone/-/clone-2.1.2.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/negotiator 32ms
npm http fetch GET 200 https://registry.npmjs.org/mime-types 36ms
npm http fetch GET 200 https://registry.npmjs.org/read/-/read-1.0.7.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/tail 51ms
npm http fetch GET 200 https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz 61ms
npm http fetch GET 200 https://registry.npmjs.org/bytes 58ms
npm http fetch GET 200 https://registry.npmjs.org/negotiator/-/negotiator-0.6.2.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/http-errors 62ms
npm http fetch GET 200 https://registry.npmjs.org/mime-types/-/mime-types-2.1.31.tgz 78ms
npm http fetch GET 200 https://registry.npmjs.org/tail/-/tail-2.2.2.tgz 77ms
npm http fetch GET 200 https://registry.npmjs.org/iconv-lite 79ms
npm http fetch GET 200 https://registry.npmjs.org/@node-red%2fregistry 230ms
npm http fetch GET 200 https://registry.npmjs.org/raw-body 77ms
npm http fetch GET 200 https://registry.npmjs.org/@node-red/util/-/util-1.3.5.tgz 487ms
npm http fetch GET 200 https://registry.npmjs.org/bytes/-/bytes-3.1.0.tgz 93ms
npm http fetch GET 200 https://registry.npmjs.org/abbrev 53ms
npm http fetch GET 200 https://registry.npmjs.org/http-errors/-/http-errors-1.7.2.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/raw-body/-/raw-body-2.4.0.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz 66ms
npm http fetch GET 200 https://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz 46ms
npm http fetch GET 200 https://registry.npmjs.org/cors 44ms
npm http fetch GET 200 https://registry.npmjs.org/ms 56ms
npm http fetch GET 200 https://registry.npmjs.org/express-session 52ms
npm http fetch GET 200 https://registry.npmjs.org/memorystore 60ms
npm http fetch GET 200 https://registry.npmjs.org/@node-red%2feditor-client 79ms
npm http fetch GET 200 https://registry.npmjs.org/mime 62ms
npm http fetch GET 200 https://registry.npmjs.org/express-session/-/express-session-1.17.1.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/cors/-/cors-2.8.5.tgz 54ms
npm http fetch GET 200 https://registry.npmjs.org/ms/-/ms-2.0.0.tgz 54ms
npm http fetch GET 200 https://registry.npmjs.org/multer 49ms
npm http fetch GET 200 https://registry.npmjs.org/mustache 48ms
npm http fetch GET 200 https://registry.npmjs.org/memorystore/-/memorystore-1.6.6.tgz 54ms
npm http fetch GET 200 https://registry.npmjs.org/mime/-/mime-2.5.2.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/multer/-/multer-1.4.2.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/mustache/-/mustache-4.2.0.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/passport-http-bearer 44ms
npm http fetch GET 200 https://registry.npmjs.org/oauth2orize 49ms
npm http fetch GET 200 https://registry.npmjs.org/passport 29ms
npm http fetch GET 200 https://registry.npmjs.org/unpipe 44ms
npm http fetch GET 200 https://registry.npmjs.org/ee-first 35ms
npm http fetch GET 200 https://registry.npmjs.org/passport-http-bearer/-/passport-http-bearer-1.0.1.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/ws 69ms
npm http fetch GET 200 https://registry.npmjs.org/oauth2orize/-/oauth2orize-1.11.0.tgz 63ms
npm http fetch GET 200 https://registry.npmjs.org/passport/-/passport-0.4.1.tgz 54ms
npm http fetch GET 200 https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/ws/-/ws-6.2.1.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/destroy 29ms
npm http fetch GET 200 https://registry.npmjs.org/ipaddr.js 35ms
npm http fetch GET 200 https://registry.npmjs.org/http-errors/-/http-errors-1.7.3.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/mime/-/mime-1.6.0.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/ms/-/ms-2.1.1.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/forwarded 72ms
npm http fetch GET 200 https://registry.npmjs.org/destroy/-/destroy-1.0.4.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/media-typer 29ms
npm http fetch GET 200 https://registry.npmjs.org/ipaddr.js/-/ipaddr.js-1.9.1.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/forwarded/-/forwarded-0.2.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/media-typer/-/media-typer-0.3.0.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/tslib 40ms
npm http fetch GET 200 https://registry.npmjs.org/colors 43ms
npm http fetch GET 200 https://registry.npmjs.org/mute-stream 35ms
npm http fetch GET 200 https://registry.npmjs.org/follow-redirects 55ms
npm http fetch GET 200 https://registry.npmjs.org/mime-db 37ms
npm http fetch GET 200 https://registry.npmjs.org/tslib/-/tslib-2.2.0.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/mute-stream/-/mute-stream-0.0.8.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.14.1.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/colors/-/colors-1.0.3.tgz 60ms
npm http fetch GET 200 https://registry.npmjs.org/mime-db/-/mime-db-1.48.0.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/i18next 106ms
npm http fetch GET 200 https://registry.npmjs.org/moment-timezone 60ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.clonedeep 63ms
npm http fetch GET 200 https://registry.npmjs.org/jsonata 67ms
npm http fetch GET 200 https://registry.npmjs.org/inherits 64ms
npm http fetch GET 200 https://registry.npmjs.org/@node-red/editor-client/-/editor-client-1.3.5.tgz 599ms
npm http fetch GET 200 https://registry.npmjs.org/jsonata/-/jsonata-1.8.4.tgz 185ms
npm http fetch GET 200 https://registry.npmjs.org/moment-timezone/-/moment-timezone-0.5.33.tgz 188ms
npm http fetch GET 200 https://registry.npmjs.org/toidentifier 195ms
npm http fetch GET 200 https://registry.npmjs.org/i18next/-/i18next-15.1.2.tgz 199ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.clonedeep/-/lodash.clonedeep-4.5.0.tgz 192ms
npm http fetch GET 200 https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz 190ms
npm http fetch GET 200 https://registry.npmjs.org/@node-red/registry/-/registry-1.3.5.tgz 710ms
npm http fetch GET 200 https://registry.npmjs.org/passport-oauth2-client-password 577ms
npm http fetch GET 200 https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz 11ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/toidentifier/-/toidentifier-1.0.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/safer-buffer 27ms
npm http fetch GET 200 https://registry.npmjs.org/depd/-/depd-2.0.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/lru-cache 31ms
npm http fetch GET 200 https://registry.npmjs.org/on-headers 49ms
npm http fetch GET 200 https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.0.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/debug/-/debug-4.3.1.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/object-assign 64ms
npm http fetch GET 200 https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/uid-safe 86ms
npm http fetch GET 200 https://registry.npmjs.org/append-field 62ms
npm http fetch GET 200 https://registry.npmjs.org/lru-cache/-/lru-cache-4.1.5.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/on-headers/-/on-headers-1.0.2.tgz 56ms
npm http fetch GET 200 https://registry.npmjs.org/passport-oauth2-client-password/-/passport-oauth2-client-password-0.1.2.tgz 118ms
npm http fetch GET 200 https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz 5ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/busboy 43ms
npm http fetch GET 200 https://registry.npmjs.org/utils-merge/-/utils-merge-1.0.1.tgz 3ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/mkdirp 28ms
npm http fetch GET 200 https://registry.npmjs.org/debug/-/debug-2.6.9.tgz 6ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/uid-safe/-/uid-safe-2.1.5.tgz 64ms
npm http fetch GET 200 https://registry.npmjs.org/append-field/-/append-field-1.0.0.tgz 56ms
npm http fetch GET 200 https://registry.npmjs.org/concat-stream 65ms
npm http fetch GET 200 https://registry.npmjs.org/passport-strategy 43ms
npm http fetch GET 200 https://registry.npmjs.org/xtend 45ms
npm http fetch GET 200 https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.5.tgz 75ms
npm http fetch GET 200 https://registry.npmjs.org/uid2 93ms
npm http fetch GET 200 https://registry.npmjs.org/busboy/-/busboy-0.2.14.tgz 98ms
npm http fetch GET 200 https://registry.npmjs.org/pause 69ms
npm http fetch GET 200 https://registry.npmjs.org/xtend/-/xtend-4.0.2.tgz 66ms
npm http fetch GET 200 https://registry.npmjs.org/concat-stream/-/concat-stream-1.6.2.tgz 76ms
npm http fetch GET 200 https://registry.npmjs.org/passport-strategy/-/passport-strategy-1.0.0.tgz 83ms
npm http fetch GET 200 https://registry.npmjs.org/async-limiter 62ms
npm http fetch GET 200 https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz 63ms
npm http fetch GET 200 https://registry.npmjs.org/uid2/-/uid2-0.0.3.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/moment 53ms
npm http fetch GET 200 https://registry.npmjs.org/pause/-/pause-0.0.1.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fruntime 50ms
npm http fetch GET 200 https://registry.npmjs.org/ms/-/ms-2.1.2.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/pseudomap 26ms
npm http fetch GET 200 https://registry.npmjs.org/async-limiter/-/async-limiter-1.0.1.tgz 164ms
npm http fetch GET 200 https://registry.npmjs.org/yallist 151ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/runtime/-/runtime-7.14.0.tgz 151ms
npm http fetch GET 200 https://registry.npmjs.org/dicer 129ms
npm http fetch GET 200 https://registry.npmjs.org/uglify-js 182ms
npm http fetch GET 200 https://registry.npmjs.org/random-bytes 154ms
npm http fetch GET 200 https://registry.npmjs.org/moment/-/moment-2.29.1.tgz 167ms
npm http fetch GET 200 https://registry.npmjs.org/pseudomap/-/pseudomap-1.0.2.tgz 139ms
npm http fetch GET 200 https://registry.npmjs.org/tar 208ms
npm http fetch GET 200 https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz 33ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/buffer-from 64ms
npm http fetch GET 200 https://registry.npmjs.org/dicer/-/dicer-0.2.5.tgz 77ms
npm http fetch GET 200 https://registry.npmjs.org/yallist/-/yallist-2.1.2.tgz 81ms
npm http fetch GET 200 https://registry.npmjs.org/random-bytes/-/random-bytes-1.0.0.tgz 74ms
npm http fetch GET 200 https://registry.npmjs.org/tar/-/tar-6.1.0.tgz 70ms
npm http fetch GET 200 https://registry.npmjs.org/uglify-js/-/uglify-js-3.13.3.tgz 77ms
npm http fetch GET 200 https://registry.npmjs.org/readable-stream 70ms
npm http fetch GET 200 https://registry.npmjs.org/typedarray 61ms
npm http fetch GET 200 https://registry.npmjs.org/streamsearch 55ms
npm http fetch GET 200 https://registry.npmjs.org/readable-stream 130ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.1.tgz 68ms
npm http fetch GET 200 https://registry.npmjs.org/regenerator-runtime 61ms
npm http fetch GET 200 https://registry.npmjs.org/readable-stream/-/readable-stream-1.1.14.tgz 65ms
npm http fetch GET 200 https://registry.npmjs.org/fs-minipass 70ms
npm http fetch GET 200 https://registry.npmjs.org/minipass 73ms
npm http fetch GET 200 https://registry.npmjs.org/streamsearch/-/streamsearch-0.1.2.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/chownr 90ms
npm http fetch GET 200 https://registry.npmjs.org/typedarray/-/typedarray-0.0.6.tgz 63ms
npm http fetch GET 200 https://registry.npmjs.org/fs-minipass/-/fs-minipass-2.1.0.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/minipass/-/minipass-3.1.3.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/mkdirp/-/mkdirp-1.0.4.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.7.tgz 86ms
npm http fetch GET 200 https://registry.npmjs.org/yallist/-/yallist-4.0.0.tgz 59ms
npm http fetch GET 200 https://registry.npmjs.org/minizlib 68ms
npm http fetch GET 200 https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz 3ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/string_decoder 32ms
npm http fetch GET 200 https://registry.npmjs.org/core-util-is 85ms
npm http fetch GET 200 https://registry.npmjs.org/isarray 82ms
npm http fetch GET 200 https://registry.npmjs.org/chownr/-/chownr-2.0.0.tgz 126ms
npm http fetch GET 200 https://registry.npmjs.org/minizlib/-/minizlib-2.1.2.tgz 73ms
npm http fetch GET 200 https://registry.npmjs.org/isarray 70ms
npm http fetch GET 200 https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/process-nextick-args 78ms
npm http fetch GET 200 https://registry.npmjs.org/isarray/-/isarray-0.0.1.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.13.7.tgz 200ms
npm http fetch GET 200 https://registry.npmjs.org/util-deprecate 29ms
npm http fetch GET 200 https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz 54ms
npm http fetch GET 200 https://registry.npmjs.org/string_decoder/-/string_decoder-0.10.31.tgz 107ms
npm http fetch GET 200 https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz 80ms
npm timing npm Completed in 3271ms
npm ERR! cb() never called!

npm ERR! This is an error with npm itself. Please report this error at:
npm ERR!     <https://npm.community>

npm ERR! A complete log of this run can be found in:
npm ERR!     /openwrt/tmp/npm-cache-RQIme0ygNd/_logs/2021-06-09T19_30_02_178Z-debug.log
make[3]: *** [Makefile:98: /openwrt/build_dir/target-x86_64_musl/node-red-1.3.5/.built] Error 1
```
