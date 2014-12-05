range_num       = 1001
sum_vals        = 1
new_val         = sum_vals
skip_val        = 0
for i in xrange(1,range_num,2):
        for j in xrange(1,5):
                new_val         = new_val + i + 1
                sum_vals        += new_val

print sum_vals
