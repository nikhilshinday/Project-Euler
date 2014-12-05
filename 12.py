import math
import collections
# choose(n+1,2) for the nth triangle number is the triangle number itself.
# then, the range of numbers that can be included in the factors are up
# to the previous choices up to two for all levels. 

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

def format_prime(l):
	return collections.Counter(l)

def num_factors(c):
	return reduce(lambda x,y: (y + 1) * x, c.values(), 1)



triangle_num = 1
triangle_sum = 1
while num_factors(format_prime(prime_factors(triangle_sum))) < 500:
	triangle_num += 1
	triangle_sum += triangle_num
print triangle_sum