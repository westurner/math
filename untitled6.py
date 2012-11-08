# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 06:20:44 2011

@author: wturner
"""

from itertools import chain, izip, count, product, permutations, combinations
from collections import defaultdict

axisiter = lambda l,maxn: izip(count(), chain(*(product(*((l,)*n)) for n in range(maxn+1))))


matrixiter = lambda l,maxn: enumerate(product(axisiter(l,maxn), axisiter(l,maxn)))
def matrixiter2(l, maxn):
    axis = list(axisiter2(l, maxn))
    for p in enumerate(product(axis, axis)):
        yield p

def matrixiter3(l, maxn):
    axis_ = list(axisiter(l, maxn))
    #axis = dict( (v,i) for i,v in axis_ )
    
    for i, data in enumerate(product(xrange(len(axis_)), xrange(len(axis_)))):
        yield i, data



def formatpair(x,y):
    fmt='%s %s'
    terms_x = (str(t) for t in x)
    terms_y = (str(t) for t in y)
    

axisiter2 = lambda l,maxn: izip(count(), chain(*(combinations(l,n) for n in range(maxn+1))))
#matrixiter4 = lambda l, maxn: izip(
#    count(),
#    chain(*
#        (
#        permutations(axisiter2(l,maxn), n) for n in range(maxn+1)
#        )
#    )
#    )
matrixiter4 = lambda l, maxn: izip(
count(),
permutations(axisiter2(l,maxn),2) # for n in xrange(maxn+1))
)
def matrixiter5(l, maxn, full=True):

    i_ = count()
    for (i, ((yn,(y)), (xn,(x)))) in matrixiter4(l, maxn): 
                                    #izip(count(), permutations(axisiter2(l, maxn))):
        #print xn, yn
        if full or not xn or yn < xn:
            reali = i_.next()
            d = i - reali
            yield '%10d %10d %10d   (%3d,%-3d)   %r %r' % (reali, d, i, xn, yn, x, y)
            #next
        else:
            yield '%10s %10s %10d   (%3d,%-3d)   %r %r' % ('*', '*', i, xn, yn, x, y)
        #((n, (x, (xlabel)), (y, (ylabel))),) = item


def dframe(l, maxn):
    from pandas import DataFrame, Index
    
    axis = [x for x in axisiter(l, maxn)]
    idx=Index(axis)
    data = (x for x in matrixiter(l, maxn))
    df = DataFrame(data, idx)





import unittest 
def main():
    unittest.main()


EASYPEASY={
'axes': ('w','x','y','z', 's'),
'data': (
    ('a',(1,1,0,0, 0,), ),
    ('b',(1,1,1,0, 1,), ),
    ('c',(1,1,0,1, 0,), ),
    ('d',(0,1,1,0, 1,), ),
    ('e',(1,1,1,1, 0,), ),
    ('f',(1,1,1,0, 1,), ),
    )
}


def to_dataframe(ds=EASYPEASY):
    """
    load a dataset dict into a DataFrame
    
    :param ds: dataset dict
    :type ds: {'axes': ['x','y','z', 's'], 'data': ( (key, (data)), ... ) }
    
    :returns: DataFrame.transpose
    """
    from pandas import DataFrame, Index
    axes = ds['axes']
    data = dict((k, dict(izip(axes,v)) ) for (k,v) in ds['data'])
    #print data
    #axes_nlookup = dict((v, n) for v in enumerate(ds['axes']))
    return DataFrame(data=data, index=Index(axes)).T
            
def two_dataframes(ds=EASYPEASY, splitter='s'):
    """
    split a dataset dict in two based on a boolean attr, cast to DataFrames
    
    :param ds: dataset dict
    :type ds: {'axes': ['x','y','z', 's'], 'data': ( (key, (data)), ... ) }
    :param spliiter: attribute to split on (e.g. known observation)
    :type spltter: attr name
    
    :returns: (DataFrame(attr==true).T , DataFrame(attr==false).T))
    
    .. Note::
        
        PyTables / h5py supports more 'normal' table queries.
        single-writer per-file, multiple readers
        
        See: http://www.pytables.org/moin/HintsForSQLUsers
    
    """
    from pandas import DataFrame, Index
    axes = ds['axes']
    data = ds['data']
    
    sol = {}
    notsol = {}
    
    solaxis=axes.index(splitter)
    
    for k,v in data:
        if bool(v[solaxis]):
            sol[k] = v # TODO: assumes uniq keys 
        else:
            notsol[k] = v
            
    idx=Index(axes)
    
    # Tranpose DataFrames from:
        #  (x,y) = attr, key
    # to:
        # (x,y) = key, attr
    return (
        DataFrame(data=sol, index=idx).T,
        DataFrame(data=notsol, index=idx).T,
    )
        
            
def freq_of(df, args):
    """
    ~p() of arg1 [ ⋂ arg2 ⋂ ... ⋂ argn ]

    :param df: DataFrame to query
    :type df: bool DataFrame
    :param args: attribute[s] to count for
    :type args: list, iterable
    
    :returns: actual frequency of (arg1 AND arg2 ... AND argn)

    seeAlso: 

    """
    ew = df.T.apply(lambda x: all([x[k] > 0 for k in args]))
    return ew.mean() #, ew.std()

def freq_of_not(df, args):
    """
    ~p() of arg1 and NOT(arg2 ⋃ arg3 ... ⋃ argn) *

    :param df: DataFrame to query
    :type df: bool DataFrame
    :param args: attribute[s] to count for
    :type args: list, iterable

    :returns: actual frequency of (arg1 AND NOT arg2 ... AND NOT argn)
        or 0 if args are empty
        
    #TODO:
    """
    if not args:
        return 0
    if hasattr(args, 'next'):
        arg1 = args.next()
    elif hasattr(args, 'pop'):
        arg1 = args.pop()
    else:
        arg1 = args[0]
        args = args[1:]
        if not args:
            return 0
    ew = df.T.apply(lambda x: arg1 > 0 and not any([x[k] > 0 for k in args]))
    return ew.mean()

def freq_of_only(df, args):
    """
    
    
    :param df: DataFrame to query
    :type df: bool DataFrame
    :param args: attribute[s] to count for
    :type args: list, iterable

    :returns: actual frequency of (arg1 AND NOT ALLarg2 ... NOT argn)
    
    #TODO:
    """
    if not args:
        return 0
    if hasattr(args, 'next'):
        arg1 = args.next()
    elif hasattr(args, 'pop'):
        arg1 = args.pop()
    else:
        arg1 = args[0]
        args = args[1:]
        if not len(args):
            return 0
    ew = df.T.apply(lambda x: arg1 > 0 and not all((x[k] for k in args)))
    return ew.mean()            

class TestThis(unittest.TestCase):
    def test_iters(self):
        l = ['x ','y ','z ','t ','sx','sy','sz']
        l = ['X','Y','Z','T','A','B']
        l = ['X','Y','Z','T']
        l = ['1','0']
        #l = ['the','cat','walked']
        maxn = len(l) #min((len(l), 5))

        for m in matrixiter5(l, maxn):
            print m

    def test_to_dataframe(self):
        ds=EASYPEASY
        
        axes=ds['axes']
        df_sol, df_notsol = two_dataframes(ds)
        solaxes = ('s',)
        
        
        print "solution"
        print df_sol
        
        print "not solution"
        print df_notsol
        
        
        print df_sol['s'].mean()
        ds['axes']

        
     
        funcs = {
            #'freq:AND': freq_of,
            'freq: AND NOT ANY(%s)': freq_of_not,
            'freq: AND NOT ALL(%s)': freq_of_only,
        }        

        
        allsols = defaultdict(lambda: defaultdict(list))
        

        for (i,v) in axisiter2([a for a in axes if a not in solaxes], len(axes)):
            solfreq = freq_of(df_sol, v)
            notsolfreq = freq_of(df_notsol, v)
            allsols[v]['freq:AND'] = (solfreq-notsolfreq, i, solfreq, notsolfreq)            
            
            #if len(v) >= 2:
            #    for k, func in funcs.iteritems():
            #        solfreq = func(df_sol, v)
            #        notsolfreq = func(df_notsol, v)
            #        sol = (solfreq-notsolfreq, i, solfreq, notsolfreq)
            #        allsols[(v[0],)][k % ', '.join(v[1:])] = sol
                    

            

        for k in sorted(allsols.iterkeys()):
            v = allsols[k]
            
            illogical = sum(v_[0] for v_ in allsols[k].itervalues()) / float(len(allsols[k]))
            allsols[k]['illogical'] = illogical

            print '\n', k
            for k_ in sorted(v.iterkeys()):
                v_ = v[k_]
                print '%-32s %r' % (k_, v_)



        

        #for (i, ((yn,(y)), (xn,(x)))) in matrixiter4(axes, len(axes)):
        #    print i, yn, xn, x, ':', y, '::', ', '.join(str(df_notsol[k].mean()) for k in x), ':', ', '.join(str(df_sol[k].mean()) for k in y)

        print df_sol
        print df_notsol
        

if __name__=="__main__":
    main()
