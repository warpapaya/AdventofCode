import re

def valid_mul_instructions(line):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, line)
    return [(int(a), int(b)) for a, b in matches]

def process_file(filename):
    total_sum = 0
    with open(filename, 'r') as file:
        for line in file:
            instructions = valid_mul_instructions(line)
            for a, b in instructions:
                total_sum += a * b
    return total_sum

result = process_file('puzzleinput.txt')
print(f"The sum of all valid multiplication results is: {result}")