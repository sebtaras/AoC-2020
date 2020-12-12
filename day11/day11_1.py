def update_seat(seat, grid, row, col):
    
    occ = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r != row or c != col:
                if grid[r][c] == '#':
                    occ += 1

    if seat == 'L' and occ == 0:
        return '#'
    elif seat == '#' and occ >= 4:
        return 'L'
    else:
        return seat

def change(grid1, grid2):
    dim_x = len(grid1)
    dim_y = len(grid1[0])
    for i in range(0, dim_x):
        for j in range(0, dim_y):
            if grid1[i][j] != grid2[i][j]:
                return True
    return False

def count_occupied(grid):
    res = 0
    dim_x = len(grid)
    dim_y = len(grid[0])

    for i in range(0, dim_x):
        for j in range(0, dim_y):
            if grid[i][j] == "#":
                res += 1
    return res

f = open("day11input.txt")

grid = []
pad = True
ln = 0
for line in f:
    ln = len(line.strip())+2
    if pad:
        grid.append("."*ln)
        pad = False
    grid.append("." + line.strip() + ".")
grid.append("."*ln)

rows = len(grid)
cols = len(grid[0])

new_grid = grid[:]
temp_grid = grid[:]
while(True):
    for row in range(1, rows-1):
        line = temp_grid[row][1:rows-1]
        new_line = ""
        for col in range(1, cols-1):
            seat = temp_grid[row][col]
            new_line += update_seat(seat, temp_grid, row, col)
        new_grid[row] = "." + new_line + "."
    if change(temp_grid, new_grid) == False:
        break
    temp_grid = new_grid[:]

print(count_occupied(new_grid))