text = input("Enter name of the source file: ")
with open("text.txt","r")as file:
    content = file.read()
    new_file = input("Enter the name of the destination file: ")
    with open(new_file,"w")as file:
        copied = file.write(content)
        print("copied Successful ")
