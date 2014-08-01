def enumerate_fib(n):
	a,b = 1,2
	arr = [a,b]
	while (b < n):
		a,b = b, a + b
		if b < n:
			arr.append(b)
	return arr

def is_even(x):
		return x % 2 == 0

def add(x,y): return x+y

print(reduce(add,filter(is_even, enumerate_fib(4000000))))

