---
title: "compile.44"
date: 2021-08-01 09:45:27.115468
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
npm info using npm@6.14.13
npm info using node@v14.17.3
npm info lifecycle ejdb2_node@2.61.4~preinstall: ejdb2_node@2.61.4
npm timing stage:loadCurrentTree Completed in 11ms
npm timing stage:loadIdealTree:cloneCurrentTree Completed in 0ms
npm timing stage:loadIdealTree:loadShrinkwrap Completed in 1ms
npm http fetch GET 200 https://registry.npmjs.org/gauge 176ms
npm http fetch GET 200 https://registry.npmjs.org/ava 182ms
npm http fetch GET 200 https://registry.npmjs.org/request 186ms
npm http fetch GET 200 https://registry.npmjs.org/rimraf 178ms
npm http fetch GET 200 https://registry.npmjs.org/chai 192ms
npm http fetch GET 200 https://registry.npmjs.org/semver 179ms
npm http fetch GET 200 https://registry.npmjs.org/extract-zip 192ms
npm http fetch GET 200 https://registry.npmjs.org/request-progress 182ms
npm http fetch GET 200 https://registry.npmjs.org/@types%2fnode 227ms
npm http fetch GET 200 https://registry.npmjs.org/ava/-/ava-2.4.0.tgz 122ms
npm http fetch GET 200 https://registry.npmjs.org/semver/-/semver-6.3.0.tgz 104ms
npm http fetch GET 200 https://registry.npmjs.org/extract-zip/-/extract-zip-1.7.0.tgz 105ms
npm http fetch GET 200 https://registry.npmjs.org/request/-/request-2.88.2.tgz 117ms
npm http fetch GET 200 https://registry.npmjs.org/chai/-/chai-4.3.4.tgz 114ms
npm http fetch GET 200 https://registry.npmjs.org/request-progress/-/request-progress-3.0.0.tgz 114ms
npm http fetch GET 200 https://registry.npmjs.org/rimraf/-/rimraf-2.7.1.tgz 117ms
npm http fetch GET 200 https://registry.npmjs.org/gauge/-/gauge-2.7.4.tgz 149ms
npm WARN deprecated request@2.88.2: request has been deprecated, see https://github.com/request/request/issues/3142
npm http fetch GET 200 https://registry.npmjs.org/@types/node/-/node-12.20.17.tgz 125ms
npm http fetch GET 200 https://registry.npmjs.org/assertion-error 46ms
npm http fetch GET 200 https://registry.npmjs.org/check-error 54ms
npm http fetch GET 200 https://registry.npmjs.org/deep-eql 56ms
npm http fetch GET 200 https://registry.npmjs.org/type-detect 75ms
npm http fetch GET 200 https://registry.npmjs.org/pathval 93ms
npm http fetch GET 200 https://registry.npmjs.org/glob 61ms
npm http fetch GET 200 https://registry.npmjs.org/debug 54ms
npm http fetch GET 200 https://registry.npmjs.org/throttleit 82ms
npm http fetch GET 200 https://registry.npmjs.org/concat-stream 70ms
npm http fetch GET 200 https://registry.npmjs.org/get-func-name 105ms
npm http fetch GET 200 https://registry.npmjs.org/assertion-error/-/assertion-error-1.1.0.tgz 59ms
npm http fetch GET 200 https://registry.npmjs.org/check-error/-/check-error-1.0.2.tgz 54ms
npm http fetch GET 200 https://registry.npmjs.org/deep-eql/-/deep-eql-3.0.1.tgz 58ms
npm http fetch GET 200 https://registry.npmjs.org/type-detect/-/type-detect-4.0.8.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/pathval/-/pathval-1.1.1.tgz 60ms
npm http fetch GET 200 https://registry.npmjs.org/yauzl 42ms
npm http fetch GET 200 https://registry.npmjs.org/glob/-/glob-7.1.7.tgz 59ms
npm http fetch GET 200 https://registry.npmjs.org/throttleit/-/throttleit-1.0.0.tgz 54ms
npm http fetch GET 200 https://registry.npmjs.org/debug/-/debug-2.6.9.tgz 60ms
npm http fetch GET 200 https://registry.npmjs.org/get-func-name/-/get-func-name-2.0.0.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/concat-stream/-/concat-stream-1.6.2.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/mkdirp 51ms
npm http fetch GET 200 https://registry.npmjs.org/yauzl/-/yauzl-2.10.0.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/aproba 45ms
npm http fetch GET 200 https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.5.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/has-unicode 34ms
npm http fetch GET 200 https://registry.npmjs.org/object-assign 35ms
npm http fetch GET 200 https://registry.npmjs.org/console-control-strings 41ms
npm http fetch GET 200 https://registry.npmjs.org/signal-exit 48ms
npm http fetch GET 200 https://registry.npmjs.org/strip-ansi 48ms
npm http fetch GET 200 https://registry.npmjs.org/string-width 48ms
npm http fetch GET 200 https://registry.npmjs.org/aproba/-/aproba-1.2.0.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/wide-align 52ms
npm http fetch GET 200 https://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/@ava%2fbabel-preset-stage-4 56ms
npm http fetch GET 200 https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.3.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/wide-align/-/wide-align-1.1.3.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-escapes 46ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fcore 85ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fgenerator 72ms
npm http fetch GET 200 https://registry.npmjs.org/@ava/babel-preset-stage-4/-/babel-preset-stage-4-4.0.0.tgz 84ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-styles 82ms
npm http fetch GET 200 https://registry.npmjs.org/arr-flatten 82ms
npm http fetch GET 200 https://registry.npmjs.org/@concordance%2freact 97ms
npm http fetch GET 200 https://registry.npmjs.org/array-union 84ms
npm http fetch GET 200 https://registry.npmjs.org/array-uniq 84ms
npm http fetch GET 200 https://registry.npmjs.org/@ava%2fbabel-preset-transform-test-files 193ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-escapes/-/ansi-escapes-4.3.2.tgz 93ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/generator/-/generator-7.14.8.tgz 81ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/core/-/core-7.14.8.tgz 83ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz 60ms
npm http fetch GET 200 https://registry.npmjs.org/arrify 61ms
npm http fetch GET 200 https://registry.npmjs.org/array-uniq/-/array-uniq-2.1.0.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/array-union/-/array-union-2.1.0.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/@concordance/react/-/react-2.0.0.tgz 56ms
npm http fetch GET 200 https://registry.npmjs.org/@ava/babel-preset-transform-test-files/-/babel-preset-transform-test-files-6.0.0.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/arr-flatten/-/arr-flatten-1.1.0.tgz 100ms
npm http fetch GET 200 https://registry.npmjs.org/bluebird 36ms
npm http fetch GET 200 https://registry.npmjs.org/arrify/-/arrify-2.0.1.tgz 54ms
npm http fetch GET 200 https://registry.npmjs.org/chokidar 60ms
npm http fetch GET 200 https://registry.npmjs.org/chalk 62ms
npm http fetch GET 200 https://registry.npmjs.org/chunkd 57ms
npm http fetch GET 200 https://registry.npmjs.org/bluebird/-/bluebird-3.7.2.tgz 63ms
npm http fetch GET 200 https://registry.npmjs.org/cli-cursor 46ms
npm http fetch GET 200 https://registry.npmjs.org/clean-yaml-object 48ms
npm http fetch GET 200 https://registry.npmjs.org/ci-parallel-vars 50ms
npm http fetch GET 200 https://registry.npmjs.org/clean-stack 51ms
npm http fetch GET 200 https://registry.npmjs.org/cli-truncate 47ms
npm http fetch GET 200 https://registry.npmjs.org/code-excerpt 61ms
npm http fetch GET 200 https://registry.npmjs.org/chalk/-/chalk-2.4.2.tgz 63ms
npm http fetch GET 200 https://registry.npmjs.org/chunkd/-/chunkd-1.0.0.tgz 66ms
npm http fetch GET 200 https://registry.npmjs.org/chokidar/-/chokidar-3.5.2.tgz 67ms
npm http fetch GET 200 https://registry.npmjs.org/ci-parallel-vars/-/ci-parallel-vars-1.0.1.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/cli-cursor/-/cli-cursor-3.1.0.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/clean-stack/-/clean-stack-2.2.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/cli-truncate/-/cli-truncate-2.1.0.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/clean-yaml-object/-/clean-yaml-object-0.1.0.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/common-path-prefix 30ms
npm http fetch GET 200 https://registry.npmjs.org/code-excerpt/-/code-excerpt-2.1.1.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/concordance 31ms
npm http fetch GET 200 https://registry.npmjs.org/convert-source-map 28ms
npm http fetch GET 200 https://registry.npmjs.org/currently-unhandled 29ms
npm http fetch GET 200 https://registry.npmjs.org/debug/-/debug-4.3.2.tgz 23ms
npm http fetch GET 200 https://registry.npmjs.org/del 25ms
npm http fetch GET 200 https://registry.npmjs.org/common-path-prefix/-/common-path-prefix-1.0.0.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/concordance/-/concordance-4.0.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/dot-prop 57ms
npm http fetch GET 200 https://registry.npmjs.org/emittery 57ms
npm http fetch GET 200 https://registry.npmjs.org/equal-length 45ms
npm http fetch GET 200 https://registry.npmjs.org/del/-/del-4.1.1.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/currently-unhandled/-/currently-unhandled-0.4.1.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/convert-source-map/-/convert-source-map-1.8.0.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/empower-core 59ms
npm http fetch GET 200 https://registry.npmjs.org/escape-string-regexp 42ms
npm http fetch GET 200 https://registry.npmjs.org/equal-length/-/equal-length-1.0.1.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/dot-prop/-/dot-prop-5.3.0.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/empower-core/-/empower-core-1.2.0.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/emittery/-/emittery-0.4.1.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-2.0.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/find-up 37ms
npm http fetch GET 200 https://registry.npmjs.org/figures 42ms
npm http fetch GET 200 https://registry.npmjs.org/esm 52ms
npm http fetch GET 200 https://registry.npmjs.org/get-port 42ms
npm http fetch GET 200 https://registry.npmjs.org/globby 54ms
npm http fetch GET 200 https://registry.npmjs.org/ignore-by-default 28ms
npm http fetch GET 200 https://registry.npmjs.org/figures/-/figures-3.2.0.tgz 75ms
npm http fetch GET 200 https://registry.npmjs.org/get-port/-/get-port-5.1.1.tgz 72ms
npm http fetch GET 200 https://registry.npmjs.org/import-local 69ms
npm http fetch GET 200 https://registry.npmjs.org/esm/-/esm-3.2.25.tgz 75ms
npm http fetch GET 200 https://registry.npmjs.org/find-up/-/find-up-4.1.0.tgz 81ms
npm http fetch GET 200 https://registry.npmjs.org/indent-string 69ms
npm http fetch GET 200 https://registry.npmjs.org/is-ci 70ms
npm http fetch GET 200 https://registry.npmjs.org/is-error 68ms
npm http fetch GET 200 https://registry.npmjs.org/globby/-/globby-10.0.2.tgz 74ms
npm http fetch GET 200 https://registry.npmjs.org/ignore-by-default/-/ignore-by-default-1.0.1.tgz 77ms
npm http fetch GET 200 https://registry.npmjs.org/is-error/-/is-error-2.2.2.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/indent-string/-/indent-string-4.0.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/is-ci/-/is-ci-2.0.0.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/import-local/-/import-local-3.0.2.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/is-plain-object 35ms
npm http fetch GET 200 https://registry.npmjs.org/lodash 35ms
npm http fetch GET 200 https://registry.npmjs.org/make-dir 32ms
npm http fetch GET 200 https://registry.npmjs.org/loud-rejection 37ms
npm http fetch GET 200 https://registry.npmjs.org/is-observable 46ms
npm http fetch GET 200 https://registry.npmjs.org/is-promise 46ms
npm http fetch GET 200 https://registry.npmjs.org/matcher 34ms
npm http fetch GET 200 https://registry.npmjs.org/meow 46ms
npm http fetch GET 200 https://registry.npmjs.org/md5-hex 127ms
npm http fetch GET 200 https://registry.npmjs.org/micromatch 130ms
npm http fetch GET 200 https://registry.npmjs.org/is-plain-object/-/is-plain-object-3.0.1.tgz 130ms
npm http fetch GET 200 https://registry.npmjs.org/make-dir/-/make-dir-3.1.0.tgz 125ms
npm http fetch GET 200 https://registry.npmjs.org/loud-rejection/-/loud-rejection-2.2.0.tgz 125ms
npm http fetch GET 200 https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz 131ms
npm http fetch GET 200 https://registry.npmjs.org/is-observable/-/is-observable-2.1.0.tgz 125ms
npm http fetch GET 200 https://registry.npmjs.org/is-promise/-/is-promise-2.2.2.tgz 123ms
npm http fetch GET 200 https://registry.npmjs.org/matcher/-/matcher-2.1.0.tgz 116ms
npm http fetch GET 200 https://registry.npmjs.org/meow/-/meow-5.0.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/md5-hex/-/md5-hex-3.0.1.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/micromatch/-/micromatch-4.0.4.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/ms 24ms
npm http fetch GET 200 https://registry.npmjs.org/ora 30ms
npm http fetch GET 200 https://registry.npmjs.org/observable-to-promise 32ms
npm http fetch GET 200 https://registry.npmjs.org/pretty-ms 33ms
npm http fetch GET 200 https://registry.npmjs.org/package-hash 37ms
npm http fetch GET 200 https://registry.npmjs.org/plur 39ms
npm http fetch GET 200 https://registry.npmjs.org/pkg-conf 44ms
npm http fetch GET 200 https://registry.npmjs.org/require-precompiled 34ms
npm http fetch GET 200 https://registry.npmjs.org/slash 34ms
npm http fetch GET 200 https://registry.npmjs.org/resolve-cwd 40ms
npm http fetch GET 200 https://registry.npmjs.org/ms/-/ms-2.1.3.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/observable-to-promise/-/observable-to-promise-1.0.0.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/ora/-/ora-3.4.0.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/pretty-ms/-/pretty-ms-5.1.0.tgz 24ms
npm http fetch GET 200 https://registry.npmjs.org/package-hash/-/package-hash-4.0.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/plur/-/plur-3.1.1.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/slash/-/slash-3.0.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/pkg-conf/-/pkg-conf-3.1.0.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/require-precompiled/-/require-precompiled-0.1.0.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/resolve-cwd/-/resolve-cwd-3.0.0.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/source-map-support 46ms
npm http fetch GET 200 https://registry.npmjs.org/strip-ansi/-/strip-ansi-5.2.0.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/strip-bom-buf 32ms
npm http fetch GET 200 https://registry.npmjs.org/stack-utils 38ms
npm http fetch GET 200 https://registry.npmjs.org/trim-off-newlines 24ms
npm http fetch GET 200 https://registry.npmjs.org/trim-right 25ms
npm http fetch GET 200 https://registry.npmjs.org/strip-bom-buf/-/strip-bom-buf-2.0.0.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/supertap 54ms
npm http fetch GET 200 https://registry.npmjs.org/source-map-support/-/source-map-support-0.5.19.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/unique-temp-dir 45ms
npm http fetch GET 200 https://registry.npmjs.org/update-notifier 45ms
npm http fetch GET 200 https://registry.npmjs.org/stack-utils/-/stack-utils-1.0.5.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/supports-color 64ms
npm http fetch GET 200 https://registry.npmjs.org/write-file-atomic 45ms
npm http fetch GET 200 https://registry.npmjs.org/trim-off-newlines/-/trim-off-newlines-1.0.1.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/trim-right/-/trim-right-1.0.1.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/unique-temp-dir/-/unique-temp-dir-1.0.0.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/update-notifier/-/update-notifier-3.0.1.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/supertap/-/supertap-1.0.0.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/supports-color/-/supports-color-7.2.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/write-file-atomic/-/write-file-atomic-3.0.3.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/aws-sign2 27ms
npm http fetch GET 200 https://registry.npmjs.org/caseless 28ms
npm http fetch GET 200 https://registry.npmjs.org/aws4 34ms
npm http fetch GET 200 https://registry.npmjs.org/combined-stream 55ms
npm http fetch GET 200 https://registry.npmjs.org/extend 46ms
npm http fetch GET 200 https://registry.npmjs.org/aws-sign2/-/aws-sign2-0.7.0.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/aws4/-/aws4-1.11.0.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/forever-agent 28ms
npm http fetch GET 200 https://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/har-validator 50ms
npm http fetch GET 200 https://registry.npmjs.org/is-typedarray 43ms
npm http fetch GET 200 https://registry.npmjs.org/form-data 57ms
npm http fetch GET 200 https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/http-signature 46ms
npm http fetch GET 200 https://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/extend/-/extend-3.0.2.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/json-stringify-safe 45ms
npm http fetch GET 200 https://registry.npmjs.org/isstream 60ms
npm http fetch GET 200 https://registry.npmjs.org/mime-types 48ms
npm http fetch GET 200 https://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/har-validator/-/har-validator-5.1.5.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/http-signature/-/http-signature-1.2.0.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/form-data/-/form-data-2.3.3.tgz 45ms
npm WARN deprecated har-validator@5.1.5: this library is no longer supported
npm http fetch GET 200 https://registry.npmjs.org/oauth-sign 30ms
npm http fetch GET 200 https://registry.npmjs.org/performance-now 30ms
npm http fetch GET 200 https://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/qs 34ms
npm http fetch GET 200 https://registry.npmjs.org/mime-types/-/mime-types-2.1.32.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/safe-buffer 33ms
npm http fetch GET 200 https://registry.npmjs.org/tunnel-agent 35ms
npm http fetch GET 200 https://registry.npmjs.org/uuid 35ms
npm http fetch GET 200 https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/tough-cookie 56ms
npm http fetch GET 200 https://registry.npmjs.org/oauth-sign/-/oauth-sign-0.9.0.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/qs/-/qs-6.5.2.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/fs.realpath 35ms
npm http fetch GET 200 https://registry.npmjs.org/inflight 49ms
npm http fetch GET 200 https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/uuid/-/uuid-3.4.0.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/tough-cookie/-/tough-cookie-2.5.0.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/inherits 35ms
npm WARN deprecated uuid@3.4.0: Please upgrade  to version 7 or higher.  Older versions may use Math.random() in certain circumstances, which is known to be problematic.  See https://v8.dev/blog/math-random for details.
npm http fetch GET 200 https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/once 38ms
npm http fetch GET 200 https://registry.npmjs.org/minimatch 49ms
npm http fetch GET 200 https://registry.npmjs.org/path-is-absolute 38ms
npm http fetch GET 200 https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/ms/-/ms-2.0.0.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-from 49ms
npm http fetch GET 200 https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/readable-stream 34ms
npm http fetch GET 200 https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/once/-/once-1.4.0.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/typedarray 34ms
npm http fetch GET 200 https://registry.npmjs.org/fd-slicer 43ms
npm http fetch GET 200 https://registry.npmjs.org/minimist 35ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-crc32 41ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.2.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.7.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/code-point-at 33ms
npm http fetch GET 200 https://registry.npmjs.org/typedarray/-/typedarray-0.0.6.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/is-fullwidth-code-point 60ms
npm http fetch GET 200 https://registry.npmjs.org/minimist/-/minimist-1.2.5.tgz 54ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-regex 52ms
npm http fetch GET 200 https://registry.npmjs.org/fd-slicer/-/fd-slicer-1.1.0.tgz 59ms
npm http fetch GET 200 https://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz 46ms
npm http fetch GET 200 https://registry.npmjs.org/string-width/-/string-width-2.1.1.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-crc32/-/buffer-crc32-0.2.13.tgz 61ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fplugin-proposal-async-generator-functions 49ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fplugin-proposal-dynamic-import 54ms
npm http fetch GET 200 https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fplugin-transform-modules-commonjs 46ms
npm http fetch GET 200 https://registry.npmjs.org/type-fest 44ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fplugin-proposal-optional-catch-binding 63ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fplugin-transform-dotall-regex 56ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/plugin-proposal-async-generator-functions/-/plugin-proposal-async-generator-functions-7.14.7.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/source-map 38ms
npm http fetch GET 200 https://registry.npmjs.org/jsesc 49ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2ftypes 61ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/plugin-proposal-dynamic-import/-/plugin-proposal-dynamic-import-7.14.5.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/plugin-transform-modules-commonjs/-/plugin-transform-modules-commonjs-7.14.5.tgz 70ms
npm http fetch GET 200 https://registry.npmjs.org/type-fest/-/type-fest-0.21.3.tgz 67ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/types/-/types-7.14.8.tgz 54ms
npm http fetch GET 200 https://registry.npmjs.org/jsesc/-/jsesc-2.5.2.tgz 63ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fcode-frame 64ms
npm http fetch GET 200 https://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz 68ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-compilation-targets 54ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/plugin-proposal-optional-catch-binding/-/plugin-proposal-optional-catch-binding-7.14.5.tgz 74ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/plugin-transform-dotall-regex/-/plugin-transform-dotall-regex-7.14.5.tgz 74ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-module-transforms 80ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.14.5.tgz 90ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.14.5.tgz 93ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fparser 73ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelpers 88ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2ftemplate 76ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2ftraverse 78ms
npm http fetch GET 200 https://registry.npmjs.org/gensync 44ms
npm http fetch GET 200 https://registry.npmjs.org/json5 39ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.14.8.tgz 72ms
npm http fetch GET 200 https://registry.npmjs.org/color-convert 26ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helpers/-/helpers-7.14.8.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/template/-/template-7.14.5.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/traverse/-/traverse-7.14.8.tgz 54ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/parser/-/parser-7.14.8.tgz 66ms
npm http fetch GET 200 https://registry.npmjs.org/babel-plugin-espower 52ms
npm http fetch GET 200 https://registry.npmjs.org/gensync/-/gensync-1.0.0-beta.2.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/json5/-/json5-2.2.0.tgz 59ms
npm http fetch GET 200 https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz 56ms
npm http fetch GET 200 https://registry.npmjs.org/arrify/-/arrify-1.0.1.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/@ava%2fbabel-plugin-throws-helper 92ms
npm http fetch GET 200 https://registry.npmjs.org/babel-plugin-espower/-/babel-plugin-espower-3.0.1.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/anymatch 32ms
npm http fetch GET 200 https://registry.npmjs.org/supports-color/-/supports-color-5.5.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/glob-parent 38ms
npm http fetch GET 200 https://registry.npmjs.org/braces 43ms
npm http fetch GET 200 https://registry.npmjs.org/is-glob 34ms
npm http fetch GET 200 https://registry.npmjs.org/is-binary-path 50ms
npm http fetch GET 200 https://registry.npmjs.org/normalize-path 26ms
npm http fetch GET 200 https://registry.npmjs.org/anymatch/-/anymatch-3.1.2.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/braces/-/braces-3.0.2.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/@ava/babel-plugin-throws-helper/-/babel-plugin-throws-helper-4.0.0.tgz 77ms
npm http fetch GET 200 https://registry.npmjs.org/readdirp 38ms
npm http fetch GET 200 https://registry.npmjs.org/restore-cursor 34ms
npm http fetch GET 200 https://registry.npmjs.org/is-binary-path/-/is-binary-path-2.1.0.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/normalize-path/-/normalize-path-3.0.0.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/fsevents 46ms
npm http fetch GET 200 https://registry.npmjs.org/is-glob/-/is-glob-4.0.1.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/slice-ansi 43ms
npm http fetch GET 200 https://registry.npmjs.org/restore-cursor/-/restore-cursor-3.1.0.tgz 65ms
npm http fetch GET 200 https://registry.npmjs.org/fsevents/-/fsevents-2.3.2.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/readdirp/-/readdirp-3.6.0.tgz 69ms
npm http fetch GET 200 https://registry.npmjs.org/convert-to-spaces 57ms
npm http fetch GET 200 https://registry.npmjs.org/string-width/-/string-width-4.2.2.tgz 58ms
npm http fetch GET 200 https://registry.npmjs.org/slice-ansi/-/slice-ansi-3.0.0.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/ms/-/ms-2.1.2.tgz 58ms
npm http fetch GET 200 https://registry.npmjs.org/date-time 62ms
npm http fetch GET 200 https://registry.npmjs.org/esutils 57ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.flattendeep 43ms
npm http fetch GET 200 https://registry.npmjs.org/js-string-escape 47ms
npm http fetch GET 200 https://registry.npmjs.org/fast-diff 62ms
npm http fetch GET 200 https://registry.npmjs.org/convert-to-spaces/-/convert-to-spaces-1.0.2.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.clonedeep 46ms
npm http fetch GET 200 https://registry.npmjs.org/date-time/-/date-time-2.1.0.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.merge 47ms
npm http fetch GET 200 https://registry.npmjs.org/md5-hex/-/md5-hex-2.0.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.flattendeep/-/lodash.flattendeep-4.4.0.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/js-string-escape/-/js-string-escape-1.0.1.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/fast-diff/-/fast-diff-1.2.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/semver/-/semver-5.7.1.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.merge/-/lodash.merge-4.6.2.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/well-known-symbols 23ms
npm http fetch GET 200 https://registry.npmjs.org/globby/-/globby-6.1.0.tgz 23ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.clonedeep/-/lodash.clonedeep-4.5.0.tgz 60ms
npm http fetch GET 200 https://registry.npmjs.org/p-map 24ms
npm http fetch GET 200 https://registry.npmjs.org/@types%2fglob 46ms
npm http fetch GET 200 https://registry.npmjs.org/is-path-in-cwd 39ms
npm http fetch GET 200 https://registry.npmjs.org/well-known-symbols/-/well-known-symbols-2.0.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/is-path-cwd 46ms
npm http fetch GET 200 https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/pify 36ms
npm http fetch GET 200 https://registry.npmjs.org/array-find-index 27ms
npm http fetch GET 200 https://registry.npmjs.org/p-map/-/p-map-2.1.0.tgz 24ms
npm http fetch GET 200 https://registry.npmjs.org/@types/glob/-/glob-7.1.4.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/is-path-in-cwd/-/is-path-in-cwd-2.1.0.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/is-path-cwd/-/is-path-cwd-2.2.0.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/pify/-/pify-4.0.1.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/call-signature 40ms
npm http fetch GET 200 https://registry.npmjs.org/core-js 38ms
npm http fetch GET 200 https://registry.npmjs.org/is-obj 52ms
npm http fetch GET 200 https://registry.npmjs.org/locate-path 36ms
npm http fetch GET 200 https://registry.npmjs.org/path-exists 33ms
npm http fetch GET 200 https://registry.npmjs.org/dir-glob 35ms
npm http fetch GET 200 https://registry.npmjs.org/array-find-index/-/array-find-index-1.0.2.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/core-js/-/core-js-2.6.12.tgz 84ms
npm http fetch GET 200 https://registry.npmjs.org/locate-path/-/locate-path-5.0.0.tgz 82ms
npm http fetch GET 200 https://registry.npmjs.org/dir-glob/-/dir-glob-3.0.1.tgz 76ms
npm http fetch GET 200 https://registry.npmjs.org/call-signature/-/call-signature-0.0.2.tgz 87ms
npm http fetch GET 200 https://registry.npmjs.org/merge2 75ms
npm http fetch GET 200 https://registry.npmjs.org/ignore 81ms
npm http fetch GET 200 https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz 84ms
npm http fetch GET 200 https://registry.npmjs.org/fast-glob 91ms
npm http fetch GET 200 https://registry.npmjs.org/is-obj/-/is-obj-2.0.0.tgz 91ms
npm WARN deprecated core-js@2.6.12: core-js@<3.3 is no longer maintained and not recommended for usage due to the number of issues. Because of the V8 engine whims, feature detection in old core-js versions could cause a slowdown up to 100x even if nothing is polyfilled. Please, upgrade your dependencies to the actual version of core-js.
npm http fetch GET 200 https://registry.npmjs.org/fast-glob/-/fast-glob-3.2.7.tgz 20ms
npm http fetch GET 200 https://registry.npmjs.org/merge2/-/merge2-1.4.1.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/ignore/-/ignore-5.1.8.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/decamelize-keys 30ms
npm http fetch GET 200 https://registry.npmjs.org/minimist-options 33ms
npm http fetch GET 200 https://registry.npmjs.org/ci-info 41ms
npm http fetch GET 200 https://registry.npmjs.org/pkg-dir 41ms
npm http fetch GET 200 https://registry.npmjs.org/loud-rejection/-/loud-rejection-1.6.0.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/camelcase-keys 42ms
npm http fetch GET 200 https://registry.npmjs.org/normalize-package-data 32ms
npm http fetch GET 200 https://registry.npmjs.org/redent 27ms
npm http fetch GET 200 https://registry.npmjs.org/decamelize-keys/-/decamelize-keys-1.1.0.tgz 20ms
npm http fetch GET 200 https://registry.npmjs.org/read-pkg-up 35ms
npm http fetch GET 200 https://registry.npmjs.org/minimist-options/-/minimist-options-3.0.2.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/camelcase-keys/-/camelcase-keys-4.2.0.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/pkg-dir/-/pkg-dir-4.2.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/ci-info/-/ci-info-2.0.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/trim-newlines 29ms
npm http fetch GET 200 https://registry.npmjs.org/normalize-package-data/-/normalize-package-data-2.5.0.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/redent/-/redent-2.0.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/yargs-parser 39ms
npm http fetch GET 200 https://registry.npmjs.org/read-pkg-up/-/read-pkg-up-3.0.0.tgz 46ms
npm http fetch GET 200 https://registry.npmjs.org/picomatch 21ms
npm http fetch GET 200 https://registry.npmjs.org/trim-newlines/-/trim-newlines-2.0.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/blueimp-md5 29ms
npm http fetch GET 200 https://registry.npmjs.org/cli-spinners 27ms
npm http fetch GET 200 https://registry.npmjs.org/yargs-parser/-/yargs-parser-10.1.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/cli-cursor/-/cli-cursor-2.1.0.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/log-symbols 27ms
npm http fetch GET 200 https://registry.npmjs.org/wcwidth 29ms
npm http fetch GET 200 https://registry.npmjs.org/parse-ms 28ms
npm http fetch GET 200 https://registry.npmjs.org/picomatch/-/picomatch-2.3.0.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/cli-spinners/-/cli-spinners-2.6.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/symbol-observable 39ms
npm http fetch GET 200 https://registry.npmjs.org/blueimp-md5/-/blueimp-md5-2.18.0.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/log-symbols/-/log-symbols-2.2.0.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.islength 450ms
npm http fetch GET 200 https://registry.npmjs.org/wcwidth/-/wcwidth-1.0.1.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/irregular-plurals 36ms
npm http fetch GET 200 https://registry.npmjs.org/parse-ms/-/parse-ms-2.1.0.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/graceful-fs 41ms
npm http fetch GET 200 https://registry.npmjs.org/symbol-observable/-/symbol-observable-1.2.0.tgz 23ms
npm http fetch GET 200 https://registry.npmjs.org/hasha 27ms
npm http fetch GET 200 https://registry.npmjs.org/release-zalgo 33ms
npm http fetch GET 200 https://registry.npmjs.org/load-json-file 32ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.islength/-/lodash.islength-4.0.1.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/irregular-plurals/-/irregular-plurals-2.0.0.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/resolve-from 41ms
npm http fetch GET 200 https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.6.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/find-up/-/find-up-3.0.0.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-regex/-/ansi-regex-4.1.0.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/hasha/-/hasha-5.2.2.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/is-utf8 27ms
npm http fetch GET 200 https://registry.npmjs.org/release-zalgo/-/release-zalgo-1.0.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/resolve-from/-/resolve-from-5.0.0.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/load-json-file/-/load-json-file-5.3.0.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/js-yaml 38ms
npm http fetch GET 200 https://registry.npmjs.org/serialize-error 47ms
npm http fetch GET 200 https://registry.npmjs.org/is-utf8/-/is-utf8-0.2.1.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/indent-string/-/indent-string-3.2.0.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/strip-ansi/-/strip-ansi-4.0.0.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/os-tmpdir 43ms
npm http fetch GET 200 https://registry.npmjs.org/boxen 59ms
npm http fetch GET 200 https://registry.npmjs.org/uid2 59ms
npm http fetch GET 200 https://registry.npmjs.org/has-yarn 37ms
npm http fetch GET 200 https://registry.npmjs.org/js-yaml/-/js-yaml-3.14.1.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/serialize-error/-/serialize-error-2.1.0.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz 46ms
npm http fetch GET 200 https://registry.npmjs.org/import-lazy 41ms
npm http fetch GET 200 https://registry.npmjs.org/is-npm 43ms
npm http fetch GET 200 https://registry.npmjs.org/is-installed-globally 45ms
npm http fetch GET 200 https://registry.npmjs.org/configstore 122ms
npm http fetch GET 200 https://registry.npmjs.org/boxen/-/boxen-3.2.0.tgz 84ms
npm http fetch GET 200 https://registry.npmjs.org/has-yarn/-/has-yarn-2.1.0.tgz 83ms
npm http fetch GET 200 https://registry.npmjs.org/is-installed-globally/-/is-installed-globally-0.1.0.tgz 77ms
npm http fetch GET 200 https://registry.npmjs.org/is-npm/-/is-npm-3.0.0.tgz 78ms
npm http fetch GET 200 https://registry.npmjs.org/uid2/-/uid2-0.0.3.tgz 86ms
npm http fetch GET 200 https://registry.npmjs.org/import-lazy/-/import-lazy-2.1.0.tgz 81ms
npm http fetch GET 200 https://registry.npmjs.org/is-yarn-global 21ms
npm http fetch GET 200 https://registry.npmjs.org/configstore/-/configstore-4.0.0.tgz 24ms
npm http fetch GET 200 https://registry.npmjs.org/latest-version 31ms
npm http fetch GET 200 https://registry.npmjs.org/imurmurhash 45ms
npm http fetch GET 200 https://registry.npmjs.org/semver-diff 57ms
npm http fetch GET 200 https://registry.npmjs.org/typedarray-to-buffer 44ms
npm http fetch GET 200 https://registry.npmjs.org/has-flag 52ms
npm http fetch GET 200 https://registry.npmjs.org/ajv 48ms
npm http fetch GET 200 https://registry.npmjs.org/xdg-basedir 58ms
npm http fetch GET 200 https://registry.npmjs.org/delayed-stream 57ms
npm http fetch GET 200 https://registry.npmjs.org/har-schema 46ms
npm http fetch GET 200 https://registry.npmjs.org/is-yarn-global/-/is-yarn-global-0.3.0.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/latest-version/-/latest-version-5.1.0.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/semver-diff/-/semver-diff-2.1.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/typedarray-to-buffer/-/typedarray-to-buffer-3.1.5.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/has-flag/-/has-flag-4.0.0.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/xdg-basedir/-/xdg-basedir-3.0.0.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/ajv/-/ajv-6.12.6.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/har-schema/-/har-schema-2.0.0.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/assert-plus 45ms
npm http fetch GET 200 https://registry.npmjs.org/jsprim 42ms
npm http fetch GET 200 https://registry.npmjs.org/sshpk 31ms
npm http fetch GET 200 https://registry.npmjs.org/mime-db 28ms
npm http fetch GET 200 https://registry.npmjs.org/asynckit 39ms
npm http fetch GET 200 https://registry.npmjs.org/jsprim/-/jsprim-1.4.1.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/psl 48ms
npm http fetch GET 200 https://registry.npmjs.org/wrappy 50ms
npm http fetch GET 200 https://registry.npmjs.org/core-util-is 42ms
npm http fetch GET 200 https://registry.npmjs.org/punycode 56ms
npm http fetch GET 200 https://registry.npmjs.org/sshpk/-/sshpk-1.16.1.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/mime-db/-/mime-db-1.49.0.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/brace-expansion 53ms
npm http fetch GET 200 https://registry.npmjs.org/psl/-/psl-1.8.0.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/isarray 31ms
npm http fetch GET 200 https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/process-nextick-args 29ms
npm http fetch GET 200 https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/punycode/-/punycode-2.1.1.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/util-deprecate 36ms
npm http fetch GET 200 https://registry.npmjs.org/string_decoder 38ms
npm http fetch GET 200 https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz 24ms
npm http fetch GET 200 https://registry.npmjs.org/pend 44ms
npm http fetch GET 200 https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-2.0.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/number-is-nan 38ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-plugin-utils 44ms
npm http fetch GET 200 https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fplugin-syntax-async-generators 38ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-remap-async-to-generator 49ms
npm http fetch GET 200 https://registry.npmjs.org/pend/-/pend-1.2.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fplugin-syntax-dynamic-import 44ms
npm http fetch GET 200 https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/babel-plugin-dynamic-import-node 24ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.14.5.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-remap-async-to-generator/-/helper-remap-async-to-generator-7.14.5.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/plugin-syntax-dynamic-import/-/plugin-syntax-dynamic-import-7.8.3.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/to-fast-properties 41ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fplugin-syntax-optional-catch-binding 41ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/plugin-syntax-async-generators/-/plugin-syntax-async-generators-7.8.4.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-simple-access 60ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-validator-identifier 48ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-create-regexp-features-plugin 42ms
npm http fetch GET 200 https://registry.npmjs.org/babel-plugin-dynamic-import-node/-/babel-plugin-dynamic-import-node-2.3.3.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fcompat-data 33ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/plugin-syntax-optional-catch-binding/-/plugin-syntax-optional-catch-binding-7.8.3.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-validator-option 42ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-simple-access/-/helper-simple-access-7.14.8.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.14.8.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/browserslist 35ms
npm http fetch GET 200 https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-2.0.0.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-create-regexp-features-plugin/-/helper-create-regexp-features-plugin-7.14.5.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-module-imports 46ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhighlight 54ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.14.7.tgz 63ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.14.5.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/browserslist/-/browserslist-4.16.6.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.14.5.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/highlight/-/highlight-7.14.5.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-split-export-declaration 37ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-function-name 37ms
npm http fetch GET 200 https://registry.npmjs.org/color-name 30ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-replace-supers 55ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-hoist-variables 45ms
npm http fetch GET 200 https://registry.npmjs.org/espower-location-detector 30ms
npm http fetch GET 200 https://registry.npmjs.org/globals 46ms
npm http fetch GET 200 https://registry.npmjs.org/call-matcher 37ms
npm http fetch GET 200 https://registry.npmjs.org/espurify 29ms
npm http fetch GET 200 https://registry.npmjs.org/estraverse 31ms
npm http fetch GET 200 https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz 23ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-split-export-declaration/-/helper-split-export-declaration-7.14.5.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-function-name/-/helper-function-name-7.14.5.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/espower-location-detector/-/espower-location-detector-1.0.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/globals/-/globals-11.12.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/espurify/-/espurify-1.8.1.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-hoist-variables/-/helper-hoist-variables-7.14.5.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/estraverse/-/estraverse-4.3.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-replace-supers/-/helper-replace-supers-7.14.5.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/call-matcher/-/call-matcher-1.1.0.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/has-flag/-/has-flag-3.0.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/fill-range 23ms
npm http fetch GET 200 https://registry.npmjs.org/binary-extensions 22ms
npm http fetch GET 200 https://registry.npmjs.org/emoji-regex 20ms
npm http fetch GET 200 https://registry.npmjs.org/is-extglob 28ms
npm http fetch GET 200 https://registry.npmjs.org/onetime 28ms
npm http fetch GET 200 https://registry.npmjs.org/astral-regex 27ms
npm http fetch GET 200 https://registry.npmjs.org/md5-o-matic 29ms
npm http fetch GET 200 https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.0.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/fill-range/-/fill-range-7.0.1.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/binary-extensions/-/binary-extensions-2.2.0.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/time-zone 48ms
npm http fetch GET 200 https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/onetime/-/onetime-5.1.2.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/astral-regex/-/astral-regex-2.0.0.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/md5-o-matic/-/md5-o-matic-0.1.1.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/array-union/-/array-union-1.0.2.tgz 25ms
npm http fetch GET 200 https://registry.npmjs.org/time-zone/-/time-zone-1.0.0.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/pify/-/pify-2.3.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/pinkie-promise 38ms
npm http fetch GET 200 https://registry.npmjs.org/p-locate 25ms
npm http fetch GET 200 https://registry.npmjs.org/@types%2fminimatch 41ms
npm http fetch GET 200 https://registry.npmjs.org/is-path-inside 30ms
npm http fetch GET 200 https://registry.npmjs.org/@types/node/-/node-16.4.9.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/path-type 51ms
npm http fetch GET 200 https://registry.npmjs.org/pinkie-promise/-/pinkie-promise-2.0.1.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/decamelize 31ms
npm http fetch GET 200 https://registry.npmjs.org/@nodelib%2ffs.stat 44ms
npm http fetch GET 200 https://registry.npmjs.org/p-locate/-/p-locate-4.1.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/map-obj 33ms
npm http fetch GET 200 https://registry.npmjs.org/@nodelib%2ffs.walk 54ms
npm http fetch GET 200 https://registry.npmjs.org/is-path-inside/-/is-path-inside-2.1.0.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/@types/minimatch/-/minimatch-3.0.5.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/path-type/-/path-type-4.0.0.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/map-obj/-/map-obj-1.0.1.tgz 23ms
npm http fetch GET 200 https://registry.npmjs.org/decamelize/-/decamelize-1.2.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/is-plain-obj 24ms
npm http fetch GET 200 https://registry.npmjs.org/camelcase 31ms
npm http fetch GET 200 https://registry.npmjs.org/quick-lru 31ms
npm http fetch GET 200 https://registry.npmjs.org/hosted-git-info 31ms
npm http fetch GET 200 https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/map-obj/-/map-obj-2.0.0.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz 46ms
npm http fetch GET 200 https://registry.npmjs.org/resolve 39ms
npm http fetch GET 200 https://registry.npmjs.org/validate-npm-package-license 37ms
npm http fetch GET 200 https://registry.npmjs.org/is-plain-obj/-/is-plain-obj-1.1.0.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/strip-indent 32ms
npm http fetch GET 200 https://registry.npmjs.org/camelcase/-/camelcase-4.1.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/hosted-git-info/-/hosted-git-info-2.8.9.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/quick-lru/-/quick-lru-1.1.0.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/resolve/-/resolve-1.20.0.tgz 24ms
npm http fetch GET 200 https://registry.npmjs.org/find-up/-/find-up-2.1.0.tgz 25ms
npm http fetch GET 200 https://registry.npmjs.org/validate-npm-package-license/-/validate-npm-package-license-3.0.4.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/read-pkg 44ms
npm http fetch GET 200 https://registry.npmjs.org/locate-path/-/locate-path-3.0.0.tgz 23ms
npm http fetch GET 200 https://registry.npmjs.org/strip-indent/-/strip-indent-2.0.0.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/restore-cursor/-/restore-cursor-2.0.0.tgz 60ms
npm http fetch GET 200 https://registry.npmjs.org/defaults 52ms
npm http fetch GET 200 https://registry.npmjs.org/is-stream 44ms
npm http fetch GET 200 https://registry.npmjs.org/type-fest/-/type-fest-0.8.1.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/es6-error 34ms
npm http fetch GET 200 https://registry.npmjs.org/parse-json 31ms
npm http fetch GET 200 https://registry.npmjs.org/read-pkg/-/read-pkg-3.0.0.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/type-fest/-/type-fest-0.3.1.tgz 23ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-regex/-/ansi-regex-3.0.0.tgz 22ms
npm http fetch GET 200 https://registry.npmjs.org/es6-error/-/es6-error-4.1.1.tgz 19ms
npm http fetch GET 200 https://registry.npmjs.org/defaults/-/defaults-1.0.3.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/esprima 29ms
npm http fetch GET 200 https://registry.npmjs.org/argparse 32ms
npm http fetch GET 200 https://registry.npmjs.org/parse-json/-/parse-json-4.0.0.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/strip-bom 48ms
npm http fetch GET 200 https://registry.npmjs.org/is-stream/-/is-stream-2.0.1.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-align 36ms
npm http fetch GET 200 https://registry.npmjs.org/cli-boxes 40ms
npm http fetch GET 200 https://registry.npmjs.org/camelcase/-/camelcase-5.3.1.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/string-width/-/string-width-3.1.0.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/term-size 37ms
npm http fetch GET 200 https://registry.npmjs.org/esprima/-/esprima-4.0.1.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/argparse/-/argparse-1.0.10.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/strip-bom/-/strip-bom-3.0.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-align/-/ansi-align-3.0.0.tgz 46ms
npm http fetch GET 200 https://registry.npmjs.org/global-dirs 42ms
npm http fetch GET 200 https://registry.npmjs.org/widest-line 53ms
npm http fetch GET 200 https://registry.npmjs.org/term-size/-/term-size-1.2.0.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/cli-boxes/-/cli-boxes-2.2.1.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/make-dir/-/make-dir-1.3.0.tgz 22ms
npm http fetch GET 200 https://registry.npmjs.org/write-file-atomic/-/write-file-atomic-2.4.3.tgz 20ms
npm http fetch GET 200 https://registry.npmjs.org/is-path-inside/-/is-path-inside-1.0.1.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/dot-prop/-/dot-prop-4.2.1.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/widest-line/-/widest-line-2.0.1.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/package-json 33ms
npm http fetch GET 200 https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz 7ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/fast-deep-equal 32ms
npm http fetch GET 200 https://registry.npmjs.org/unique-string 44ms
npm http fetch GET 200 https://registry.npmjs.org/global-dirs/-/global-dirs-0.1.1.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/fast-json-stable-stringify 52ms
npm http fetch GET 200 https://registry.npmjs.org/json-schema-traverse 38ms
npm http fetch GET 200 https://registry.npmjs.org/uri-js 38ms
npm http fetch GET 200 https://registry.npmjs.org/package-json/-/package-json-6.5.0.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/unique-string/-/unique-string-1.0.0.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/extsprintf 39ms
npm http fetch GET 200 https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/verror 38ms
npm http fetch GET 200 https://registry.npmjs.org/asn1 38ms
npm http fetch GET 200 https://registry.npmjs.org/json-schema 41ms
npm http fetch GET 200 https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/dashdash 30ms
npm http fetch GET 200 https://registry.npmjs.org/getpass 31ms
npm http fetch GET 200 https://registry.npmjs.org/safer-buffer 34ms
npm http fetch GET 200 https://registry.npmjs.org/asn1/-/asn1-0.2.4.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/json-schema/-/json-schema-0.2.3.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/verror/-/verror-1.10.0.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz 25ms
npm http fetch GET 200 https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/bcrypt-pbkdf 29ms
npm http fetch GET 200 https://registry.npmjs.org/jsbn 44ms
npm http fetch GET 200 https://registry.npmjs.org/ecc-jsbn 38ms
npm http fetch GET 200 https://registry.npmjs.org/tweetnacl 42ms
npm http fetch GET 200 https://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.2.tgz 21ms
npm http fetch GET 200 https://registry.npmjs.org/balanced-match 28ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-annotate-as-pure 36ms
npm http fetch GET 200 https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/concat-map 46ms
npm http fetch GET 200 https://registry.npmjs.org/object.assign 28ms
npm http fetch GET 200 https://registry.npmjs.org/regexpu-core 29ms
npm http fetch GET 200 https://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.2.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/caniuse-lite 48ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-wrap-function 76ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-annotate-as-pure/-/helper-annotate-as-pure-7.14.5.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/regexpu-core/-/regexpu-core-4.7.1.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/object.assign/-/object.assign-4.1.2.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/colorette 68ms
npm http fetch GET 200 https://registry.npmjs.org/electron-to-chromium 83ms
npm http fetch GET 200 https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001248.tgz 82ms
npm http fetch GET 200 https://registry.npmjs.org/escalade 82ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-wrap-function/-/helper-wrap-function-7.14.5.tgz 82ms
npm http fetch GET 200 https://registry.npmjs.org/node-releases 38ms
npm http fetch GET 200 https://registry.npmjs.org/colorette/-/colorette-1.2.2.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/js-tokens 38ms
npm http fetch GET 200 https://registry.npmjs.org/is-url 42ms
npm http fetch GET 200 https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.3.792.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-get-function-arity 46ms
npm http fetch GET 200 https://registry.npmjs.org/xtend 38ms
npm http fetch GET 200 https://registry.npmjs.org/escalade/-/escalade-3.1.1.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-optimise-call-expression 43ms
npm http fetch GET 200 https://registry.npmjs.org/node-releases/-/node-releases-1.1.73.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-member-expression-to-functions 45ms
npm http fetch GET 200 https://registry.npmjs.org/is-url/-/is-url-1.2.4.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/deep-equal 41ms
npm http fetch GET 200 https://registry.npmjs.org/xtend/-/xtend-4.0.2.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-get-function-arity/-/helper-get-function-arity-7.14.5.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-member-expression-to-functions/-/helper-member-expression-to-functions-7.14.7.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.0.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/deep-equal/-/deep-equal-1.1.1.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/mimic-fn 30ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-optimise-call-expression/-/helper-optimise-call-expression-7.14.5.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/to-regex-range 38ms
npm http fetch GET 200 https://registry.npmjs.org/array-uniq/-/array-uniq-1.0.3.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/pinkie 33ms
npm http fetch GET 200 https://registry.npmjs.org/p-limit 33ms
npm http fetch GET 200 https://registry.npmjs.org/mimic-fn/-/mimic-fn-2.1.0.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/path-is-inside 32ms
npm http fetch GET 200 https://registry.npmjs.org/fastq 29ms
npm http fetch GET 200 https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/is-core-module 30ms
npm http fetch GET 200 https://registry.npmjs.org/locate-path/-/locate-path-2.0.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/pinkie/-/pinkie-2.0.4.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/@nodelib%2ffs.scandir 46ms
npm http fetch GET 200 https://registry.npmjs.org/p-limit/-/p-limit-2.3.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/path-parse 45ms
npm http fetch GET 200 https://registry.npmjs.org/path-is-inside/-/path-is-inside-1.0.2.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/fastq/-/fastq-1.11.1.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/spdx-correct 28ms
npm http fetch GET 200 https://registry.npmjs.org/is-core-module/-/is-core-module-2.5.0.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/spdx-expression-parse 24ms
npm http fetch GET 200 https://registry.npmjs.org/p-locate/-/p-locate-3.0.0.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz 46ms
npm http fetch GET 200 https://registry.npmjs.org/path-exists/-/path-exists-3.0.0.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/onetime/-/onetime-2.0.1.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/load-json-file/-/load-json-file-4.0.0.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/spdx-correct/-/spdx-correct-3.1.1.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/spdx-expression-parse/-/spdx-expression-parse-3.0.1.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/path-type/-/path-type-3.0.0.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/clone 55ms
npm http fetch GET 200 https://registry.npmjs.org/error-ex 41ms
npm http fetch GET 200 https://registry.npmjs.org/json-parse-better-errors 45ms
npm http fetch GET 200 https://registry.npmjs.org/emoji-regex/-/emoji-regex-7.0.3.tgz 25ms
npm http fetch GET 200 https://registry.npmjs.org/sprintf-js 32ms
npm http fetch GET 200 https://registry.npmjs.org/execa 24ms
npm http fetch GET 200 https://registry.npmjs.org/clone/-/clone-1.0.4.tgz 21ms
npm http fetch GET 200 https://registry.npmjs.org/error-ex/-/error-ex-1.3.2.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/is-obj/-/is-obj-1.0.1.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/pify/-/pify-3.0.0.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/ini 36ms
npm http fetch GET 200 https://registry.npmjs.org/execa/-/execa-0.7.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/got 59ms
npm http fetch GET 200 https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz 20ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/json-parse-better-errors/-/json-parse-better-errors-1.0.2.tgz 60ms
npm http fetch GET 200 https://registry.npmjs.org/registry-auth-token 57ms
npm http fetch GET 200 https://registry.npmjs.org/sprintf-js/-/sprintf-js-1.0.3.tgz 62ms
npm http fetch GET 200 https://registry.npmjs.org/registry-url 49ms
npm http fetch GET 200 https://registry.npmjs.org/crypto-random-string 41ms
npm http fetch GET 200 https://registry.npmjs.org/ini/-/ini-1.3.8.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/extsprintf/-/extsprintf-1.4.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/got/-/got-9.6.0.tgz 24ms
npm http fetch GET 200 https://registry.npmjs.org/registry-auth-token/-/registry-auth-token-4.2.1.tgz 22ms
npm http fetch GET 200 https://registry.npmjs.org/registry-url/-/registry-url-5.1.0.tgz 25ms
npm http fetch GET 200 https://registry.npmjs.org/regenerate 21ms
npm http fetch GET 200 https://registry.npmjs.org/regjsparser 28ms
npm http fetch GET 200 https://registry.npmjs.org/regenerate-unicode-properties 32ms
npm http fetch GET 200 https://registry.npmjs.org/unicode-match-property-ecmascript 28ms
npm http fetch GET 200 https://registry.npmjs.org/regjsgen 34ms
npm http fetch GET 200 https://registry.npmjs.org/crypto-random-string/-/crypto-random-string-1.0.0.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/unicode-match-property-value-ecmascript 27ms
npm http fetch GET 200 https://registry.npmjs.org/call-bind 28ms
npm http fetch GET 200 https://registry.npmjs.org/regenerate/-/regenerate-1.4.2.tgz 25ms
npm http fetch GET 200 https://registry.npmjs.org/define-properties 27ms
npm http fetch GET 200 https://registry.npmjs.org/regjsgen/-/regjsgen-0.5.2.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/unicode-match-property-ecmascript/-/unicode-match-property-ecmascript-1.0.4.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/has-symbols 51ms
npm http fetch GET 200 https://registry.npmjs.org/regenerate-unicode-properties/-/regenerate-unicode-properties-8.2.0.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/regjsparser/-/regjsparser-0.6.9.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/unicode-match-property-value-ecmascript/-/unicode-match-property-value-ecmascript-1.2.0.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/object-keys 46ms
npm http fetch GET 200 https://registry.npmjs.org/call-bind/-/call-bind-1.0.2.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/is-arguments 37ms
npm http fetch GET 200 https://registry.npmjs.org/define-properties/-/define-properties-1.1.3.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/has-symbols/-/has-symbols-1.0.2.tgz 23ms
npm http fetch GET 200 https://registry.npmjs.org/object-keys/-/object-keys-1.1.1.tgz 20ms
npm http fetch GET 200 https://registry.npmjs.org/is-regex 20ms
npm http fetch GET 200 https://registry.npmjs.org/is-arguments/-/is-arguments-1.1.0.tgz 24ms
npm http fetch GET 200 https://registry.npmjs.org/is-number 26ms
npm http fetch GET 200 https://registry.npmjs.org/regexp.prototype.flags 34ms
npm http fetch GET 200 https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz 6ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/p-locate/-/p-locate-2.0.0.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/p-try 33ms
npm http fetch GET 200 https://registry.npmjs.org/object-is 42ms
npm http fetch GET 200 https://registry.npmjs.org/is-date-object 48ms
npm http fetch GET 200 https://registry.npmjs.org/reusify 37ms
npm http fetch GET 200 https://registry.npmjs.org/has 33ms
npm http fetch GET 200 https://registry.npmjs.org/is-regex/-/is-regex-1.1.3.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/p-try/-/p-try-2.2.0.tgz 24ms
npm http fetch GET 200 https://registry.npmjs.org/object-is/-/object-is-1.1.5.tgz 23ms
npm http fetch GET 200 https://registry.npmjs.org/reusify/-/reusify-1.0.4.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/has/-/has-1.0.3.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/is-date-object/-/is-date-object-1.0.4.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/regexp.prototype.flags/-/regexp.prototype.flags-1.3.1.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/mimic-fn/-/mimic-fn-1.2.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/run-parallel 70ms
npm http fetch GET 200 https://registry.npmjs.org/spdx-license-ids 85ms
npm http fetch GET 200 https://registry.npmjs.org/is-arrayish 83ms
npm http fetch GET 200 https://registry.npmjs.org/cross-spawn 85ms
npm http fetch GET 200 https://registry.npmjs.org/spdx-exceptions 89ms
npm http fetch GET 200 https://registry.npmjs.org/get-stream 77ms
npm http fetch GET 200 https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz 75ms
npm http fetch GET 200 https://registry.npmjs.org/run-parallel/-/run-parallel-1.2.0.tgz 61ms
npm http fetch GET 200 https://registry.npmjs.org/spdx-license-ids/-/spdx-license-ids-3.0.9.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/npm-run-path 49ms
npm http fetch GET 200 https://registry.npmjs.org/strip-eof 34ms
npm http fetch GET 200 https://registry.npmjs.org/p-finally 55ms
npm http fetch GET 200 https://registry.npmjs.org/get-stream/-/get-stream-3.0.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/cross-spawn/-/cross-spawn-5.1.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/spdx-exceptions/-/spdx-exceptions-2.3.0.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/cacheable-request 29ms
npm http fetch GET 200 https://registry.npmjs.org/decompress-response 29ms
npm http fetch GET 200 https://registry.npmjs.org/npm-run-path/-/npm-run-path-2.0.2.tgz 25ms
npm http fetch GET 200 https://registry.npmjs.org/@sindresorhus%2fis 47ms
npm http fetch GET 200 https://registry.npmjs.org/p-finally/-/p-finally-1.0.0.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/strip-eof/-/strip-eof-1.0.0.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/duplexer3 26ms
npm http fetch GET 200 https://registry.npmjs.org/lowercase-keys 24ms
npm http fetch GET 200 https://registry.npmjs.org/get-stream/-/get-stream-4.1.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/cacheable-request/-/cacheable-request-6.1.0.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/decompress-response/-/decompress-response-3.3.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/mimic-response 21ms
npm http fetch GET 200 https://registry.npmjs.org/p-cancelable 21ms
npm http fetch GET 200 https://registry.npmjs.org/duplexer3/-/duplexer3-0.1.4.tgz 24ms
npm http fetch GET 200 https://registry.npmjs.org/to-readable-stream 27ms
npm http fetch GET 200 https://registry.npmjs.org/@szmarczak%2fhttp-timer 83ms
npm http fetch GET 200 https://registry.npmjs.org/lowercase-keys/-/lowercase-keys-1.0.1.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/url-parse-lax 33ms
npm http fetch GET 200 https://registry.npmjs.org/@sindresorhus/is/-/is-0.14.0.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/rc 33ms
npm http fetch GET 200 https://registry.npmjs.org/p-cancelable/-/p-cancelable-1.1.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/mimic-response/-/mimic-response-1.0.1.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/unicode-canonical-property-names-ecmascript 38ms
npm http fetch GET 200 https://registry.npmjs.org/unicode-property-aliases-ecmascript 30ms
npm http fetch GET 200 https://registry.npmjs.org/to-readable-stream/-/to-readable-stream-1.0.0.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/url-parse-lax/-/url-parse-lax-3.0.0.tgz 21ms
npm http fetch GET 200 https://registry.npmjs.org/rc/-/rc-1.2.8.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/jsesc/-/jsesc-0.5.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/unicode-canonical-property-names-ecmascript/-/unicode-canonical-property-names-ecmascript-1.0.4.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/function-bind 28ms
npm http fetch GET 200 https://registry.npmjs.org/unicode-property-aliases-ecmascript/-/unicode-property-aliases-ecmascript-1.1.0.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/get-intrinsic 25ms
npm http fetch GET 200 https://registry.npmjs.org/p-limit/-/p-limit-1.3.0.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/queue-microtask 28ms
npm http fetch GET 200 https://registry.npmjs.org/@szmarczak/http-timer/-/http-timer-1.1.2.tgz 66ms
npm http fetch GET 200 https://registry.npmjs.org/lru-cache 29ms
npm http fetch GET 200 https://registry.npmjs.org/function-bind/-/function-bind-1.1.1.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.1.1.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/shebang-command 33ms
npm http fetch GET 200 https://registry.npmjs.org/which 31ms
npm http fetch GET 200 https://registry.npmjs.org/path-key 32ms
npm http fetch GET 200 https://registry.npmjs.org/pump 30ms
npm http fetch GET 200 https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/lru-cache/-/lru-cache-4.1.5.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/clone-response 36ms
npm http fetch GET 200 https://registry.npmjs.org/get-stream/-/get-stream-5.2.0.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/which/-/which-1.3.1.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/pump/-/pump-3.0.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/normalize-url 25ms
npm http fetch GET 200 https://registry.npmjs.org/shebang-command/-/shebang-command-1.2.0.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/http-cache-semantics 34ms
npm http fetch GET 200 https://registry.npmjs.org/path-key/-/path-key-2.0.1.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/keyv 31ms
npm http fetch GET 200 https://registry.npmjs.org/clone-response/-/clone-response-1.0.2.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/normalize-url/-/normalize-url-4.5.1.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/http-cache-semantics/-/http-cache-semantics-4.1.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/keyv/-/keyv-3.1.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/prepend-http 24ms
npm http fetch GET 200 https://registry.npmjs.org/responselike 31ms
npm http fetch GET 200 https://registry.npmjs.org/lowercase-keys/-/lowercase-keys-2.0.0.tgz 66ms
npm http fetch GET 200 https://registry.npmjs.org/deep-extend 36ms
npm http fetch GET 200 https://registry.npmjs.org/p-try/-/p-try-1.0.0.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/strip-json-comments 34ms
npm http fetch GET 200 https://registry.npmjs.org/defer-to-connect 32ms
npm http fetch GET 200 https://registry.npmjs.org/pseudomap 28ms
npm http fetch GET 200 https://registry.npmjs.org/prepend-http/-/prepend-http-2.0.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/responselike/-/responselike-1.0.2.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/isexe 28ms
npm http fetch GET 200 https://registry.npmjs.org/yallist 30ms
npm http fetch GET 200 https://registry.npmjs.org/deep-extend/-/deep-extend-0.6.0.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/strip-json-comments/-/strip-json-comments-2.0.1.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/defer-to-connect/-/defer-to-connect-1.1.3.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/end-of-stream 41ms
npm http fetch GET 200 https://registry.npmjs.org/shebang-regex 33ms
npm http fetch GET 200 https://registry.npmjs.org/pseudomap/-/pseudomap-1.0.2.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/yallist/-/yallist-2.1.2.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/json-buffer 34ms
npm http fetch GET 200 https://registry.npmjs.org/end-of-stream/-/end-of-stream-1.4.4.tgz 23ms
npm http fetch GET 200 https://registry.npmjs.org/shebang-regex/-/shebang-regex-1.0.0.tgz 17ms
npm http fetch GET 200 https://registry.npmjs.org/json-buffer/-/json-buffer-3.0.0.tgz 23ms
npm timing stage:loadIdealTree:loadAllDepsIntoIdealTree Completed in 6143ms
npm timing stage:loadIdealTree Completed in 6236ms
npm timing stage:generateActionsToTake Completed in 59ms
npm timing audit submit Completed in 224ms
npm http fetch POST 200 https://registry.npmjs.org/-/npm/v1/security/audits/quick 227ms
npm timing audit body Completed in 16ms
npm timing action:extract Completed in 448ms
npm timing action:finalize Completed in 63ms
npm timing action:refresh-package-json Completed in 235ms
npm info lifecycle buffer-crc32@0.2.13~preinstall: buffer-crc32@0.2.13
npm info lifecycle buffer-from@1.1.2~preinstall: buffer-from@1.1.2
npm info lifecycle core-util-is@1.0.2~preinstall: core-util-is@1.0.2
npm info lifecycle inherits@2.0.4~preinstall: inherits@2.0.4
npm info lifecycle isarray@1.0.0~preinstall: isarray@1.0.0
npm info lifecycle minimist@1.2.5~preinstall: minimist@1.2.5
npm info lifecycle mkdirp@0.5.5~preinstall: mkdirp@0.5.5
npm info lifecycle ms@2.0.0~preinstall: ms@2.0.0
npm info lifecycle debug@2.6.9~preinstall: debug@2.6.9
npm info lifecycle pend@1.2.0~preinstall: pend@1.2.0
npm info lifecycle fd-slicer@1.1.0~preinstall: fd-slicer@1.1.0
npm info lifecycle process-nextick-args@2.0.1~preinstall: process-nextick-args@2.0.1
npm info lifecycle safe-buffer@5.1.2~preinstall: safe-buffer@5.1.2
npm info lifecycle string_decoder@1.1.1~preinstall: string_decoder@1.1.1
npm info lifecycle typedarray@0.0.6~preinstall: typedarray@0.0.6
npm info lifecycle util-deprecate@1.0.2~preinstall: util-deprecate@1.0.2
npm info lifecycle readable-stream@2.3.7~preinstall: readable-stream@2.3.7
npm info lifecycle concat-stream@1.6.2~preinstall: concat-stream@1.6.2
npm info lifecycle yauzl@2.10.0~preinstall: yauzl@2.10.0
npm info lifecycle ansi-regex@2.1.1~preinstall: ansi-regex@2.1.1
npm info lifecycle aproba@1.2.0~preinstall: aproba@1.2.0
npm info lifecycle code-point-at@1.1.0~preinstall: code-point-at@1.1.0
npm info lifecycle console-control-strings@1.1.0~preinstall: console-control-strings@1.1.0
npm info lifecycle has-unicode@2.0.1~preinstall: has-unicode@2.0.1
npm info lifecycle number-is-nan@1.0.1~preinstall: number-is-nan@1.0.1
npm info lifecycle is-fullwidth-code-point@1.0.0~preinstall: is-fullwidth-code-point@1.0.0
npm info lifecycle object-assign@4.1.1~preinstall: object-assign@4.1.1
npm info lifecycle signal-exit@3.0.3~preinstall: signal-exit@3.0.3
npm info lifecycle strip-ansi@3.0.1~preinstall: strip-ansi@3.0.1
npm info lifecycle string-width@1.0.2~preinstall: string-width@1.0.2
npm info lifecycle wide-align@1.1.3~preinstall: wide-align@1.1.3
npm info lifecycle throttleit@1.0.0~preinstall: throttleit@1.0.0
npm info lifecycle assert-plus@1.0.0~preinstall: assert-plus@1.0.0
npm info lifecycle asynckit@0.4.0~preinstall: asynckit@0.4.0
npm info lifecycle aws-sign2@0.7.0~preinstall: aws-sign2@0.7.0
npm info lifecycle aws4@1.11.0~preinstall: aws4@1.11.0
npm info lifecycle caseless@0.12.0~preinstall: caseless@0.12.0
npm info lifecycle core-util-is@1.0.2~preinstall: core-util-is@1.0.2
npm info lifecycle dashdash@1.14.1~preinstall: dashdash@1.14.1
npm info lifecycle delayed-stream@1.0.0~preinstall: delayed-stream@1.0.0
npm info lifecycle combined-stream@1.0.8~preinstall: combined-stream@1.0.8
npm info lifecycle extend@3.0.2~preinstall: extend@3.0.2
npm info lifecycle extsprintf@1.3.0~preinstall: extsprintf@1.3.0
npm info lifecycle fast-deep-equal@3.1.3~preinstall: fast-deep-equal@3.1.3
npm info lifecycle fast-json-stable-stringify@2.1.0~preinstall: fast-json-stable-stringify@2.1.0
npm info lifecycle forever-agent@0.6.1~preinstall: forever-agent@0.6.1
npm info lifecycle getpass@0.1.7~preinstall: getpass@0.1.7
npm info lifecycle har-schema@2.0.0~preinstall: har-schema@2.0.0
npm info lifecycle is-typedarray@1.0.0~preinstall: is-typedarray@1.0.0
npm info lifecycle isstream@0.1.2~preinstall: isstream@0.1.2
npm info lifecycle request-progress@3.0.0~preinstall: request-progress@3.0.0
npm info lifecycle request@2.88.2~preinstall: request@2.88.2
npm info lifecycle gauge@2.7.4~preinstall: gauge@2.7.4
npm info lifecycle extract-zip@1.7.0~preinstall: extract-zip@1.7.0
npm info lifecycle semver@6.3.0~preinstall: semver@6.3.0
npm info lifecycle rimraf@2.7.1~preinstall: rimraf@2.7.1
npm info lifecycle glob@7.1.7~preinstall: glob@7.1.7
npm info lifecycle inflight@1.0.6~preinstall: inflight@1.0.6
npm info lifecycle once@1.4.0~preinstall: once@1.4.0
npm info lifecycle wrappy@1.0.2~preinstall: wrappy@1.0.2
npm info lifecycle path-is-absolute@1.0.1~preinstall: path-is-absolute@1.0.1
npm info lifecycle minimatch@3.0.4~preinstall: minimatch@3.0.4
npm info lifecycle inherits@2.0.4~preinstall: inherits@2.0.4
npm info lifecycle fs.realpath@1.0.0~preinstall: fs.realpath@1.0.0
npm info lifecycle brace-expansion@1.1.11~preinstall: brace-expansion@1.1.11
npm info lifecycle concat-map@0.0.1~preinstall: concat-map@0.0.1
npm info lifecycle balanced-match@1.0.2~preinstall: balanced-match@1.0.2
npm info lifecycle http-signature@1.2.0~preinstall: http-signature@1.2.0
npm info lifecycle jsprim@1.4.1~preinstall: jsprim@1.4.1
npm info lifecycle verror@1.10.0~preinstall: verror@1.10.0
npm info lifecycle uuid@3.4.0~preinstall: uuid@3.4.0
npm info lifecycle har-validator@5.1.5~preinstall: har-validator@5.1.5
npm info lifecycle ajv@6.12.6~preinstall: ajv@6.12.6
npm info lifecycle uri-js@4.4.1~preinstall: uri-js@4.4.1
npm info lifecycle sshpk@1.16.1~preinstall: sshpk@1.16.1
npm info lifecycle bcrypt-pbkdf@1.0.2~preinstall: bcrypt-pbkdf@1.0.2
npm info lifecycle tweetnacl@0.14.5~preinstall: tweetnacl@0.14.5
npm info lifecycle tunnel-agent@0.6.0~preinstall: tunnel-agent@0.6.0
npm info lifecycle tough-cookie@2.5.0~preinstall: tough-cookie@2.5.0
npm info lifecycle ecc-jsbn@0.1.2~preinstall: ecc-jsbn@0.1.2
npm info lifecycle asn1@0.2.4~preinstall: asn1@0.2.4
npm info lifecycle safer-buffer@2.1.2~preinstall: safer-buffer@2.1.2
npm info lifecycle safe-buffer@5.2.1~preinstall: safe-buffer@5.2.1
npm info lifecycle qs@6.5.2~preinstall: qs@6.5.2
npm info lifecycle punycode@2.1.1~preinstall: punycode@2.1.1
npm info lifecycle psl@1.8.0~preinstall: psl@1.8.0
npm info lifecycle performance-now@2.1.0~preinstall: performance-now@2.1.0
npm info lifecycle oauth-sign@0.9.0~preinstall: oauth-sign@0.9.0
npm info lifecycle form-data@2.3.3~preinstall: form-data@2.3.3
npm info lifecycle mime-types@2.1.32~preinstall: mime-types@2.1.32
npm info lifecycle mime-db@1.49.0~preinstall: mime-db@1.49.0
npm info lifecycle json-stringify-safe@5.0.1~preinstall: json-stringify-safe@5.0.1
npm info lifecycle json-schema-traverse@0.4.1~preinstall: json-schema-traverse@0.4.1
npm info lifecycle json-schema@0.2.3~preinstall: json-schema@0.2.3
npm info lifecycle jsbn@0.1.1~preinstall: jsbn@0.1.1
npm timing action:preinstall Completed in 12ms
npm info linkStuff buffer-crc32@0.2.13
npm info linkStuff buffer-from@1.1.2
npm info linkStuff core-util-is@1.0.2
npm info linkStuff inherits@2.0.4
npm info linkStuff isarray@1.0.0
npm info linkStuff minimist@1.2.5
npm info linkStuff mkdirp@0.5.5
npm info linkStuff ms@2.0.0
npm info linkStuff debug@2.6.9
npm info linkStuff pend@1.2.0
npm info linkStuff fd-slicer@1.1.0
npm info linkStuff process-nextick-args@2.0.1
npm info linkStuff safe-buffer@5.1.2
npm info linkStuff string_decoder@1.1.1
npm info linkStuff typedarray@0.0.6
npm info linkStuff util-deprecate@1.0.2
npm info linkStuff readable-stream@2.3.7
npm info linkStuff concat-stream@1.6.2
npm info linkStuff yauzl@2.10.0
npm info linkStuff ansi-regex@2.1.1
npm info linkStuff aproba@1.2.0
npm info linkStuff code-point-at@1.1.0
npm info linkStuff console-control-strings@1.1.0
npm info linkStuff has-unicode@2.0.1
npm info linkStuff number-is-nan@1.0.1
npm info linkStuff is-fullwidth-code-point@1.0.0
npm info linkStuff object-assign@4.1.1
npm info linkStuff signal-exit@3.0.3
npm info linkStuff strip-ansi@3.0.1
npm info linkStuff string-width@1.0.2
npm info linkStuff wide-align@1.1.3
npm info linkStuff throttleit@1.0.0
npm info linkStuff assert-plus@1.0.0
npm info linkStuff asynckit@0.4.0
npm info linkStuff aws-sign2@0.7.0
npm info linkStuff aws4@1.11.0
npm info linkStuff caseless@0.12.0
npm info linkStuff core-util-is@1.0.2
npm info linkStuff dashdash@1.14.1
npm info linkStuff delayed-stream@1.0.0
npm info linkStuff combined-stream@1.0.8
npm info linkStuff extend@3.0.2
npm info linkStuff extsprintf@1.3.0
npm info linkStuff fast-deep-equal@3.1.3
npm info linkStuff fast-json-stable-stringify@2.1.0
npm info linkStuff forever-agent@0.6.1
npm info linkStuff getpass@0.1.7
npm info linkStuff har-schema@2.0.0
npm info linkStuff is-typedarray@1.0.0
npm info linkStuff isstream@0.1.2
npm info linkStuff jsbn@0.1.1
npm info linkStuff json-schema@0.2.3
npm info linkStuff json-schema-traverse@0.4.1
npm info linkStuff json-stringify-safe@5.0.1
npm info linkStuff mime-db@1.49.0
npm info linkStuff mime-types@2.1.32
npm info linkStuff form-data@2.3.3
npm info linkStuff oauth-sign@0.9.0
npm info linkStuff performance-now@2.1.0
npm info linkStuff psl@1.8.0
npm info linkStuff punycode@2.1.1
npm info linkStuff qs@6.5.2
npm info linkStuff safe-buffer@5.2.1
npm info linkStuff safer-buffer@2.1.2
npm info linkStuff asn1@0.2.4
npm info linkStuff ecc-jsbn@0.1.2
npm info linkStuff tough-cookie@2.5.0
npm info linkStuff tunnel-agent@0.6.0
npm info linkStuff tweetnacl@0.14.5
npm info linkStuff bcrypt-pbkdf@1.0.2
npm info linkStuff sshpk@1.16.1
npm info linkStuff uri-js@4.4.1
npm info linkStuff ajv@6.12.6
npm info linkStuff har-validator@5.1.5
npm info linkStuff uuid@3.4.0
npm info linkStuff verror@1.10.0
npm info linkStuff jsprim@1.4.1
npm info linkStuff http-signature@1.2.0
npm info linkStuff balanced-match@1.0.2
npm info linkStuff concat-map@0.0.1
npm info linkStuff brace-expansion@1.1.11
npm info linkStuff fs.realpath@1.0.0
npm info linkStuff inherits@2.0.4
npm info linkStuff minimatch@3.0.4
npm info linkStuff path-is-absolute@1.0.1
npm info linkStuff wrappy@1.0.2
npm info linkStuff once@1.4.0
npm info linkStuff inflight@1.0.6
npm info linkStuff glob@7.1.7
npm info linkStuff rimraf@2.7.1
npm info linkStuff semver@6.3.0
npm info linkStuff extract-zip@1.7.0
npm info linkStuff gauge@2.7.4
npm info linkStuff request@2.88.2
npm info linkStuff request-progress@3.0.0
npm timing action:build Completed in 24ms
npm info lifecycle buffer-crc32@0.2.13~install: buffer-crc32@0.2.13
npm info lifecycle buffer-from@1.1.2~install: buffer-from@1.1.2
npm info lifecycle core-util-is@1.0.2~install: core-util-is@1.0.2
npm info lifecycle inherits@2.0.4~install: inherits@2.0.4
npm info lifecycle isarray@1.0.0~install: isarray@1.0.0
npm info lifecycle minimist@1.2.5~install: minimist@1.2.5
npm info lifecycle mkdirp@0.5.5~install: mkdirp@0.5.5
npm info lifecycle ms@2.0.0~install: ms@2.0.0
npm info lifecycle debug@2.6.9~install: debug@2.6.9
npm info lifecycle pend@1.2.0~install: pend@1.2.0
npm info lifecycle fd-slicer@1.1.0~install: fd-slicer@1.1.0
npm info lifecycle process-nextick-args@2.0.1~install: process-nextick-args@2.0.1
npm info lifecycle safe-buffer@5.1.2~install: safe-buffer@5.1.2
npm info lifecycle string_decoder@1.1.1~install: string_decoder@1.1.1
npm info lifecycle typedarray@0.0.6~install: typedarray@0.0.6
npm info lifecycle util-deprecate@1.0.2~install: util-deprecate@1.0.2
npm info lifecycle readable-stream@2.3.7~install: readable-stream@2.3.7
npm info lifecycle concat-stream@1.6.2~install: concat-stream@1.6.2
npm info lifecycle yauzl@2.10.0~install: yauzl@2.10.0
npm info lifecycle ansi-regex@2.1.1~install: ansi-regex@2.1.1
npm info lifecycle aproba@1.2.0~install: aproba@1.2.0
npm info lifecycle code-point-at@1.1.0~install: code-point-at@1.1.0
npm info lifecycle console-control-strings@1.1.0~install: console-control-strings@1.1.0
npm info lifecycle has-unicode@2.0.1~install: has-unicode@2.0.1
npm info lifecycle number-is-nan@1.0.1~install: number-is-nan@1.0.1
npm info lifecycle is-fullwidth-code-point@1.0.0~install: is-fullwidth-code-point@1.0.0
npm info lifecycle object-assign@4.1.1~install: object-assign@4.1.1
npm info lifecycle signal-exit@3.0.3~install: signal-exit@3.0.3
npm info lifecycle strip-ansi@3.0.1~install: strip-ansi@3.0.1
npm info lifecycle string-width@1.0.2~install: string-width@1.0.2
npm info lifecycle wide-align@1.1.3~install: wide-align@1.1.3
npm info lifecycle throttleit@1.0.0~install: throttleit@1.0.0
npm info lifecycle assert-plus@1.0.0~install: assert-plus@1.0.0
npm info lifecycle asynckit@0.4.0~install: asynckit@0.4.0
npm info lifecycle aws-sign2@0.7.0~install: aws-sign2@0.7.0
npm info lifecycle aws4@1.11.0~install: aws4@1.11.0
npm info lifecycle caseless@0.12.0~install: caseless@0.12.0
npm info lifecycle core-util-is@1.0.2~install: core-util-is@1.0.2
npm info lifecycle dashdash@1.14.1~install: dashdash@1.14.1
npm info lifecycle delayed-stream@1.0.0~install: delayed-stream@1.0.0
npm info lifecycle combined-stream@1.0.8~install: combined-stream@1.0.8
npm info lifecycle extend@3.0.2~install: extend@3.0.2
npm info lifecycle extsprintf@1.3.0~install: extsprintf@1.3.0
npm info lifecycle fast-deep-equal@3.1.3~install: fast-deep-equal@3.1.3
npm info lifecycle fast-json-stable-stringify@2.1.0~install: fast-json-stable-stringify@2.1.0
npm info lifecycle forever-agent@0.6.1~install: forever-agent@0.6.1
npm info lifecycle getpass@0.1.7~install: getpass@0.1.7
npm info lifecycle har-schema@2.0.0~install: har-schema@2.0.0
npm info lifecycle is-typedarray@1.0.0~install: is-typedarray@1.0.0
npm info lifecycle isstream@0.1.2~install: isstream@0.1.2
npm info lifecycle jsbn@0.1.1~install: jsbn@0.1.1
npm info lifecycle json-schema@0.2.3~install: json-schema@0.2.3
npm info lifecycle json-schema-traverse@0.4.1~install: json-schema-traverse@0.4.1
npm info lifecycle json-stringify-safe@5.0.1~install: json-stringify-safe@5.0.1
npm info lifecycle mime-db@1.49.0~install: mime-db@1.49.0
npm info lifecycle mime-types@2.1.32~install: mime-types@2.1.32
npm info lifecycle form-data@2.3.3~install: form-data@2.3.3
npm info lifecycle oauth-sign@0.9.0~install: oauth-sign@0.9.0
npm info lifecycle performance-now@2.1.0~install: performance-now@2.1.0
npm info lifecycle psl@1.8.0~install: psl@1.8.0
npm info lifecycle punycode@2.1.1~install: punycode@2.1.1
npm info lifecycle qs@6.5.2~install: qs@6.5.2
npm info lifecycle safe-buffer@5.2.1~install: safe-buffer@5.2.1
npm info lifecycle safer-buffer@2.1.2~install: safer-buffer@2.1.2
npm info lifecycle asn1@0.2.4~install: asn1@0.2.4
npm info lifecycle ecc-jsbn@0.1.2~install: ecc-jsbn@0.1.2
npm info lifecycle tough-cookie@2.5.0~install: tough-cookie@2.5.0
npm info lifecycle tunnel-agent@0.6.0~install: tunnel-agent@0.6.0
npm info lifecycle tweetnacl@0.14.5~install: tweetnacl@0.14.5
npm info lifecycle bcrypt-pbkdf@1.0.2~install: bcrypt-pbkdf@1.0.2
npm info lifecycle sshpk@1.16.1~install: sshpk@1.16.1
npm info lifecycle uri-js@4.4.1~install: uri-js@4.4.1
npm info lifecycle ajv@6.12.6~install: ajv@6.12.6
npm info lifecycle har-validator@5.1.5~install: har-validator@5.1.5
npm info lifecycle uuid@3.4.0~install: uuid@3.4.0
npm info lifecycle verror@1.10.0~install: verror@1.10.0
npm info lifecycle jsprim@1.4.1~install: jsprim@1.4.1
npm info lifecycle http-signature@1.2.0~install: http-signature@1.2.0
npm info lifecycle balanced-match@1.0.2~install: balanced-match@1.0.2
npm info lifecycle concat-map@0.0.1~install: concat-map@0.0.1
npm info lifecycle brace-expansion@1.1.11~install: brace-expansion@1.1.11
npm info lifecycle fs.realpath@1.0.0~install: fs.realpath@1.0.0
npm info lifecycle inherits@2.0.4~install: inherits@2.0.4
npm info lifecycle minimatch@3.0.4~install: minimatch@3.0.4
npm info lifecycle path-is-absolute@1.0.1~install: path-is-absolute@1.0.1
npm info lifecycle wrappy@1.0.2~install: wrappy@1.0.2
npm info lifecycle once@1.4.0~install: once@1.4.0
npm info lifecycle inflight@1.0.6~install: inflight@1.0.6
npm info lifecycle glob@7.1.7~install: glob@7.1.7
npm info lifecycle rimraf@2.7.1~install: rimraf@2.7.1
npm info lifecycle semver@6.3.0~install: semver@6.3.0
npm info lifecycle extract-zip@1.7.0~install: extract-zip@1.7.0
npm info lifecycle gauge@2.7.4~install: gauge@2.7.4
npm info lifecycle request@2.88.2~install: request@2.88.2
npm info lifecycle request-progress@3.0.0~install: request-progress@3.0.0
npm timing action:install Completed in 13ms
npm info lifecycle buffer-crc32@0.2.13~postinstall: buffer-crc32@0.2.13
npm info lifecycle buffer-from@1.1.2~postinstall: buffer-from@1.1.2
npm info lifecycle core-util-is@1.0.2~postinstall: core-util-is@1.0.2
npm info lifecycle inherits@2.0.4~postinstall: inherits@2.0.4
npm info lifecycle isarray@1.0.0~postinstall: isarray@1.0.0
npm info lifecycle minimist@1.2.5~postinstall: minimist@1.2.5
npm info lifecycle mkdirp@0.5.5~postinstall: mkdirp@0.5.5
npm info lifecycle ms@2.0.0~postinstall: ms@2.0.0
npm info lifecycle debug@2.6.9~postinstall: debug@2.6.9
npm info lifecycle pend@1.2.0~postinstall: pend@1.2.0
npm info lifecycle fd-slicer@1.1.0~postinstall: fd-slicer@1.1.0
npm info lifecycle process-nextick-args@2.0.1~postinstall: process-nextick-args@2.0.1
npm info lifecycle safe-buffer@5.1.2~postinstall: safe-buffer@5.1.2
npm info lifecycle string_decoder@1.1.1~postinstall: string_decoder@1.1.1
npm info lifecycle typedarray@0.0.6~postinstall: typedarray@0.0.6
npm info lifecycle util-deprecate@1.0.2~postinstall: util-deprecate@1.0.2
npm info lifecycle readable-stream@2.3.7~postinstall: readable-stream@2.3.7
npm info lifecycle concat-stream@1.6.2~postinstall: concat-stream@1.6.2
npm info lifecycle yauzl@2.10.0~postinstall: yauzl@2.10.0
npm info lifecycle ansi-regex@2.1.1~postinstall: ansi-regex@2.1.1
npm info lifecycle aproba@1.2.0~postinstall: aproba@1.2.0
npm info lifecycle code-point-at@1.1.0~postinstall: code-point-at@1.1.0
npm info lifecycle console-control-strings@1.1.0~postinstall: console-control-strings@1.1.0
npm info lifecycle has-unicode@2.0.1~postinstall: has-unicode@2.0.1
npm info lifecycle number-is-nan@1.0.1~postinstall: number-is-nan@1.0.1
npm info lifecycle is-fullwidth-code-point@1.0.0~postinstall: is-fullwidth-code-point@1.0.0
npm info lifecycle object-assign@4.1.1~postinstall: object-assign@4.1.1
npm info lifecycle signal-exit@3.0.3~postinstall: signal-exit@3.0.3
npm info lifecycle strip-ansi@3.0.1~postinstall: strip-ansi@3.0.1
npm info lifecycle string-width@1.0.2~postinstall: string-width@1.0.2
npm info lifecycle wide-align@1.1.3~postinstall: wide-align@1.1.3
npm info lifecycle throttleit@1.0.0~postinstall: throttleit@1.0.0
npm info lifecycle assert-plus@1.0.0~postinstall: assert-plus@1.0.0
npm info lifecycle asynckit@0.4.0~postinstall: asynckit@0.4.0
npm info lifecycle aws-sign2@0.7.0~postinstall: aws-sign2@0.7.0
npm info lifecycle aws4@1.11.0~postinstall: aws4@1.11.0
npm info lifecycle caseless@0.12.0~postinstall: caseless@0.12.0
npm info lifecycle core-util-is@1.0.2~postinstall: core-util-is@1.0.2
npm info lifecycle dashdash@1.14.1~postinstall: dashdash@1.14.1
npm info lifecycle delayed-stream@1.0.0~postinstall: delayed-stream@1.0.0
npm info lifecycle combined-stream@1.0.8~postinstall: combined-stream@1.0.8
npm info lifecycle extend@3.0.2~postinstall: extend@3.0.2
npm info lifecycle extsprintf@1.3.0~postinstall: extsprintf@1.3.0
npm info lifecycle fast-deep-equal@3.1.3~postinstall: fast-deep-equal@3.1.3
npm info lifecycle fast-json-stable-stringify@2.1.0~postinstall: fast-json-stable-stringify@2.1.0
npm info lifecycle forever-agent@0.6.1~postinstall: forever-agent@0.6.1
npm info lifecycle getpass@0.1.7~postinstall: getpass@0.1.7
npm info lifecycle har-schema@2.0.0~postinstall: har-schema@2.0.0
npm info lifecycle is-typedarray@1.0.0~postinstall: is-typedarray@1.0.0
npm info lifecycle isstream@0.1.2~postinstall: isstream@0.1.2
npm info lifecycle jsbn@0.1.1~postinstall: jsbn@0.1.1
npm info lifecycle json-schema@0.2.3~postinstall: json-schema@0.2.3
npm info lifecycle json-schema-traverse@0.4.1~postinstall: json-schema-traverse@0.4.1
npm info lifecycle json-stringify-safe@5.0.1~postinstall: json-stringify-safe@5.0.1
npm info lifecycle mime-db@1.49.0~postinstall: mime-db@1.49.0
npm info lifecycle mime-types@2.1.32~postinstall: mime-types@2.1.32
npm info lifecycle form-data@2.3.3~postinstall: form-data@2.3.3
npm info lifecycle oauth-sign@0.9.0~postinstall: oauth-sign@0.9.0
npm info lifecycle performance-now@2.1.0~postinstall: performance-now@2.1.0
npm info lifecycle psl@1.8.0~postinstall: psl@1.8.0
npm info lifecycle punycode@2.1.1~postinstall: punycode@2.1.1
npm info lifecycle qs@6.5.2~postinstall: qs@6.5.2
npm info lifecycle safe-buffer@5.2.1~postinstall: safe-buffer@5.2.1
npm info lifecycle safer-buffer@2.1.2~postinstall: safer-buffer@2.1.2
npm info lifecycle asn1@0.2.4~postinstall: asn1@0.2.4
npm info lifecycle ecc-jsbn@0.1.2~postinstall: ecc-jsbn@0.1.2
npm info lifecycle tough-cookie@2.5.0~postinstall: tough-cookie@2.5.0
npm info lifecycle tunnel-agent@0.6.0~postinstall: tunnel-agent@0.6.0
npm info lifecycle tweetnacl@0.14.5~postinstall: tweetnacl@0.14.5
npm info lifecycle bcrypt-pbkdf@1.0.2~postinstall: bcrypt-pbkdf@1.0.2
npm info lifecycle sshpk@1.16.1~postinstall: sshpk@1.16.1
npm info lifecycle uri-js@4.4.1~postinstall: uri-js@4.4.1
npm info lifecycle ajv@6.12.6~postinstall: ajv@6.12.6
npm info lifecycle har-validator@5.1.5~postinstall: har-validator@5.1.5
npm info lifecycle uuid@3.4.0~postinstall: uuid@3.4.0
npm info lifecycle verror@1.10.0~postinstall: verror@1.10.0
npm info lifecycle jsprim@1.4.1~postinstall: jsprim@1.4.1
npm info lifecycle http-signature@1.2.0~postinstall: http-signature@1.2.0
npm info lifecycle balanced-match@1.0.2~postinstall: balanced-match@1.0.2
npm info lifecycle concat-map@0.0.1~postinstall: concat-map@0.0.1
npm info lifecycle brace-expansion@1.1.11~postinstall: brace-expansion@1.1.11
npm info lifecycle fs.realpath@1.0.0~postinstall: fs.realpath@1.0.0
npm info lifecycle inherits@2.0.4~postinstall: inherits@2.0.4
npm info lifecycle minimatch@3.0.4~postinstall: minimatch@3.0.4
npm info lifecycle path-is-absolute@1.0.1~postinstall: path-is-absolute@1.0.1
npm info lifecycle wrappy@1.0.2~postinstall: wrappy@1.0.2
npm info lifecycle once@1.4.0~postinstall: once@1.4.0
npm info lifecycle inflight@1.0.6~postinstall: inflight@1.0.6
npm info lifecycle glob@7.1.7~postinstall: glob@7.1.7
npm info lifecycle rimraf@2.7.1~postinstall: rimraf@2.7.1
npm info lifecycle semver@6.3.0~postinstall: semver@6.3.0
npm info lifecycle extract-zip@1.7.0~postinstall: extract-zip@1.7.0
npm info lifecycle gauge@2.7.4~postinstall: gauge@2.7.4
npm info lifecycle request@2.88.2~postinstall: request@2.88.2
npm info lifecycle request-progress@3.0.0~postinstall: request-progress@3.0.0
npm timing action:postinstall Completed in 10ms
npm timing stage:executeActions Completed in 841ms
npm timing stage:rollbackFailedOptional Completed in 0ms
npm info linkStuff ejdb2_node@2.61.4
npm info lifecycle ejdb2_node@2.61.4~install: ejdb2_node@2.61.4

> ejdb2_node@2.61.4 install /openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4
> node install.js

Spawn: cmake --version
cmake version 3.20.3

CMake suite maintained and supported by Kitware (kitware.com/cmake).

Spawn: make --version
GNU Make 4.2.1
,Built for x86_64-pc-linux-gnu
,Copyright (C) 1988-2016 Free Software Foundation, Inc.
,License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
,This is free software: you are free to change and redistribute it.
,There is NO WARRANTY, to the extent permitted by law.

Building EJDB2 native binding...
Git revision: 13431a2
Build temp dir: /openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88
Spawn: cmake ..,-DCMAKE_BUILD_TYPE=RelWithDebInfo,-DBUILD_NODEJS_BINDING=ON,-DNODE_BIN_ROOT=/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4
-- Using project changelog file: /openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/Changelog
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
IOWOW CMAKE_ARGS: -DOWNER_PROJECT_NAME=ejdb2;-DCMAKE_BUILD_TYPE=RelWithDebInfo;-DCMAKE_INSTALL_PREFIX=/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build;-DASAN=OFF;-DBUILD_SHARED_LIBS=OFF;-DBUILD_EXAMPLES=OFF;-DCMAKE_C_COMPILER=/openwrt/staging_dir/host/bin/ccache_cc
FACIL_URL: https://github.com/Softmotions/facil.io/archive/master.zip
FACIL CMAKE_ARGS: -DCMAKE_BUILD_TYPE=RelWithDebInfo;-DCMAKE_C_FLAGS=-fPIC;-DCMAKE_C_COMPILER=/openwrt/staging_dir/host/bin/ccache_cc
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

ejdb2 INCLUDE DIRS: /openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build/src/generated;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build/include;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build/src/extern_facil/lib/facil;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build/src/extern_facil/lib/facil/fiobj;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build/src/extern_facil/lib/facil/http;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build/src/extern_facil/lib/facil/cli;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build/src/extern_facil/lib/facil/tls;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/util;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbl;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jql;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbi;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbr

ejdb2 SOURCES: /openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/ejdb2.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/util/lwre.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/util/utf8proc.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbl/binn.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbl/jbl.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbl/jbl_json.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jql/jql.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jql/jqp.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbi/jbi_consumer.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbi/jbi_dup_scanner.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbi/jbi_full_scanner.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbi/jbi_pk_scanner.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbi/jbi_selection.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbi/jbi_sorter_consumer.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbi/jbi_uniq_scanner.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbi/jbi_util.c;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbr/jbr.c

ejdb2 PUB_HDRS: /openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/ejdb2.h;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbl/jbl.h;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jbr/jbr.h;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/jql/jql.h;/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/src/util/lwre.h

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
ejdb2 PROJECT: ejdb2 (2.61) testing; urgency=medium
ejdb2 CHANGELOG_MESSAGE:
  * Fixed incorrect arguments check in `jbn_merge_patch`
-- Configuring done
-- Generating done
-- Build files have been written to: /openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build
Spawn: make ejdb2_node
make[4]: Entering directory '/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build'
make[5]: Entering directory '/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build'
make[6]: Entering directory '/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build'
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build'
make[7]: Entering directory '/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build'
[  2%] Creating directories for 'extern_iowow'
[  5%] Performing download step (download, verify and extract) for 'extern_iowow'
-- Downloading...
   dst='/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build/src/iowow.zip'
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
          
    


make[7]: *** [src/CMakeFiles/extern_iowow.dir/build.make:97: src/extern_iowow-stamp/extern_iowow-download] Error 1
make[7]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build'
make[6]: *** [CMakeFiles/Makefile2:290: src/CMakeFiles/extern_iowow.dir/all] Error 2
make[6]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build'
make[5]: *** [CMakeFiles/Makefile2:407: src/bindings/ejdb2_node/CMakeFiles/ejdb2_node.dir/rule] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build'
make[4]: *** [Makefile:235: ejdb2_node] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/ejdb2-nodelRyW88/ejdb-13431a2599ea3de90927454025ba5fccd7c2d998/build'
Error: Exit with error code: 2
    at ChildProcess.<anonymous> (/openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/utils.js:77:16)
    at Object.onceWrapper (events.js:482:26)
    at ChildProcess.emit (events.js:375:28)
    at Process.ChildProcess._handle.onexit (internal/child_process.js:277:12)
npm info lifecycle ejdb2_node@2.61.4~install: Failed to exec install script
npm ERR! code ELIFECYCLE
npm ERR! errno 1
npm ERR! ejdb2_node@2.61.4 install: `node install.js`
npm ERR! Exit status 1
npm ERR! 
npm ERR! Failed at the ejdb2_node@2.61.4 install script.
npm ERR! This is probably not a problem with npm. There is likely additional logging output above.
npm timing npm Completed in 94999ms

npm ERR! A complete log of this run can be found in:
npm ERR!     /openwrt/tmp/npm-cache-VU3BkBgkUB/_logs/2021-08-01T07_22_05_114Z-debug.log
make[3]: *** [Makefile:96: /openwrt/build_dir/target-x86_64_musl/node-ejdb2_node-2.61.4/.built] Error 1
```
