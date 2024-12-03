from collections import Counter

def calculate_sorted_differences_from_file(file_path):
    left_numbers = []
    right_numbers = []

    with open(file_path, 'r') as file:
        for line in file:
            num1, num2 = map(int, line.split())
            left_numbers.append(num1)
            right_numbers.append(num2)
    
    left_numbers.sort()
    right_numbers.sort()
    
    if len(left_numbers) != len(right_numbers):
        raise ValueError("lists aren't the same length")

    differences = [abs(a - b) for a, b in zip(left_numbers, right_numbers)]
    
    return sum(differences)


def calculate_similarity_score_from_file(file_path):
    left_numbers = []
    right_numbers = []

    with open(file_path, 'r') as file:
        for line in file:
            num1, num2 = map(int, line.split())
            left_numbers.append(num1)
            right_numbers.append(num2)

    right_count = Counter(right_numbers)
    
    similarity_score = sum(num * right_count[num] for num in left_numbers if num in right_count)
    
    return similarity_score

file_path = 'puzzleinput.txt'
similarity = calculate_similarity_score_from_file(file_path)
answer = calculate_sorted_differences_from_file(file_path)
print(f"Similarity {similarity} Distance {answer}")