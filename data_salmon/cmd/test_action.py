
import argparse

from data_salmon import TestSuite

class _TestAction(argparse.Action):
    def __init__(self, option_strings, dest=argparse.SUPPRESS,
                 default=argparse.SUPPRESS, help=None):
        super(_TestAction, self).__init__(option_strings=option_strings,
        dest=dest,
        default=default,
        nargs=0,
        help=help)

    def __call__(self, parser, namespace, values, option_string=None):
        TestSuite.run()
        parser.exit()