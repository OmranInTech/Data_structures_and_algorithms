
def sumofnaturalsquares(n):
    """Returns the sum of the squares of the first n natural numbers."""
    if n < 1:
        return 0
    else:
        return n**2 + sumofnaturalsquares(n - 1)

  #exmaple usage 
  print(sumofnaturalsqaures(12))
