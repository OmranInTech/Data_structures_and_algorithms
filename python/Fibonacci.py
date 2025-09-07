def fibonacci_sequence (n):
  """ this function is used to find fibonacci for a number
      we create the function with base case and recursive call to 
      implement recursion concept in practise """
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibonacci_sequence(n-1)+fibonacci_sequence(n-2)

#test
number=4
print(fibonacci_sequence(number))
