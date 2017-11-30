import math

num = 100

def square(x): 	return x ** 2
def add(x,y): 	return x + y
def sum_of_squares(n): 	return reduce(add, map(square, range(1,n+1)))
def square_of_sum(n): 	return reduce(add, range(1,n+1)) ** 2

print abs(square_of_sum(num) - sum_of_squares(num))