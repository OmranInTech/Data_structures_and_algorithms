#subarray sum 
def subarray_sum(arr,k):
  #this function will return the number of subarry sum equals to k
  count=0
  n=len(arr)
  for i in range(n):
    total=0
    for j in range(i,n):
      total +=arr[j]
      if total == k:
        count+=1
  return count 
#example usage
arr=[1,2,3]
k=3
print(subarray_sum(arr,k))
'''explaniation
arr [3] and arr[1,2] '''

