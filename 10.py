max = 2000000

def primes_sieve(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
           ps.append(p)
           for i in range(p * p, n + 1, p):
               sieve[i] = False
    return ps

def add(x,y): return x + y

print reduce(add,primes_sieve(max))