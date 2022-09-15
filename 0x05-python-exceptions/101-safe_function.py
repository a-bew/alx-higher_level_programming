#!/usr/bin/python3


def safe_function(fct, *args):

    try:
        result = fct(*args)
    except Exception as error:
        print('Exception: {}'.format(error), file=sys.stderr)
