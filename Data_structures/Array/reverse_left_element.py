def reverse_element_arr(arr):
  '''this function reverse only one left element of an array'''
  new_arr=[]
  start=0
  end=len(arr)-1
  for i in range(start+1 , end+1):
    new_arr.append(arr[i])
  new_arr.append(arr[start])
  return new_arr
#example usage
arr=[1,2,3,4,5]
print(reverse_element_arr(arr))
