VERBOSE=False

def log(message):
    """Logs a message to stdout"""
    print(message)

def log_verbose(message):
    """Logs a message to stdout if VERBOSE is True"""
    if VERBOSE:
        print(message)
