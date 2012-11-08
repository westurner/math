#!/usr/bin/env python
"""
Objects
--------
obj    obj


Features
----------
bool f_k1
int    f1
bool f2
int    f3
..     ..
"""
from itertools import imap
from collections import defaultdict
import unittest

import numpy as np

def first_pass(objs, feats):
    """
    emit facts in 2d linear fill
    """
    for objkey in objs:
        obj = objs[objkey]
        for featname, feat in feats.iteritems():
            yield (objkey, featname, feat['func'](obj))

def second_pass(data, feats):
    """
    return function to estimate population parameter based on data
    """
    for featname, feat in feats.iteritems():
        if feat['type'] in ('int','long','float'):
            # differential
            #                        walk: polyreg, svm ? 
            yield (featname, build_prob_dist(data, feat))
        elif feat['type'] in ('bool'):
            yield (featname, build_prob_dist(data, feat))

class CategoricalBin():
    def __init__(self, data=None):
        self.count = 0
        self.counts = None
        self.bins = defaultdict(list)
        
        self.last_calc = 0

        if data:
            self.load_data(data)

    def append(self, k, v):
        self.count += 1
        self.bins[v].append(k)

    def load_data(self, data=None):
        bins = self.bins
        for k, v in data:
            self.bins[v].append(k)
            self.count += 1

    def calculate_probs(self):
        bins = self.bins
        count = self.count
        counts = dict(
                (k,
                (count and ( len(bins[k]) / float(count) )
                    or 0))
                for k in bins)
        self.counts = counts

    def calculate_prob(self, var): # no overloading
        return (count and ( len(self.bins[var]) / float(self.count) ) or 0)

    def print_counts(self):
        bins = self.bins
        counts = self.counts
        keys = sorted(bins.keys())
        print '-- %d vals, %d samples' % (len(keys), self.count)
        print    '%s\t%s\t%s' % ('Value','Probability','Count')
        tblfmt = '%s\t%f\t%d'
        for k in keys:
            print tblfmt % (k, counts[k], len(bins[k]))

    def print_data(self):
        fmtstr='%s\t%s'
        for k,l in self.bins.iteritems():
            print fmtstr % (k, l)

    def get_prob(self, val):
        if self.counts is None or self.last_calc < self.counts:
            self.calculate_probs()
        return self.counts[val]


    def as_numpy_array(self, dtype=np.float32):
        counts=self.counts
        self.calculate_probs()
        keys = list(counts.keys())
        values = (counts[k] for k in keys)
        keyidx = dict(enumerate(keys))

        a = np.fromiter(values, dtype=dtype)
        return a, keyidx

class NumpyCategoricalBin(object):
    def __init__(self, data=None):

        idx = Index()
        if data:
            self.load_data(data)

    def load_data(self, data, sizehint=100):
        self.data = a
            

    def calculate_probs():
        for k,v in self.data:
            np[idx[k]] += 1


class Index():
    def __init__(self):
        self.keys = {}
        self.count = 0

    def __getitem__(self, k):
        if k not in self.keys:
            idx=count
            self.keys[k] = idx
            self.count += 1
            return idx
        return self.keys[k]



class TestCategoricalBin(unittest.TestCase):
    def test_categorical_bin(self):
        b = CategoricalBin()
        self.assertEqual(b.count,0)
        self.assertEqual(b.counts, None)
        b.append('red',True)
        self.assertEqual(b.count, 1)
        self.assertEqual(b.counts, None)
        self.assertEqual(b.get_prob(True), 1.0)
        self.assertEqual(b.count,1)
        b.print_counts()
        b.append('blue', True)
        self.assertEqual(b.get_prob(True), 1.0)
        b.print_counts()
        b.append('magenta',False)
        self.assertEqual(b.get_prob(False), (1/3.0))
        b.print_counts()

        print b.as_numpy_array()

        raise Exception()

    def test_cartesian(self):
        from itertools import product
        l = ('X','Y')
        b = CategoricalBin(enumerate(','.join(sorted(s)) for s in product(l,l)))
        b.calculate_probs()
        b.print_counts()
        self.assertEqual(b.count,4)
        self.assertEqual(b.get_prob('X,X'), 0.25)
        self.assertEqual(b.get_prob('X,Y'), 0.50)
        self.assertEqual(b.get_prob('Y,Y'), 0.25)

        b.print_data()

class TestOther(unittest.TestCase):
    def test_addl(self):
        import numpy as np
        from itertools import product
        l = ('X','Y')

        a = np.zeros((len(l),)*2, np.float32)

        print a
        lx = dict( (v, i) for i,v in enumerate(l) )

        for p in product(l,l):
            pt= tuple(lx[d] for d in sorted(s for s in p)) # !
            a[pt] += 1 

        print a

        dg= (np.tril(a)*2)-(np.identity(max(a.shape),np.int))
        d = dg/float(dg.sum())

        print d


def build_prob_dist(data, feat, vartype='bool'):
    print "Building prob dist for %r (%r)" % (feat, data)

    x="""
    if vartype=='bool':
        bins = Bin(list)
        for k,d in data.iteritems():
            bins[data.get(feat)].append(k)

        def cdf(var):
            return len(bins[var])

    elif vartype=='int':
        bins = defaultdict(list)
    """

    return {
        'func':lambda *args, **kwargs: (args,kwargs),
        'stats':{
            'mean':None,
            'stddev':None,
            #..
         },
    }

def pipeline(train, knowns, feats):
    DATA = defaultdict(dict)
    POPULATION = defaultdict(dict)
    FEATURES = defaultdict(dict)

    for (obj, feat, val) in first_pass(train, feats):
        print "feat: %r %r %r" % ( feat, obj, val )
        DATA[feat][obj] = val

    for (feat, data) in second_pass(train, feats):
        POPULATION[feat] = data

    for feat in feats:
        func = POPULATION[feat]['func']
        FEATURES[feat]['data'] = (func(x) for x in DATA[feat])
        # TODO: calc variance: abs(x - func(x))^2

    return dict(data=DATA, population=POPULATION, features=FEATURES)

def main():
    import optparse
    import sys

    prs = optparse.OptionParser()
    prs.add_option('-t',dest='test',action='store_true')
    opts,args = prs.parse_args()

    if opts.test:
        sys.argv=[sys.argv[0]]+args
        unittest.main()


TESTDATA={
 "red": {
    "str": "the red string",
    "attrx": True,
 },
 "green": {
    "str": "the green str",
    "attrx": True,
 },
 "blue": {
    "str": "the blue str",
    "attrx": False,
 },
}

def invert_dict2(dict2):
    d=defaultdict(dict)
    for k1, d1 in dict2.iteritems():
        for k2, d2 in d1.iteritems():
            d[k2][k1] = d2
        return d


class TestIt(unittest.TestCase):
    def test_it(self):
        data=TESTDATA
        train=data
        knowns=data
	    
        feats={
            'len': {
                'type':'int',
                'func': lambda x: len(x.get('str')),
             },
            'maxchr': {
                'type':'int',
                'func': lambda x: chr(max(ord(c) for c in x.get('str','\0'))),
             },
        }
	result = pipeline(train,knowns,feats)

	import pprint
	print pprint.pprint(result, indent=4)

    #raise Exception()

if __name__=="__main__":
    main()

"""
--general--
CONTEXT
norm
 intr
 def cat_pop_prob(v_int)
 
                 integral point f
 bool: cat_pop_prob(v)
	

integral (? gaussian ?)


==per feat==
--supervised--
cat
integral
diff of integrals / PDF
 (abs(cat_feat_prob(v) - cat_pop_prob(v)) for v in features)

==reduce==
sort by diff of integrals / PDF


"""
