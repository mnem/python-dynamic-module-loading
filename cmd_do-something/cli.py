import os
import cli_common

def execute(args):
    cli_common.log_verbose(args)

def add_commands(parser):
    command_abs_dir = os.path.abspath(__file__)
    command_dir = os.path.basename(os.path.dirname(command_abs_dir))
    command_name = command_dir[len('cmd_'):]
    command_parser = parser.add_parser(command_name, help="Do some stuff and things.")
    command_parser.add_argument('-o', '--output', help='The output file', default='some-output')
    command_parser.set_defaults(func=execute)
