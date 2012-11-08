#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'hrm.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
axisiter = lambda l,maxn: enumerate(chain(*(imap(str.join, prd(*((l,)*n))) for n in range(maxn+1))))
matrixiter = lambda l,maxn: enumerate(prd(axisiter(l,maxn), axisiter(l,maxn)))
for x in matrixiter(['X','Y'],2): print x
from itertools import product as prd
for x in matrixiter(['X','Y'],2): print x
from itertools import product as prd, chain
for x in matrixiter(['X','Y'],2): print x
from itertools import product as prd, chain, imap
for x in matrixiter(['X','Y'],2): print x
axisiter = lambda l,maxn: enumerate(chain(*(imap(lambda x: str.join((*x,)), prd(*((l,)*n))) for n in range(maxn+1))))
axisiter = lambda l,maxn: enumerate(chain(*(imap(lambda x: str.join(*x,), prd(*((l,)*n))) for n in range(maxn+1))))
axisiter = lambda l,maxn: enumerate(chain(*(imap(lambda x: str.join(*x), prd(*((l,)*n))) for n in range(maxn+1))))
for x in matrixiter(['X','Y'],2): print x
axisiter = lambda l,maxn: enumerate(chain(*(imap(lambda x: str.join(str(s) for s in x), prd(*((l,)*n))) for n in range(maxn+1))))
for x in matrixiter(['X','Y'],2): print x
axisiter = lambda l,maxn: enumerate(chain(*(imap(lambda x: str.join(*(str(s) for s in x)), prd(*((l,)*n))) for n in range(maxn+1))))
for x in matrixiter(['X','Y'],2): print x
axisiter = lambda l,maxn: enumerate(chain(*(prd(*((l,)*n))) for n in range(maxn+1)))
axisiter = lambda l,maxn: enumerate(chain(*(prd(*((l,)*n))) for n in range(maxn+1))))
axisiter = lambda l,maxn: enumerate(chain(*(prd(*((l,)*n))) for n in range(maxn+1)))))
axisiter = lambda l,maxn: enumerate(chain(*(prd(*((l,)*n))) for n in range(maxn+1)
axisiter = lambda l,maxn: enumerate(chain(*(prd(*((l,)*n))) for n in range(maxn+1)))
axisiter = lambda l,maxn: izip(count(), chain(*(prd(*((l,)*n))) for n in range(maxn+1))))
axisiter = lambda l,maxn: izip(count(), chain(*(prd(*((l,)*n)) for n in range(maxn+1))))
for x in matrixiter(['X','Y'],2): print x
from itertools import izip, count
for x in matrixiter(['X','Y'],2): print x
for x in matrixiter(['X','Y'],4): print x
for x in matrixiter(['1','0'],4): print x
for x in matrixiter(['1','0'],1): print x
for x in matrixiter(['1','0'],2): print x
for x in matrixiter(['1','0'],3): print x
for x in matrixiter(['1','0'],4): print x
for x in matrixiter(['1','0'],5): print x
for x in matrixiter(['1','0'],6): print x
for x in matrixiter(['a','b','c'],2): print x
for x in matrixiter(['a','b'],2): print x
for x in matrixiter(['a','b','c'],4): print x
import pandas
