def is_safe_report(report):
    if len(report) < 2:
        return True
    
    is_increasing = all(report[i] < report[i+1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i+1] for i in range(len(report) - 1))
    
    if not (is_increasing or is_decreasing):
        return False

    for i in range(len(report) - 1):
        diff = abs(report[i+1] - report[i])
        if diff < 1 or diff > 3:
            return False

    return True

def enhanced_is_safe_report(report):
    if len(report) < 2:
        return True
    
    def check_sequence(seq):
        is_increasing = all(seq[i] < seq[i+1] for i in range(len(seq) - 1))
        is_decreasing = all(seq[i] > seq[i+1] for i in range(len(seq) - 1))
        if not (is_increasing or is_decreasing):
            return False

        for i in range(len(seq) - 1):
            diff = abs(seq[i+1] - seq[i])
            if diff < 1 or diff > 3:
                return False
        return True
    
    if check_sequence(report):
        return True

    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if check_sequence(new_report):
            return True

    return False

def count_safe_reports(filename):
    safe_count = 0
    enhanced_safe_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            if is_safe_report(report):
                safe_count += 1
            if enhanced_is_safe_report(report):
                enhanced_safe_count += 1

    return enhanced_safe_count, safe_count

filename = "puzzleinput.txt"
enhanced_safe_count, safe_count = count_safe_reports(filename)
print(f"Safe List: {safe_count}, Safe List with Damper: {enhanced_safe_count}")