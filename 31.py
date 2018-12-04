import numpy as np

coin_values = np.array([1, 2, 5, 10, 20, 50, 100, 200])
table = np.zeros(201)
table[0] = 1
for coin in coin_values:
    for j in range(coin, len(table)):
        table[j] += table[j - coin]
print(table[200])
