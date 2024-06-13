import re
user = input("Enter your email address: ")
regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(regex, user):
    print("valid email")
else:
    print('not matched to regular email')
