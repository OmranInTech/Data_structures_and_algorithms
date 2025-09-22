def swap_two_numbers(a,b):
    a , b =b ,a
    return a , b

# Example usage:
x = 5
y = 10  
print("Before swapping: x =", x, ", y =", y)
x, y = swap_two_numbers(x, y)
print("After swapping: x =", x, ", y =", y)
