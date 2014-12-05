less_100s = ['one', 'two', 'three', 'four', 'five','six','seven','eight','nine']
hundreds = less_100s[0:9]
less_100s += ['ten', 'eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
                'seventeen','eighteen','nineteen']
def add_strings_to_100(second):
        less_100s.append(second)
        for i in less_100s[0:9]:
                less_100s.append(second+' '+i)
add_strings_to_100('twenty')
add_strings_to_100('thirty')
add_strings_to_100('forty')
add_strings_to_100('fifty')
add_strings_to_100('sixty')
add_strings_to_100('seventy')
add_strings_to_100('eighty')
add_strings_to_100('ninety')
from_1_to_1000 = less_100s[:]
for hundred in hundreds:
        from_1_to_1000.append(hundred+' hundred')
        for less_100 in less_100s:
                from_1_to_1000.append(hundred+' hundred and '+less_100)
from_1_to_1000.append('one thousand')

print reduce(lambda x, y: x + len(''.join(y.split())), from_1_to_1000, 0)

