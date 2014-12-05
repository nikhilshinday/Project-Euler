from sets import Set
import collections

def prime_factors(n):
        """Returns all the prime factors of a positive integer"""
        factors = []
        d = 2
        while n > 1:
                while n % d == 0:
                        factors.append(d)
                        n /= d
                d = d + 1
        return factors

def proper_divisors(n):
    divs = [1]
    for fact in prime_factors(n):
        temp = []
        for div in divs:
            if fact * div not in divs:
                temp.append(fact * div)
        divs = divs + temp
    return divs[:-1]

# abundant_sums = [proper_divisors(i) for i in range(1,28124)]
abundant_nums = []
for i in range(1,28124):
        p_divs = proper_divisors(i)
        sum_p_divs = sum(p_divs)
        if sum_p_divs > i:
                abundant_nums.append(i)

sum_two_abundant_nums = []
for i in abundant_nums:
        for j in abundant_nums:
                if i + j <= 28123:
                        sum_two_abundant_nums.append(i+j)

sum_two_abundant_nums = Set(sum_two_abundant_nums)
not_sum_two_abundant_nums = 0
for i in range(1,28124):
        if i not in sum_two_abundant_nums:
                not_sum_two_abundant_nums += i

print not_sum_two_abundant_nums







