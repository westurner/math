#/usr/bin/python
def sum_seq(s,e,r):
	total = 0
	for x in range(s,e+1):
		v = pow(r,x)
		total += v
		print "%10s | %s ^ %s = %s" % (total, r,x,v)
	return total

def dbl_sum(s,e,v1,v2,op=1):
	""" sigma(start,end) [ v1^j + op(v2^j)] """
	return ((pow(v1,e+1)-1)/(v1-1)) + (op*(pow(v2,e+1)-1/(v2-1)))


t1 = sum_seq(0,8,3)
t2 = sum_seq(0,8,2)

total = t1 -t2

print "%s - %s = %s" % (t1, t2, total)

print "dblsum: %s" % dbl_sum(0,8,3,2,-1)
