import os
import cli_common
import cli_common.basictemplate as t
import datetime
import random

template = """Today is {{date_now}}

This simple rendered template is brought
to you buy {{colour}} and the number {{number}}"""

def _get_date():
    return datetime.datetime.now().isoformat()

def _get_colour():
    return random.choice(['red','orange','yellow','green','blue','indigo','violet'])

def _get_number():
    return random.randint(1, 20)

def execute(args):
    template_context = dict(date_now=_get_date(), colour=_get_colour(), number=_get_number())
    rendered = t.render_string_template(template, template_context)
    if args.output == None:
        cli_common.log(rendered)
    else:
        with open(args.output, 'w') as text_file:
            text_file.write(rendered)

def add_commands(parser):
    command_abs_dir = os.path.abspath(__file__)
    command_dir = os.path.basename(os.path.dirname(command_abs_dir))
    command_name = command_dir[len('cmd_'):]
    command_parser = parser.add_parser(command_name, help="Do some stuff and things.")
    command_parser.add_argument('-o', '--output', help='The output file')
    command_parser.set_defaults(func=execute)
