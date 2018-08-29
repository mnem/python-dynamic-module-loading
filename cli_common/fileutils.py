import os
import sys

def get_resolved_script_dir():
    """Returns the directory for this script, following symlinks as necessary"""
    namespace = sys._getframe(1).f_globals
    resolved_script_path = os.path.realpath(namespace['__file__'])
    return os.path.dirname(resolved_script_path)
