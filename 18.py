import sys

tree = [map(int, row.split()) for row in open(sys.argv[1]).read().split("\n")]

while len(tree) > 1:
        l0 = tree.pop()
        l1 = tree.pop()
        tree.append([max(l0[i],l0[i+1]) + node for i, node in enumerate(l1)])
print tree[0][0]

