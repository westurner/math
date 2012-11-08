# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 20:03:04 2011

@author: wturner
"""
from collections import defaultdict
import pprint
import os
import sys
import datetime
import decimal
import numpy as np


RESERVED = dict((k,None) for k in dict.__dict__)
[RESERVED.__setitem__(k, None) for k in (
    'uri',
    'label',
    'meta',
    'pprint',
    'pr',
    'put',
    'keyo',
    'keyo_ins',
    'created')]
#print '\n'.join(str(s) for s in sorted(RESERVED.iteritems()))

STRIP=dict((k,None) for k in ['label','uri'])

def keyj(*args):
    return os.path.join(*(str(s) for s in args))

SEPLEN=40
def prettyundr(text, char, length=None, maxlen=SEPLEN):
    return (length or max((len(text),maxlen)))*char

def indentline(l,depth=0):
    fmt = '%s%s' % (depth*'    ', '%s')
    return fmt % l

def indentlines(lines, depth=0):
    for l in lines:
        yield indentline(l,depth)

try:
    import simplejson as json
except ImportError:
    import json

class CoolJSONEncoder(json.JSONEncoder):
    """
    JSONEncoder subclass that knows how to encode date/time with microseconds.
    and np.ndarrays as lists
    
    Respect to Django
    """

    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"

    def default(self, o):
        if isinstance(o, datetime.datetime):
            #d = datetime_safe.new_datetime(o)
            output = o.strftime("%s %s" % (self.DATE_FORMAT, self.TIME_FORMAT))
            return "%s.%s" % (output, o.microsecond)
        elif isinstance(o, datetime.date):
            #d = datetime_safe.new_date(o)
            return o.strftime(self.DATE_FORMAT)
        elif isinstance(o, datetime.time):
            output = o.strftime(self.TIME_FORMAT)
            return "%s.%s" % (output, o.microsecond)
        elif isinstance(o, decimal.Decimal):
            return str(o)
        elif isinstance(o, np.ndarray):
            return o.tolist()
        else:
            return super(CoolJSONEncoder, self).default(o)

class DataSet(defaultdict, object):
    """
    DataSet form

    Stores key ins order (``.keyo_ins``) ( OrderedDict > 2.7 )
    
    :param uri: DataSet URI base
    :type uri: URI str
    :param label: DataSet Label (rdfs:label) [optional]
    :type label: str
    :param keyo: whitelisted attr display list [optional]
    :type keyo: list
    
    >>> ds = DataSet('http://ns.domain/NS/12345')
    >>> dsa = ds.a
    >>> ds.pprint()
    >>> dsa['varname'] = np.array([1,1,0])
    >>> assert dsa['varname'] == ds.a.varname
    >>> dsa.put('varname2', [0,0,0,1], label="A varname22 variable")
    >>> assert ds.a.varname2.label == dsa.varname2.label
    >>> ds.pprint()
    >>> ds.label = "Test Dataset 12345"
    >>> ds.pprint()
    >>> print ds.created
    
    Note::
        * cyclic graphs are not prevented
        * recursion will recurse until system max recursion depth
        * nested DataSet URIs are calculated automatically only at instantiation
        
        >>> ds = DataSet('<urn:here>')
        >>> print ds.uri
        >>> ds.newds('x')
        >>> ds.x.xylophone = 'CHIRP'
        >>> ds.newds('y')
        >>> ds.y['yang'] = ds.x
        >>> print ds.y.yang.uri


    """
    def __init__(self, uri=None, label=None, keyo=None):
        self.uri = uri
        self.label = label
        self.keyo = keyo or []
        self.keyo_ins = []
        self.meta = defaultdict(dict) #DataSet()
        self.created = datetime.datetime.now()

    @property
    def uri(self):
        return self['uri']
        
    @uri.setter
    def set_uri(self, uri):
        self['uri'] = uri

    @property
    def label(self):
        return self['label']
        
    @label.setter
    def set_label(self, label):
        self['label'] = label

    @property
    def meta(self):
        return self['meta']

    @meta.setter
    def set_meta(self, val):
        self['meta'] = val
 
    @property
    def keyo(self):
        return self['keyo']
        
    @keyo.setter
    def set_keyo(self, keyo):
        self['keyo'] = keyo
    
    @property
    def keyo_ins(self):
        return self['keyo_ins']

    @keyo_ins.setter
    def set_keyo_ins(self, keyo_ins):
        self['keyo_ins'] = keyo_ins

    @property
    def created(self):
        return self['created']
        
    @created.setter
    def set_created(self, created):
        self['created'] = created

    def put(self, k, v, **kwargs):
        print "%s <= %s\n%s" % (self.uri, k,v)

        if k not in self:
            self.keyo_ins.append(k)
            self.meta[k].update(kwargs) # !
            return self.__setitem__(k,v)
        else:
            raise Exception('dissonance: %r = %r ( <= %r ?)' % (self[k],k,v))

    def newds(self,key, label=None):
        print "New Dataset: %s" % k
        self.keyo_ins.append(key)
        newuri = keyj(self.uri, '#', key)
        self[key] = DataSet(uri=newuri, label=label)
        return self[key]

    def __getitem__(self, key):
        if key in self:
            return self.get(key)
        #return self.setdefault(key, copy.deepcopy(self.default))
        
        return self.setdefault(key,self.newds(key))

    def __getattr__(self,attr):
        if attr in RESERVED:
            return super(defaultdict,self).__getattr__(self,attr)

        return self.__getitem__(attr)

    def __setattr__(self,attr,value):
        if attr in RESERVED:
            return super(DataSet, self).__setattr__(attr,value)
        return self.put(attr,value)

    def __setitem__(self, k, v):
        if k not in RESERVED and k in self:
            raise Exception("Dissonance: %r ,, %r [ %r ]" % (k,v, self[k]))
        return super(DataSet, self).__setitem__(k, v)
        if k in RESERVED:
            return super(DataSet, self).__setitem__(k, v)
        return self.put(k, v) #self.__setattr__(k,v)

    def pprint(self, keyo=None, header=None, depth=0, output=sys.stdout):
        if not header:
            header = ' :: '.join(str(s) for s in  (self.uri, self.label or '',) )
        if header:
            header = header
            output.write('\n')
            output.write(indentline(header,depth))
            output.write('\n')
            output.write(indentline(prettyundr(header, '='), depth))
            output.write('\n')
        keyo = keyo or self.keyo_ins or self.keys()
        output.write(indentline("# keyo: %s" % keyo, depth))
        output.write('\n')
        for k in keyo:
            v = self.get(k)
            if hasattr(v,'uri'):
                #print "recursing : %s" % v.uri
                v.pprint(header=v.uri,depth=depth+1,output=output)
            elif k not in STRIP:
                self.pr(k, v, meta=self.meta.get(k), depth=depth+1, output=output)
            else:
                pass
                #raise Exception(k, v)
        if header:
            output.write(indentline(prettyundr(''*len(header),'='), depth))
            output.write('\n')
    
    def pr(self, k, content=None, meta=None, depth=0, output=sys.stdout):
        keyp = keyj(self.uri,'#',k)
        meta = meta or self['meta'][k]
        label = meta.get('label')
        header = ''
        if meta:
            header = ' :: '.join((keyp, label or ''))
        else:
            header = keyp
        output.write('\n')
        output.write(indentline(keyp, depth))
        output.write('\n')
        output.write(indentline(prettyundr(keyp, '~'), depth))
        output.write('\n')

        if meta is not None:
            for k in sorted(meta.keys()):
                output.write(indentline('.%s\t\t= %r' % (k, meta[k]), depth))
                output.write('\n')

        if content is not None:
            #if isinstance(content, defaultdict):
            #    content = dict(content)
            for l in indentlines( pprint.pformat(content).split('\n') , depth ):
                output.write(l)
                output.write('\n')
        output.write('\n')

    def to_json(self, **kwargs):
        return json.dumps(dict(self), cls=CoolJSONEncoder, **kwargs)
        
    def to_triples(self):
        # TODO: check uris ...
        yield (self.uri, 'a', 'DataSet')
        yield (self.uri, 'a', 'void:Dataset')

        if self.created:
            yield (self.uri, 'dcterms:created', str(self.created)) # TODO: datefmt

        keyo = self.keyo or self.keyo_ins
        yield (self.uri, 'keyo', str(keyo)) # ! orderigs

        for k in keyo:
            v = self.get(k)
            
            if isinstance(v, DataSet): #'id' in v:
                yield (self.uri, 'hasDataSet', v.uri)
                if v.label:
                    yield (k, 'rdfs:label', v.label) # TODO: VOID ...
                if v.created:
                    yield (k, 'dcterms:created', str(v.created)) # TODO: datefmt
                for t in v.to_triples():
                    yield t
            elif isinstance(v, dict):     
                key = keyj(self.uri, '#', k)
                yield (key, 'a', 'dict')
                
                for k_, v_ in v.iteritems():
                    key_ = keyj(key, k_)
                    yield (key, 'hasKey', key_)
                    yield (key_, 'hasValue', v_)
            else:
                key = keyj(self.uri, '#', k)
                yield (self.uri, 'hasItem', key)
                yield (key, 'a', type(v).__name__) # ! *
                
                if isinstance(v, (int, str, float, long, bool)):
                    value = v
                elif isinstance(v, (datetime.datetime, datetime.time)):
                    value = str(v) # TODO: datefmt
                elif isinstance(v, (np.ndarray)):
                    value = str(v.tolist()) # !
                    #yield (key, 'hasHash', hashfunc(value))
                else:
                    raise Exception('incomplete types ... %r : %s' % 
                                        (type(v), pprint.pformat(v)))
                yield (key, 'hasValue', value)
                
            meta = self.meta.get(k)
            if meta:
                for k_, v_ in meta.iteritems():
                    if k_ not in {'hasItem':None, 'hasValue':None }:
                        yield (key, k_, v_) # goosy
                    else:
                        raise Exception()
            
        
        def from_triples(self):
            raise NotImplementedError()
        
import unittest
class TestDataSet(unittest.TestCase):
    def test_pbj(self):
        import numpy as np
        def pbj(x):
            return np.tril(
                (x + (
                    np.tri(*x.shape, k=-1, dtype=bool)
                    .transpose()
                    * x
                    )
                    .transpose()
                )
            )

        x=np.array([
            [1,9,2],
            [0,1,1],
            [4,1,0],
        ])
        
        # print x
        
        x.diagonal()
        
        ds_uri="http://path_to/root"
        ds = DataSet(ds_uri)
        
        ds.x = x
        # self.assertEqual(ds.x, ds['x']) # array compare
        
        ds.pprint()
       
        v=pbj(ds.x)

        k='x_fold'
        ds[k]=v
        ds.meta[k]['label'] = 'X PBJ Folded'
        ds.meta[k]['addl'] = 'WHOA'
        
        ds.y=np.array([
            [1,0,1],
            [0,2,0],
            [0,0,3],
        ])
        
        ds.y_fold = pbj(ds.y)
        ds.pprint()
        
        for t in ds.to_triples():
            print t
        
    def test_dataset(self):
        ds_uri='http://test_data/root'
        ds = DataSet(ds_uri, label="DS Dataset")
        self.assertEqual(ds.uri, ds_uri)

        ds1 = ds.newds('ds1', label="DS1 Dataset")
        ds1.var1 = {'var_xyz':'This is a dict value'}
        self.assertEqual(ds1.var1, ds['ds1']['var1'])
        
        ds1_2 = ds1.newds('ds1_2')
        ds1_2.var1_2 = True
        self.assertEqual(ds1_2['var1_2' ], ds['ds1']['ds1_2'].var1_2)        
        
        ds2 = ds['whoa']
        ds2.variablename = True
        #ds2.pprint()

        ds.pprint(header='ds')
        ds3 = ds2['deep']
        
        # ds3.cool = ds2 # !! .. __set(item|attr) overhead
        
        # !*
        ds3.cool = ds.y
        
        import StringIO
        ob1 = StringIO.StringIO()
        op1=ds.pprint(header='op1', output=ob1)
        print 'op1', '\n'.join(ob1.readlines())

        ob2 = StringIO.StringIO()
        op2=ds.pprint(header='op2', output=ob2)
        print 'op2', '\n'.join(ob2.readlines())
        self.assertEqual(ob1, ob2)
        self.assertEqual(op1, op2)
        
        # All adults here ?
        notatree = ds['notatree']
        notatree = ds1_2 # ..breaks uris
        notatree.uri
        notatree = ds2 # ... breaks uris
        notatree.uri
        notatree.pprint(header='notatree')
        
        # failUnlessRaises
        #ds['notatree'] = None
        #ds.notatree = None
        
        import pickle
        pickled =  pickle.dumps(ds)
        unpickled = pickle.loads(pickled)
        
        #self.assertEqual(ds, unpickled) # array compare
        
        ob1_unpickled = StringIO.StringIO()
        op1_unpickled = unpickled.pprint(output=ob1_unpickled)
        
        self.assertEqual(ob1, ob1_unpickled)  
        self.assertEqual(op1, op1_unpickled)
        
        print "unpickled: ", unpickled.uri
        print pprint.pformat(dict(unpickled))
        print "ds: "
        print pprint.pformat(dict(ds))
        self.assertEqual(unpickled.uri, ds.uri)
        
        import numpy as np
        ds.put('123123123',
            np.array(
                [
                [1,0,1],
                [0,1,0],
                [1,0,1],
                ]),
            label='Labelzz',
            addl_prop='coolz')
        ds.pprint(header='ds')
        
        uhm = ds.to_json(indent=4)
        print uhm
        print '---'
        
        for t in ds.to_triples():
            print t


        
if __name__=="__main__":
    unittest.main()
