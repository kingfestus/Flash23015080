
import re

    # Regular expressions to check for password strength factors
length = r'.{8,}'
uppercase = r'[A-Z]'
lowercase = r'[a-z]'
digit = r'\d'
regex = r'[!@#$%^&*()-+=.]'
password = input("Enter your password: ")

# Check password length
if not re.search(length, password):
    print ("Password should be at least 8 characters long.")

# Check for uppercase letters
if not re.search(uppercase, password):
    print ("Password should contain at least one uppercase letter.")

# Check for lowercase letters
if not re.search(lowercase, password):
    print ("Password should contain at least one lowercase letter.")

# Check for digits
if not re.search(digit, password):
    print ("Password should contain at least one digit.")

# Check for special characters
if not re.search(regex, password):
    print("Password should contain at least one special character.")
print("Password is strong!")

# Example usage:
result = password
print(result)

