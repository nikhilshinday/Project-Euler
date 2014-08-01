from sets import Set

def calculate_nth_triangle_num(n):
	sum = 0
	for i in range(1,n+1):
		sum += i
	return sum


guess = 1

factors = Set([])

while guess < 10:
	triangle_num = calculate_nth_triangle_num(guess)
	factors.add(triangle_num)
	factors.add(1)

	print "guess: ", guess, " triangle_num: ", triangle_num
	for i in range(1,triangle_num+1):
		if triangle_num % i == 0:
			factors.add(i)
	print factors
	print len(factors)
	if len(factors) > 500:
		break
	else: 
		guess += 1
		factors = Set([])