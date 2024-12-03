import re

def valid_mul_instructions(line, mul_enabled):
    pattern = r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))'
    instructions = re.findall(pattern, line)
    
    total_sum = 0
    for instruction in instructions:
        if instruction.startswith('mul'):
            if mul_enabled:
                nums = re.findall(r'\d+', instruction)
                a, b = map(int, nums)
                total_sum += a * b
        elif instruction == "do()":
            mul_enabled = True
        elif instruction == "don't()":
            mul_enabled = False
    
    return total_sum, mul_enabled

def process_file(filename):
    total_sum = 0
    mul_enabled = True
    
    with open(filename, 'r') as file:
        for line in file:
            line_sum, mul_enabled = valid_mul_instructions(line, mul_enabled)
            total_sum += line_sum
    
    return total_sum

result = process_file('puzzleinput.txt')
print(result)