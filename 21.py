from sets import Set

# amicable numbers
UNDER = 10000
proper_divisors = {}

for num in xrange(1,UNDER+1):
        for divisor in xrange((num/2)+1,0,-1):
                if num % divisor == 0:
                        if num in proper_divisors:
                                factors_list = proper_divisors[num]
                                factors_list.append(divisor)
                        else:
                                proper_divisors[num] = [divisor]
for k,v in proper_divisors.iteritems():
        proper_divisors[k] = sum(v)
amicable_nums = Set()
for k,v in proper_divisors.iteritems():
        if k in proper_divisors and v in proper_divisors:
                if k == proper_divisors[v] and v == proper_divisors[k] and k != v:
                        amicable_nums.update([k])
                        amicable_nums.update([proper_divisors[v]])
print sum(list(amicable_nums))