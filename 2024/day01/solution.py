
def parse_file(filepath="./input.txt"):
    with open(filepath) as f:
        ids = f.read().strip().split()
    left_list = [int(id) for i,id in enumerate(ids) if i % 2 == 0]
    right_list = [int(id) for i,id in enumerate(ids) if i % 2 == 1]
    return [left_list, right_list] 

def total_distance(lists):
    total = 0
    llist = sorted(lists[0])
    rlist= sorted(lists[1])
    for i in range(len(lists[0])):
        gap = abs(llist[i] - rlist[i])
        total += gap
    return total


def similarity_score(lists):
    score = 0
    for l_id in lists[0]:
        count = 0
        for r_id in lists[1]:
            count += l_id == r_id
        score += count * l_id
    return score

lists = parse_file("./input.txt")
print("Part 1:", total_distance(lists))
print("Part 2:", similarity_score(lists))

