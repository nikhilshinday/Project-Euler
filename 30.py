counter = 2;
collection = []

while counter < (9**5)*5:
        if counter == reduce(lambda x,y: x + int(y) ** 5, str(counter), 0):
                collection.append(counter)
        counter += 1

print sum(collection)