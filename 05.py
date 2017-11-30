def primes_sieve(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
           ps.append(p)
           for i in range(p * p, n + 1, p):
               sieve[i] = False
    return ps

def smallest_number_divisible_by_or_under(n):
	arr = primes_sieve(n)
	print arr
	for i,x in enumerate(arr):
		power = 1
		base = x
		while arr[i] < n:
			arr[i] = base ** power
			power += 1
		arr[i] = base ** (power - 2)
	return arr

def mult(x,y): return x * y

print reduce (mult, smallest_number_divisible_by_or_under(20))