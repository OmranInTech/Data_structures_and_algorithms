def factorial (n):
  """
  this is factorial function use to find factorial of a number 
  we use base case and recursive call to implement recursion concept
  in practise.
  """
  if n == 0:
    return 1
  else : 
    return n*factorial(n-1)
#examle usage
number=3
print(factorial(number))



