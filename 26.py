def primes_sieve(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
           ps.append(p)
           for i in range(p * p, n + 1, p):
               sieve[i] = False
    return ps

reciprocal_nums = [(((10 ** (i-1)) - 1)/i,i) for i in primes_sieve(1000)]
print reciprocal_nums

max_len = 0
max_index = 0
for cyclic_num, num in reciprocal_nums:
        if max_len < len(str(cyclic_num)):
                max_len = len(str(cyclic_num))
                max_index = num

print max_index
