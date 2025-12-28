def parse_file(filepath="./input.txt"):
    with open(filepath) as f:
        rows = f.read().strip().splitlines()
    grid = [[col for col in row] for row in rows]

    return grid

def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()


def n_splits(grid):
    number_of_splits = 0
    beam_locations = {len(grid[0])//2}
    for x in range(1,len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "^":
                for loc in list(beam_locations):
                    if loc == y:
                        beam_locations.remove(loc)
                        beam_locations.add(loc-1)
                        beam_locations.add(loc+1)
                        number_of_splits += 1
                        grid[x][y+1] = "|"
                        grid[x][y-1] = "|"


            if grid[x][y] == ".":
                if y in beam_locations:
                    grid[x][y] = "|"
                continue


    
    print_grid(grid)
    return number_of_splits



grid = parse_file("./example.txt")

# print_grid(grid)

print("Part 1 :", n_splits(grid))
# print("Part 2 :", n_timelines(0,{len(grid[0])//2}))