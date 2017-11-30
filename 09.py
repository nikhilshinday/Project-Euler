sum = 1000
arr,triples = [],[]
def enumerate_factors(n):
	arr = []
	for i in range(1,n+1):
		if i > n / i:
			return arr
		if n % i == 0:
			arr.append([n/i, i])

def is_even(x): return x % 2 == 0

for i in filter(is_even,range(3,sum+1)):
	factors = enumerate_factors(i/2)
	for m,n in factors:
		a,b,c = m**2-n**2, 2*m*n, m**2+n**2
		if a**2+b**2 == c**2: 
			triples += [[a,b,c]] 

for a,b,c in triples:
	if a+b+c == 1000: 
		print a*b*c