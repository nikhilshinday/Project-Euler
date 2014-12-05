def collazt_length(num):
        length = 1
        while (num != 1):
                if num % 2 == 0:
                        num = num / 2
                else:
                        num = (3 * num) + 1
                length += 1
        return length

max_len = 0
collazt_number = 0
for i in range(1, 1000000):
        curr_length = collazt_length(i)
        if curr_length > max_len:
                collazt_number = i
                max_len = curr_length

print collazt_number

