#this program will reverse the text of a user
def reverse_string():
    txt = input( " pls enter your text :  ")
    for x in txt:
        new_txt = txt[::-1]
        return new_txt
        
print(reverse_string())
#it has reversed the text of the user