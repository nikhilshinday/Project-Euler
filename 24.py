import math

n = 1000000
numbers = list(map(str, range(10)))


# assumes sorted list of numbers
def get_nth_perm(numbers, n):
    if len(numbers) == 0:
        return ''
    k = len(numbers) - 1
    kfact = math.factorial(k)
    idx = n // kfact
    rem = n % kfact
    thisval = numbers.pop(idx)
    return thisval + get_nth_perm(numbers, rem)


print(get_nth_perm(numbers, n-1))
