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
    return '%s%s' % (depth*'    ', l)
    return fmt % l

def indentlines(lines, depth=0):
    for l in lines:
        yield indentline(l,depth)

try:
    import simplejson as json
except:
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
    A serializable DataSet
    
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
        >>> print ds.y.yang.xylophone

    """
    def __init__(self, uri=None, label=None, keyo=None):
        """
        Initialize a new DataSet with URI, label, and optional key display order
        
        :param uri: DataSet URI base
        :type uri: URI str
        :param label: DataSet Label (rdfs:label) [optional]
        :type label: str
        :param keyo: whitelisted attr display list [optional]
        :type keyo: list
        """
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
    def uri(self, uri):
        self['uri'] = uri

    @property
    def label(self):
        return self['label']
        
    @label.setter
    def label(self, label):
        self['label'] = label

    @property
    def meta(self):
        return self['meta']

    @meta.setter
    def meta(self, val):
        self['meta'] = val
 
    @property
    def keyo(self):
        return self['keyo']
        
    @keyo.setter
    def keyo(self, keyo):
        self['keyo'] = keyo
    
    @property
    def keyo_ins(self):
        return self['keyo_ins']

    @keyo_ins.setter
    def keyo_ins(self, keyo_ins):
        self['keyo_ins'] = keyo_ins

    @property
    def created(self):
        return self['created']
        
    @created.setter
    def created(self, created):
        self['created'] = created

    def put(self, k, v, **kwargs):
        """
        Add a key and value to the dataset
        
        :param k: key
        :type k: hashable
        :param v: value
        :type v:
        :param kwargs: kwargs for meta[k]
        :type kwargs: dict
        
        :returns: self.__setitem__(k, v)
        """
        print "%s <= %s\n%s" % (self.uri, k,v)

        if k not in self:
            self.keyo_ins.append(k)
            self.meta[k].update(kwargs) # !
            return self.__setitem__(k,v)
        else:
            raise Exception('dissonance: %r = %r ( <= %r ?)' % (self[k],k,v))

    def newds(self, k, label=None, **kwargs):
        """
        Instantiate a nested DataSet at self[k]
        
        :param k: key
        :type k: hashable
        :param label: DataSet Label
        :type label: str
        :param kwargs: kwargs for DataSet(..., **kwargs)
        
        :returns: self[k] (new DataSet ds where ds.uri = (self.uri + "#" + k))
        """
        print "New Dataset: %s" % k
        self.keyo_ins.append(k)
        newuri = keyj(self.uri, '#', k)
        self[k] = DataSet(uri=newuri, label=label, **kwargs)
        return self[k]

    def __getitem__(self, k):
        """
        self[k]
        
        If k exists, return self[k]
        Else create a new dataset at k
        
        :param k: item key
        :type k: hashable
        """
        if k in self:
            return self.get(k)
        #return self.setdefault(k, copy.deepcopy(self.default))
        
        return self.setdefault(k,self.newds(k))

    def __getattr__(self,k):
        """
        var = self.attr
        
        proxy to self.__getitem__ for unreserved k
        
        :param k: attrname
        :type k: str
        """
        if k in RESERVED:
            return super(defaultdict,self).__getattr__(self,k)

        return self.__getitem__(k)

    def __setattr__(self,k,v):
        """
        selt.attr = var
        
        proxy to self.put for unreserved k
        
        :param k: attrname
        :type k: str
        :param v: attrval
        :type v: 
        
        """
        if k in RESERVED:
            return super(DataSet, self).__setattr__(k,v)
        return self.put(k,v)

    def __setitem__(self, k, v):
        """
        self['k12354'] = 1234.567
        
        :param k: key
        :type k: str
        :param v: value
        :type v:
        """
        if k not in RESERVED and k in self:
            raise Exception("Dissonance: %r ,, %r [ %r ]" % (k,v, self[k]))
        return super(DataSet, self).__setitem__(k, v)
        if k in RESERVED:
            return super(DataSet, self).__setitem__(k, v)
        return self.put(k, v) #self.__setattr__(k,v)

    def pprint(self, keyo=None, header=None, depth=0, output=sys.stdout):
        """
        Recursively print the DataSet to output
        Indents nested Datasets
        Adds headings and fetches metadata per variable
        
        :param keyo: List of keys to print [optional]
        :type keyo: list
        :param header: Text header [optional]
        :type header: str
        :param depth: Current Depth
        :type depth: int >= 0
        :param output: output stream [default: sys.stdout]
        :type output: requires <output>.write
        
        :returns: output stream [default:sys.stdout]
        """
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
            
        return output
    
    def pr(self, k, v=None, meta=None, depth=0, output=sys.stdout):
        """"
        Print a key k and value v with metadata meta at depth depth to
        output stream output
        
        :param k: key
        :type k: str
        :param v: value
        :type v:
        :param meta: metadata dict for k
        :type meta: dict
        :param depth: recursion depth (to determine indent level)
        :type depth: int
        :param output: output stream [default: sys.stdout]
        :type output: requires <output>.write
        
        :returns: output
        """
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
            for k_ in sorted(meta.keys()):
                output.write(indentline('.%s\t\t= %r' % (k_, meta[k_]), depth))
                output.write('\n')

        if v is not None:
            #if isinstance(v, defaultdict):
            #    content = dict(v)
            for l in indentlines( pprint.pformat(v).split('\n') , depth ):
                output.write(l)
                output.write('\n')
        output.write('\n')
        
        return output

    def to_json(self, **kwargs):
        """
        Recursively serialize dataset to JSON
        
        Handles python builtins, datetime types, and numpy.ndarray (.tolist())
        
        :param kwargs: kwargs for json.dumps
        :type kwargs: dict
        
        :returns: JSON string
        """
        return json.dumps(dict(self), cls=CoolJSONEncoder, **kwargs)
        
    def to_triples(self):
        """
        Recursively serialize dataset to triples
        
        :returns: triple-tuple generator
        
        """
        # TODO: check uris ...
        yield (self.uri, 'a', 'DataSet')
        #yield (self.uri, 'a', 'void:Dataset')

        if self.created:
            yield (self.uri, 'dcterms:created', str(self.created)) # TODO: datefmt

        keyo = self.keyo or self.keyo_ins
        yield (self.uri, 'keyo', str(keyo)) # ! orderigs

        for k in keyo:
            v = self.get(k)
            
            if isinstance(v, DataSet): #'id' in v:
                yield (self.uri, 'hasDataSet', v.uri)
                if v.label:
                    yield (self.uri, 'rdfs:label', v.label) # TODO: VOID ...
                if v.created:
                    yield (self.uri, 'dcterms:created', str(v.created)) # TODO: datefmt
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
        
        ds.x_fold=pbj(ds.x)
        ds['meta']['x_fold']['label'] = 'X PBJ Folded'
        ds['meta']['x_fold']['addl'] = 'WHOA'
        
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
        
        
        op1=ds.pprint(header='op1') # !*
        print 'op1', op1
        op1_=ds.pprint(header='op1_')
        print op1
        #self.assertEqual(op1, op1_) # None == None
        
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
              
        op2=unpickled.pprint()
        
        self.assertEqual(op1, op2)  
        
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