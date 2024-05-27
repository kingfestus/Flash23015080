#this program gives you the maximum and minimum values in a tuple of numbers
def find_max_min(numbers):
    if not numbers:  # Check if the tuple is empty or not
        return None, None
    
    max_value = max(numbers)
    min_value = min(numbers)
    
    return max_value, min_value

numbers = (3, 5, 7, 2, 8, -1, 4)
result = find_max_min(numbers)
print(result)
