#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import argparse
import importlib
import os
import cli_common.fileutils as fu
import cli_common

def create_root_parser():
    root_parser = argparse.ArgumentParser()
    root_parser.add_argument('-v', '--verbose', help='Output verbosely', action='store_true')
    return root_parser

def get_command_dirs(path):
    """Creates a generator returning all command directories at the specified path"""
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        # Make sure we're looking at a directory
        if not os.path.isdir(item_path):
            continue
        # Make sure it looks like a command
        if not item.startswith("cmd_"):
            continue
        # Looks like a command dir
        yield item, item_path

def add_commands(root_parser):
    command_parsers = root_parser.add_subparsers(dest='command', title='Commands')
    command_parsers.required = True
    script_dir = fu.get_resolved_script_dir()
    for command, dir in get_command_dirs(script_dir):
        cli = importlib.import_module("{}.cli".format(command))
        cli.add_commands(command_parsers)

def main():
    root_parser = create_root_parser()
    add_commands(root_parser)
    args = root_parser.parse_args()
    cli_common.VERBOSE = args.verbose
    args.func(args)

if __name__ == "__main__":
    main()