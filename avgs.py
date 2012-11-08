#!/usr/bin/env python
import math
from itertools import izip, count

def simpleavg(s):
    return float(sum(s)) / len(s)



def streamavg_weak(itr):
    nasty = []
    for i,val in enumerate(itr):
        nasty.append(val)
        yield i, val, simpleavg(nasty)


TESTDATA = range(0,1000,10)

TESTDATA_SEGS = (
    range(0,500,10),
    range(500,600,10),
    range(600,1000,10),
)

import unittest
import operator

class TestTestData(unittest.TestCase):
    def test_testdata(self):
        self.assertEqual(  
            reduce(operator.add, TESTDATA_SEGS),
            TESTDATA

        )

class TestStreamAvgWeak(unittest.TestCase):
    def test_streamavg_weak(self):
        for x in streamavg_weak(TESTDATA):
            print x


def streamavg_running(itr):
    """
    caluclate :) continuous momentary mean (cumsum)
    from start to finish

    :param itr: summable iterable
    :type itr: iterable
    :returns: cummean generator
    """
    if not hasattr(itr, 'next'):
        itr = iter(itr)
    avg=itr.next()
    yield 0, avg, avg
    for i,val in izip(count(1), itr):
        weight=(1.0 / (i+1) )
        newavg=avg - (avg*weight) + (weight*val)
        # ~= newavg=(avg*i + val)/(i + 1)

        yield i, val, newavg
        avg=newavg

def streamavg_running_segment(itr, avg=None, seqpos=0):
    """
    calculate momentary mean (cumsum/n)
    optionally from {avg,seqpos}

    :param itr: summable iterable
    :type itr: iterable
    :returns: cummean float generator
    """
    if not hasattr(itr, 'next'):
        itr = iter(itr)
    avg = avg or itr.next()
    yield seqpos, avg, avg
    for i,val in izip(count(seqpos+1), itr):
        weight = (1.0 / (i+1) )
        newavg = avg - (avg*weight) + (weight*val)

        yield i, val, newavg
        avg=newavg


class TestStreamAvgRunning(unittest.TestCase):
    def test_streamavg_runing(self):
        for x in streamavg_running(TESTDATA):
            print x

class TestSanity(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(
                [x for x in streamavg_weak(TESTDATA)],
                [x for x in streamavg_running(TESTDATA)]
                )


class TestStreamAvgRunningSegment(unittest.TestCase):
    def test_(self):

        import itertools
       
        self.assertEqual(
            [x for x in streamavg_weak(sum(TESTDATA_SIGS))], # reduce(operator.add, TESTDATA_SEGS))],
            [x for x in itertools.chain(
                *(streamavg_running_segment(TESTDATA_SEGS[i]) for i in xrange(0,len(TESTDATA_SEGS)))
                )]
        )

if __name__=="__main__":
     val = None
    for x in streamavg_weak(range(0,100000,2)):
        val = x
    print val
