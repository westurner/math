#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
randstr() {
    # Generate a random string
    # param $1: number of characters
    echo $(dd if=/dev/urandom bs=1 count=$1 2>/dev/null |
            base64 -w 0 |
            rev |
            cut -b 2- |
            tr '/+' '0' |
            rev)
}

writehistline() {
    # Write a line to the USRLOG file
    # param $1: text (command) to log
    printf "%-11s: %s ::: %s\n" "$TERM_ID" "`date +'%D %R.%S'`" "$1" >> $USRLOG
}
"""

import os
import subprocess

def find_usrlog_files(*args):
    files = [
        os.path.expand_user('~/.usrlog'),
    ]
    if 'WORKON_HOME' in os.environ:
        p = subprocess.Popen("find . -maxdepth 1 -name '.usrlog'", shell=True)
        output = p.communicate().readlines() # TODO
        files.extend(s.strip() for s in output)
    return files

def progname():
    """
    mainfunc
    """
    pass


import unittest
class Test_progname(unittest.TestCase):
    def test_progname(self):
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

    progname()

if __name__ == "__main__":
    main()

