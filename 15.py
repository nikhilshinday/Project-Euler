# intuition: same as number of paths through a graph with each node
# as one of the points on the graph. How many paths are there?
import math
grid_dim = 20
print math.factorial(grid_dim * 2) / (math.factorial (grid_dim) ** 2)