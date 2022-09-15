#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    check = True
    try:
        print("{:d}".format(value))
    except (ValueError,TypeError) as error:
        print('Exception: {}'.format(error), file=sys.stderr)
        check = False
    finally:
        return (check)
