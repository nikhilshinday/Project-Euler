prime_enum = 10001
guess = 10000000

def primes_sieve(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
           ps.append(p)
           for i in range(p * p, n + 1, p):
               sieve[i] = False
    return ps

arr = primes_sieve(guess)

while len(arr) < prime_enum:
	guess *= 2
	arr = primes_sieve(guess)

print arr[prime_enum - 1]