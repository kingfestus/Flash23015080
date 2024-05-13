 # this Program is to check if a number is prime number or not

def check_prime():
    num = int(input(" Pls enter your number :  "))
    for i in range( 2 , num ):
        if num % i == 1:
            return True
        elif num % i == 0:
            return False


print(check_prime())