def sorted_arr(arr):
  '''this function is use to check wether an array is sorted or not 
  if sorted it will print True if not sorted it will print False'''
  start=0
  end=len(arr)-1
  for i in range(start,end):
    if arr[i] > arr[i+1]:
      return False
  return True
#example usage
arr=[1,2,3,4]
arr_1=[2,4,3,1]
print(sorted_arr(arr))
print(sorted_arr(arr_1))
