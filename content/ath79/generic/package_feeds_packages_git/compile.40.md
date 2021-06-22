---
title: "compile.40"
date: 2021-06-22 10:45:15.523129
hidden: false
draft: false
weight: -40
---

build number: `40`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/git/compile -j$(nproc) || make package/feeds/packages/git/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-configure_for_crosscompiling.patch using plaintext: 
patching file configure.ac

Applying ./patches/200-imapsend_without_curl.patch using plaintext: 
patching file Makefile

Applying ./patches/300-openssl-deprecated.patch using plaintext: 
patching file imap-send.c

Applying ./patches/310-fix-uname-detection-for-crosscompiling using plaintext: 
patching file config.mak.uname
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: /openwrt/staging_dir/host/bin/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal -I /openwrt/staging_dir/hostpkg/share/aclocal -I /openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal -I m4 -I . --force 
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: running: /openwrt/staging_dir/host/bin/autoconf --include=/openwrt/staging_dir/target-mips_24kc_musl/host/share/aclocal --include=/openwrt/staging_dir/hostpkg/share/aclocal --include=/openwrt/staging_dir/target-mips_24kc_musl/usr/share/aclocal --include=m4 --include=. --prepend-include=/openwrt/staging_dir/host/share/aclocal --force
autoreconf: configure.ac: not using Autoheader
autoreconf: configure.ac: not using Automake
autoreconf: Leaving directory `.'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2'
GIT_VERSION = 2.30.2
    GEN configure
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2'
configure: WARNING: unrecognized options: --disable-nls
configure: loading site script /openwrt/include/site/mips
configure: Setting lib to 'lib' (the default)
configure: Will try -pthread then -lpthread to enable POSIX Threads.
configure: CHECKS for site configuration
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking how to run the C preprocessor... ccache_cc -E
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking for size_t... yes
checking for working alloca.h... yes
checking for alloca... yes
configure: CHECKS for programs
checking for mips-openwrt-linux-cc... (cached) ccache_cc
checking whether we are using the GNU C compiler... (cached) yes
checking whether ccache_cc accepts -g... (cached) yes
checking for ccache_cc option to accept ISO C89... (cached) none needed
checking for inline... inline
checking if linker supports -R... yes
checking for mips-openwrt-linux-gar... mips-openwrt-linux-musl-gcc-ar
checking for gtar... no
checking for tar... tar
checking for gnudiff... no
checking for gdiff... no
checking for diff... diff
checking for asciidoc... asciidoc
checking for asciidoc version... asciidoc 9.0.0rc1 (unknown)
Using 'grep -a' for sane_grep
configure: CHECKS for libraries
checking for SHA1_Init in -lcrypto... no
checking for SHA1_Init in -lssl... no
checking for curl_global_init in -lcurl... no
checking for XML_ParserCreate in -lexpat... yes
checking for deflateBound in -lz... yes
checking for socket in -lc... yes
checking for inet_ntop... yes
checking for inet_pton... yes
checking for hstrerror... yes
checking for basename in -lc... yes
checking if libc contains libintl... yes
checking libintl.h usability... yes
checking libintl.h presence... yes
checking for libintl.h... yes
configure: CHECKS for header files
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking poll.h usability... yes
checking poll.h presence... yes
checking for poll.h... yes
checking sys/poll.h usability... yes
checking sys/poll.h presence... yes
checking for sys/poll.h... yes
checking for inttypes.h... (cached) yes
checking for old iconv()... no
configure: CHECKS for typedefs, structures, and compiler characteristics
checking for socklen_t... yes
checking for struct itimerval... yes
checking for struct stat.st_mtimespec.tv_nsec... no
checking for struct stat.st_mtim.tv_nsec... yes
checking for struct dirent.d_type... yes
checking for struct passwd.pw_gecos... yes
checking for struct sockaddr_storage... yes
checking for struct addrinfo... yes
checking for getaddrinfo... (cached) yes
checking for library containing getaddrinfo... none required
checking whether the platform regex supports REG_STARTEND... no
checking whether system succeeds to read fopen'ed directory... no
checking whether snprintf() and/or vsnprintf() return bogus value... no
checking whether the platform uses typical file type bits... yes
configure: CHECKS for library functions
checking libgen.h usability... yes
checking libgen.h presence... yes
checking for libgen.h... yes
checking paths.h usability... yes
checking paths.h presence... yes
checking for paths.h... yes
checking libcharset.h usability... no
checking libcharset.h presence... no
checking for libcharset.h... no
checking for strings.h... (cached) yes
checking for locale_charset in -liconv... no
checking for locale_charset in -lcharset... no
checking for clock_gettime... yes
checking for library containing clock_gettime... none required
checking for CLOCK_MONOTONIC... yes
checking for setitimer... yes
checking for library containing setitimer... none required
checking for strcasestr... yes
checking for library containing strcasestr... none required
checking for memmem... yes
checking for library containing memmem... none required
checking for strlcpy... yes
checking for library containing strlcpy... none required
checking for uintmax_t... yes
checking for strtoumax... yes
checking for library containing strtoumax... none required
checking for setenv... yes
checking for library containing setenv... none required
checking for unsetenv... yes
checking for library containing unsetenv... none required
checking for mkdtemp... yes
checking for library containing mkdtemp... none required
checking for initgroups... yes
checking for library containing initgroups... none required
checking for getdelim... yes
checking for library containing getdelim... none required
checking for BSD sysctl... no
checking for POSIX Threads with ''... yes
configure: creating ./config.status
config.status: creating config.mak.autogen
config.status: executing config.mak.autogen commands
configure: WARNING: unrecognized options: --disable-nls
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2'
    * new build flags
make[4]: Nothing to be done for 'gitweb'.
make -C gitweb install
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/gitweb'
make[6]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2'
make[6]: 'GIT-VERSION-FILE' is up to date.
make[6]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2'
    GEN static/gitweb.js
    GEN gitweb.cgi
install -d -m 755 '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/www/cgi-bin'
install -m 755 gitweb.cgi '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/www/cgi-bin'
install -d -m 755 '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/www/cgi-bin/static'
install -m 644 static/gitweb.js static/gitweb.css static/git-logo.png static/git-favicon.png '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/www/cgi-bin/static'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/gitweb'
    CC fuzz-commit-graph.o
    CC fuzz-pack-headers.o
    CC fuzz-pack-idx.o
    CC daemon.o
    * new link flags
    CC common-main.o
    CC abspath.o
    CC add-interactive.o
    CC add-patch.o
    CC advice.o
    CC alias.o
    CC alloc.o
    CC apply.o
    CC archive-tar.o
    CC archive-zip.o
    CC archive.o
    * new prefix flags
    CC base85.o
    CC bisect.o
    CC blame.o
    CC blob.o
    CC bloom.o
    CC branch.o
    CC bulk-checkin.o
    CC bundle.o
    CC cache-tree.o
    CC chdir-notify.o
    CC checkout.o
    CC color.o
    CC column.o
    CC combine-diff.o
    CC commit-graph.o
    CC commit-reach.o
    CC commit.o
    CC compat/obstack.o
    CC compat/terminal.o
    CC config.o
    CC connect.o
    CC connected.o
    CC convert.o
    CC copy.o
    CC credential.o
    CC csum-file.o
    CC ctype.o
    CC date.o
    CC decorate.o
    CC delta-islands.o
    CC diff-delta.o
    CC diff-lib.o
    CC diff-no-index.o
    CC diff.o
    CC diffcore-break.o
    CC diffcore-delta.o
    CC diffcore-order.o
    CC diffcore-pickaxe.o
    CC diffcore-rename.o
    CC dir-iterator.o
    CC dir.o
    CC editor.o
    CC entry.o
    CC environment.o
    CC ewah/bitmap.o
    CC ewah/ewah_bitmap.o
    CC ewah/ewah_io.o
    CC ewah/ewah_rlw.o
    CC exec-cmd.o
    CC fetch-negotiator.o
    CC fetch-pack.o
    CC fmt-merge-msg.o
    CC fsck.o
    CC fsmonitor.o
    CC gettext.o
    CC gpg-interface.o
    CC graph.o
    CC grep.o
    CC hashmap.o
    GEN command-list.h
    CC hex.o
    CC ident.o
    CC json-writer.o
    CC kwset.o
    CC levenshtein.o
    CC line-log.o
    CC line-range.o
    CC linear-assignment.o
    CC list-objects-filter-options.o
    CC list-objects-filter.o
    CC list-objects.o
    CC ll-merge.o
    CC lockfile.o
    CC log-tree.o
    CC ls-refs.o
    CC mailinfo.o
    CC mailmap.o
    CC match-trees.o
    CC mem-pool.o
    CC merge-blobs.o
    CC merge-ort.o
    CC merge-ort-wrappers.o
    CC merge-recursive.o
    CC merge.o
    CC mergesort.o
    CC midx.o
    CC name-hash.o
    CC negotiator/default.o
    CC negotiator/noop.o
    CC negotiator/skipping.o
    CC notes-cache.o
    CC notes-merge.o
    CC notes-utils.o
    CC notes.o
    CC object.o
    CC oid-array.o
    CC oidmap.o
    CC oidset.o
    CC pack-bitmap-write.o
    CC pack-bitmap.o
    CC pack-check.o
    CC pack-objects.o
    CC pack-revindex.o
    CC pack-write.o
    CC packfile.o
    CC pager.o
    CC parse-options-cb.o
    CC parse-options.o
    CC patch-delta.o
    CC patch-ids.o
    CC path.o
    CC pathspec.o
    CC pkt-line.o
    CC preload-index.o
    CC pretty.o
    CC prio-queue.o
    CC progress.o
    CC promisor-remote.o
    CC prompt.o
    CC protocol.o
    CC prune-packed.o
    CC quote.o
    CC range-diff.o
    CC reachable.o
    CC read-cache.o
    CC rebase-interactive.o
    CC rebase.o
    CC ref-filter.o
    CC reflog-walk.o
    CC refs.o
    CC refs/debug.o
    CC refs/files-backend.o
    CC refs/iterator.o
    CC refs/packed-backend.o
    CC refs/ref-cache.o
    CC refspec.o
    CC remote.o
    CC replace-object.o
    CC repo-settings.o
    CC repository.o
    CC rerere.o
    CC reset.o
    CC resolve-undo.o
    CC revision.o
    CC run-command.o
    CC send-pack.o
    CC sequencer.o
    CC serve.o
    CC server-info.o
    CC setup.o
    CC sha1-file.o
    CC sha1-lookup.o
    CC sha1-name.o
    CC shallow.o
    CC sideband.o
    CC sigchain.o
    CC split-index.o
    CC stable-qsort.o
    CC strbuf.o
    CC streaming.o
    CC string-list.o
    CC strmap.o
    CC strvec.o
    CC sub-process.o
    CC submodule-config.o
    CC submodule.o
    CC symlinks.o
    CC tag.o
    CC tempfile.o
    CC thread-utils.o
    CC tmp-objdir.o
    CC trace.o
    CC trace2.o
    CC trace2/tr2_cfg.o
    CC trace2/tr2_cmd_name.o
    CC trace2/tr2_dst.o
    CC trace2/tr2_sid.o
    CC trace2/tr2_sysenv.o
    CC trace2/tr2_tbuf.o
    CC trace2/tr2_tgt_event.o
    CC trace2/tr2_tgt_normal.o
    CC trace2/tr2_tgt_perf.o
    CC trace2/tr2_tls.o
    CC trailer.o
    CC transport-helper.o
    CC transport.o
    CC tree-diff.o
    CC tree-walk.o
    CC tree.o
    CC unpack-trees.o
    CC upload-pack.o
    CC url.o
    CC urlmatch.o
    CC usage.o
    CC userdiff.o
    CC utf8.o
    CC varint.o
    CC versioncmp.o
    CC walker.o
    CC wildmatch.o
    CC worktree.o
    CC wrapper.o
    CC write-or-die.o
    CC ws.o
    CC wt-status.o
    CC xdiff-interface.o
    CC zlib.o
    CC sha1dc_git.o
    CC sha1dc/sha1.o
    CC sha1dc/ubc_check.o
    CC sha256/block/sha256.o
    CC compat/qsort_s.o
    CC compat/regex/regex.o
    CC xdiff/xdiffi.o
    CC xdiff/xemit.o
    CC xdiff/xhistogram.o
    CC xdiff/xmerge.o
    CC xdiff/xpatience.o
    CC xdiff/xprepare.o
    CC xdiff/xutils.o
    CC http-backend.o
    CC imap-send.o
    CC sh-i18n--envsubst.o
    CC shell.o
    * new script parameters
    GEN git-instaweb
    CC git.o
    CC builtin/add.o
    CC builtin/am.o
    CC builtin/annotate.o
    CC builtin/apply.o
    CC builtin/archive.o
    CC builtin/bisect--helper.o
    CC builtin/blame.o
    CC builtin/branch.o
    CC builtin/bugreport.o
    CC builtin/bundle.o
    CC builtin/cat-file.o
    CC builtin/check-attr.o
    CC builtin/check-ignore.o
    CC builtin/check-mailmap.o
    CC builtin/check-ref-format.o
    CC builtin/checkout-index.o
    CC builtin/checkout.o
    CC builtin/clean.o
    CC builtin/clone.o
    CC builtin/column.o
    CC builtin/commit-graph.o
    CC builtin/commit-tree.o
    CC builtin/commit.o
    CC builtin/config.o
    CC builtin/count-objects.o
    CC builtin/credential-cache--daemon.o
    CC builtin/credential-cache.o
    CC builtin/credential-store.o
    CC builtin/credential.o
    CC builtin/describe.o
    CC builtin/diff-files.o
    CC builtin/diff-index.o
    CC builtin/diff-tree.o
    CC builtin/diff.o
    CC builtin/difftool.o
    CC builtin/env--helper.o
    CC builtin/fast-export.o
    CC builtin/fast-import.o
    CC builtin/fetch-pack.o
    CC builtin/fetch.o
    CC builtin/fmt-merge-msg.o
    CC builtin/for-each-ref.o
    CC builtin/for-each-repo.o
    CC builtin/fsck.o
    CC builtin/gc.o
    CC builtin/get-tar-commit-id.o
    CC builtin/grep.o
    CC builtin/hash-object.o
    GEN config-list.h
    CC builtin/index-pack.o
    CC builtin/init-db.o
    CC builtin/interpret-trailers.o
    CC builtin/log.o
    CC builtin/ls-files.o
    CC builtin/ls-remote.o
    CC builtin/ls-tree.o
    CC builtin/mailinfo.o
    CC builtin/mailsplit.o
    CC builtin/merge-base.o
    CC builtin/merge-file.o
    CC builtin/merge-index.o
    CC builtin/merge-ours.o
    CC builtin/merge-recursive.o
    CC builtin/merge-tree.o
    CC builtin/merge.o
    CC builtin/mktag.o
    CC builtin/mktree.o
    CC builtin/multi-pack-index.o
    CC builtin/mv.o
    CC builtin/name-rev.o
    CC builtin/notes.o
    CC builtin/pack-objects.o
    CC builtin/pack-redundant.o
    CC builtin/pack-refs.o
    CC builtin/patch-id.o
    CC builtin/prune-packed.o
    CC builtin/prune.o
    CC builtin/pull.o
    CC builtin/push.o
    CC builtin/range-diff.o
    CC builtin/read-tree.o
    CC builtin/rebase.o
    CC builtin/receive-pack.o
    CC builtin/reflog.o
    CC builtin/remote-ext.o
    CC builtin/remote-fd.o
    CC builtin/remote.o
    CC builtin/repack.o
    CC builtin/replace.o
    CC builtin/rerere.o
    CC builtin/reset.o
    CC builtin/rev-list.o
    CC builtin/rev-parse.o
    CC builtin/revert.o
    CC builtin/rm.o
    CC builtin/send-pack.o
    CC builtin/shortlog.o
    CC builtin/show-branch.o
    CC builtin/show-index.o
    CC builtin/show-ref.o
    CC builtin/sparse-checkout.o
    CC builtin/stash.o
    CC builtin/stripspace.o
    CC builtin/submodule--helper.o
    CC builtin/symbolic-ref.o
    CC builtin/tag.o
    CC builtin/unpack-file.o
    CC builtin/unpack-objects.o
    CC builtin/update-index.o
    CC builtin/update-ref.o
    CC builtin/update-server-info.o
    CC builtin/upload-archive.o
    CC builtin/upload-pack.o
    CC builtin/var.o
    CC builtin/verify-commit.o
    CC builtin/verify-pack.o
    CC builtin/verify-tag.o
    CC builtin/worktree.o
    CC builtin/write-tree.o
    GEN git-mergetool--lib
    GEN git-rebase--preserve-merges
    GEN git-sh-i18n
    GEN git-sh-setup
    CC attr.o
    CC help.o
    CC version.o
    AR xdiff/lib.a
    GEN git-bisect
    GEN git-difftool--helper
    GEN git-filter-branch
    GEN git-merge-octopus
    GEN git-merge-one-file
    GEN git-merge-resolve
    GEN git-mergetool
    GEN git-quiltimport
    GEN git-request-pull
    GEN git-submodule
    GEN git-web--browse
    GEN git-add--interactive
    GEN git-archimport
    GEN git-cvsexportcommit
    GEN git-cvsimport
    GEN git-cvsserver
    GEN git-send-email
    GEN git-svn
    GEN git-p4
    CC builtin/help.o
    AR libgit.a
    LINK git-daemon
    LINK git-http-backend
    LINK git-imap-send
    LINK git-sh-i18n--envsubst
    LINK git-shell
    LINK git
    BUILTIN git-add
    BUILTIN git-am
    BUILTIN git-annotate
    BUILTIN git-apply
    BUILTIN git-archive
    BUILTIN git-bisect--helper
    BUILTIN git-blame
    BUILTIN git-branch
    BUILTIN git-bugreport
    BUILTIN git-bundle
    BUILTIN git-cat-file
    BUILTIN git-check-attr
    BUILTIN git-check-ignore
    BUILTIN git-check-mailmap
    BUILTIN git-check-ref-format
    BUILTIN git-checkout-index
    BUILTIN git-checkout
    BUILTIN git-clean
    BUILTIN git-clone
    BUILTIN git-column
    BUILTIN git-commit-graph
    BUILTIN git-commit-tree
    BUILTIN git-commit
    BUILTIN git-config
    BUILTIN git-count-objects
    BUILTIN git-credential-cache--daemon
    BUILTIN git-credential-cache
    BUILTIN git-credential-store
    BUILTIN git-credential
    BUILTIN git-describe
    BUILTIN git-diff-files
    BUILTIN git-diff-index
    BUILTIN git-diff-tree
    BUILTIN git-diff
    BUILTIN git-difftool
    BUILTIN git-env--helper
    BUILTIN git-fast-export
    BUILTIN git-fast-import
    BUILTIN git-fetch-pack
    BUILTIN git-fetch
    BUILTIN git-fmt-merge-msg
    BUILTIN git-for-each-ref
    BUILTIN git-for-each-repo
    BUILTIN git-fsck
    BUILTIN git-gc
    BUILTIN git-get-tar-commit-id
    BUILTIN git-grep
    BUILTIN git-hash-object
    BUILTIN git-help
    BUILTIN git-index-pack
    BUILTIN git-init-db
    BUILTIN git-interpret-trailers
    BUILTIN git-log
    BUILTIN git-ls-files
    BUILTIN git-ls-remote
    BUILTIN git-ls-tree
    BUILTIN git-mailinfo
    BUILTIN git-mailsplit
    BUILTIN git-merge-base
    BUILTIN git-merge-file
    BUILTIN git-merge-index
    BUILTIN git-merge-ours
    BUILTIN git-merge-recursive
    BUILTIN git-merge-tree
    BUILTIN git-merge
    BUILTIN git-mktag
    BUILTIN git-mktree
    BUILTIN git-multi-pack-index
    BUILTIN git-mv
    BUILTIN git-name-rev
    BUILTIN git-notes
    BUILTIN git-pack-objects
    BUILTIN git-pack-redundant
    BUILTIN git-pack-refs
    BUILTIN git-patch-id
    BUILTIN git-prune-packed
    BUILTIN git-prune
    BUILTIN git-pull
    BUILTIN git-push
    BUILTIN git-range-diff
    BUILTIN git-read-tree
    BUILTIN git-rebase
    BUILTIN git-receive-pack
    BUILTIN git-reflog
    BUILTIN git-remote-ext
    BUILTIN git-remote-fd
    BUILTIN git-remote
    BUILTIN git-repack
    BUILTIN git-replace
    BUILTIN git-rerere
    BUILTIN git-reset
    BUILTIN git-rev-list
    BUILTIN git-rev-parse
    BUILTIN git-revert
    BUILTIN git-rm
    BUILTIN git-send-pack
    BUILTIN git-shortlog
    BUILTIN git-show-branch
    BUILTIN git-show-index
    BUILTIN git-show-ref
    BUILTIN git-sparse-checkout
    BUILTIN git-stash
    BUILTIN git-stripspace
    BUILTIN git-submodule--helper
    BUILTIN git-symbolic-ref
    BUILTIN git-tag
    BUILTIN git-unpack-file
    BUILTIN git-unpack-objects
    BUILTIN git-update-index
    BUILTIN git-update-ref
    BUILTIN git-update-server-info
    BUILTIN git-upload-archive
    BUILTIN git-upload-pack
    BUILTIN git-var
    BUILTIN git-verify-commit
    BUILTIN git-verify-pack
    BUILTIN git-verify-tag
    BUILTIN git-worktree
    BUILTIN git-write-tree
    BUILTIN git-cherry
    BUILTIN git-cherry-pick
    BUILTIN git-format-patch
    BUILTIN git-fsck-objects
    BUILTIN git-init
    BUILTIN git-maintenance
    BUILTIN git-merge-subtree
    BUILTIN git-restore
    BUILTIN git-show
    BUILTIN git-stage
    BUILTIN git-status
    BUILTIN git-switch
    BUILTIN git-whatchanged
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/templates'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/templates'
    CC t/helper/test-fake-ssh.o
    CC t/helper/test-tool.o
    CC t/helper/test-advise.o
    CC t/helper/test-bloom.o
    CC t/helper/test-chmtime.o
    CC t/helper/test-config.o
    CC t/helper/test-crontab.o
    CC t/helper/test-ctype.o
    CC t/helper/test-date.o
    CC t/helper/test-delta.o
    CC t/helper/test-dir-iterator.o
    CC t/helper/test-drop-caches.o
    CC t/helper/test-dump-cache-tree.o
    CC t/helper/test-dump-fsmonitor.o
    CC t/helper/test-dump-split-index.o
    CC t/helper/test-dump-untracked-cache.o
    CC t/helper/test-example-decorate.o
    CC t/helper/test-fast-rebase.o
    CC t/helper/test-genrandom.o
    CC t/helper/test-genzeros.o
    CC t/helper/test-hash-speed.o
    CC t/helper/test-hash.o
    CC t/helper/test-hashmap.o
    CC t/helper/test-index-version.o
    CC t/helper/test-json-writer.o
    CC t/helper/test-lazy-init-name-hash.o
    CC t/helper/test-match-trees.o
    CC t/helper/test-mergesort.o
    CC t/helper/test-mktemp.o
    CC t/helper/test-oid-array.o
    CC t/helper/test-oidmap.o
    CC t/helper/test-online-cpus.o
    CC t/helper/test-parse-options.o
    CC t/helper/test-parse-pathspec-file.o
    CC t/helper/test-path-utils.o
    CC t/helper/test-pkt-line.o
    CC t/helper/test-prio-queue.o
    CC t/helper/test-proc-receive.o
    CC t/helper/test-progress.o
    CC t/helper/test-reach.o
    CC t/helper/test-read-cache.o
    CC t/helper/test-read-graph.o
    CC t/helper/test-read-midx.o
    CC t/helper/test-ref-store.o
    CC t/helper/test-regex.o
    CC t/helper/test-repository.o
    CC t/helper/test-revision-walking.o
    CC t/helper/test-run-command.o
    CC t/helper/test-scrap-cache-tree.o
    CC t/helper/test-serve-v2.o
    CC t/helper/test-sha1.o
    CC t/helper/test-sha256.o
    CC t/helper/test-sigchain.o
    CC t/helper/test-strcmp-offset.o
    CC t/helper/test-string-list.o
    CC t/helper/test-submodule-config.o
    CC t/helper/test-submodule-nested-repo-config.o
    CC t/helper/test-subprocess.o
    CC t/helper/test-trace2.o
    CC t/helper/test-urlmatch-normalization.o
    CC t/helper/test-wildmatch.o
    CC t/helper/test-windows-named-pipe.o
    CC t/helper/test-write-cache.o
    CC t/helper/test-xml-encode.o
    GEN bin-wrappers/git
    GEN bin-wrappers/git-receive-pack
    GEN bin-wrappers/git-shell
    GEN bin-wrappers/git-upload-archive
    GEN bin-wrappers/git-upload-pack
    GEN bin-wrappers/git-cvsserver
    GEN bin-wrappers/test-fake-ssh
    GEN bin-wrappers/test-tool
    LINK t/helper/test-fake-ssh
    LINK t/helper/test-tool
install -d -m 755 '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/bin'
install -d -m 755 '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/lib/git-core'
install   git-daemon git-http-backend git-imap-send git-sh-i18n--envsubst git-shell git-bisect git-difftool--helper git-filter-branch git-merge-octopus git-merge-one-file git-merge-resolve git-mergetool git-quiltimport git-request-pull git-submodule git-web--browse git-add--interactive git-archimport git-cvsexportcommit git-cvsimport git-cvsserver git-send-email git-svn git-p4 git-instaweb '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/lib/git-core'
install -m 644  git-mergetool--lib git-rebase--preserve-merges git-sh-i18n git-sh-setup '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/lib/git-core'
install git git-receive-pack git-shell git-upload-archive git-upload-pack git-cvsserver '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/bin'
make -C templates DESTDIR='/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install' install
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/templates'
install -d -m 755 '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/share/git-core/templates'
(cd blt && tar cf - .) | \
(cd '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/share/git-core/templates' && umask 022 && tar xof -)
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/templates'
install -d -m 755 '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/lib/git-core/mergetools'
install -m 644 mergetools/* '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/lib/git-core/mergetools'
bindir=$(cd '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/bin' && pwd) && \
execdir=$(cd '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/lib/git-core' && pwd) && \
destdir_from_execdir_SQ=$(echo 'lib/git-core' | sed -e 's|[^/][^/]*|..|g') && \
{ test "$bindir/" = "$execdir/" || \
  for p in git git-shell git-cvsserver; do \
	rm -f "$execdir/$p" && \
	test -n "" && \
	ln -s "$destdir_from_execdir_SQ/bin/$p" "$execdir/$p" || \
	{ test -z "yes" && \
	  ln "$bindir/$p" "$execdir/$p" 2>/dev/null || \
	  cp "$bindir/$p" "$execdir/$p" || exit; } \
  done; \
} && \
for p in git-receive-pack git-upload-archive git-upload-pack; do \
	rm -f "$bindir/$p" && \
	test -n "" && \
	ln -s "git" "$bindir/$p" || \
	{ test -z "yes" && \
	  ln "$bindir/git" "$bindir/$p" 2>/dev/null || \
	  ln -s "git" "$bindir/$p" 2>/dev/null || \
	  cp "$bindir/git" "$bindir/$p" || exit; }; \
done && \
for p in  git-add git-am git-annotate git-apply git-archive git-bisect--helper git-blame git-branch git-bugreport git-bundle git-cat-file git-check-attr git-check-ignore git-check-mailmap git-check-ref-format git-checkout-index git-checkout git-clean git-clone git-column git-commit-graph git-commit-tree git-commit git-config git-count-objects git-credential-cache--daemon git-credential-cache git-credential-store git-credential git-describe git-diff-files git-diff-index git-diff-tree git-diff git-difftool git-env--helper git-fast-export git-fast-import git-fetch-pack git-fetch git-fmt-merge-msg git-for-each-ref git-for-each-repo git-fsck git-gc git-get-tar-commit-id git-grep git-hash-object git-help git-index-pack git-init-db git-interpret-trailers git-log git-ls-files git-ls-remote git-ls-tree git-mailinfo git-mailsplit git-merge-base git-merge-file git-merge-index git-merge-ours git-merge-recursive git-merge-tree git-merge git-mktag git-mktree git-multi-pack-index git-mv git-name-rev git-notes git-pack-objects git-pack-redundant git-pack-refs git-patch-id git-prune-packed git-prune git-pull git-push git-range-diff git-read-tree git-rebase git-receive-pack git-reflog git-remote-ext git-remote-fd git-remote git-repack git-replace git-rerere git-reset git-rev-list git-rev-parse git-revert git-rm git-send-pack git-shortlog git-show-branch git-show-index git-show-ref git-sparse-checkout git-stash git-stripspace git-submodule--helper git-symbolic-ref git-tag git-unpack-file git-unpack-objects git-update-index git-update-ref git-update-server-info git-upload-archive git-upload-pack git-var git-verify-commit git-verify-pack git-verify-tag git-worktree git-write-tree git-cherry git-cherry-pick git-format-patch git-fsck-objects git-init git-maintenance git-merge-subtree git-restore git-show git-stage git-status git-switch git-whatchanged; do \
	rm -f "$execdir/$p" && \
	if test -z ""; \
	then \
		test -n "" && \
		ln -s "$destdir_from_execdir_SQ/bin/git" "$execdir/$p" || \
		{ test -z "yes" && \
		  ln "$execdir/git" "$execdir/$p" 2>/dev/null || \
		  ln -s "git" "$execdir/$p" 2>/dev/null || \
		  cp "$execdir/git" "$execdir/$p" || exit; }; \
	fi \
done && \
remote_curl_aliases="" && \
for p in $remote_curl_aliases; do \
	rm -f "$execdir/$p" && \
	test -n "" && \
	ln -s "git-remote-http" "$execdir/$p" || \
	{ test -z "yes" && \
	  ln "$execdir/git-remote-http" "$execdir/$p" 2>/dev/null || \
	  ln -s "git-remote-http" "$execdir/$p" 2>/dev/null || \
	  cp "$execdir/git-remote-http" "$execdir/$p" || exit; } \
done && \
./check_bindir "z$bindir" "z$execdir" "$bindir/git-add"
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2'
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/templates'
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/templates'
install -d -m 755 '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/bin'
install -d -m 755 '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/lib/git-core'
install   git-daemon git-http-backend git-imap-send git-sh-i18n--envsubst git-shell git-bisect git-difftool--helper git-filter-branch git-merge-octopus git-merge-one-file git-merge-resolve git-mergetool git-quiltimport git-request-pull git-submodule git-web--browse git-add--interactive git-archimport git-cvsexportcommit git-cvsimport git-cvsserver git-send-email git-svn git-p4 git-instaweb '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/lib/git-core'
install -m 644  git-mergetool--lib git-rebase--preserve-merges git-sh-i18n git-sh-setup '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/lib/git-core'
install git git-receive-pack git-shell git-upload-archive git-upload-pack git-cvsserver '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/bin'
make -C templates DESTDIR='/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install' install
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/templates'
install -d -m 755 '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/share/git-core/templates'
(cd blt && tar cf - .) | \
(cd '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/share/git-core/templates' && umask 022 && tar xof -)
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/templates'
install -d -m 755 '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/lib/git-core/mergetools'
install -m 644 mergetools/* '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/lib/git-core/mergetools'
bindir=$(cd '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/bin' && pwd) && \
execdir=$(cd '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/lib/git-core' && pwd) && \
destdir_from_execdir_SQ=$(echo 'lib/git-core' | sed -e 's|[^/][^/]*|..|g') && \
{ test "$bindir/" = "$execdir/" || \
  for p in git git-shell git-cvsserver; do \
	rm -f "$execdir/$p" && \
	test -n "" && \
	ln -s "$destdir_from_execdir_SQ/bin/$p" "$execdir/$p" || \
	{ test -z "yes" && \
	  ln "$bindir/$p" "$execdir/$p" 2>/dev/null || \
	  cp "$bindir/$p" "$execdir/$p" || exit; } \
  done; \
} && \
for p in git-receive-pack git-upload-archive git-upload-pack; do \
	rm -f "$bindir/$p" && \
	test -n "" && \
	ln -s "git" "$bindir/$p" || \
	{ test -z "yes" && \
	  ln "$bindir/git" "$bindir/$p" 2>/dev/null || \
	  ln -s "git" "$bindir/$p" 2>/dev/null || \
	  cp "$bindir/git" "$bindir/$p" || exit; }; \
done && \
for p in  git-add git-am git-annotate git-apply git-archive git-bisect--helper git-blame git-branch git-bugreport git-bundle git-cat-file git-check-attr git-check-ignore git-check-mailmap git-check-ref-format git-checkout-index git-checkout git-clean git-clone git-column git-commit-graph git-commit-tree git-commit git-config git-count-objects git-credential-cache--daemon git-credential-cache git-credential-store git-credential git-describe git-diff-files git-diff-index git-diff-tree git-diff git-difftool git-env--helper git-fast-export git-fast-import git-fetch-pack git-fetch git-fmt-merge-msg git-for-each-ref git-for-each-repo git-fsck git-gc git-get-tar-commit-id git-grep git-hash-object git-help git-index-pack git-init-db git-interpret-trailers git-log git-ls-files git-ls-remote git-ls-tree git-mailinfo git-mailsplit git-merge-base git-merge-file git-merge-index git-merge-ours git-merge-recursive git-merge-tree git-merge git-mktag git-mktree git-multi-pack-index git-mv git-name-rev git-notes git-pack-objects git-pack-redundant git-pack-refs git-patch-id git-prune-packed git-prune git-pull git-push git-range-diff git-read-tree git-rebase git-receive-pack git-reflog git-remote-ext git-remote-fd git-remote git-repack git-replace git-rerere git-reset git-rev-list git-rev-parse git-revert git-rm git-send-pack git-shortlog git-show-branch git-show-index git-show-ref git-sparse-checkout git-stash git-stripspace git-submodule--helper git-symbolic-ref git-tag git-unpack-file git-unpack-objects git-update-index git-update-ref git-update-server-info git-upload-archive git-upload-pack git-var git-verify-commit git-verify-pack git-verify-tag git-worktree git-write-tree git-cherry git-cherry-pick git-format-patch git-fsck-objects git-init git-maintenance git-merge-subtree git-restore git-show git-stage git-status git-switch git-whatchanged; do \
	rm -f "$execdir/$p" && \
	if test -z ""; \
	then \
		test -n "" && \
		ln -s "$destdir_from_execdir_SQ/bin/git" "$execdir/$p" || \
		{ test -z "yes" && \
		  ln "$execdir/git" "$execdir/$p" 2>/dev/null || \
		  ln -s "git" "$execdir/$p" 2>/dev/null || \
		  cp "$execdir/git" "$execdir/$p" || exit; }; \
	fi \
done && \
remote_curl_aliases="" && \
for p in $remote_curl_aliases; do \
	rm -f "$execdir/$p" && \
	test -n "" && \
	ln -s "git-remote-http" "$execdir/$p" || \
	{ test -z "yes" && \
	  ln "$execdir/git-remote-http" "$execdir/$p" 2>/dev/null || \
	  ln -s "git-remote-http" "$execdir/$p" 2>/dev/null || \
	  cp "$execdir/git-remote-http" "$execdir/$p" || exit; } \
done && \
./check_bindir "z$bindir" "z$execdir" "$bindir/git-add"
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2'
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-mips_24kc/git/usr/bin/git: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-mips_24kc/git/usr/bin/git-shell: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-mips_24kc/git/usr/lib/git-core/git-imap-send: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-mips_24kc/git/usr/lib/git-core/git-sh-i18n--envsubst: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-mips_24kc/git/usr/lib/git-core/git: executable
patchelf: no section headers. The input file is probably a statically linked, self-decompressing binary
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-mips_24kc/git/usr/lib/git-core/git-daemon: executable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-mips_24kc/git/usr/lib/git-core/git-shell: executable
patchelf: no section headers. The input file is probably a statically linked, self-decompressing binary
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-mips_24kc/git into /openwrt/bin/packages/mips_24kc/packages/git_2.30.2-1_mips_24kc.ipk
cp: cannot stat '/openwrt/build_dir/target-mips_24kc_musl/git-2.30.2/ipkg-install/usr/lib/git-core/git-http-fetch': No such file or directory
make[3]: *** [Makefile:164: /openwrt/bin/packages/mips_24kc/packages/git-http_2.30.2-1_mips_24kc.ipk] Error 1
```
