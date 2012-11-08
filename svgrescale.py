#!/usr/bin/env python
# encoding: utf-8
"""
SVG Rescale
"""


def main():
    """
    mainfunc
    """
    raise Exception("fail")
    pass


def rescale_svg(filename):
    """
    TODO: fix this
    #FIXME: this TODO
    """
    with open(filename, 'rb') as f:
        tree = etree.parse(f)

        grp = tree.new_group("rescalesvggroup", tree.select_all() )
        new_dims = resize_within_bounds(grp, margin='0.05')
        (h,w), (x,y) = new_dims

        tree.height = h
        tree.width = w
        grp.x = x
        grp.y = y

        


def invert_svg(filename):
    with open(filename, 'rb') as f:
        tree = etree.parse(f)

        for s in tree.shapes:
            s.colors = invert(s.colors)

def export_to_png(tree, filename):
    # export to PDF
    tree.draw_bkg_layer(tree.dims)
    svg_to_png(tree, filename)


if __name__ == "__main__":
    import optparse
    import logging

    prs = optparse.OptionParser(usage="./")

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
        sys.argv = sys.argv[0] + args
        import unittest
        exit(unittest.main())

    main()

# add a TODO: here
import unittest


class TestSVGRescale(unittest.TestCase):
    def test_func_name(self):
        print "test"
        main()
        raise NotImplementedError()
        #raise Exception()
