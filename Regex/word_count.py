text = input("Enter a text Pls: ")
with open("text.txt","w")as file:
    file.write(text)
    print(f"Total words in the file:{file.write(text)}:")
