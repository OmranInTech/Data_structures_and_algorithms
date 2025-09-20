#subarray sum 
def subarray_sum(arr,k):
  count=0
  n=len(arr)
  for i in range(n):
    total=0
    for j in range(i,n):
      total +=arr[j]
      if total == k:
        count+=1
  return count 

