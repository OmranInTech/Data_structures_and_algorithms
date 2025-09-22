def sum_of_naturals(n):
  ''' this function will return the same of natural numbers give by a user'''
  if n>1:
    return 'please input number greaterthan zero!'
  elif n==1:
    return 1
  else:
    return n+sum_of_naturals(n-1)
#example usage
print(sum_of_naturals(4))
