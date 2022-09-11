#!/usr/bin/python
import argparse
import sys

import lokaord


if __name__ == '__main__':
    lokaord.ArgParser = argparse.ArgumentParser(
        description='Loka-Orð', formatter_class=argparse.RawTextHelpFormatter
    )
    lokaord.ArgParser._actions[0].help = 'Show this help message and exit.'
    lokaord.ArgParser.add_argument('-v', '--version', action='store_true', help=(
        'Print version and exit.'
    ))
    lokaord.ArgParser.add_argument('-ln', '--logger-name', default='frettaskra', help=(
        'Define logger name (Default: "frettaskra").'
    ))
    lokaord.ArgParser.add_argument('-ldir', '--log-directory', default='./logs/', help=(
        'Directory to write logs in. Default: "./logs/".'
    ))
    lokaord.ArgParser.add_argument('-r', '--role', default='cli', help=(
        'Define runner role.\n'
        'Available options: "cli", "api", "cron", "hook", "mod" (Default: "cli").'
    ))
    pargs = lokaord.ArgParser.parse_args()
    if len(sys.argv) == 1:
        lokaord.print_help_and_exit()
    if pargs.version is True:
        print(lokaord.__version__)
    arguments = {
        'logger_name': pargs.logger_name,
        'log_directory': pargs.log_directory,
        'role': pargs.role,
    }
    lokaord.main(arguments)