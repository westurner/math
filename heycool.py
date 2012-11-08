#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'heycool.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
import operator
import sympy
from sympy import *
from sympy.plotting import Plot

def oavg(seq):
    """ regular average of seq """
    d=reduce(operator.add, seq);
    return float(d)/len(l)

def coolavg():
    """ """

    #[Out]# avg + val/(1 + i) - avg/(1 + i)
    #return newavg
    pass

#newavg.integrate()
#[Out]# avg**2*(i*val/2 - val*log(1 + i)/2) + avg*val**2*log(1 + i)/2

def other():
    from itertools import product
    l=['1','-1','0']
    matrix_iter=product(l,l)
    [x for x in matrix_iter]
    #[Out]# [('1', '1'), ('1', '-1'), ('1', '0'), ('-1', '1'), ('-1', '-1'), ('-1', '0'), ('0', '1'), ('0', '-1'), ('0', '0')]
    x
    #[Out]# ('0', '0')
    
    l=[0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,200]

    oavg(l)
    #[Out]# 9.6190476190476186
    # newavg.subs({avg: , val: , i}) for (i_, val) in enumerate(l))

    for i2, term in enumerate(newavg.subs({avg:0 , val:v , i:i_}) for (i_, v) in enumerate([1]*20)):
        print '%i\t%f\t\t %s' % (i2, term,term)
    for i2, term in enumerate(newavg.subs({avg:0 , val:v , i:i_}) for (i_, v) in enumerate([2]*20)):
        print '%i\t%f\t\t %s' % (i2, term,term)
    for i2, term in enumerate(newavg.subs({avg:0 , val:v , i:i_}) for (i_, v) in enumerate([2]*20)):
        print '%i\t%f\t\t %s' % (i2+1, term,term)


def main(ipshell=None):

    avg,i,weight,val=symbols(('avg','i','weight','val'))
    weight=(1.0 / (i+1))
    newavg =avg-(avg*weight)+(weight*val)
    print newavg
    #[Out]# avg + val/(1 + i) - avg/(1 + i)
    # ...simplify() = (avg*i + val)/(i + 1)

    newavgf = newavg.factor()
    print newavgf
    #(1.0*avg*i + 1.0*val)/(i + 1)

    print 'one', newavg.count_ops(visual=True)
    print 'two', newavgf.count_ops(visual=True)

    import sys
    if '-p' in sys.argv:
        p=Plot(width=1280,height=1024,bgcolor=(0.05,0.05,0.05,0.0), axes='label_axes=true; label_ticks=false; overlay=true; ')
        p.axes.toggle_colors()
        #for (z,n) in enumerate([0]): #range(0,1000,100)):
        #    print z, n

        p.append(newavgf.subs({avg:10}), [0,100],[0,100]) #,'style=wireframe;')
        #p.append(newavgf.subs({avg:100}), [0,100]) #,'style=wireframe;')

    if '-i' in sys.argv:
        import IPython
        IPython.Shell.IPShellEmbed(argv=sys.argv[0:0])(local_ns=locals(),global_ns=globals())

if __name__=="__main__":
    main()
