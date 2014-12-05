import sys
strings = open(sys.argv[1]).read().split('\n')[:-1]
grid = []
for string in strings:
	grid.append(map(lambda x: int(x), string.split(' ')))

max_val = 0
height = len(grid)
width = len(grid[0])

def across(i, j):
	if (j+3) >= width:
		return 0
	return grid[i][j] * grid[i][(j+1)%width] * grid[i][(j+2)%width] * grid[i][(j+3)%width]
def down (i, j):
	if (i+3) >= height:
		return 0
	return grid[i][j] * grid[(i+1)%height][j] * grid[(i+2)%height][j] * grid[(i+3)%height][j] 
def diag_r (i, j):
	if (i+3) >= height or (j+3) >= width:
		return 0
	return grid[i][j] * grid[(i+1)%height][(j+1)%width] * grid[(i+2)%height][(j+2)%width] * grid[(i+3)%height][(j+3)%width]
def diag_l(i, j):
	if (i+3) >= height or (j-3) < 0:
		return 0
	return grid[i][j] * grid[(i+1)%height][(j-1)%width] * grid[(i+2)%height][(j-2)%width] * grid[(i+3)%height][(j-3)%width]

for i in xrange(height):
	for j in xrange(width):
		max_val = max(max_val, max(across(i,j), down(i,j), diag_l(i,j), diag_r(i,j)))
		print i,j,max_val

print max_val