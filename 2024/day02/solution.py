
def parse_file(filepath="./input.txt"):
    with open(filepath) as f:
        lines = f.read().strip().splitlines()

    reports = []
    for line in lines:
        levels = [int(level) for level in line.split()]
        reports.append(levels)
    return reports

def n_safe(reports):
    number_of_safe_reports = 0
    for report in reports:
        is_safe = True # assume is safe until not

        if report[0] > report[1]: # decreasing
            for i in range(len(report)-1):
                a = report[i]
                b = report[i+1]
                if a <= b or a-b > 3: 
                    is_safe = False
                    break

        elif report[0] < report[1]: # increasing
            for i in range(len(report)-1):
                a = report[i]
                b = report[i+1]
                # print(a,b, end=" ")
                if a >= b or b-a > 3: 
                    is_safe = False
                    break
        else:
            is_safe = False

        number_of_safe_reports += is_safe
    return number_of_safe_reports

def n_safe_with_dampner(reports):
    number_of_safe_reports = 0
    for report in reports:
        is_safe = False # assume not safe until proven safe
        
        def check_safe(levels):
            if len(levels) < 2:
                return True
            if levels[0] == levels[1]:
                return False
            is_increasing = levels[0] < levels[1]
            for i in range(len(levels)-1):
                a = levels[i]
                b = levels[i+1]
                if is_increasing:
                    if a >= b or b-a > 3:
                        return False
                else:
                    if a <= b or a-b > 3:
                        return False
            return True
        
        if check_safe(report):
            is_safe = True
        else:
            # Try removing each level
            for skip_idx in range(len(report)):
                test_report = report[:skip_idx] + report[skip_idx+1:]
                if check_safe(test_report):
                    is_safe = True
                    break

        number_of_safe_reports += is_safe
    return number_of_safe_reports

reports = parse_file("./input.txt")
print("Part 1:", n_safe(reports))
print("Part 2:", n_safe_with_dampner(reports))

