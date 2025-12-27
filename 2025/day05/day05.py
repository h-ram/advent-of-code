def parse_file(filepath="./input.txt"):
    with open(filepath) as f:
        parts = f.read().strip().split("\n\n")
    
    ranges = []
    ids = []
    
    for line in parts[0].split('\n'):
        start, end = map(int, line.split('-'))
        ranges.append((start, end))
    
    for line in parts[1].split('\n'):
        ids.append(int(line))
    
    return (ranges, ids)

def n_fresh(ranges, ids):
    fresh_count = 0
    for id in ids:
        for range in ranges:
            if range[0] <= id <= range[1]:
                fresh_count += 1
                # print(f"{id} is fresh {range}")
                break
    return fresh_count

def combine_ranges(ranges):
    if len(ranges) == 0:
        return ranges
    
    sorted_ranges = sorted(ranges)
    
    combined = [sorted_ranges[0]]
    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = combined[-1]
        if current_start <= last_end + 1:
            combined[-1] = (last_start, max(last_end, current_end))
        else:
            combined.append((current_start, current_end))
    
    return combined

def n_possible_fresh(ranges):
    new_ranges = combine_ranges(ranges)
    
    n_ids = 0
    for mini, maxi in new_ranges:
        gap = maxi - mini + 1
        n_ids += gap
    
    return n_ids

ranges, ids = parse_file("./input.txt")
print("Part 1 :", n_fresh(ranges, ids))
print("Part 2 :", n_possible_fresh(ranges))