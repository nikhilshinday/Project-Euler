import sys
names = open(sys.argv[1]).read().replace('"', '').split(',')
names.sort()
score = 0
name_sum = 0
# for char in names[937]:
#         name_sum += (ord(char) - 64)
# print name_sum
# print name_sum * 938

for i in range(len(names)):
        name_sum = 0
        for char in names[i]:
                name_sum += (ord(char) - 64)
        score += (name_sum * (i+1))
print score

