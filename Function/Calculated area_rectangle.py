#this program wil calculate the area of a rectangle and give the result base on user input
def calculate_area_rectangle():
    length = int(input('Pls enter your length :  '))
    width = int(input('Pls enter your width :  '))
    result = f' The area of your rectangle is {length * width }'
    return result
   
print(calculate_area_rectangle())
