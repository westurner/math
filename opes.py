#!/usr/bin/env python
# encoding: utf-8
"""
Connectives
"""


import operator
from itertools import product


def crossproduct(_set=(0, 1), deg=2):
    return product(*(_set,) * deg)

import unittest
class TestTestTestName(unittest.TestCase):
    def test_func_name(self):
        connectives = {}
        connectives['bool'] = ['and','or',('and','!')]
        pass
        raise NotImplementedError()

def inspect_operators():
    raise NotImplemented
    import inspect
    oattrs = (getattr(operator, x) for x in dir(operator)
                                    if not x.startswith('_'))
    for f in oattrs:
        if inspect.iscode(f):
            print '-----', f, inspect.getargspec(f)
        else:
            print f, '/0/0/0'

    #?inspect.getargs
    print '\t'.join(sorted(dir(operator)))


def main():
    """
    mainfunc
    """
    pass


if __name__ == "__main__":
    import optparse
    import logging

    prs = optparse.OptionParser(usage="./")

    prs.add_option('-v', '--verbose',
                    dest='verbose',
                    action='store_true')
    prs.add_option('-q', '--quiet',
                    dest='quiet',
                    action='store_true')
    prs.add_option('-t', '--test',
                    dest='run_tests',
                    action='store_true')

    (opts, args) = prs.parse_args()

    if not opts.quiet:
        logging.basicConfig()

        if opts.verbose:
            logging.getLogger().setLevel(logging.DEBUG)

    if opts.run_tests:
        import sys
        sys.argv = sys.argv[0] + args
        import unittest
        exit(unittest.main())

    main()
