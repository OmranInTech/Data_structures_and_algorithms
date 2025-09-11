def duplicate_arr(arr):
  new_arr=[]
  for i in arr:
    if i not in new_arr:
      new_arr.append(i)
  return new_arr

arr=[1,2,2,2,2,3,5]
print(duplicate_arr(arr))
