def parse_file(filepath="./input.txt"):
    with open(filepath) as f:
        banks = f.read().strip().splitlines()
    return banks


def joltage_2(banks):
    sum = 0
    for bank in banks:
        batteries = [int(battery) for battery in bank]

        max_1 = max(batteries[:-1]) 
        max_1_idx = batteries.index(max_1)
        
        max_2 = max(batteries[max_1_idx+1:]) 

        bank_joltage = int(f"{max_1}{max_2}")
        sum += bank_joltage

        # print("Batteries :", batteries, end=" => ")
        # print("Bank Joltage :", bank_joltage)
    return sum

def joltage_12(banks):
    sum = 0
    for bank in banks:
        batteries = [int(battery) for battery in bank]

        max_1 = max(batteries[:-11]) 
        max_1_idx = batteries.index(max_1)
        
        max_2 = max(batteries[max_1_idx+1:-10])
        max_2_idx = batteries.index(max_2, max_1_idx+1)

        max_3 = max(batteries[max_2_idx+1:-9])
        max_3_idx = batteries.index(max_3, max_2_idx+1)

        max_4 = max(batteries[max_3_idx+1:-8])
        max_4_idx = batteries.index(max_4, max_3_idx+1)

        max_5 = max(batteries[max_4_idx+1:-7])
        max_5_idx = batteries.index(max_5, max_4_idx+1)

        max_6 = max(batteries[max_5_idx+1:-6])
        max_6_idx = batteries.index(max_6, max_5_idx+1)

        max_7 = max(batteries[max_6_idx+1:-5])
        max_7_idx = batteries.index(max_7, max_6_idx+1)

        max_8 = max(batteries[max_7_idx+1:-4])
        max_8_idx = batteries.index(max_8, max_7_idx+1)

        max_9 = max(batteries[max_8_idx+1:-3])
        max_9_idx = batteries.index(max_9, max_8_idx+1)

        max_10 = max(batteries[max_9_idx+1:-2])
        max_10_idx = batteries.index(max_10, max_9_idx+1)

        max_11 = max(  batteries[max_10_idx+1:-1])
        max_11_idx = batteries.index(max_11, max_10_idx+1)

        max_12 = max(batteries[max_11_idx+1:])

        bank_joltage = int(f"{max_1}{max_2}{max_3}{max_4}{max_5}{max_6}{max_7}{max_8}{max_9}{max_10}{max_11}{max_12}")
        sum += bank_joltage

        # print("Batteries :", batteries, end=" => ")
        # print("Bank Joltage :", bank_joltage)
    return sum

banks = parse_file("./input.txt")

print("Part 1 :", joltage_2(banks))
print("Part 2 :", joltage_12(banks))