sum_num = 0

range_num = 1000
for i in xrange(1,range_num+1):
        sum_num += i ** i

print str(sum_num)[-10:]
