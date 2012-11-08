from functools import wraps
import sys


import time
def timef(f):
    """ ... """
    @wraps(f)
    def fwrapper(*args,**kwargs):
        #print f, args, kwargs
        start = time.time()
        result = f(*args,**kwargs)
        stop = time.time()
        print '%f' % (stop-start)
        return result
    return fwrapper

@timef
def sleepsort(ds):
    import threading as t
    from Queue import Queue

    q = Queue()
    sds = []


    def append_to(q, val):
        print val
        q.put(val)

    def print_queue(q, sds):
        print q, sds
        try:
            n = q.get()
            sds.append(n)
        except Exception, e:
            print e

    for a in ds:
        t.Timer(int(a),append_to,(q,a)).start()

    mt = t.Timer(1,print_queue, (q,sds))
    mt.daemon = True
    mt.start()
    q.join()
    return sds

@timef
def sortedsort(ds):
    return sorted(ds)

@timef
def inplacesort(ds):
    ds.sort()
    return ds

def gettestdata():
    return range(0,100,10)

def main():

    print sys.argv

    tests = {
        'sleepsort': sleepsort,
        'sorted': sortedsort,
        'sort': inplacesort,
    }

    if '-t' in sys.argv:
        ds = gettestdata()
    else:
        ds = sys.argv[1:]

    print "DS.len: %d" % len(ds)

    for tk, func in tests.iteritems():
        print "Test: %s" % tk
        sortedds = func(ds)


if __name__=="__main__":
    main()
