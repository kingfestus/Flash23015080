#this gives the fibonacci_sequence of a non negative integer
def fibonacci_sequence(n):
    if n <= 1:
        return n
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

# Example usage:
n = int(input(" pls enter a non-negative integer "))
print(fibonacci_sequence(n))  # Output will be 13
