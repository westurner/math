#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
normal_dist
"""


import sympy
from sympy.statistics import Normal
from sympy.abc import x

def normal_dist(mu=100, sigma=15):
    """
    mainfunc
    """
    dist = Normal(mu,sigma)
    dist_cdf = dist.cdf(x)
    sympy.Plot(dist_cdf)
    pass


import unittest
class Test_normal_dist(unittest.TestCase):
    def test_normal_dist(self):
        pass


def main():
    import optparse
    import logging

    prs = optparse.OptionParser(usage="./%prog : args")

    prs.add_option('-v', '--verbose',
                    dest='verbose',
                    action='store_true',)
    prs.add_option('-q', '--quiet',
                    dest='quiet',
                    action='store_true',)
    prs.add_option('-t', '--test',
                    dest='run_tests',
                    action='store_true',)

    (opts, args) = prs.parse_args()

    if not opts.quiet:
        logging.basicConfig()

        if opts.verbose:
            logging.getLogger().setLevel(logging.DEBUG)

    if opts.run_tests:
        import sys
        sys.argv = [sys.argv[0]] + args
        import unittest
        exit(unittest.main())

    normal_dist()

if __name__ == "__main__":
    main()
