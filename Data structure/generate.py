# this program generates a Generator expression to generate squares of numbers from 1 to 10
squares = (x**2 for x in range(1, 11))
for square in squares:
    print(square)
