#this program takes a string as input and returns a dictionary containing the count of each word in the string 
def count_words(input_string):
    words = input_string.split()
    
    word_counts = {}
    
    for word in words:
        word = word.lower()
        
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts

input_string = "This is a test. This test is only a test."
result = count_words(input_string)
print(result)
