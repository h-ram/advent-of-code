def parse_file(filepath="./input.txt"):
    with open(filepath) as f:
        ranges = f.read().strip().split(",")

    ids= []
    for span in ranges:
        min, max = span.split("-")
        ids.extend(range(int(min),int(max)+1))
    return ids


def sum_of_invalid_halfs(ids):
    sum = 0
    for id in ids:
        id_str = str(id)
        first_half = id_str[0:len(id_str)//2]
        second_half = id_str[len(id_str)//2:]      
        if first_half == second_half:
            sum += id       
    return sum

def sum_of_invalid_pairs(ids):
    sum = 0
    for id in ids:
        id_str = str(id)
        for i in range(1,len(id_str) // 2 + 1):
            if id_str[:i] * (len(id_str) // i) == id_str:
                sum += id
                break
    return sum

ids = parse_file("./input.txt")

print("Part 1 :", sum_of_invalid_halfs(ids))
print("Part 2 :", sum_of_invalid_pairs(ids))