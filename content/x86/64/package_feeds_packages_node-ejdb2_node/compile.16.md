---
title: "compile.16"
date: 2021-05-13 20:43:06.859591
hidden: false
draft: false
weight: -16
---

build number: `16`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/node-ejdb2_node/compile -j$(nproc) || make package/feeds/packages/node-ejdb2_node/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/999-fix_install_js.patch using plaintext: 
patching file install.js

Applying ./patches/999-fix_strip_issue.patch using plaintext: 
patching file install.js

Applying ./patches/999-mips_support.patch using plaintext: 
patching file package.json
npm info it worked if it ends with ok
npm info using npm@6.14.12
npm info using node@v14.16.1
npm timing stage:loadCurrentTree Completed in 40ms
npm timing stage:loadIdealTree:cloneCurrentTree Completed in 0ms
npm timing stage:loadIdealTree:loadShrinkwrap Completed in 1ms
npm http fetch GET 200 https://registry.npmjs.org/extract-zip 190ms
npm http fetch GET 200 https://registry.npmjs.org/request 217ms
npm http fetch GET 200 https://registry.npmjs.org/gauge 220ms
npm http fetch GET 200 https://registry.npmjs.org/request-progress 222ms
npm http fetch GET 200 https://registry.npmjs.org/extract-zip/-/extract-zip-1.7.0.tgz 90ms
npm http fetch GET 200 https://registry.npmjs.org/semver 280ms
npm http fetch GET 200 https://registry.npmjs.org/rimraf 284ms
npm http fetch GET 200 https://registry.npmjs.org/request/-/request-2.88.2.tgz 117ms
npm http fetch GET 200 https://registry.npmjs.org/gauge/-/gauge-2.7.4.tgz 118ms
npm http fetch GET 200 https://registry.npmjs.org/request-progress/-/request-progress-3.0.0.tgz 84ms
npm WARN deprecated request@2.88.2: request has been deprecated, see https://github.com/request/request/issues/3142
npm http fetch GET 200 https://registry.npmjs.org/semver/-/semver-6.3.0.tgz 79ms
npm http fetch GET 200 https://registry.npmjs.org/rimraf/-/rimraf-2.7.1.tgz 85ms
npm http fetch GET 200 https://registry.npmjs.org/concat-stream 51ms
npm http fetch GET 200 https://registry.npmjs.org/mkdirp 53ms
npm http fetch GET 200 https://registry.npmjs.org/yauzl 63ms
npm http fetch GET 200 https://registry.npmjs.org/debug 71ms
npm http fetch GET 200 https://registry.npmjs.org/concat-stream/-/concat-stream-1.6.2.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.5.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/debug/-/debug-2.6.9.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/yauzl/-/yauzl-2.10.0.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/inherits 41ms
npm http fetch GET 200 https://registry.npmjs.org/readable-stream 42ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-from 47ms
npm http fetch GET 200 https://registry.npmjs.org/typedarray 45ms
npm http fetch GET 200 https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.7.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/typedarray/-/typedarray-0.0.6.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.1.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz 46ms
npm http fetch GET 200 https://registry.npmjs.org/core-util-is 26ms
npm http fetch GET 200 https://registry.npmjs.org/process-nextick-args 41ms
npm http fetch GET 200 https://registry.npmjs.org/string_decoder 42ms
npm http fetch GET 200 https://registry.npmjs.org/util-deprecate 46ms
npm http fetch GET 200 https://registry.npmjs.org/safe-buffer 47ms
npm http fetch GET 200 https://registry.npmjs.org/isarray 55ms
npm http fetch GET 200 https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz 58ms
npm http fetch GET 200 https://registry.npmjs.org/ms 24ms
npm http fetch GET 200 https://registry.npmjs.org/ms/-/ms-2.0.0.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/minimist 33ms
npm http fetch GET 200 https://registry.npmjs.org/minimist/-/minimist-1.2.5.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/fd-slicer 23ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-crc32 44ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-crc32/-/buffer-crc32-0.2.13.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/fd-slicer/-/fd-slicer-1.1.0.tgz 106ms
npm http fetch GET 200 https://registry.npmjs.org/pend 37ms
npm http fetch GET 200 https://registry.npmjs.org/pend/-/pend-1.2.0.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/has-unicode 35ms
npm http fetch GET 200 https://registry.npmjs.org/signal-exit 42ms
npm http fetch GET 200 https://registry.npmjs.org/console-control-strings 47ms
npm http fetch GET 200 https://registry.npmjs.org/string-width 45ms
npm http fetch GET 200 https://registry.npmjs.org/aproba 53ms
npm http fetch GET 200 https://registry.npmjs.org/wide-align 64ms
npm http fetch GET 200 https://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.3.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/aproba/-/aproba-1.2.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/strip-ansi 94ms
npm http fetch GET 200 https://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/wide-align/-/wide-align-1.1.3.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/object-assign 109ms
npm http fetch GET 200 https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/is-fullwidth-code-point 41ms
npm http fetch GET 200 https://registry.npmjs.org/code-point-at 50ms
npm http fetch GET 200 https://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz 24ms
npm http fetch GET 200 https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/number-is-nan 38ms
npm http fetch GET 200 https://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-regex 31ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/caseless 33ms
npm http fetch GET 200 https://registry.npmjs.org/extend 49ms
npm http fetch GET 200 https://registry.npmjs.org/aws-sign2 58ms
npm http fetch GET 200 https://registry.npmjs.org/aws4 58ms
npm http fetch GET 200 https://registry.npmjs.org/form-data 57ms
npm http fetch GET 200 https://registry.npmjs.org/har-validator 61ms
npm http fetch GET 200 https://registry.npmjs.org/combined-stream 68ms
npm http fetch GET 200 https://registry.npmjs.org/forever-agent 67ms
npm http fetch GET 200 https://registry.npmjs.org/http-signature 76ms
npm http fetch GET 200 https://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/extend/-/extend-3.0.2.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/is-typedarray 83ms
npm http fetch GET 200 https://registry.npmjs.org/aws-sign2/-/aws-sign2-0.7.0.tgz 58ms
npm http fetch GET 200 https://registry.npmjs.org/aws4/-/aws4-1.11.0.tgz 59ms
npm http fetch GET 200 https://registry.npmjs.org/har-validator/-/har-validator-5.1.5.tgz 60ms
npm http fetch GET 200 https://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz 56ms
npm http fetch GET 200 https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz 56ms
npm http fetch GET 200 https://registry.npmjs.org/form-data/-/form-data-2.3.3.tgz 64ms
npm http fetch GET 200 https://registry.npmjs.org/http-signature/-/http-signature-1.2.0.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/json-stringify-safe 45ms
npm WARN deprecated har-validator@5.1.5: this library is no longer supported
npm http fetch GET 200 https://registry.npmjs.org/isstream 55ms
npm http fetch GET 200 https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/performance-now 56ms
npm http fetch GET 200 https://registry.npmjs.org/qs 49ms
npm http fetch GET 200 https://registry.npmjs.org/tough-cookie 55ms
npm http fetch GET 200 https://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz 61ms
npm http fetch GET 200 https://registry.npmjs.org/tunnel-agent 56ms
npm http fetch GET 200 https://registry.npmjs.org/oauth-sign 68ms
npm http fetch GET 200 https://registry.npmjs.org/mime-types 70ms
npm http fetch GET 200 https://registry.npmjs.org/uuid 72ms
npm http fetch GET 200 https://registry.npmjs.org/qs/-/qs-6.5.2.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/oauth-sign/-/oauth-sign-0.9.0.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/mime-types/-/mime-types-2.1.30.tgz 46ms
npm http fetch GET 200 https://registry.npmjs.org/tough-cookie/-/tough-cookie-2.5.0.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz 58ms
npm http fetch GET 200 https://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz 63ms
npm http fetch GET 200 https://registry.npmjs.org/uuid/-/uuid-3.4.0.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/delayed-stream 36ms
npm http fetch GET 200 https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/asynckit 25ms
npm http fetch GET 200 https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/mime-db 26ms
npm http fetch GET 200 https://registry.npmjs.org/mime-db/-/mime-db-1.47.0.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/har-schema 24ms
npm http fetch GET 200 https://registry.npmjs.org/har-schema/-/har-schema-2.0.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/ajv 58ms
npm http fetch GET 200 https://registry.npmjs.org/ajv/-/ajv-6.12.6.tgz 46ms
npm http fetch GET 200 https://registry.npmjs.org/uri-js 32ms
npm http fetch GET 200 https://registry.npmjs.org/json-schema-traverse 37ms
npm http fetch GET 200 https://registry.npmjs.org/fast-deep-equal 43ms
npm http fetch GET 200 https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/fast-json-stable-stringify 86ms
npm http fetch GET 200 https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/punycode 25ms
npm http fetch GET 200 https://registry.npmjs.org/punycode/-/punycode-2.1.1.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/assert-plus 23ms
npm http fetch GET 200 https://registry.npmjs.org/sshpk 30ms
npm http fetch GET 200 https://registry.npmjs.org/jsprim 33ms
npm http fetch GET 200 https://registry.npmjs.org/sshpk/-/sshpk-1.16.1.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/jsprim/-/jsprim-1.4.1.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz 58ms
npm http fetch GET 200 https://registry.npmjs.org/json-schema 27ms
npm http fetch GET 200 https://registry.npmjs.org/extsprintf 28ms
npm http fetch GET 200 https://registry.npmjs.org/verror 32ms
npm http fetch GET 200 https://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/verror/-/verror-1.10.0.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/json-schema/-/json-schema-0.2.3.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/bcrypt-pbkdf 35ms
npm http fetch GET 200 https://registry.npmjs.org/tweetnacl 41ms
npm http fetch GET 200 https://registry.npmjs.org/getpass 45ms
npm http fetch GET 200 https://registry.npmjs.org/jsbn 46ms
npm http fetch GET 200 https://registry.npmjs.org/ecc-jsbn 52ms
npm http fetch GET 200 https://registry.npmjs.org/asn1 57ms
npm http fetch GET 200 https://registry.npmjs.org/dashdash 59ms
npm http fetch GET 200 https://registry.npmjs.org/safer-buffer 60ms
npm http fetch GET 200 https://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.2.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz 25ms
npm http fetch GET 200 https://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.2.tgz 65ms
npm http fetch GET 200 https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz 60ms
npm http fetch GET 200 https://registry.npmjs.org/asn1/-/asn1-0.2.4.tgz 66ms
npm http fetch GET 200 https://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz 65ms
npm http fetch GET 200 https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz 81ms
npm http fetch GET 200 https://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz 76ms
npm http fetch GET 200 https://registry.npmjs.org/psl 34ms
npm http fetch GET 200 https://registry.npmjs.org/psl/-/psl-1.8.0.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/throttleit 34ms
npm http fetch GET 200 https://registry.npmjs.org/throttleit/-/throttleit-1.0.0.tgz 25ms
npm http fetch GET 200 https://registry.npmjs.org/glob 30ms
npm http fetch GET 200 https://registry.npmjs.org/glob/-/glob-7.1.7.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/inflight 26ms
npm http fetch GET 200 https://registry.npmjs.org/once 40ms
npm http fetch GET 200 https://registry.npmjs.org/fs.realpath 45ms
npm http fetch GET 200 https://registry.npmjs.org/path-is-absolute 47ms
npm http fetch GET 200 https://registry.npmjs.org/minimatch 50ms
npm http fetch GET 200 https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/once/-/once-1.4.0.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz 67ms
npm http fetch GET 200 https://registry.npmjs.org/wrappy 26ms
npm http fetch GET 200 https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz 62ms
npm http fetch GET 200 https://registry.npmjs.org/brace-expansion 37ms
npm http fetch GET 200 https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/balanced-match 30ms
npm http fetch GET 200 https://registry.npmjs.org/concat-map 36ms
npm http fetch GET 200 https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz 22ms
npm http fetch GET 200 https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz 53ms
npm timing stage:loadIdealTree:loadAllDepsIntoIdealTree Completed in 3227ms
npm timing stage:loadIdealTree Completed in 3264ms
npm timing stage:generateActionsToTake Completed in 19ms
npm timing action:extract Completed in 518ms
npm timing action:finalize Completed in 57ms
npm timing action:refresh-package-json Completed in 225ms
npm info lifecycle ansi-regex@2.1.1~preinstall: ansi-regex@2.1.1
npm info lifecycle aproba@1.2.0~preinstall: aproba@1.2.0
npm info lifecycle assert-plus@1.0.0~preinstall: assert-plus@1.0.0
npm info lifecycle asynckit@0.4.0~preinstall: asynckit@0.4.0
npm info lifecycle aws-sign2@0.7.0~preinstall: aws-sign2@0.7.0
npm info lifecycle aws4@1.11.0~preinstall: aws4@1.11.0
npm info lifecycle balanced-match@1.0.2~preinstall: balanced-match@1.0.2
npm info lifecycle buffer-crc32@0.2.13~preinstall: buffer-crc32@0.2.13
npm info lifecycle buffer-from@1.1.1~preinstall: buffer-from@1.1.1
npm info lifecycle caseless@0.12.0~preinstall: caseless@0.12.0
npm info lifecycle code-point-at@1.1.0~preinstall: code-point-at@1.1.0
npm info lifecycle concat-map@0.0.1~preinstall: concat-map@0.0.1
npm info lifecycle brace-expansion@1.1.11~preinstall: brace-expansion@1.1.11
npm info lifecycle console-control-strings@1.1.0~preinstall: console-control-strings@1.1.0
npm info lifecycle core-util-is@1.0.2~preinstall: core-util-is@1.0.2
npm info lifecycle dashdash@1.14.1~preinstall: dashdash@1.14.1
npm info lifecycle delayed-stream@1.0.0~preinstall: delayed-stream@1.0.0
npm info lifecycle combined-stream@1.0.8~preinstall: combined-stream@1.0.8
npm info lifecycle extend@3.0.2~preinstall: extend@3.0.2
npm info lifecycle extsprintf@1.3.0~preinstall: extsprintf@1.3.0
npm info lifecycle fast-deep-equal@3.1.3~preinstall: fast-deep-equal@3.1.3
npm info lifecycle fast-json-stable-stringify@2.1.0~preinstall: fast-json-stable-stringify@2.1.0
npm info lifecycle forever-agent@0.6.1~preinstall: forever-agent@0.6.1
npm info lifecycle fs.realpath@1.0.0~preinstall: fs.realpath@1.0.0
npm info lifecycle getpass@0.1.7~preinstall: getpass@0.1.7
npm info lifecycle har-schema@2.0.0~preinstall: har-schema@2.0.0
npm info lifecycle has-unicode@2.0.1~preinstall: has-unicode@2.0.1
npm info lifecycle inherits@2.0.4~preinstall: inherits@2.0.4
npm info lifecycle is-typedarray@1.0.0~preinstall: is-typedarray@1.0.0
npm info lifecycle isarray@1.0.0~preinstall: isarray@1.0.0
npm info lifecycle isstream@0.1.2~preinstall: isstream@0.1.2
npm info lifecycle jsbn@0.1.1~preinstall: jsbn@0.1.1
npm info lifecycle json-schema@0.2.3~preinstall: json-schema@0.2.3
npm info lifecycle json-schema-traverse@0.4.1~preinstall: json-schema-traverse@0.4.1
npm info lifecycle json-stringify-safe@5.0.1~preinstall: json-stringify-safe@5.0.1
npm info lifecycle mime-db@1.47.0~preinstall: mime-db@1.47.0
npm info lifecycle mime-types@2.1.30~preinstall: mime-types@2.1.30
npm info lifecycle form-data@2.3.3~preinstall: form-data@2.3.3
npm info lifecycle minimatch@3.0.4~preinstall: minimatch@3.0.4
npm info lifecycle minimist@1.2.5~preinstall: minimist@1.2.5
npm info lifecycle mkdirp@0.5.5~preinstall: mkdirp@0.5.5
npm info lifecycle ms@2.0.0~preinstall: ms@2.0.0
npm info lifecycle debug@2.6.9~preinstall: debug@2.6.9
npm info lifecycle number-is-nan@1.0.1~preinstall: number-is-nan@1.0.1
npm info lifecycle is-fullwidth-code-point@1.0.0~preinstall: is-fullwidth-code-point@1.0.0
npm info lifecycle oauth-sign@0.9.0~preinstall: oauth-sign@0.9.0
npm info lifecycle object-assign@4.1.1~preinstall: object-assign@4.1.1
npm info lifecycle path-is-absolute@1.0.1~preinstall: path-is-absolute@1.0.1
npm info lifecycle pend@1.2.0~preinstall: pend@1.2.0
npm info lifecycle fd-slicer@1.1.0~preinstall: fd-slicer@1.1.0
npm info lifecycle ejdb2_node@2.0.603~preinstall: ejdb2_node@2.0.603
npm info lifecycle semver@6.3.0~preinstall: semver@6.3.0
npm info lifecycle rimraf@2.7.1~preinstall: rimraf@2.7.1
npm info lifecycle request-progress@3.0.0~preinstall: request-progress@3.0.0
npm info lifecycle request@2.88.2~preinstall: request@2.88.2
npm info lifecycle gauge@2.7.4~preinstall: gauge@2.7.4
npm info lifecycle extract-zip@1.7.0~preinstall: extract-zip@1.7.0
npm info lifecycle yauzl@2.10.0~preinstall: yauzl@2.10.0
npm info lifecycle glob@7.1.7~preinstall: glob@7.1.7
npm info lifecycle inflight@1.0.6~preinstall: inflight@1.0.6
npm info lifecycle once@1.4.0~preinstall: once@1.4.0
npm info lifecycle wrappy@1.0.2~preinstall: wrappy@1.0.2
npm info lifecycle wide-align@1.1.3~preinstall: wide-align@1.1.3
npm info lifecycle http-signature@1.2.0~preinstall: http-signature@1.2.0
npm info lifecycle jsprim@1.4.1~preinstall: jsprim@1.4.1
npm info lifecycle verror@1.10.0~preinstall: verror@1.10.0
npm info lifecycle uuid@3.4.0~preinstall: uuid@3.4.0
npm info lifecycle concat-stream@1.6.2~preinstall: concat-stream@1.6.2
npm info lifecycle readable-stream@2.3.7~preinstall: readable-stream@2.3.7
npm info lifecycle util-deprecate@1.0.2~preinstall: util-deprecate@1.0.2
npm info lifecycle har-validator@5.1.5~preinstall: har-validator@5.1.5
npm info lifecycle ajv@6.12.6~preinstall: ajv@6.12.6
npm info lifecycle uri-js@4.4.1~preinstall: uri-js@4.4.1
npm info lifecycle typedarray@0.0.6~preinstall: typedarray@0.0.6
npm info lifecycle sshpk@1.16.1~preinstall: sshpk@1.16.1
npm info lifecycle bcrypt-pbkdf@1.0.2~preinstall: bcrypt-pbkdf@1.0.2
npm info lifecycle tweetnacl@0.14.5~preinstall: tweetnacl@0.14.5
npm info lifecycle tunnel-agent@0.6.0~preinstall: tunnel-agent@0.6.0
npm info lifecycle tough-cookie@2.5.0~preinstall: tough-cookie@2.5.0
npm info lifecycle throttleit@1.0.0~preinstall: throttleit@1.0.0
npm info lifecycle string-width@1.0.2~preinstall: string-width@1.0.2
npm info lifecycle strip-ansi@3.0.1~preinstall: strip-ansi@3.0.1
npm info lifecycle string_decoder@1.1.1~preinstall: string_decoder@1.1.1
npm info lifecycle signal-exit@3.0.3~preinstall: signal-exit@3.0.3
npm info lifecycle ecc-jsbn@0.1.2~preinstall: ecc-jsbn@0.1.2
npm info lifecycle asn1@0.2.4~preinstall: asn1@0.2.4
npm info lifecycle safer-buffer@2.1.2~preinstall: safer-buffer@2.1.2
npm info lifecycle safe-buffer@5.1.2~preinstall: safe-buffer@5.1.2
npm info lifecycle qs@6.5.2~preinstall: qs@6.5.2
npm info lifecycle punycode@2.1.1~preinstall: punycode@2.1.1
npm info lifecycle psl@1.8.0~preinstall: psl@1.8.0
npm info lifecycle process-nextick-args@2.0.1~preinstall: process-nextick-args@2.0.1
npm info lifecycle performance-now@2.1.0~preinstall: performance-now@2.1.0
npm timing action:preinstall Completed in 23ms
npm info linkStuff ansi-regex@2.1.1
npm info linkStuff aproba@1.2.0
npm info linkStuff assert-plus@1.0.0
npm info linkStuff asynckit@0.4.0
npm info linkStuff aws-sign2@0.7.0
npm info linkStuff aws4@1.11.0
npm info linkStuff balanced-match@1.0.2
npm info linkStuff buffer-crc32@0.2.13
npm info linkStuff buffer-from@1.1.1
npm info linkStuff caseless@0.12.0
npm info linkStuff code-point-at@1.1.0
npm info linkStuff concat-map@0.0.1
npm info linkStuff brace-expansion@1.1.11
npm info linkStuff console-control-strings@1.1.0
npm info linkStuff core-util-is@1.0.2
npm info linkStuff dashdash@1.14.1
npm info linkStuff delayed-stream@1.0.0
npm info linkStuff combined-stream@1.0.8
npm info linkStuff extend@3.0.2
npm info linkStuff extsprintf@1.3.0
npm info linkStuff fast-deep-equal@3.1.3
npm info linkStuff fast-json-stable-stringify@2.1.0
npm info linkStuff forever-agent@0.6.1
npm info linkStuff fs.realpath@1.0.0
npm info linkStuff getpass@0.1.7
npm info linkStuff har-schema@2.0.0
npm info linkStuff has-unicode@2.0.1
npm info linkStuff inherits@2.0.4
npm info linkStuff is-typedarray@1.0.0
npm info linkStuff isarray@1.0.0
npm info linkStuff isstream@0.1.2
npm info linkStuff jsbn@0.1.1
npm info linkStuff json-schema@0.2.3
npm info linkStuff json-schema-traverse@0.4.1
npm info linkStuff json-stringify-safe@5.0.1
npm info linkStuff mime-db@1.47.0
npm info linkStuff mime-types@2.1.30
npm info linkStuff form-data@2.3.3
npm info linkStuff minimatch@3.0.4
npm info linkStuff minimist@1.2.5
npm info linkStuff mkdirp@0.5.5
npm info linkStuff ms@2.0.0
npm info linkStuff debug@2.6.9
npm info linkStuff number-is-nan@1.0.1
npm info linkStuff is-fullwidth-code-point@1.0.0
npm info linkStuff oauth-sign@0.9.0
npm info linkStuff object-assign@4.1.1
npm info linkStuff path-is-absolute@1.0.1
npm info linkStuff pend@1.2.0
npm info linkStuff fd-slicer@1.1.0
npm info linkStuff performance-now@2.1.0
npm info linkStuff process-nextick-args@2.0.1
npm info linkStuff psl@1.8.0
npm info linkStuff punycode@2.1.1
npm info linkStuff qs@6.5.2
npm info linkStuff safe-buffer@5.1.2
npm info linkStuff safer-buffer@2.1.2
npm info linkStuff asn1@0.2.4
npm info linkStuff ecc-jsbn@0.1.2
npm info linkStuff signal-exit@3.0.3
npm info linkStuff string_decoder@1.1.1
npm info linkStuff strip-ansi@3.0.1
npm info linkStuff string-width@1.0.2
npm info linkStuff throttleit@1.0.0
npm info linkStuff tough-cookie@2.5.0
npm info linkStuff tunnel-agent@0.6.0
npm info linkStuff tweetnacl@0.14.5
npm info linkStuff bcrypt-pbkdf@1.0.2
npm info linkStuff sshpk@1.16.1
npm info linkStuff typedarray@0.0.6
npm info linkStuff uri-js@4.4.1
npm info linkStuff ajv@6.12.6
npm info linkStuff har-validator@5.1.5
npm info linkStuff util-deprecate@1.0.2
npm info linkStuff readable-stream@2.3.7
npm info linkStuff concat-stream@1.6.2
npm info linkStuff uuid@3.4.0
npm info linkStuff verror@1.10.0
npm info linkStuff jsprim@1.4.1
npm info linkStuff http-signature@1.2.0
npm info linkStuff wide-align@1.1.3
npm info linkStuff wrappy@1.0.2
npm info linkStuff once@1.4.0
npm info linkStuff inflight@1.0.6
npm info linkStuff glob@7.1.7
npm info linkStuff yauzl@2.10.0
npm info linkStuff extract-zip@1.7.0
npm info linkStuff gauge@2.7.4
npm info linkStuff request@2.88.2
npm info linkStuff request-progress@3.0.0
npm info linkStuff rimraf@2.7.1
npm info linkStuff semver@6.3.0
npm info linkStuff ejdb2_node@2.0.603
npm timing action:build Completed in 52ms
npm info lifecycle ansi-regex@2.1.1~install: ansi-regex@2.1.1
npm info lifecycle aproba@1.2.0~install: aproba@1.2.0
npm info lifecycle assert-plus@1.0.0~install: assert-plus@1.0.0
npm info lifecycle asynckit@0.4.0~install: asynckit@0.4.0
npm info lifecycle aws-sign2@0.7.0~install: aws-sign2@0.7.0
npm info lifecycle aws4@1.11.0~install: aws4@1.11.0
npm info lifecycle balanced-match@1.0.2~install: balanced-match@1.0.2
npm info lifecycle buffer-crc32@0.2.13~install: buffer-crc32@0.2.13
npm info lifecycle buffer-from@1.1.1~install: buffer-from@1.1.1
npm info lifecycle caseless@0.12.0~install: caseless@0.12.0
npm info lifecycle code-point-at@1.1.0~install: code-point-at@1.1.0
npm info lifecycle concat-map@0.0.1~install: concat-map@0.0.1
npm info lifecycle brace-expansion@1.1.11~install: brace-expansion@1.1.11
npm info lifecycle console-control-strings@1.1.0~install: console-control-strings@1.1.0
npm info lifecycle core-util-is@1.0.2~install: core-util-is@1.0.2
npm info lifecycle dashdash@1.14.1~install: dashdash@1.14.1
npm info lifecycle delayed-stream@1.0.0~install: delayed-stream@1.0.0
npm info lifecycle combined-stream@1.0.8~install: combined-stream@1.0.8
npm info lifecycle extend@3.0.2~install: extend@3.0.2
npm info lifecycle extsprintf@1.3.0~install: extsprintf@1.3.0
npm info lifecycle fast-deep-equal@3.1.3~install: fast-deep-equal@3.1.3
npm info lifecycle fast-json-stable-stringify@2.1.0~install: fast-json-stable-stringify@2.1.0
npm info lifecycle forever-agent@0.6.1~install: forever-agent@0.6.1
npm info lifecycle fs.realpath@1.0.0~install: fs.realpath@1.0.0
npm info lifecycle getpass@0.1.7~install: getpass@0.1.7
npm info lifecycle har-schema@2.0.0~install: har-schema@2.0.0
npm info lifecycle has-unicode@2.0.1~install: has-unicode@2.0.1
npm info lifecycle inherits@2.0.4~install: inherits@2.0.4
npm info lifecycle is-typedarray@1.0.0~install: is-typedarray@1.0.0
npm info lifecycle isarray@1.0.0~install: isarray@1.0.0
npm info lifecycle isstream@0.1.2~install: isstream@0.1.2
npm info lifecycle jsbn@0.1.1~install: jsbn@0.1.1
npm info lifecycle json-schema@0.2.3~install: json-schema@0.2.3
npm info lifecycle json-schema-traverse@0.4.1~install: json-schema-traverse@0.4.1
npm info lifecycle json-stringify-safe@5.0.1~install: json-stringify-safe@5.0.1
npm info lifecycle mime-db@1.47.0~install: mime-db@1.47.0
npm info lifecycle mime-types@2.1.30~install: mime-types@2.1.30
npm info lifecycle form-data@2.3.3~install: form-data@2.3.3
npm info lifecycle minimatch@3.0.4~install: minimatch@3.0.4
npm info lifecycle minimist@1.2.5~install: minimist@1.2.5
npm info lifecycle mkdirp@0.5.5~install: mkdirp@0.5.5
npm info lifecycle ms@2.0.0~install: ms@2.0.0
npm info lifecycle debug@2.6.9~install: debug@2.6.9
npm info lifecycle number-is-nan@1.0.1~install: number-is-nan@1.0.1
npm info lifecycle is-fullwidth-code-point@1.0.0~install: is-fullwidth-code-point@1.0.0
npm info lifecycle oauth-sign@0.9.0~install: oauth-sign@0.9.0
npm info lifecycle object-assign@4.1.1~install: object-assign@4.1.1
npm info lifecycle path-is-absolute@1.0.1~install: path-is-absolute@1.0.1
npm info lifecycle pend@1.2.0~install: pend@1.2.0
npm info lifecycle fd-slicer@1.1.0~install: fd-slicer@1.1.0
npm info lifecycle performance-now@2.1.0~install: performance-now@2.1.0
npm info lifecycle process-nextick-args@2.0.1~install: process-nextick-args@2.0.1
npm info lifecycle psl@1.8.0~install: psl@1.8.0
npm info lifecycle punycode@2.1.1~install: punycode@2.1.1
npm info lifecycle qs@6.5.2~install: qs@6.5.2
npm info lifecycle safe-buffer@5.1.2~install: safe-buffer@5.1.2
npm info lifecycle safer-buffer@2.1.2~install: safer-buffer@2.1.2
npm info lifecycle asn1@0.2.4~install: asn1@0.2.4
npm info lifecycle ecc-jsbn@0.1.2~install: ecc-jsbn@0.1.2
npm info lifecycle signal-exit@3.0.3~install: signal-exit@3.0.3
npm info lifecycle string_decoder@1.1.1~install: string_decoder@1.1.1
npm info lifecycle strip-ansi@3.0.1~install: strip-ansi@3.0.1
npm info lifecycle string-width@1.0.2~install: string-width@1.0.2
npm info lifecycle throttleit@1.0.0~install: throttleit@1.0.0
npm info lifecycle tough-cookie@2.5.0~install: tough-cookie@2.5.0
npm info lifecycle tunnel-agent@0.6.0~install: tunnel-agent@0.6.0
npm info lifecycle tweetnacl@0.14.5~install: tweetnacl@0.14.5
npm info lifecycle bcrypt-pbkdf@1.0.2~install: bcrypt-pbkdf@1.0.2
npm info lifecycle sshpk@1.16.1~install: sshpk@1.16.1
npm info lifecycle typedarray@0.0.6~install: typedarray@0.0.6
npm info lifecycle uri-js@4.4.1~install: uri-js@4.4.1
npm info lifecycle ajv@6.12.6~install: ajv@6.12.6
npm info lifecycle har-validator@5.1.5~install: har-validator@5.1.5
npm info lifecycle util-deprecate@1.0.2~install: util-deprecate@1.0.2
npm info lifecycle readable-stream@2.3.7~install: readable-stream@2.3.7
npm info lifecycle concat-stream@1.6.2~install: concat-stream@1.6.2
npm info lifecycle uuid@3.4.0~install: uuid@3.4.0
npm info lifecycle verror@1.10.0~install: verror@1.10.0
npm info lifecycle jsprim@1.4.1~install: jsprim@1.4.1
npm info lifecycle http-signature@1.2.0~install: http-signature@1.2.0
npm info lifecycle wide-align@1.1.3~install: wide-align@1.1.3
npm info lifecycle wrappy@1.0.2~install: wrappy@1.0.2
npm info lifecycle once@1.4.0~install: once@1.4.0
npm info lifecycle inflight@1.0.6~install: inflight@1.0.6
npm info lifecycle glob@7.1.7~install: glob@7.1.7
npm info lifecycle yauzl@2.10.0~install: yauzl@2.10.0
npm info lifecycle extract-zip@1.7.0~install: extract-zip@1.7.0
npm info lifecycle gauge@2.7.4~install: gauge@2.7.4
npm info lifecycle request@2.88.2~install: request@2.88.2
npm info lifecycle request-progress@3.0.0~install: request-progress@3.0.0
npm info lifecycle rimraf@2.7.1~install: rimraf@2.7.1
npm info lifecycle semver@6.3.0~install: semver@6.3.0
npm info lifecycle ejdb2_node@2.0.603~install: ejdb2_node@2.0.603

> ejdb2_node@2.0.603 install /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib/node_modules/ejdb2_node
> node install.js

Spawn: cmake --version
cmake version 3.19.1

CMake suite maintained and supported by Kitware (kitware.com/cmake).

Spawn: make --version
GNU Make 4.2.1
,Built for x86_64-pc-linux-gnu
,Copyright (C) 1988-2016 Free Software Foundation, Inc.
,License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
,This is free software: you are free to change and redistribute it.
,There is NO WARRANTY, to the extent permitted by law.

Building EJDB2 native binding...
Git revision: be72ee7
Build temp dir: /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA
Spawn: cmake ..,-DCMAKE_BUILD_TYPE=RelWithDebInfo,-DBUILD_NODEJS_BINDING=ON,-DNODE_BIN_ROOT=/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603
-- Using project changelog file: /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/Changelog
-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/host/bin/ccache_cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Resolving GIT Version
-- Found Git: /openwrt/staging_dir/host/bin/git (found version "2.25.1") 
-- GIT hash: 
IOWOW_URL: https://github.com/Softmotions/iowow/archive/master.zip
IOWOW CMAKE_ARGS: -DOWNER_PROJECT_NAME=ejdb2;-DCMAKE_BUILD_TYPE=RelWithDebInfo;-DCMAKE_INSTALL_PREFIX=/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build;-DASAN=OFF;-DBUILD_SHARED_LIBS=OFF;-DBUILD_EXAMPLES=OFF;-DCMAKE_C_COMPILER=/openwrt/staging_dir/host/bin/ccache_cc
FACIL_URL: https://github.com/Softmotions/facil.io/archive/master.zip
FACIL CMAKE_ARGS: -DCMAKE_BUILD_TYPE=RelWithDebInfo;-DCMAKE_C_FLAGS=-fPIC;-DCMAKE_C_COMPILER=/openwrt/staging_dir/host/bin/ccache_cc
-- Check if the system is big endian
-- Searching 16 bit integer
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Searching 16 bit integer - Using unsigned short
-- Check if the system is big endian - little endian
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Looking for stdlib.h
-- Looking for stdlib.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stdbool.h
-- Looking for stdbool.h - found

CMAKE_GENERATOR: Unix Makefiles
ejdb2 LINK LIBS: iowow_s;m;facil_s
ejdb2 ASAN: OFF

ejdb2 INCLUDE DIRS: /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build/src/generated;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build/include;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build/src/extern_facil/lib/facil;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build/src/extern_facil/lib/facil/fiobj;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build/src/extern_facil/lib/facil/http;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build/src/extern_facil/lib/facil/cli;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build/src/extern_facil/lib/facil/tls;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/util;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbl;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jql;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbi;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbr

ejdb2 SOURCES: /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/ejdb2.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/util/lwre.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/util/utf8proc.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbl/binn.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbl/jbl.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbl/jbl_json.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jql/jql.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jql/jqp.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbi/jbi_consumer.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbi/jbi_dup_scanner.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbi/jbi_full_scanner.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbi/jbi_pk_scanner.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbi/jbi_selection.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbi/jbi_sorter_consumer.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbi/jbi_uniq_scanner.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbi/jbi_util.c;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbr/jbr.c

ejdb2 PUB_HDRS: /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/ejdb2.h;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbl/jbl.h;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jbr/jbr.h;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/jql/jql.h;/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/src/util/lwre.h

ejdb2 CMAKE_BUILD_TYPE: RelWithDebInfo
ejdb2 ANDROID_ABIS: x86;x86_64;arm64-v8a;armeabi-v7a
ejdb2 ENABLE_HTTP: ON
ejdb2 BUILD_SHARED_LIBS: ON
ejdb2 BUILD_TESTS: OFF
ejdb2 BUILD_EXAMPLES: ON
ejdb2 BUILD_BENCHMARKS: OFF
ejdb2 BUILD_DART_BINDING: OFF
ejdb2 BUILD_ANDROID_LIBS: OFF
ejdb2 BUILD_JNI_BINDING: OFF
ejdb2 BUILD_NODEJS_BINDING: ON
ejdb2 BUILD_REACT_NATIVE_BINDING: OFF
ejdb2 BUILD_FLUTTER_BINDING: OFF
ejdb2 BUILD_SWIFT_BINDING: OFF
ejdb2 GIT_REVISION: 
ejdb2 CMAKE_INSTALL_PREFIX: /usr/local
ejdb2 CPACK_GENERATORS: TGZ;ZIP
ejdb2 CMAKE_GENERATOR: Unix Makefiles
ejdb2 CMAKE_SYSTEM_NAME: Linux
ejdb2 CPU: x86_64
ejdb2 SIZEOF *VOID: 8
ejdb2 PROJECT: ejdb2 (2.0.60) UNRELEASED; urgency=medium
ejdb2 CHANGELOG_MESSAGE:
  * Added typescript generic to JBDOC in node binding (#311) 
  * Removed -fvisibility=hidden compiler flag from facil.io lib
-- Configuring done
-- Generating done
-- Build files have been written to: /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build
Spawn: make ejdb2_node
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build'
make[5]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build'
make[6]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build'
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build'
Scanning dependencies of target extern_iowow
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build'
make[7]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build'
[  2%] Creating directories for 'extern_iowow'
[  5%] Performing download step (download, verify and extract) for 'extern_iowow'
-- Downloading...
   dst='/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build/src/iowow.zip'
   timeout='360 seconds'
   inactivity timeout='none'
-- Using src='https://github.com/Softmotions/iowow/archive/master.zip'
-- Retrying...
-- Using src='https://github.com/Softmotions/iowow/archive/master.zip'
-- Retry after 5 seconds (attempt #2) ...
-- Using src='https://github.com/Softmotions/iowow/archive/master.zip'
-- Retry after 5 seconds (attempt #3) ...
-- Using src='https://github.com/Softmotions/iowow/archive/master.zip'
-- Retry after 15 seconds (attempt #4) ...
-- Using src='https://github.com/Softmotions/iowow/archive/master.zip'
-- Retry after 60 seconds (attempt #5) ...
-- Using src='https://github.com/Softmotions/iowow/archive/master.zip'
CMake Error at extern_iowow-stamp/download-extern_iowow.cmake:170 (message):
  Each download failed!

    error: downloading 'https://github.com/Softmotions/iowow/archive/master.zip' failed
          status_code: 6
          status_string: "Couldn't resolve host name"
          log:
          --- LOG BEGIN ---
          getaddrinfo(3) failed for github.com:443

  Couldn't resolve host 'github.com'

  Closing connection 0

  

          --- LOG END ---
          error: downloading 'https://github.com/Softmotions/iowow/archive/master.zip' failed
          status_code: 6
          status_string: "Couldn't resolve host name"
          log:
          --- LOG BEGIN ---
          getaddrinfo(3) failed for github.com:443

  Couldn't resolve host 'github.com'

  Closing connection 0

  

          --- LOG END ---
          error: downloading 'https://github.com/Softmotions/iowow/archive/master.zip' failed
          status_code: 6
          status_string: "Couldn't resolve host name"
          log:
          --- LOG BEGIN ---
          getaddrinfo(3) failed for github.com:443

  Couldn't resolve host 'github.com'

  Closing connection 0

  

          --- LOG END ---
          error: downloading 'https://github.com/Softmotions/iowow/archive/master.zip' failed
          status_code: 6
          status_string: "Couldn't resolve host name"
          log:
          --- LOG BEGIN ---
          getaddrinfo(3) failed for github.com:443

  Couldn't resolve host 'github.com'

  Closing connection 0

  

          --- LOG END ---
          error: downloading 'https://github.com/Softmotions/iowow/archive/master.zip' failed
          status_code: 6
          status_string: "Couldn't resolve host name"
          log:
          --- LOG BEGIN ---
          getaddrinfo(3) failed for github.com:443

  Couldn't resolve host 'github.com'

  Closing connection 0

  

          --- LOG END ---
          error: downloading 'https://github.com/Softmotions/iowow/archive/master.zip' failed
          status_code: 6
          status_string: "Couldn't resolve host name"
          log:
          --- LOG BEGIN ---
          getaddrinfo(3) failed for github.com:443

  Couldn't resolve host 'github.com'

  Closing connection 0

  

          --- LOG END ---
          
    


make[7]: *** [src/CMakeFiles/extern_iowow.dir/build.make:109: src/extern_iowow-stamp/extern_iowow-download] Error 1
make[7]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build'
make[6]: *** [CMakeFiles/Makefile2:326: src/CMakeFiles/extern_iowow.dir/all] Error 2
make[6]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build'
make[5]: *** [CMakeFiles/Makefile2:447: src/bindings/ejdb2_node/CMakeFiles/ejdb2_node.dir/rule] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build'
make[4]: *** [Makefile:250: ejdb2_node] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ejdb2-nodePwqcpA/ejdb-be72ee75b27e4cf59a775680f26a1bc994443ae0/build'
Error: Exit with error code: 2
    at ChildProcess.<anonymous> (/openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/utils.js:77:16)
    at Object.onceWrapper (events.js:422:26)
    at ChildProcess.emit (events.js:315:20)
    at Process.ChildProcess._handle.onexit (internal/child_process.js:277:12)
npm info lifecycle ejdb2_node@2.0.603~install: Failed to exec install script
npm timing action:install Completed in 90048ms
npm WARN rollback Rolling back ansi-regex@2.1.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/ansi-regex is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back aproba@1.2.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/aproba is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back assert-plus@1.0.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/assert-plus is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back asynckit@0.4.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/asynckit is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back aws-sign2@0.7.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/aws-sign2 is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back aws4@1.11.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/aws4 is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back balanced-match@1.0.2 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/balanced-match is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back buffer-crc32@0.2.13 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/buffer-crc32 is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back buffer-from@1.1.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/buffer-from is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back caseless@0.12.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/caseless is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back code-point-at@1.1.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/code-point-at is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back concat-map@0.0.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/concat-map is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back brace-expansion@1.1.11 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/brace-expansion is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back console-control-strings@1.1.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/console-control-strings is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back core-util-is@1.0.2 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/core-util-is is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back dashdash@1.14.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/dashdash is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back delayed-stream@1.0.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/delayed-stream is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back combined-stream@1.0.8 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/combined-stream is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back extend@3.0.2 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/extend is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back extsprintf@1.3.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/extsprintf is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back fast-deep-equal@3.1.3 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/fast-deep-equal is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back fast-json-stable-stringify@2.1.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/fast-json-stable-stringify is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back forever-agent@0.6.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/forever-agent is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back fs.realpath@1.0.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/fs.realpath is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back getpass@0.1.7 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/getpass is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back har-schema@2.0.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/har-schema is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back has-unicode@2.0.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/has-unicode is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back inherits@2.0.4 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/inherits is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back is-typedarray@1.0.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/is-typedarray is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back isarray@1.0.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/isarray is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back isstream@0.1.2 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/isstream is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back jsbn@0.1.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/jsbn is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back json-schema@0.2.3 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/json-schema is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back json-schema-traverse@0.4.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/json-schema-traverse is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back json-stringify-safe@5.0.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/json-stringify-safe is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back mime-db@1.47.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/mime-db is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back mime-types@2.1.30 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/mime-types is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back form-data@2.3.3 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/form-data is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back minimatch@3.0.4 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/minimatch is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back minimist@1.2.5 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/minimist is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back mkdirp@0.5.5 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/mkdirp is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back ms@2.0.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/ms is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back debug@2.6.9 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/debug is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back number-is-nan@1.0.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/number-is-nan is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back is-fullwidth-code-point@1.0.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/is-fullwidth-code-point is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back oauth-sign@0.9.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/oauth-sign is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back object-assign@4.1.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/object-assign is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back path-is-absolute@1.0.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/path-is-absolute is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back pend@1.2.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/pend is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back fd-slicer@1.1.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/fd-slicer is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back performance-now@2.1.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/performance-now is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back process-nextick-args@2.0.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/process-nextick-args is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back psl@1.8.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/psl is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back punycode@2.1.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/punycode is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back qs@6.5.2 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/qs is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back safe-buffer@5.1.2 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/safe-buffer is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back safer-buffer@2.1.2 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/safer-buffer is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back asn1@0.2.4 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/asn1 is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back ecc-jsbn@0.1.2 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/ecc-jsbn is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back signal-exit@3.0.3 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/signal-exit is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back string_decoder@1.1.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/string_decoder is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back strip-ansi@3.0.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/strip-ansi is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back string-width@1.0.2 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/string-width is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back throttleit@1.0.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/throttleit is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back tough-cookie@2.5.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/tough-cookie is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back tunnel-agent@0.6.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/tunnel-agent is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back tweetnacl@0.14.5 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/tweetnacl is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back bcrypt-pbkdf@1.0.2 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/bcrypt-pbkdf is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back sshpk@1.16.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/sshpk is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back typedarray@0.0.6 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/typedarray is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back uri-js@4.4.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/uri-js is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back ajv@6.12.6 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/ajv is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back har-validator@5.1.5 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/har-validator is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back util-deprecate@1.0.2 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/util-deprecate is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back readable-stream@2.3.7 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/readable-stream is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back concat-stream@1.6.2 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/concat-stream is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back uuid@3.4.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/uuid is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back verror@1.10.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/verror is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back jsprim@1.4.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/jsprim is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back http-signature@1.2.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/http-signature is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back wide-align@1.1.3 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/wide-align is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back wrappy@1.0.2 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/wrappy is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back once@1.4.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/once is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back inflight@1.0.6 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/inflight is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back glob@7.1.7 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/glob is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back yauzl@2.10.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/yauzl is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back extract-zip@1.7.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/extract-zip is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back gauge@2.7.4 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/gauge is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back request@2.88.2 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/request is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back request-progress@3.0.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/request-progress is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back rimraf@2.7.1 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/rimraf is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm WARN rollback Rolling back semver@6.3.0 failed (this is probably harmless): /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/node_modules/semver is not a child of /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/ipkg-install/usr/lib
npm timing stage:rollbackFailedOptional Completed in 36ms
npm timing stage:runTopLevelLifecycles Completed in 94320ms
npm ERR! code ELIFECYCLE
npm ERR! errno 1
npm ERR! ejdb2_node@2.0.603 install: `node install.js`
npm ERR! Exit status 1
npm ERR! 
npm ERR! Failed at the ejdb2_node@2.0.603 install script.
npm ERR! This is probably not a problem with npm. There is likely additional logging output above.
npm timing npm Completed in 94634ms

npm ERR! A complete log of this run can be found in:
npm ERR!     /openwrt/tmp/npm-cache-Ni7kRGNU8a/_logs/2021-05-13T19_23_36_284Z-debug.log
make[3]: *** [Makefile:97: /openwrt/build_dir/target-aarch64_cortex-a72_musl/node-ejdb2_node-2.0.603/.built] Error 1
```
