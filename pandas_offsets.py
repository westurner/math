"""

Pandas Date Offset Reference

"Python for Data Analysis: Agile Tools for Real World Data"
by Wes McKinney

http://shop.oreilly.com/product/0636920023784.do

http://pandas.pydata.org/pandas-docs/stable/timeseries.html#dateoffset-objects
http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases

"""

import inspect
import pandas.tseries.offsets as off

def local_reference():
    """alphabetical list of date offset codes"""
    def iter_frequency_rules():
        for thingname in dir(off):
            thing = getattr(off, thingname)
            if (
                inspect.isclass(thing) and
                off.DateOffset in inspect.getmro(thing) and
                thing not in (
                    off.DateOffset,
                    off.CacheableOffset,
                    off.WeekOfMonth,
                    off.Tick)):
                _thing = thing()
                yield ('%-10s%-20s' % (
                    _thing.rule_code,
                    thing.__name__,))
                    #str(thing.__doc__).strip().split('\n')[0].strip()[:52]))
    print(
        str.join('\n',
            (str(s) for s in sorted(set(iter_frequency_rules()) ))))
    print('W-DAY     Week [SUN, MON, TUE, WED, THU, FRI, SAT]')

if __name__=="__main__":
    local_reference()
