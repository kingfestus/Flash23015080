#This program will execute the number of vowel in the text give by user
def count_vowels(text):
    vowels = 'a,e,i,u,o'
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return f' the number of vowels are {vowel_count}'

text = input("pls enter a text : ")
print(count_vowels(text))
