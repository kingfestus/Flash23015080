#this program takes two list and return a new list frm both list without duplicates
def merge_list(list1, list2):
    combined_set = set(list1) | set(list2)
    merged_list = list(combined_set)
    return merged_list

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

merged_list = merge_list(list1, list2)
print(merged_list)
#the program ran sucessfully
