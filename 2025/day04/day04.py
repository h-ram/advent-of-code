def parse_file(filepath="./input.txt"):
    with open(filepath) as f:
        rows = f.read().strip().splitlines()
    grid = [list(row) for row in rows]
    return grid

def print_grid(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            print(grid[x][y], end="")
        print() 


def n_accessable_rolls(grid):
    count = 0
    grid_copy = [row.copy() for row in grid]
    for x in range(len(grid)):
        n_cols = len(grid)
        n_rows = len(grid[x])
        for y in range(n_rows):
            if grid[x][y] != '@':
                continue

            adjacent_count = 0 

            adjacent_count +=  (x != 0 and y!=0 ) and grid[x-1][y-1] == '@' # Top-Left
            adjacent_count +=  (x != 0) and grid[x-1][y] == '@' # Top
            adjacent_count +=  (x != 0 and y!=n_rows-1 ) and grid[x-1][y+1] == '@' # Top-Right
            adjacent_count +=  (y!=n_rows-1 ) and grid[x][y+1]   == '@' # Right
            adjacent_count +=  (x != n_cols-1 and y!=n_rows-1 ) and grid[x+1][y+1] == '@' # Bottom-Right
            adjacent_count +=  (x != n_cols-1 ) and grid[x+1][y]   == '@' # Bottom
            adjacent_count +=  (x != n_cols-1 and y!=0 ) and grid[x+1][y-1] == '@' # Bottom-Left
            adjacent_count +=  (y!=0 ) and grid[x][y-1] == '@' # Left

            if adjacent_count < 4:
                count += 1
                grid_copy[x][y] = "x"
                # print(f"Roll at ({x},{y}) has {adjacent_count} adjacent '@'s")


 
    return (count, grid_copy)

def n_removable_rolls(grid):
    old_count = 0
    count, grid = n_accessable_rolls(grid)
    while count != old_count:
        old_count = count
        new_count, grid = n_accessable_rolls(grid)
        count += new_count

    return count 

grid = parse_file("./input.txt")

print("Part 1 :", n_accessable_rolls(grid)[0])
print("Part 2 :", n_removable_rolls(grid))