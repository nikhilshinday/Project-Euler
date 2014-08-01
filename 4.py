
max = 0

def is_palindrome(n):
	test_str = str(n)
	for i in range(len(test_str) / 2):
		if test_str[i] != test_str[-1 * i - 1]:
			return False
	return True

for i in range (100,1000):
	for j in range (100,1000):
		if is_palindrome(i*j) and max < i * j :
			max = i*j
print max