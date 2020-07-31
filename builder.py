import json
import os
import re
import shutil
from pathlib import Path

import click
from src import *


@click.group()
@click.option('-d', '--dry-run', 'dry',
              is_flag=True, default=False, help='Dry run mode( and show config on the screen, if possible)')
@click.option('-sdk', '--using-sdk', 'sdk',
              is_flag=True, default=False, help="Using OpenWrt's SDK to build packages(SDK Mode)")
@click.pass_context
def cli(ctx, dry: bool, sdk: bool):
    'An opde builder'
    ctx.ensure_object(dict)
    ctx.obj['set'] = OpdeSetting()
    ctx.obj['dry'] = dry
    ctx.obj['sdk'] = sdk


@cli.command()
@click.pass_context
def feeds(ctx):
    'Initilize feeds'
    setting: OpdeSetting = ctx.obj['set']
    feeds_conf = setting.feeds_conf(ctx.obj['sdk'])
    if ctx.obj['dry']:
        print(feeds_conf)
        return
    setting.openwrt_dir.joinpath(
        'feeds.conf').write_text(feeds_conf)
    shutil.rmtree(setting.openwrt_dir.joinpath('tmp'), ignore_errors=True)
    run('./scripts/feeds update -a && ./scripts/feeds install -a',
        cwd=setting.openwrt_dir.as_posix())


@cli.command()
@click.option('--sdk-archive', type=click.Path(exists=True, file_okay=True, dir_okay=False),
              help="(needed when -sdk or --using-sdk) Path to Openwrt's SDK archive. eg: openwrt-sdk-x86-64_gcc-8.4.0_musl.Linux-x86_64.tar.xz")
@click.pass_context
def init(ctx, sdk_archive: str):
    '''
    Initilize opde (run only once)
     - move OpenWrt source repo to other path (only with --sdk)
     - unpack sdk (only with --sdk)
     - patch to openwrt source to export some necessery infomation
    '''
    setting: OpdeSetting = ctx.obj['set']
    if not ctx.obj['sdk']:
        patchOpenwrt(setting.openwrt_dir, ctx.obj['dry'])
        return
    if not sdk_archive:
        raise click.UsageError('Missing option --sdk-archive', ctx=ctx)
    print(sdk_archive)
    op_repo = setting.submodule(setting.openwrt_dir.as_posix())
    if op_repo:
        if not ctx.obj['dry']:
            op_repo.move(setting.openwrt_dir_in_sdk.as_posix())
    else:
        print('It seem that OpenWrt Source repo has been moved. (%s)' %
              setting.openwrt_dir)
    if not ctx.obj['dry']:
        tmpdir: Path = setting.opde_dir.joinpath('.tmp')
        if tmpdir.exists():
            shutil.rmtree(tmpdir, ignore_errors=True)
        tmpdir.mkdir(parents=True, exist_ok=False)
        run('tar -xvf %s -C %s' % (sdk_archive, tmpdir.absolute().as_posix()))
        sdk_potential_dirs = [x for x in tmpdir.iterdir() if x.is_dir()]
        if len(sdk_potential_dirs) != 1:
            raise BaseException('Something Wrong in SDK')
        sdk_unpack_dir: Path = sdk_potential_dirs[0]
        if setting.openwrt_dir.exists():
            shutil.rmtree(setting.openwrt_dir)
        shutil.move(sdk_unpack_dir, setting.openwrt_dir)
    patchOpenwrt(setting.openwrt_dir, ctx.obj['dry'], not ctx.obj['sdk'])


@cli.command()
@click.pass_context
def deinit(ctx):
    '''
    Deinitilize opde (run only once)
     - revert patch to openwrt source
     - removing sdk (only with --sdk)
     - move OpenWrt source repo back to origin path (only with --sdk)
    '''
    setting: OpdeSetting = ctx.obj['set']
    revertPatchOpenwrt(setting.openwrt_dir, ctx.obj['dry'], not ctx.obj['sdk'])
    if not ctx.obj['sdk']:
        return
    if setting.openwrt_dir.exists():
        print('Removing SDK...')
        if not ctx.obj['dry']:
            shutil.rmtree(setting.openwrt_dir)
    if not ctx.obj['dry']:
        print('Moving OpenWrt source repo back to origin path')
        op_repo = setting.submodule(setting.openwrt_dir_in_sdk.as_posix())
        if op_repo:
            if not ctx.obj['dry']:
                op_repo.move(setting.openwrt_dir.as_posix())
        else:
            BaseException('Unable to find OpenWrt Source repo. (%s)' %
                          setting.openwrt_dir_in_sdk)


@cli.command()
@click.option('-sdk', '--build-sdk', 'sdk',
              is_flag=True, default=False, help='Build the OpenWrt SDK')
@click.option('-ib', '--build-image-builder', 'ib',
              is_flag=True, default=False, help='Build the OpenWrt Image Builder')
@click.option('-ke', '--linux-embedded-modules', 'ke',
              is_flag=True, default=False, help='Select kernel modules removed in SDK')
@click.option('-a', '--all-packages', 'all_packs',
              is_flag=True, default=False, help='Select all userspace packages by default')
@click.pass_context
def config(ctx, sdk: bool, ib: bool, all_packs: bool, ke: bool):
    'Configurate openwrt'
    setting: OpdeSetting = ctx.obj['set']
    setting.openwrt_dir.joinpath('logs').mkdir(parents=True, exist_ok=True)
    configer = Configer()
    configer.compose(*setting.targets)
    if ctx.obj['sdk']:
        configer.sdk_mode()
    configer.download_dir(setting.cache_dir.joinpath('openwrt'))
    if sdk:
        configer.build_sdk()
    if ib:
        configer.build_image_builder()
    if all_packs:
        configer.select_all()
    if ke:
        modules = ['# kernel modules removed in SDK']
        modules.extend(['CONFIG_PACKAGE_%s=m' %
                        i for i in setting.linux_embedded_module])
        configer.inject('\n'.join(modules))
    conf = configer.commit()
    if ctx.obj['dry']:
        print(conf)
        return
    setting.openwrt_dir.joinpath('.config').write_text(configer.commit())
    shutil.copyfile(setting.openwrt_dir.joinpath('.config'),
                    setting.openwrt_dir.joinpath('logs', 'min-config.in'))
    run('make defconfig', cwd=setting.openwrt_dir.as_posix())


@cli.command()
@click.pass_context
def download(ctx):
    "Download Openwrt's downloaded source bundles"
    setting: OpdeSetting = ctx.obj['set']
    if ctx.obj['dry']:
        print('Download Done')
        return

    run('make -j{0} download && make -j{0} download && make -j{0} download'.format(os.cpu_count() * 4),
        cwd=setting.openwrt_dir.as_posix())


@cli.command()
@click.pass_context
def build(ctx):
    'Build OpenWrt'
    setting: OpdeSetting = ctx.obj['set']
    if ctx.obj['dry']:
        print('Build Done')
        return
    run('make -j%s IGNORE_ERRORS="y m n" |& tee logs/log.out' % os.cpu_count(),
        cwd=setting.openwrt_dir.as_posix())


@cli.command()
@click.argument('logdir', type=click.Path(exists=True, dir_okay=True, file_okay=False))
@click.argument('database', type=click.Path(file_okay=True, dir_okay=False))
@click.argument('run-number', type=click.INT)
@click.pass_context
def extract(ctx, logdir: str, database: str, run_number):
    'Extract build information from logs'
    setting: OpdeSetting = ctx.obj['set']
    extractor = LogsExtractor(Path(logdir))
    setting.logs_ast = extractor.logsAst
    if ctx.obj['dry']:
        print('Extract Done')
        return
    db = LogsDb(database)
    for logAst in setting.logs_ast:
        item = LogsDb.merge(logAst, *setting.targets, run_number=run_number)
        db.insert(item)
    db.close()


@cli.command()
@click.argument('database', type=click.Path(file_okay=True, dir_okay=False))
@click.argument('run-number', type=click.INT)
@click.pass_context
def check(ctx, database: str, run_number):
    '''
    Check if error exist
    0: not error exist
    1: exist error
    '''
    setting: OpdeSetting = ctx.obj['set']
    db = LogsDb(database)
    ans = 1 if db.exist_error(*setting.targets, run_number=run_number) else 0
    db.close()
    print(ans)
    exit(ans)


@cli.command()
@click.argument('number', type=click.INT, default=20)
@click.argument('database', type=click.Path(file_okay=True, dir_okay=False))
@click.option('-ke', '--linux-embedded-modules', 'ke',
              is_flag=True, default=False, help='Disable filter out kernel modules removed in SDK from tasks')
@click.pass_context
def assign(ctx, number: int, ke: bool, database: str):
    'Assignments all packages to serval(default:20) workers'
    setting: OpdeSetting = ctx.obj['set']
    deps_tree = DependsTree()
    deps_tree.inject_package_info(setting.packageinfo_ast)
    db = LogsDb(database)
    deps_tree.inject_costs(db, *setting.targets)
    db.close()
    setting.deps_dag = deps_tree.to_json()
    distributor = WorksDistributor()
    distributor.build(setting.deps_dag_file)
    setting.tasks_list = distributor.deduce_depends_all(number)
    if not ke:
        linux_embedded_module = set(setting.linux_embedded_module)
        new_tasks_list = []
        for worker in setting.tasks_list:
            tasks = []
            for pack in worker:
                if pack in linux_embedded_module:
                    continue
                tasks.append(pack)
            tasks = list(set(tasks))
            tasks.sort()
            new_tasks_list.append(tasks)
        setting.tasks_list = new_tasks_list
    tasks_list = setting.tasks_list
    setting.worker_conf_dir.mkdir(parents=True, exist_ok=True)
    for i in range(number):
        conf = ['# worker %s' % (i + 1)]
        conf.extend(['CONFIG_PACKAGE_%s=m' % pack for pack in tasks_list[i]])
        setting.worker_conf_dir.joinpath(
            '{:0>2}.worker.in'.format(i + 1)).write_text('\n'.join(conf))
    print('workers conf save in %s' % setting.worker_conf_dir)


@cli.command()
@click.pass_context
def metadata(ctx):
    """
    generate metadata forOpenwrt's Source bundle
    """
    setting: OpdeSetting = ctx.obj['set']
    print(json.dumps(setting.metadata_hash, indent=2,
                     sort_keys=True, separators=(",", ":")))


@cli.command('@hack-sdk', hidden=True)
@click.argument('directory', type=click.Path(exists=True, dir_okay=True, file_okay=False))
@click.pass_context
def _hack_sdk(ctx, directory: str):
    'hack configuration in SDK, run by makefile'
    setting: OpdeSetting = ctx.obj['set']

    print(Path(directory).absolute())
    sdk_dir = Path(directory)
    build_conf_path = sdk_dir.joinpath('Config-build.in')
    shutil.copy(build_conf_path, sdk_dir.joinpath('.Config-build.in.ori'))
    worker_build_conf_path = sdk_dir.joinpath('.Config-build.in.worker')
    print('fixing %s' % build_conf_path.as_posix())
    parser = KconfigParser()
    ast = parser.gen_ast(build_conf_path.read_text())
    setting.sdk_buildin_ast = ast

    linux_embedded_module = set(setting.linux_embedded_module)
    packages = set(setting.packages)
    # needs compile in sdk
    packages.remove('base-files')
    new_conf = []
    worker_conf = []
    reg = re.compile('^(DEFAULT_|PACKAGE_|LUCI_LANG_|FEED_)(.*)')
    for i in setting.sdk_buildin_ast:
        match = reg.match(i['sym'])
        if not match:
            # reset some option
            if i['sym'] == 'DOWNLOAD_FOLDER':
                i['default'] = '';
            new_conf.append(i)
            worker_conf.append(i)
        else:
            gps = match.groups()
            if gps[0] in ['LUCI_LANG_', 'FEED_']:
                pass
            elif gps[1] in linux_embedded_module:
                new_conf.append(i)
                # worker_conf.append(i)
            elif gps[1] in packages:
                if gps[0] in ['DEFAULT_']:
                    new_conf.append(i)
            else:
                worker_conf.append(i)
                new_conf.append(i)

    build_conf_path.write_text(KconfigDumper(new_conf))
    worker_build_conf_path.write_text(KconfigDumper(worker_conf))
    revertPatchOpenwrt(directory, False, False)


@cli.command('install-sdk')
@click.pass_context
def install_sdk(ctx):
    setting: OpdeSetting = ctx.obj['set']
    run('make target/sdk/install V=s -j4', cwd=setting.openwrt_dir.as_posix())


@cli.command('@output', hidden=True)
@click.argument('variable', type=str)
@click.pass_context
def output_openwrt(ctx, variable):
    '''
    output variable
    opdir,arch,board,logdir,metadata
    '''
    setting: OpdeSetting = ctx.obj['set']
    if variable == 'opdir':
        print(setting.openwrt_dir.absolute())
    elif variable == 'logdir':
        print(setting.openwrt_dir.joinpath('logs').absolute())
    elif variable == 'arch':
        print(setting.targets[0])
    elif variable == 'board':
        print(setting.targets[1])
    elif variable == 'metadata':
        metadata = {}
        for makefile in setting.packageinfo_ast:
            for pack in makefile['packages']:
                metadata[pack['Package']] = '/'.join(
                    [pack[i] for i in ['Package-Source-Version',
                                       'Package-Hash', 'Package-Mirror-Hash']]
                )
        print(json.dumps(metadata, indent=2, separators=(",", ":"), sort_keys=True))


if __name__ == '__main__':
    os.environ['OPDE_BUILDER'] = Path(__file__).absolute().as_posix()
    os.environ['OPDE_PYTHON'] = shutil.which('python3')
    cli(obj={})
