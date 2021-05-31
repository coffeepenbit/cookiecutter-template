import argparse
import os
from pathlib import Path


def get_cli_args():
    return _get_argparser().parse_args()


def _get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--log-level',
        dest='loglevel',
        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'],
        default='WARNING'
    )
    parser.add_argument(
        '-c', '--conf',
        dest='conf_path',
        default=(Path('./conf.yml')
                 if os.path.exists('./conf.yml')
                 else Path('conf.yml.example')),
        type=_path
    )
    # parser.add_argument(
    #     '-f', '--flag',
    #     help="Help me",
    #     dest='flag_variable_name',
    #     choices=['foo','bar']
    #     type=int, # can also use func handle here to parse argument
    #     default=None
    # )
    

    return parser


def _default_conf_path():
    os.path.exists


def _path(path):
    return Path(path)
