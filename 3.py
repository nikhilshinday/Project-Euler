import math

num = 600851475143

def primes_sieve(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
           ps.append(p)
           for i in range(p * p, n + 1, p):
               sieve[i] = False
    return ps

arr = primes_sieve(int(math.sqrt(num)))
max_prime = 0
for i in arr:
	if num % i == 0: max_prime = i

print max_prime



