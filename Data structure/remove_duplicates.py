#this program takes a lust as input and returns a new list containing only unique elements, preserving their orginal order
def remove_duplicates(input_list):
    seen = set()
    unique_list = []
    
    for item in input_list:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    
    return unique_list

input_list = [1, 3, 2, 3, 4, 2, 1, 5]
result = remove_duplicates(input_list)
print(result)
