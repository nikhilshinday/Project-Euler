def enumerate_fib(n):
	a,b = 1,2
	arr = [a,b]
	while (b < n):
		a,b = b, a + b
		if b < n:
			arr.append(b)
	return arr

print(reduce(lambda x,y: x+y,filter(lambda x: x%2, enumerate_fib(4000000))))

