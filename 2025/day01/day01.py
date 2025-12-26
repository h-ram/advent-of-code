def parse_file(filepath="./input.txt"):
    with open(filepath) as f:
        lines = f.read().strip().splitlines()

    rotations = []
    for line in lines:
        direction = line[0]
        amount = int(line[1:])
        rotations.append(-amount if direction == 'L' else amount)
    return rotations


def landed_on_zero(rotations):
    position = 50
    count = 0
    for rot in rotations:
        position = (position + rot) % 100
        if position == 0:
            count += 1
    return count

def passed_by_zero(rotations):
    position = 50
    count = 0
    for rot in rotations:
        step = 1 if rot > 0 else -1
        for _ in range(abs(rot)):
            position = (position + step) % 100
            if position == 0:
                count += 1
    return count

input = parse_file("./input-custom.txt")
print("Part 1 (landed on zero):", landed_on_zero(input))
print("Part 2 (passed by zero):", passed_by_zero(input))