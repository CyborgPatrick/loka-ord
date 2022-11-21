#!/usr/bin/python
import argparse
import sys

import lokaord


def print_help_and_exit():
    if lokaord.ArgParser is not None:
        lokaord.ArgParser.print_help(sys.stderr)
    else:
        logman.warning('lokaord.ArgParser was None.')
        logman.error('Exiting ..')
    sys.exit(1)


if __name__ == '__main__':
    lokaord.ArgParser = argparse.ArgumentParser(
        description='\033[33mLoka-Orð\033[0m', formatter_class=argparse.RawTextHelpFormatter
    )
    lokaord.ArgParser.prog = 'lokaord'
    lokaord.ArgParser._actions[0].help = 'Show this help message and exit.'
    lokaord.ArgParser.add_argument('-v', '--version', action='store_true', help=(
        'Print version and exit.'
    ))
    lokaord.ArgParser.add_argument('-ln', '--logger-name', default='lokaord', help=(
        'Define logger name (Default: "lokaord").'
    ))
    lokaord.ArgParser.add_argument('-ldir', '--log-directory', default='./logs/', help=(
        'Directory to write logs in. Default: "./logs/".'
    ))
    lokaord.ArgParser.add_argument('-r', '--role', default='cli', help=(
        'Define runner role.\n'
        'Available options: "cli", "api", "cron", "hook", "mod" (Default: "cli").'
    ))
    lokaord.ArgParser.add_argument('-bdb', '--build-db', action='store_true', help=(
        'Build database from datafiles.'
    ))
    lokaord.ArgParser.add_argument('-rbdb', '--rebuild-db', action='store_true', help=(
        'Delete current database and rebuild from datafiles.'
    ))
    lokaord.ArgParser.add_argument('-bakdb', '--backup-db', action='store_true', help=(
        'Create backup of current SQLite database file.'
    ))
    lokaord.ArgParser.add_argument('-wf', '--write-files', action='store_true', help=(
        'Write data from database to JSON textfiles.'
    ))
    lokaord.ArgParser.add_argument('-aw', '--add-word', action='store_true', help=(
        'Add word CLI.'
    ))
    lokaord.ArgParser.add_argument('-s', '--search', metavar=('WORD', ), help=(
        'Search for word in database.'
    ))
    lokaord.ArgParser.add_argument('-st', '--stats', action='store_true', help=(
        'Print database word count data in JSON string.'
    ))
    lokaord.ArgParser.add_argument('-mdst', '--md-stats', action='store_true', help=(
        'Print database word count in Markdown table.'
    ))
    pargs = lokaord.ArgParser.parse_args()
    if len(sys.argv) == 1:
        print_help_and_exit()
    if pargs.version is True:
        print('%s %s' % (lokaord.ArgParser.prog, lokaord.__version__))
        sys.exit(0)
    arguments = {
        'logger_name': pargs.logger_name,
        'log_directory': pargs.log_directory,
        'role': pargs.role,
        'build_db': pargs.build_db,
        'rebuild_db': pargs.rebuild_db,
        'backup_db': pargs.backup_db,
        'write_files': pargs.write_files,
        'add_word': None,
        'add_word_cli': pargs.add_word,
        'search': pargs.search,
        'stats': pargs.stats,
        'md-stats': pargs.md_stats,
    }
    lokaord.main(arguments)
