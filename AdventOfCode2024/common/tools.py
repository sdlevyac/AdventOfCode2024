def draw(grid):
	for row in grid:
		print("".join([str(_) for _ in row]))

def add(a,b):
	return [a[0] + b[0], a[1] + b[1]]

def inRange(coord,x,y):
	return coord[0] >= 0 and coord[0] < x and coord[1] >= 0 and coord[1] < y
