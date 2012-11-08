#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'mwtable-mwclient.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
#!/usr/bin/env python
import mwclient
site = mwclient.site('en.wikipedia.org')
site = mwclient.Site('en.wikipedia.org')
guitpage=site.Pages['Guitar']
guitpage
#[Out]# <Page object 'Guitar' for <Site object 'en.wikipedia.org/w/'>>
guitpage.revision
#[Out]# 446762545
guitpage.images 
#[Out]# <bound method Page.images of <Page object 'Guitar' for <Site object 'en.wikipedia.org/w/'>>>
guitpage.categories 
#[Out]# <bound method Page.categories of <Page object 'Guitar' for <Site object 'en.wikipedia.org/w/'>>>
guitpage.categories()
#[Out]# <List object 'categories' for <Site object 'en.wikipedia.org/w/'>>
[c for c in guitpage.categories()]
#[Out]# [<Category object 'Category:Wikipedia indefinitely semi-protected pages' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:All articles with specifically marked weasel-worded phrases' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Spanish musical instruments' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Articles containing Ancient Greek language text' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Articles with unsourced statements from December 2007' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Articles with specifically marked weasel-worded phrases from April 2011' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Wikipedia indefinitely move-protected pages' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Articles with unsourced statements from April 2011' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Articles containing French language text' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Arabic words and phrases' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Articles containing non-English language text' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Articles containing German language text' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:All articles with unsourced statements' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Celtic musical instruments' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Guitars' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Articles with unsourced statements from August 2007' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Articles containing Latin language text' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Articles containing Spanish language text' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Irish musical instruments' for <Site object 'en.wikipedia.org/w/'>>, <Category object 'Category:Articles with unsourced statements from January 2009' for <Site object 'en.wikipedia.org/w/'>>]
chr(43)
#[Out]# '+'
chr(68)
#[Out]# 'D'
chr(69)
#[Out]# 'E'
chr(36)
#[Out]# '$'
s='''https://encrypted.google.com/search?hl=en&sa=X&ei=v_3tTaPHGsX10gG2_aWZCA&ved=0CBoQvwUoAQ&q=%22graphs+such+as+call+graphs%22&spell=1&biw=1283&bih=684'''
sa
s
#[Out]# 'https://encrypted.google.com/search?hl=en&sa=X&ei=v_3tTaPHGsX10gG2_aWZCA&ved=0CBoQvwUoAQ&q=%22graphs+such+as+call+graphs%22&spell=1&biw=1283&bih=684'
import urlparse
urlparse(s)
urlparse.urlparse(s)
#[Out]# ParseResult(scheme='https', netloc='encrypted.google.com', path='/search', params='', query='hl=en&sa=X&ei=v_3tTaPHGsX10gG2_aWZCA&ved=0CBoQvwUoAQ&q=%22graphs+such+as+call+graphs%22&spell=1&biw=1283&bih=684', fragment='')
url=urlparse.urlparse(s)
url.netloc
#[Out]# 'encrypted.google.com'
url.path
#[Out]# '/search'
url.query
#[Out]# 'hl=en&sa=X&ei=v_3tTaPHGsX10gG2_aWZCA&ved=0CBoQvwUoAQ&q=%22graphs+such+as+call+graphs%22&spell=1&biw=1283&bih=684'
urlparse.urlparse(url.query)
#[Out]# ParseResult(scheme='', netloc='', path='hl=en&sa=X&ei=v_3tTaPHGsX10gG2_aWZCA&ved=0CBoQvwUoAQ&q=%22graphs+such+as+call+graphs%22&spell=1&biw=1283&bih=684', params='', query='', fragment='')
import urllib
urllib.unquote(s)
#[Out]# 'https://encrypted.google.com/search?hl=en&sa=X&ei=v_3tTaPHGsX10gG2_aWZCA&ved=0CBoQvwUoAQ&q="graphs+such+as+call+graphs"&spell=1&biw=1283&bih=684'
urllib.urlparse(urllib.unquote(s))
urlparse.urlparse(urllib.unquote(s))
#[Out]# ParseResult(scheme='https', netloc='encrypted.google.com', path='/search', params='', query='hl=en&sa=X&ei=v_3tTaPHGsX10gG2_aWZCA&ved=0CBoQvwUoAQ&q="graphs+such+as+call+graphs"&spell=1&biw=1283&bih=684', fragment='')
urllib.urlparse(urllib.unquote(s))
urlparse.urlparse(urllib.unquote(s))
#[Out]# ParseResult(scheme='https', netloc='encrypted.google.com', path='/search', params='', query='hl=en&sa=X&ei=v_3tTaPHGsX10gG2_aWZCA&ved=0CBoQvwUoAQ&q="graphs+such+as+call+graphs"&spell=1&biw=1283&bih=684', fragment='')
urlparse.urlparse(urllib.unquote(s)).query
#[Out]# 'hl=en&sa=X&ei=v_3tTaPHGsX10gG2_aWZCA&ved=0CBoQvwUoAQ&q="graphs+such+as+call+graphs"&spell=1&biw=1283&bih=684'
urlparse.urlparse(urlparse.urlparse(urllib.unquote(s)).query)
#[Out]# ParseResult(scheme='', netloc='', path='hl=en&sa=X&ei=v_3tTaPHGsX10gG2_aWZCA&ved=0CBoQvwUoAQ&q="graphs+such+as+call+graphs"&spell=1&biw=1283&bih=684', params='', query='', fragment='')
#?urllib.urlcleanup
urllib.urlcleanup(s)
#?urllib.splitquery
urllib.splitquery(s)
#[Out]# ('https://encrypted.google.com/search', 'hl=en&sa=X&ei=v_3tTaPHGsX10gG2_aWZCA&ved=0CBoQvwUoAQ&q=%22graphs+such+as+call+graphs%22&spell=1&biw=1283&bih=684')
url.query
#[Out]# 'hl=en&sa=X&ei=v_3tTaPHGsX10gG2_aWZCA&ved=0CBoQvwUoAQ&q=%22graphs+such+as+call+graphs%22&spell=1&biw=1283&bih=684'
url.query.split('&')
#[Out]# ['hl=en', 'sa=X', 'ei=v_3tTaPHGsX10gG2_aWZCA', 'ved=0CBoQvwUoAQ', 'q=%22graphs+such+as+call+graphs%22', 'spell=1', 'biw=1283', 'bih=684']
url.query.split('&q=')
#[Out]# ['hl=en&sa=X&ei=v_3tTaPHGsX10gG2_aWZCA&ved=0CBoQvwUoAQ', '%22graphs+such+as+call+graphs%22&spell=1&biw=1283&bih=684']
url.query.split('&q=')[1]
#[Out]# '%22graphs+such+as+call+graphs%22&spell=1&biw=1283&bih=684'
urlparse.parse_qs(url.query)
#[Out]# {'ei': ['v_3tTaPHGsX10gG2_aWZCA'], 'bih': ['684'], 'spell': ['1'], 'q': ['"graphs such as call graphs"'], 'ved': ['0CBoQvwUoAQ'], 'hl': ['en'], 'biw': ['1283'], 'sa': ['X']}
urlparse.parse_qs(url.query)['q']
#[Out]# ['"graphs such as call graphs"']
urlparse.parse_qs(url.query)['hl']
#[Out]# ['en']
_ip.magic("hist -n 48")
url.path
#[Out]# '/search'
if url.netloc in {'www.google.com':None,'google.com':None,'encrypted.google.com':None} and url.path == '/search'
import ConfigParse
import configparse
import ConfigParser
#?ConfigParser
#?ConfigParser
#?ConfigParser.ConfigParser.items
#?ConfigParser
#?ConfigParser
#?dict.update
#?UnicodeDecodeError?
#?UnicodeDecodeError.object
#?UnicodeDecodeError?
#?UnicodeEncodeError
NotImplementedError.reaso
#?UnicodeDecodeError.reason
import os
#?os.tmpfile
#?os.tmpnam
import tempfile
#?tempfile.mkdtemp
#?tempfile.mkstemp
import dirs
dir 
#[Out]# <built-in function dir>
#?dir
import shutil
#?shutil.copyfile
_ip.system("/bin/ls --color=auto ")
shutil.copyfile('opes.py','./mdp')
#?tempfile.gettempdir
#?tempfile.tempdir
tempfile.tempdir
#?tempfile.mkstemp
#?shutil.copy2
#?shutil.copy
#?shutil.copyfile
#?shutil.rmtree
import os
#?os.mkdir
from sqlalchemy.orm import 
import sqlalchemy.orm
l=[1,2,3]
l.index(2)
#[Out]# 1
l.index(3)
#[Out]# 2
l.index(0)
l.index(1)
#[Out]# 0
#?l.index
