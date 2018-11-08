from tqdm import tqdm

def get_9_pandigital(val):
    rv = ''
    i = 1
    rv += str(val)
    while True:
        if len(rv) == 9:
            return int(rv)
        elif len(rv) > 9:
            return None
        else:
            i += 1
            rv += str(val * i)


# print(get_9_pandigital(9999))

print(max(
        list(
            filter(lambda x: x,
                    (map(get_9_pandigital,
                            tqdm(range(10000))))))))
# results = []
# for i in range(10000):
#     val = get_9_pandigital(i)
