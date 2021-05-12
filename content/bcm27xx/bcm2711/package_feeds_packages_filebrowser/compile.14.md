---
title: "compile.14"
date: 2021-05-12 23:05:59.585688
hidden: false
draft: false
weight: -14
---

build number: `14`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/filebrowser/compile -j$(nproc) || make package/feeds/packages/filebrowser/compile V=s
```

#### Compile.txt

``` bash
Copying files from /openwrt/build_dir/target-aarch64_cortex-a72_musl/filebrowser-2.13.0 into /openwrt/build_dir/target-aarch64_cortex-a72_musl/filebrowser-2.13.0/.go_work/build/src/github.com/filebrowser/filebrowser
auth/auth.go
auth/json.go
auth/none.go
auth/proxy.go
auth/storage.go
cmd/cmd.go
cmd/cmds.go
cmd/cmds_add.go
cmd/cmds_ls.go
cmd/cmds_rm.go
cmd/config.go
cmd/config_cat.go
cmd/config_export.go
cmd/config_import.go
cmd/config_init.go
cmd/config_set.go
cmd/docs.go
cmd/hash.go
cmd/root.go
cmd/rule_rm.go
cmd/rules.go
cmd/rules_add.go
cmd/rules_ls.go
cmd/upgrade.go
cmd/users.go
cmd/users_add.go
cmd/users_export.go
cmd/users_find.go
cmd/users_import.go
cmd/users_rm.go
cmd/users_update.go
cmd/utils.go
cmd/version.go
diskcache/cache.go
diskcache/file_cache.go
diskcache/file_cache_test.go
diskcache/noop_cache.go
errors/errors.go
files/file.go
files/listing.go
files/sorting.go
files/utils.go
fileutils/copy.go
fileutils/dir.go
fileutils/file.go
fileutils/file_test.go
frontend/assets.go
go.mod
go.sum
http/auth.go
http/commands.go
http/data.go
http/http.go
http/preview.go
http/preview_enum.go
http/public.go
http/public_test.go
http/raw.go
http/resource.go
http/search.go
http/settings.go
http/share.go
http/static.go
http/users.go
http/utils.go
img/service.go
img/service_enum.go
img/service_test.go
main.go
rules/rules.go
rules/rules_test.go
runner/parser.go
runner/runner.go
search/conditions.go
search/search.go
settings/branding.go
settings/defaults.go
settings/dir.go
settings/settings.go
settings/storage.go
share/share.go
share/storage.go
storage/bolt/auth.go
storage/bolt/bolt.go
storage/bolt/config.go
storage/bolt/importer/conf.go
storage/bolt/importer/importer.go
storage/bolt/importer/users.go
storage/bolt/share.go
storage/bolt/users.go
storage/bolt/utils.go
storage/storage.go
users/password.go
users/permissions.go
users/storage.go
users/storage_test.go
users/users.go
version/version.go

Symlinking directories from /openwrt/staging_dir/target-aarch64_cortex-a72_musl/usr/share/gocode/src into /openwrt/build_dir/target-aarch64_cortex-a72_musl/filebrowser-2.13.0/.go_work/build/src
.../github.com/Erope
.../github.com/iawia002
.../github.com/xtls
.../github.com/txthinking

npm info it worked if it ends with ok
npm info using npm@6.14.12
npm info using node@v14.16.1
npm info prepare initializing installer
npm info prepare Done in 0.06s
npm http fetch GET 200 https://registry.npmjs.org/vue-lazyload/-/vue-lazyload-1.3.3.tgz 2660ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.clonedeep/-/lodash.clonedeep-4.5.0.tgz 2686ms
npm http fetch GET 200 https://registry.npmjs.org/vuex-router-sync/-/vuex-router-sync-5.0.0.tgz 2680ms
npm http fetch GET 200 https://registry.npmjs.org/normalize.css/-/normalize.css-8.0.1.tgz 2685ms
npm http fetch GET 200 https://registry.npmjs.org/@vue/cli-plugin-eslint/-/cli-plugin-eslint-4.1.1.tgz 2682ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.throttle/-/lodash.throttle-4.1.1.tgz 2709ms
npm http fetch GET 200 https://registry.npmjs.org/utif 2698ms
npm http fetch GET 200 https://registry.npmjs.org/clipboard/-/clipboard-2.0.4.tgz 2758ms
npm http fetch GET 200 https://registry.npmjs.org/qrcode.vue/-/qrcode.vue-1.7.0.tgz 2719ms
npm http fetch GET 200 https://registry.npmjs.org/babel-eslint/-/babel-eslint-10.0.3.tgz 2838ms
npm http fetch GET 200 https://registry.npmjs.org/vue-i18n/-/vue-i18n-8.15.3.tgz 2868ms
npm http fetch GET 200 https://registry.npmjs.org/vue-template-compiler/-/vue-template-compiler-2.6.10.tgz 2995ms
npm http fetch GET 200 https://registry.npmjs.org/eslint-plugin-vue/-/eslint-plugin-vue-6.1.2.tgz 3051ms
npm http fetch GET 200 https://registry.npmjs.org/js-base64/-/js-base64-2.5.1.tgz 3013ms
npm http fetch GET 200 https://registry.npmjs.org/noty/-/noty-3.2.0-beta.tgz 3232ms
npm http fetch GET 200 https://registry.npmjs.org/vue-router/-/vue-router-3.1.3.tgz 3627ms
npm http fetch GET 200 https://registry.npmjs.org/@vue/cli-plugin-babel/-/cli-plugin-babel-4.1.2.tgz 3844ms
npm http fetch GET 200 https://registry.npmjs.org/vuex/-/vuex-3.1.2.tgz 3849ms
npm http fetch GET 200 https://registry.npmjs.org/@vue/cli-service/-/cli-service-4.1.2.tgz 3988ms
npm http fetch GET 200 https://registry.npmjs.org/moment/-/moment-2.24.0.tgz 4170ms
npm http fetch GET 200 https://registry.npmjs.org/eslint/-/eslint-6.7.2.tgz 4520ms
npm http fetch GET 200 https://registry.npmjs.org/vue/-/vue-2.6.10.tgz 6234ms
npm http fetch GET 200 https://registry.npmjs.org/ace-builds/-/ace-builds-1.4.7.tgz 90868ms
npm info teardown Done in 0s
npm ERR! code ECONNRESET
npm ERR! errno ECONNRESET
npm ERR! network request to https://registry.npmjs.org/yorkie/-/yorkie-2.0.0.tgz failed, reason: Client network socket disconnected before secure TLS connection was established
npm ERR! network This is a problem related to network connectivity.
npm ERR! network In most cases you are behind a proxy or have bad network settings.
npm ERR! network 
npm ERR! network If you are behind a proxy, please make sure that the
npm ERR! network 'proxy' config is set properly.  See: 'npm help config'
npm WARN registry Unexpected warning for https://registry.npmjs.org/: Miscellaneous Warning ECONNRESET: request to https://registry.npmjs.org/utif failed, reason: Client network socket disconnected before secure TLS connection was established
npm WARN registry Using stale data from https://registry.npmjs.org/ due to a request error during revalidation.
npm http fetch GET 200 https://registry.npmjs.org/utif 196018ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/material-design-icons/-/material-design-icons-3.0.1.tgz 404732ms
npm http fetch GET 200 https://registry.npmjs.org/utif/-/utif-3.1.0.tgz 115948ms attempt #3
npm http fetch GET 200 https://registry.npmjs.org/pako/-/pako-1.0.8.tgz 6258ms
npm timing npm Completed in 518401ms

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/opde/.npm/_logs/2021-05-12T15_55_01_077Z-debug.log
npm info it worked if it ends with ok
npm info using npm@6.14.12
npm info using node@v14.16.1
npm info lifecycle filebrowser-frontend@2.0.0~prelint: filebrowser-frontend@2.0.0
npm info lifecycle filebrowser-frontend@2.0.0~lint: filebrowser-frontend@2.0.0

> filebrowser-frontend@2.0.0 lint /openwrt/build_dir/target-aarch64_cortex-a72_musl/filebrowser-2.13.0/frontend
> vue-cli-service lint --fix

sh: 1: vue-cli-service: not found
npm info lifecycle filebrowser-frontend@2.0.0~lint: Failed to exec lint script
npm ERR! code ELIFECYCLE
npm ERR! syscall spawn
npm ERR! file sh
npm ERR! errno ENOENT
npm ERR! filebrowser-frontend@2.0.0 lint: `vue-cli-service lint --fix`
npm ERR! spawn ENOENT
npm ERR! 
npm ERR! Failed at the filebrowser-frontend@2.0.0 lint script.
npm ERR! This is probably not a problem with npm. There is likely additional logging output above.
npm timing npm Completed in 66ms

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/opde/.npm/_logs/2021-05-12T15_57_04_268Z-debug.log
npm info it worked if it ends with ok
npm info using npm@6.14.12
npm info using node@v14.16.1
npm info lifecycle filebrowser-frontend@2.0.0~prebuild: filebrowser-frontend@2.0.0
npm info lifecycle filebrowser-frontend@2.0.0~build: filebrowser-frontend@2.0.0

> filebrowser-frontend@2.0.0 build /openwrt/build_dir/target-aarch64_cortex-a72_musl/filebrowser-2.13.0/frontend
> find ./dist -maxdepth 1 -mindepth 1 ! -name '.gitignore' -exec rm -r {} + && vue-cli-service build --no-clean

sh: 1: vue-cli-service: not found
npm info lifecycle filebrowser-frontend@2.0.0~build: Failed to exec build script
npm ERR! code ELIFECYCLE
npm ERR! syscall spawn
npm ERR! file sh
npm ERR! errno ENOENT
npm ERR! filebrowser-frontend@2.0.0 build: `find ./dist -maxdepth 1 -mindepth 1 ! -name '.gitignore' -exec rm -r {} + && vue-cli-service build --no-clean`
npm ERR! spawn ENOENT
npm ERR! 
npm ERR! Failed at the filebrowser-frontend@2.0.0 build script.
npm ERR! This is probably not a problem with npm. There is likely additional logging output above.
npm timing npm Completed in 71ms

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/opde/.npm/_logs/2021-05-12T15_57_04_444Z-debug.log
make[3]: *** [Makefile:94: /openwrt/build_dir/target-aarch64_cortex-a72_musl/filebrowser-2.13.0/.built] Error 1
```
