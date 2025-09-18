def count_awarness(arr,n):
  '''count an element in array'''
  total=0
  for i in arr:
    if i == n :
      total +=1
  return total 
#example usage of function
arr=[1,2,3,4,5,5,6,5,5]
print(count_awarness(arr,5))#output is 4
