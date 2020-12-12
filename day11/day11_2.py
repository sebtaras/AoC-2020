def update_seat(seat, grid, row, col):
    #print(seat, row, col)
    #adjecent_seats = [] #dont need to store these
    dim_x = len(grid)
    dim_y = len(grid[0])
    occ = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r != row or c != col:
                (m, n) = (r, c) # -> m: _row, n: _col
                #row, col -> seat
                while grid[m][c] == '.':
                    print(m, c, grid[m][c])
                    if m > row and c == col:    #row+1, col -> below seat
                        m += 1
                    
                    elif m < row and c == col:    #row-1, col -> above seat
                        m -= 1
   
                    elif m == row and c < col:    #row,   col-1 -> left of seat
                        c -= 1

                    elif m == row and c > col:    #row,   col+1 -> right of seat
                        c += 1

                    elif m < row and c < col:     #row-1, col-1 -> left, up from seat
                        m -= 1
                        c -= 1

                    elif m < row and c > col:     #row-1, col+1 -> left, down from seat
                        m -= 1
                        c += 1
                    elif m > row and c < col:     #row+1, col-1 -> right, up from seat
                        m += 1
                        c -= 1
                    elif m > row and c > col:     #row+1, col+1 -> right, down from seat
                        m += 1
                        c -= 1          
                    
                    if m < dim_x and n < dim_y and (m, n) >= (0, 0):
                        continue
                    else:
                        break
                #adjecent_seats.append(grid[r][c])
                #print(r, c, grid[r][c])
                if grid[m][n] == '#':
                    occ += 1

    #print(adjecent_seats, occ)

    if seat == 'L' and occ == 0:
        #print("seat =", seat, "occ =", occ, "returning #")
        return '#'
    elif seat == '#' and occ >= 4:
        #print("seat =", seat, "occ =", occ, "returning L")
        return 'L'
    else:
        #print("seat =", seat, "occ =", occ, "returning", seat)
        return seat

def change(grid1, grid2):
    dim_x = len(grid1)
    dim_y = len(grid1[0])

    #print(len(grid1[0]), len(grid1))
    #print(len(grid2[0]), len(grid2))

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

f = open("day11inpu.txt")

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
    print()
    for n in new_grid:
        print(n)
    if change(temp_grid, new_grid) == False:
        break
    temp_grid = new_grid[:]

print(count_occupied(new_grid))