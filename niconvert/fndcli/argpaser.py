from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser(
        description='弹幕字幕下载和转换工具',
        prefix_chars='-+')

    add_arg = parser.add_argument_group('输入输出').add_argument

    add_arg('path',
            help='niconvert JSON 文件路径',
            type=str)

    add_arg('-o', '--output-filename',
            required=True,
            metavar='FILENAME',
            help='输出文件名',
            type=str,
            default=None)

    add_arg = parser.add_argument_group('弹幕选项').add_argument

    add_arg('-f', '--custom-filter',
            metavar='FILE',
            help='过滤文件，关键词过滤规则文件名',
            type=str,
            default=None)

    add_arg('-T', '--disable-top-filter',
            help='不要过滤顶部弹幕',
            action='store_true')

    add_arg('-B', '--disable-bottom-filter',
            help='不要过滤底部弹幕',
            action='store_true')

    add_arg('-G', '--disable-guest-filter',
            help='不要过滤游客弹幕',
            action='store_true')

    add_arg = parser.add_argument_group('字幕选项').add_argument

    add_arg('+r', '--play-resolution',
            metavar='WIDTHxHEIGHT',
            help='播放分辨率，默认为 %(default)s',
            type=str,
            default='1920x1080')

    add_arg('+f', '--font-name',
            metavar='NAME',
            help='字体名称，默认为自动选择',
            type=str,
            default=None)

    add_arg('+s', '--font-size',
            metavar='SIZE',
            help='字体大小，默认为 %(default)s 像素',
            type=int,
            default=32)

    add_arg('+l', '--line-count',
            metavar='COUNT',
            help='限制行数，默认为 %(default)s 行',
            type=int,
            default=4)

    add_arg('+a', '--layout-algorithm',
            metavar='NAME',
            help='布局算法，默认为 %(default)s 算法',
            type=str,
            choices=('sync', 'async'),
            default='sync')

    add_arg('+t', '--tune-duration',
            metavar='SECONDS',
            help='微调时长，默认为 %(default)s 秒',
            type=int,
            default=0)

    add_arg('+d', '--drop-offset',
            metavar='SECONDS',
            help='丢弃偏移，默认为 %(default)s 秒',
            type=int,
            default=5)

    add_arg('+b', '--bottom-margin',
            metavar='HEIGHT',
            help='底部边距，默认为 %(default)s 像素',
            type=int,
            default=0)

    add_arg('+c', '--custom-offset',
            metavar='LENGTH',
            help='自定偏移',
            type=str,
            default='0')

    add_arg('+h', '--header-file',
            metavar='FILE',
            help='样式模板，ass 的样式模板文件',
            type=str,
            default=None)

    return parser

argpaser = create_parser()
