#this program will give you the multiplication times table of the inputed value from a user and print till 12 times table

num1 = int(input('pls enter your multiplication number: '))
for i in range(num1, 13):
 for j in range(1, 13):
   print(f'{i} * {j} = {i * j} ')

