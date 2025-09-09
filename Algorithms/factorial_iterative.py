def factorial (n):
'''this function is used to find factorail for a number 
we use iterative function and logic to implement iterative logic 
'''
  if n==0 : 
    return 1
  fact=1
  for i in range (1,n+1):
    fact *=i
  return fact

#test
print(factorial(4))



